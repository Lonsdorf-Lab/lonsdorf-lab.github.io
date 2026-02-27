"""
cite process to convert sources and metasources into full citations
"""

import traceback
from importlib import import_module
from pathlib import Path
from dotenv import load_dotenv
from util import *
import re
import string
from collections import defaultdict


# custom function to include only latest publication
def apply_suppression_rules(sources, config_path="_data/citation_config.yaml"):
    """
    Apply suppression logic to compiled sources before citation generation.

    Suppression logic:
    1. If a journal (non-preprint) exists for a title → suppress all preprints.
    2. If only preprints exist → keep newest preprint only.

    Preprints are detected via configurable publisher list.
    Modifies sources in-place by setting source["remove"] = True.
    """

    import string
    import re
    from collections import defaultdict

    # ----------------------------
    # Load Config
    # ----------------------------

    try:
        config = load_data(config_path)
    except Exception:
        log("No citation_config.yaml found. Skipping suppression.", level="WARNING")
        return sources

    suppression_cfg = config.get("suppression", {})

    if not suppression_cfg.get("enabled", False):
        log("Suppression disabled via config.")
        return sources

    suppress_preprints_if_journal = suppression_cfg.get(
        "suppress_preprints_if_journal_exists", True
    )

    keep_latest_preprint_only = suppression_cfg.get(
        "keep_latest_preprint_only", True
    )

    preprint_publishers = suppression_cfg.get("preprint_publishers", [])

    # Normalize publisher patterns for robust matching
    preprint_publishers = [p.lower() for p in preprint_publishers]

    # ----------------------------
    # Helper Functions
    # ----------------------------

    def normalize_title(title):
        if not title:
            return ""
        title = title.lower()
        title = title.translate(str.maketrans("", "", string.punctuation))
        return " ".join(title.split())

    def is_preprint(source):
        publisher = get_safe(source, "publisher", "")
        publisher = str(publisher).lower()

        if not publisher:
            return False

        return any(pattern in publisher for pattern in preprint_publishers)

    def extract_version(doi):
        match = re.search(r"_v(\d+)$", doi or "")
        return int(match.group(1)) if match else None

    # ----------------------------
    # Group Sources by Normalized Title
    # ----------------------------

    log("Applying suppression rules")

    grouped = defaultdict(list)

    for idx, source in enumerate(sources):
        title = get_safe(source, "title", "")
        doi = get_safe(source, "id", "")
        date = get_safe(source, "date", "")

        norm = normalize_title(title)

        grouped[norm].append({
            "index": idx,
            "doi": doi,
            "date": date,
            "is_preprint": is_preprint(source),
            "version": extract_version(doi)
        })

    suppressed_count = 0

    # ----------------------------
    # Apply Suppression Logic
    # ----------------------------

    for norm_title, entries in grouped.items():

        has_journal = any(not e["is_preprint"] for e in entries)

        # Case 1: Journal exists → suppress all preprints
        if has_journal and suppress_preprints_if_journal:
            for e in entries:
                if e["is_preprint"]:
                    sources[e["index"]]["remove"] = True
                    suppressed_count += 1

        # Case 2: Only preprints exist → keep newest only
        elif keep_latest_preprint_only:
            preprints = [e for e in entries if e["is_preprint"]]

            if len(preprints) <= 1:
                continue

            # Sort newest first
            preprints.sort(
                key=lambda x: (
                    x["version"] if x["version"] is not None else -1,
                    x["date"]
                ),
                reverse=True
            )

            keep_index = preprints[0]["index"]

            for e in preprints:
                if e["index"] != keep_index:
                    sources[e["index"]]["remove"] = True
                    suppressed_count += 1

    log(f"{suppressed_count} source(s) suppressed by rules", level=1)

    return sources



# load environment variables
load_dotenv()


# save errors/warnings for reporting at end
errors = []
warnings = []

# output citations file
output_file = "_data/citations.yaml"


log()

log("Compiling sources")

# compiled list of sources
sources = []

# in-order list of plugins to run
plugins = ["google-scholar", "pubmed", "orcid", "sources"]

# loop through plugins
for plugin in plugins:
    # convert into path object
    plugin = Path(f"plugins/{plugin}.py")

    log(f"Running {plugin.stem} plugin")

    # get all data files to process with current plugin
    files = Path.cwd().glob(f"_data/{plugin.stem}*.*")
    files = list(filter(lambda p: p.suffix in [".yaml", ".yml", ".json"], files))

    log(f"Found {len(files)} {plugin.stem}* data file(s)", indent=1)

    # loop through data files
    for file in files:
        log(f"Processing data file {file.name}", indent=1)

        # load data from file
        try:
            data = load_data(file)
            # check if file in correct format
            if not list_of_dicts(data):
                raise Exception(f"{file.name} data file not a list of dicts")
        except Exception as e:
            log(e, indent=2, level="ERROR")
            errors.append(e)
            continue

        # loop through data entries
        for index, entry in enumerate(data):
            log(f"Processing entry {index + 1} of {len(data)}, {label(entry)}", level=2)

            # run plugin on data entry to expand into multiple sources
            try:
                expanded = import_module(f"plugins.{plugin.stem}").main(entry)
                # check that plugin returned correct format
                if not list_of_dicts(expanded):
                    raise Exception(f"{plugin.stem} plugin didn't return list of dicts")
            # catch any plugin error
            except Exception as e:
                # log detailed pre-formatted/colored trace
                print(traceback.format_exc())
                # log high-level error
                log(e, indent=3, level="ERROR")
                errors.append(e)
                continue

            # loop through sources
            for source in expanded:
                if plugin.stem != "sources":
                    log(label(source), level=3)

                # include meta info about source
                source["plugin"] = plugin.name
                source["file"] = file.name

                # add source to compiled list
                sources.append(source)

            if plugin.stem != "sources":
                log(f"{len(expanded)} source(s)", indent=3)


log("Merging sources by id")

# merge sources with matching (non-blank) ids
for a in range(0, len(sources)):
    a_id = get_safe(sources, f"{a}.id", "")
    if not a_id:
        continue
    for b in range(a + 1, len(sources)):
        b_id = get_safe(sources, f"{b}.id", "")
        if b_id == a_id:
            log(f"Found duplicate {b_id}", indent=2)
            sources[a].update(sources[b])
            sources[b] = {}
sources = [entry for entry in sources if entry]


log(f"{len(sources)} total source(s) to cite")



# Apply suppression rules before citation generation
sources = apply_suppression_rules(sources)



log()

log("Generating citations")

# list of new citations
citations = []


# loop through compiled sources
for index, source in enumerate(sources):
    log(f"Processing source {index + 1} of {len(sources)}, {label(source)}")

    # if explicitly flagged, remove/ignore entry
    if get_safe(source, "remove", False) == True:
        continue

    # new citation data for source
    citation = {}

    # source id
    _id = get_safe(source, "id", "").strip()

    # Manubot doesn't work without an id
    if _id:
        log("Using Manubot to generate citation", indent=1)

        try:
            # run Manubot and set citation
            citation = cite_with_manubot(_id)

        # if Manubot cannot cite source
        except Exception as e:
            plugin = get_safe(source, "plugin", "")
            file = get_safe(source, "file", "")
            # if regular source (id entered by user), throw error
            if plugin == "sources.py":
                log(e, indent=3, level="ERROR")
                errors.append(f"Manubot could not generate citation for source {_id}")
            # otherwise, if from metasource (id retrieved from some third-party API), just warn
            else:
                log(e, indent=3, level="WARNING")
                warnings.append(
                    f"Manubot could not generate citation for source {_id} (from {file} with {plugin})"
                )
                # discard source from citations
                continue

       # preserve fields from input source, overriding existing fields
    citation.update(source)

    # --------------------------------------------------
    # Determine publication type (preprint vs paper)
    # --------------------------------------------------

    # Load suppression config (same logic as suppression rules)
    try:
        config = load_data("_data/citation_config.yaml")
        suppression_cfg = config.get("suppression", {})
        preprint_publishers = suppression_cfg.get("preprint_publishers", [])
        preprint_publishers = [p.lower() for p in preprint_publishers]
    except Exception:
        preprint_publishers = []

    publisher = str(get_safe(citation, "publisher", "")).lower()

    is_preprint = any(pattern in publisher for pattern in preprint_publishers)

    publication_type = "preprint" if is_preprint else "paper"

    # --------------------------------------------------
    # Insert "type" directly after "title"
    # --------------------------------------------------

    if "title" in citation:
        new_citation = {}
        for key, value in citation.items():
            new_citation[key] = value
            if key == "title":
                new_citation["type"] = publication_type
        citation = new_citation
    else:
        # fallback (should not happen normally)
        citation["type"] = publication_type

    # ensure date in proper format for correct date sorting
    if get_safe(citation, "date", ""):
        citation["date"] = format_date(get_safe(citation, "date", ""))

    # add new citation to list
    citations.append(citation)



log()

log("Saving updated citations")


# save new citations
try:
    save_data(output_file, citations)
except Exception as e:
    log(e, level="ERROR")
    errors.append(e)


log()


# exit at end, so user can see all errors/warnings in one run
if len(warnings):
    log(f"{len(warnings)} warning(s) occurred above", level="WARNING")
    for warning in warnings:
        log(warning, indent=1, level="WARNING")

if len(errors):
    log(f"{len(errors)} error(s) occurred above", level="ERROR")
    for error in errors:
        log(error, indent=1, level="ERROR")
    log()
    exit(1)

else:
    log("All done!", level="SUCCESS")

log()

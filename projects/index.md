---
type: page
title: Projects
schema_type: project
nav:
  order: 2
  tooltip: Software, datasets, and more
---

# {% include icon.html icon="fa-solid fa-diagram-project" %} Projects

Get a glimpse into the work we do: from ongoing investigations to completed projects.

---

## Current Projects

{% assign current_projects = site.projects | where: "group", "on-going" %}

{% for project in current_projects %}
### [{{ project.title }}]({{ project.url | relative_url }})

{{ project.description }}

{% endfor %}

---

## Past Projects

{% assign past_projects = site.projects | where: "group", "finished" %}

{% for project in past_projects %}
### [{{ project.title }}]({{ project.url | relative_url }})

{{ project.description }}

{% endfor %}

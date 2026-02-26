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

## {% include icon.html icon="fa-solid fa-hourglass" %} Current Projects

{% assign current_projects = site.projects | where: "group", "on-going" %}

{% for project in current_projects %}

### [{{ project.title }}]({{ project.url | relative_url }})

{% assign max_chars = 350 %}
{% assign full_text = project.description | strip_html %}
{% assign text_length = full_text | size %}

<div class="project-description">
  {% if text_length > max_chars %}
    {{ full_text | truncate: max_chars, "…" }}
  {% else %}
    {{ full_text }}
  {% endif %}
  <a href="{{ project.url | relative_url }}" class="project-description-link">
    see more<span class="arrow">→</span>
  </a>
</div>


---

## {% include icon.html icon="fa-solid fa-check" %} Past Projects

{% assign past_projects = site.projects | where: "group", "finished" %}

{% for project in past_projects %}

### [{{ project.title }}]({{ project.url | relative_url }})

{% assign max_chars = 350 %}
{% assign full_text = project.description | strip_html %}
{% assign text_length = full_text | size %}

<div class="project-description">
  {% if text_length > max_chars %}
    {{ full_text | truncate: max_chars, "…" }}
  {% else %}
    {{ full_text }}
  {% endif %}
  <a href="{{ project.url | relative_url }}" class="project-description-link">
    see more<span class="arrow">→</span>
  </a>
</div>


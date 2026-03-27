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
{% assign parent_projects = current_projects | where: "project_level", "parent" %}
{% assign sub_projects = current_projects | where: "project_level", "sub" %}

{% for project in parent_projects %}
#### [{{ project.title }}]({{ project.url | relative_url }})

<div class="project-description">
  {{ project.content | strip_html | truncatewords: 50 }} 
  <a href="{{ project.url | relative_url }}" class="project-description-link">
    see more<span class="arrow">&rarr;</span>
  </a>
</div>
{% endfor %}

{% for parent in parent_projects %}
  {% assign parent_subprojects = sub_projects | where: "parent_project", parent.title %}
  {% if parent_subprojects != empty %}
    {% for subproject in parent_subprojects %}
#### [{{ subproject.title }}]({{ subproject.url | relative_url }})

<div class="project-description" style="margin-left: 20px;">
  {{ subproject.content | strip_html | truncatewords: 50 }} 
  <a href="{{ subproject.url | relative_url }}" class="project-description-link">
    see more<span class="arrow">&rarr;</span>
  </a>
</div>
    {% endfor %}
  {% endif %}
{% endfor %}

## {% include icon.html icon="fa-solid fa-check" %} Past Projects

{% assign past_projects = site.projects | where: "group", "finished" %}
{% assign parent_projects = past_projects | where: "project_level", "parent" %}
{% assign sub_projects = past_projects | where: "project_level", "sub" %}

{% for project in parent_projects %}
#### [{{ project.title }}]({{ project.url | relative_url }})

<div class="project-description">
  {{ project.content | strip_html | truncatewords: 50 }} 
  <a href="{{ project.url | relative_url }}" class="project-description-link">
    see more<span class="arrow">&rarr;</span>
  </a>
</div>
{% endfor %}

{% for parent in parent_projects %}
  {% assign parent_subprojects = sub_projects | where: "parent_project", parent.title %}
  {% if parent_subprojects != empty %}
    {% for subproject in parent_subprojects %}
#### [{{ subproject.title }}]({{ subproject.url | relative_url }})

<div class="project-description" style="margin-left: 20px;">
  {{ subproject.content | strip_html | truncatewords: 50 }} 
  <a href="{{ subproject.url | relative_url }}" class="project-description-link">
    see more<span class="arrow">&rarr;</span>
  </a>
</div>
    {% endfor %}
  {% endif %}
{% endfor %}

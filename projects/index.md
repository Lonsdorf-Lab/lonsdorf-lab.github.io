---
title: Projects
nav:
  order: 2
  tooltip: Software, datasets, and more
---

# {% include icon.html icon="fa-solid fa-wrench" %}Projects

Get a glimpse into the work we do: from ongoing investigations to completed projects.

{% include tags.html tags="publication, resource, website" %}

{% include search-info.html %}

{% include section.html %}

## Current Projects

{% include list.html component="card" data="projects" filter="group == 'on-going'" %}

{% include section.html %}

## Past Projects

{% include list.html component="card" data="projects" filter="group == 'finished'" style="small" %}

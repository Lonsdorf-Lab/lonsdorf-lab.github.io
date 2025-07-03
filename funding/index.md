---
title: Funding
nav:
  order: 4
  tooltip: funding
---

# {% include icon.html icon="fa-solid fa-wrench" %}Projects

Get a glimpse into the work we do: from ongoing investigations to completed projects.

{% include tags.html tags="publication, resource, website" %}

{% include search-info.html %}

{% include section.html %}

## Featured

{% include list.html component="card" data="projects" filter="group == 'featured'" %}

{% include section.html %}

## More

{% include list.html component="card" data="projects" filter="!group" style="small" %}

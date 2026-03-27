---
type: page
title: Projects
schema_type: project
nav:
  order: 2
  tooltip: Software, datasets, and more
---

## {% include icon.html icon="fa-solid fa-hourglass" %} Current Projects

{% assign current_projects = site.projects | where: "group", "on-going" %}

{% for project in current_projects %}
  
  {% if project.project_level == "parent" %}
  
  <h4>
  <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
  </h4>
  
  <div class="project-description">
    
    {{ project.content | strip_html | truncatewords: 50 }}
    
  <a href="{{ project.url | relative_url }}" class="project-description-link">
    see more<span class="arrow">&rarr;</span>
  </a>
  
  </div>
  
  {% elsif project.project_level == "sub" %}
  
 {% if project.parent_project_url %}
  
  <h4 class="project-parent-title">
  
  <a href="{{ project.parent_project_url }}" target="_blank" rel="noopener">{{ project.parent_project }}</a>
  
  </h4>

{% else %}
  
  <h4>{{ project.parent_project }}</h4>

{% endif %}
  
  <div style="margin-left: 20px;">
    
  <h5 class="project-sub-title">
    
  <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
  
  </h5>
  
  <div class="project-description">
    
    {{ project.content | strip_html | truncatewords: 50 }}
    
  <a href="{{ project.url | relative_url }}" class="project-description-link">
    see more<span class="arrow">&rarr;</span>
  </a>
  
  </div>
  </div>
  
  {% endif %}

{% endfor %}

## {% include icon.html icon="fa-solid fa-check" %} Past Projects

{% assign past_projects = site.projects | where: "group", "finished" %}

{% for project in past_projects %}
  
{% if project.project_level == "parent" %}
    
#### [{{ project.title }}]({{ project.url | relative_url }})
  
<div class="project-description">
  
  {{ project.content | strip_html | truncatewords: 50 }}
  
  <a href="{{ project.url | relative_url }}" class="project-description-link">
    see more<span class="arrow">&rarr;</span>
  </a>
</div>
  
{% elsif project.project_level == "sub" %}
    
{% assign parent_project = site.projects | where: "title", project.parent_project | first %}
    
#### {{ parent_project.title }}

<div style="margin-left: 20px;">
  
##### [{{ project.title }}]({{ project.url | relative_url }})

<div class="project-description" style="margin-left: 20px;">
  
  {{ project.content | strip_html | truncatewords: 50 }}
  
  <a href="{{ project.url | relative_url }}" class="project-description-link">
    see more<span class="arrow">&rarr;</span>
  </a>
</div>
</div>
  
{% endif %}

{% endfor %}
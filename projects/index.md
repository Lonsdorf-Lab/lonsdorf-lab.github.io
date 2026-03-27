---
type: page
title: Projects
schema_type: project
nav:
  order: 2
  tooltip: Software, datasets, and more
---

## {% include icon.html icon="fa-solid fa-hourglass" %} Current Projects

{%- assign current_parent_projects = site.projects | where: "group", "on-going" | where: "project_level", "parent" -%}

{%- assign current_subprojects = site.projects | where: "group", "on-going" | where: "project_level", "sub" -%}

{%- for project in current_parent_projects -%}
  
  <h4 class="project-title">
    
    <a href="{{ project.url | relative_url }}">{{ project.title }}</a>
  
  </h4>
  
  <div class="project-description">
    
  {{ project.content | strip_html | truncatewords: 50 }}
  
  <a href="{{ project.url | relative_url }}" class="project-description-link">
    see more<span class="arrow">&rarr;</span>
  </a>
  
  </div>

{%- endfor -%}

{%- assign parent_projects = "" | split: "" -%}

{%- for project in current_subprojects -%}
  
  {%- unless parent_projects contains project.parent_project -%}
    
  {%- assign parent_projects = parent_projects | push: project.parent_project -%}
  
  {%- endunless -%}

{%- endfor -%}

{%- for parent in parent_projects -%}
  
  {%- assign parent_subprojects = current_subprojects | where: "parent_project", parent -%}
  
  {%- assign example_project = parent_subprojects[0] -%}
  
  {%- if example_project.parent_project_url -%}
    
  <h4 class="project-parent-title">
    
    <a href="{{ example_project.parent_project_url }}" target="_blank" rel="noopener">{{ parent }}</a>
  
  </h4>
  
  {%- else -%}
  
  <h4 class="project-parent-title">{{ parent }}</h4>
  
  {%- endif -%}
  
  {%- for project in parent_subprojects -%}
  
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
  
  {%- endfor -%}

{%- endfor -%}


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
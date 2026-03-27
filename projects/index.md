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
{% assign parent_projects = current_projects | where: "project_level", "parent" %}
{% assign sub_projects = current_projects | where: "project_level", "sub" %}

{% for parent in parent_projects %}
  
  <h4 class="project-title">
    
    {% if parent.external_url %}
      
      <a href="{{ parent.external_url }}" target="_blank" rel="noopener">{{ parent.title }}</a>
    
    {% else %}
      
      <a href="{{ parent.url | relative_url }}">{{ parent.title }}</a>
    
    {% endif %}
  
  </h4>
  
  <div class="project-description">
    
    {{ parent.content | strip_html | truncatewords: 50 }}
    
    <a href="{{ parent.url | relative_url }}" class="project-description-link">
      see more<span class="arrow">&rarr;</span>
    </a>
  
  </div>

  {% assign sublist = sub_projects | where: "parent_project", parent.title %}
  
  {% for sub in sublist %}
    
    <div style="margin-left: 20px;">
      
      <h5 class="project-sub-title">
        <a href="{{ sub.url | relative_url }}">{{ sub.title }}</a>
      </h5>
      
      <div class="project-description">
        
        {{ sub.content | strip_html | truncatewords: 50 }}
        
        <a href="{{ sub.url | relative_url }}" class="project-description-link">
          see more<span class="arrow">&rarr;</span>
        </a>
      
      </div>
    
    </div>
  
  {% endfor %}

{% endfor %}

## {% include icon.html icon="fa-solid fa-check" %} Past Projects

{% assign past_projects = site.projects | where: "group", "finished" %}
{% assign parent_projects = past_projects | where: "project_level", "parent" %}
{% assign sub_projects = past_projects | where: "project_level", "sub" %}

{% for parent in parent_projects %}
  <h4 class="project-title">
    {% if parent.external_url %}
      <a href="{{ parent.external_url }}" target="_blank" rel="noopener">{{ parent.title }}</a>
    {% else %}
      <a href="{{ parent.url | relative_url }}">{{ parent.title }}</a>
    {% endif %}
  </h4>
  <div class="project-description">
    {{ parent.content | strip_html | truncatewords: 50 }}
    <a href="{{ parent.url | relative_url }}" class="project-description-link">
      see more<span class="arrow">&rarr;</span>
    </a>
  </div>

  {% assign sublist = sub_projects | where: "parent_project", parent.title %}
  {% for sub in sublist %}
    <div style="margin-left: 20px;">
      <h5 class="project-sub-title">
        <a href="{{ sub.url | relative_url }}">{{ sub.title }}</a>
      </h5>
      <div class="project-description">
        {{ sub.content | strip_html | truncatewords: 50 }}
        <a href="{{ sub.url | relative_url }}" class="project-description-link">
          see more<span class="arrow">&rarr;</span>
        </a>
      </div>
    </div>
  {% endfor %}
{% endfor %}

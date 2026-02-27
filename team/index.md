---
type: page
title: Team
schema_type: "team"
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %} Team

We are an interdisciplinary team with diverse expertise in psychology, philosophy, computer science, and the social, behavioral, and cognitive and computational neurosciences. Together, we investigate the neurobiological foundations of fear, anxiety, adversity, and stress-related processes. We are committed to open, transparent, and reproducible science — and we deeply value collaboration and teamwork.

{% include section.html %}

## Current Lab Members

{% assign team_current_members = "" | split: "" %}
{% assign member_group = site.members | where: "group", "member" %}

{% for m in member_group %}
  {% unless m.role == "undergrad" %}
    {% assign team_current_members = team_current_members | push: m %}
  {% endunless %}
{% endfor %}

{% include people.html persons=team_current_members kind="member" view="portrait" role_priority=site.data.people.team_overview_role_priority %}
{% include section.html %}

## Coming Soon

{% assign team_coming_soon = site.members | where: "group", "coming-soon" %}
{% include people.html persons=team_coming_soon kind="member" view="portrait" %}
{% include section.html %}

## Student Assistants & Research Interns

{% assign team_assistants = "" | split: "" %}

{% for m in site.members %}
  {% if m.group == "member" and m.role == "undergrad" %}
    {% assign team_assistants = team_assistants | push: m %}
  {% endif %}
{% endfor %}

{% include people.html persons=team_assistants kind="member" view="small" %}

## Alumni

{% assign team_alumni = site.members | where: "group", "alum" %}

{% include people.html persons=team_alumni kind="member" view="small" %}

{% include section.html background="images/background.png" dark=false %}

{{ current_members | size }}
{{ coming_soon | size }}
{{ undergrads | size }}
{{ alumni | size }}

**Interested in joining the lab?**

We always seek motivated postdoctoral researchers, PhD students and Master students as well as research interns. Candidates interested in joining the lab are strongly encouraged to apply for fellowships. Please contact us if you are interested.

{% include section.html %}

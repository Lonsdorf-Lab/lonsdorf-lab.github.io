---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team


We are an interdisciplinary team with diverse expertise in psychology, philosophy, computer science, and the social, behavioral, and cognitive and computational neurosciences. Together, we investigate the neurobiological foundations of fear, anxiety, adversity, and stress-related processes. We are committed to open, transparent, and reproducible science — and we deeply value collaboration and teamwork. 


{% include section.html %}

# Current Lab Members

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator' and group != 'alum'" %}
{% include list.html data="members" component="portrait" filter="role == 'team-coordinator' and group != 'alum'" %}
{% include list.html data="members" component="portrait" filter="role == 'postdoc' and group != 'alum'" %}
{% include list.html data="members" component="portrait" filter="role == 'phd' and group != 'alum'" %}

{% include section.html %}

# Student Assistants & Research Interns

{% include list.html data="members" component="portrait" filter="role == 'undergrad' and group != 'alum'" style="small" %}

{% include section.html background="images/background.png" dark=true %}

Interested in joining the lab?
We always seek motivated postdoctoral researchers, PhD students and Master students as well as research interns. Candidates interested in joining the lab are strongly encouraged to apply for fellowships. Please contact us if you are interested.

{% include section.html %}

## Alumni

{% capture content %}

{% include list.html data="members" component="portrait" filter="group == 'alum'" style="small" %}

{% endcapture %}

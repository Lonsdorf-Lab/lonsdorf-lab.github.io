---
title: Team
nav:
  order: 3
  tooltip: About our team
---

# {% include icon.html icon="fa-solid fa-users" %}Team


We are an interdisciplinary team with diverse expertise in psychology, philosophy, computer science, and the social, behavioral, and cognitive and computational neurosciences. Together, we investigate the neurobiological foundations of fear, anxiety, adversity, and stress-related processes. We are committed to open, transparent, and reproducible science — and we deeply value collaboration and teamwork. 


{% include section.html %}

{% include list.html data="members" component="portrait" filter="role == 'principal-investigator'" %}
{% include list.html data="members" component="portrait" filter="role == 'secretary'" %}
{% include list.html data="members" component="portrait" filter="role == 'postdoc'" %}
{% include list.html data="members" component="portrait" filter="role == 'phd'" %}
{% include list.html data="members" component="portrait" filter="role == 'undergrad'" %}

{% include section.html background="images/background.jpg" dark=true %}

Interested in joining the lab?
We always seek motivated postdoctoral researchers, PhD students and Master students as well as research interns. Candidates interested in joining the lab are strongly encouraged to apply for fellowships. Please contact us if you are interested.

{% include section.html %}

{% capture content %}

{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}
{% include figure.html image="images/photo.jpg" %}

{% endcapture %}

{% include grid.html style="square" content=content %}

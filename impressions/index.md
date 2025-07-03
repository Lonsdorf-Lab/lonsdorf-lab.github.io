---
title: Impressions
nav:
  order: 6
  tooltip: pictures
---

# {% include icon.html icon="fa-solid fa-users" %}Impressions of the Team

# PUG 2024
{% capture content %}
  {% include figure.html image="images/events/24pug/pic1.jpg" %}
  {% include figure.html image="images/events/24pug/pic2.jpg" width = "100%" %}
{% endcapture %}

{%
  include grid.html
  content=content
  style="square"
%}

# EMHFC 2024
{% capture content %}
  ![](images/events/24emhfc/pic1.jpg)
  ![](images/events/24emhfc/pic2.jpg)
  ![](images/events/24emhfc/pic3.jpg)
{% endcapture %}

{% include grid.html content=content %}

{% include section.html %}

# {% include icon.html icon="fa-solid fa-microscope" %}Impressions of the Lab

This part is currently under construction.

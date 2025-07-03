---
---

# Website of the Lonsdorf Lab

An engaging 1-3 sentence description of your lab.

{% include section.html %}

## Highlights

{% capture text %}

Find here all our publications.

{%
  include button.html
  link="publications"
  text="See our publications"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/rof.png"
  link="publications"
  title="Our Publications"
  text=text
%}

{% capture text %}

Get a glimpse into the work we do: from ongoing investigations to completed projects.

{%
  include button.html
  link="projects"
  text="Browse our projects"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/fearbase.jpg"
  link="projects"
  title="Our Projects"
  flip=true
  style="bare"
  text=text
%}

{% capture text %}

We are an interdisciplinary team with diverse expertise in psychology, philosophy, computer science, and the social, behavioral, and cognitive and computational neurosciences.

{%
  include button.html
  link="team"
  text="Meet our team"
  icon="fa-solid fa-arrow-right"
  flip=true
  style="bare"
%}

{% endcapture %}

{%
  include feature.html
  image="images/team1.jpg"
  link="team"
  title="Our Team"
  text=text
%}

---
title: Contact
nav:
  order: 5
  tooltip: Email, address, and location
---

# {% include icon.html icon="fa-regular fa-envelope" %}Contact

Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor
incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis
nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.

{%
  include button.html
  type="email"
  text="sekretariat-ae14@uni-bielefeld.de"
  link="sekretariat-ae14@uni-bielefeld.de"
%}
{%
  include button.html
  type="phone"
  text="+49-521-106-4482"
  link="+49-521-106-4482"
%}
{%
  include button.html
  type="address"
  tooltip="Our location on Google Maps for easy navigation"
  link="https://www.google.com/maps/place/Bielefeld+University/@52.0367271,8.4926664,17z/data=!3m2!4b1!5s0x47ba980fd0e9d4bb:0x2cc7502b92aebcec!4m6!3m5!1s0x47ba22b5ad10b98f:0xa128cd4b4ccac32d!8m2!3d52.0367238!4d8.4952413!16zL20vMDU5YmJj?entry=ttu&g_ep=EgoyMDI1MDIwOS4wIKXMDSoASAFQAw%3D%3D"
%}

{% include section.html %}

{% capture col1 %}

{%
  include figure.html
  image="images/team1.jpg"
  caption="PUG 2024"
%}

{% endcapture %}

{% capture col2 %}

{%
  include figure.html
  image="images/team2.jpg"
  caption="EMHFC 2024"
%}

{% endcapture %}

{% include cols.html col1=col1 col2=col2 %}
---
layout: archive
title: Publication
permalink: /publication/
---

{% include base_path %}

{% for post in site.publications reversed %}
  {% include archive-single.html %}
{% endfor %}

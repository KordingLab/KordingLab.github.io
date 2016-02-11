---
title: Reference
permalink: /resources/
---

We move all of [resources page](http://klab.smpp.northwestern.edu/wiki/index.php5/Resources)
from Kording lab page to here. We hope it will be must better and faster for people who want to share
and view it on mobile.

<hr>


{% assign reference_types = "scientists|students|discussion" | split: "|" %}

{% for type in reference_types %}

{% if type == 'scientists' %}
### **For scientists**
 {% elsif type == 'students' %}
### **For students, lab members**
 {% elsif type == 'discussion' %}
### **Random bits of discussion**
{% endif %}

<div class="content list">
  {% for post in site.posts %}
    {% if post.categories contains type %}
    <div class="list-item">
      <p class="list-post-title">
        <a href="{{ site.baseurl }}{{ post.url }}">- {{ post.title }}</a>
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>

<hr>
{% endfor %}

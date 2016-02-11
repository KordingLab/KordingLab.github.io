---
title: Reference
permalink: /resources/
---

We move all of [resources page](http://klab.smpp.northwestern.edu/wiki/index.php5/Resources)
from Kording lab page to here. We hope it will be must better and faster for people who want to share
and view it on mobile.

<hr>

### **For scientists**<br>

<div class="content list">
  {% for post in site.posts %}
    {% if post.categories contains 'scientists' %}
    <div class="list-item">
      <p class="list-post-title">
        <a href="{{ site.baseurl }}{{ post.url }}">- {{ post.title }}</a>
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>

<hr>

### **For students, lab members**<br>

<div class="content list">
  {% for post in site.posts %}
    {% if post.categories contains 'students' %}
    <div class="list-item">
      <p class="list-post-title">
        <a href="{{ site.baseurl }}{{ post.url }}">- {{ post.title }}</a>
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>

<hr>

### **Random bits of discussion**

<div class="content list">
  {% for post in site.posts %}
    {% if post.categories contains 'discussion' %}
    <div class="list-item">
      <p class="list-post-title">
        <a href="{{ site.baseurl }}{{ post.url }}">- {{ post.title }}</a>
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>

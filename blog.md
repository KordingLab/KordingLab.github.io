---
title: Blog
permalink: /blog/
---

### **Blog posts from the lab**

<div class="content list">
  {% for post in site.posts %}
    {% if post.categories contains 'blog' %}
    <div class="list-item">      
        <h5>
        <small>{{post.date | date: '%B %-d, %Y' }} </small><br />
        <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a>
        </h5>      
    </div>
    {% endif %}
  {% endfor %}
</div>

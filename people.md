---
title: People
permalink: /people/
---

<div class="content list">
  {% for profile in site.posts %}    
    {% if profile.categories contains 'people' %}
    <div class="list-item">
      <p class="list-post-title">
        <a href="{{ site.baseurl }}{{ profile.url }}">{{ profile.title }}</a>
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>

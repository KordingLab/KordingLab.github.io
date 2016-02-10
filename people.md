---
title: People
permalink: /people/
---

<div class="content list">
  {% for profile in site.people %}   
    <div class="list-item">
      <p class="list-post-title">
        <a href="{{ site.baseurl }}{{ profile.url }}">{{ profile.title }}</a>
      </p>
    </div>
  {% endfor %}
</div>
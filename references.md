---
title: Reference
permalink: /reference/
---

**all the useful stuff from Kording lab page**

<div class="content list">

  {% for ref in site.references %}
    <div class="list-item">
      <p class="list-post-title">
        <a href="{{ site.baseurl }}{{ ref.url }}">- {{ ref.title }}</a>
      </p>
    </div>
  {% endfor %}

</div>

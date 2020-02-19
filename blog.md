---
title: blog
permalink: /blog/
---

### **Blog posts from the lab**

<div class="content list">
  {% for post in site.posts %}
    {% if post.categories contains 'newblog' %}
    <div class="list-item">
      <p class="list-post-title">
        <a href="{{ post.url | prepend: site.baseurl }}">
            <div class="row">
                <div class="col-sm-4">
                    <img src="/{% if post.header-img %}{{ post.header-img }}{% else %}{{ site.header-img }}{% endif %}">
                </div>
                <div class="col-sm-8">
                    <h3 class="post-title">
                        {{ post.title }}
                    </h3>
                    <p class="post-meta">posted on {{ post.date | date: "%B %-d, %Y" }}</p>
                    {{ post.content | strip_html | truncatewords:30 }}
                </div>
            </div>
        </a>
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>


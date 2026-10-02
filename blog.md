---
title: blog
permalink: /blog/
---

### **Blog posts from the lab**

> **Konrad's blog has moved to Substack.** New posts appear at [Rethinking Brains, Data, and Science](https://kording.substack.com). The posts below are kept here as an archive.

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
                    <p class="list-post-title">
                      posted on {{ post.date | date: "%B %-d, %Y" }}
                    </p>
                    <p class="list-detail" >
                      {{ post.content | strip_html | truncatewords:30 }}
                    </p>
                </div>
            </div>
            <hr/>
        </a>
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>

---
title: Reference
permalink: /resources/
---

{% assign reference_types = "scientists|students|blog|discussion" | split: "|" %}

{% for type in reference_types %}

{% if type == 'scientists' %}
### **For scientists:**
 {% elsif type == 'students' %}
### **For students, lab members**
 {% elsif type == 'blog' %}
### **Blogs**
 {% elsif type == 'discussion' %}
### **Random bits of discussion**
{% endif %}

<div class="content list">
  {% for post in site.posts %}

    {% if post.categories contains type %}
    <div class="list-item">
      <p class="list-post-title">
        <a href="{{ post.url | prepend: site.baseurl }}">
            <div class="row">
                <div class="col-sm-4">
                    <img src="/{% if post.header-img %}{{ post.header-img }}{% else %}{{ site.header-img }}{% endif %}">
                </div>
                <div class="col-sm-8">
                    <h2 class="post-title">
                        {{ post.title }}
                    </h2>
                    {% if post.subtitle %}
                        {{ post.subtitle }}
                    {% endif %}
                    <p class="post-meta">Posted by {% if post.author %}{{ post.author }}{% else %}{{ site.title }}{% endif %} on {{ post.date | date: "%B %-d, %Y" }}</p>
                </div>
            </div>
        </a>
      </p>
    </div>
    {% endif %}

  {% endfor %}
</div>

<hr/>
{% endfor %}

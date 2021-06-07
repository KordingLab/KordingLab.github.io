---
title: Reference
permalink: /resources/
---

### Upcoming lab teachings

Every Friday at 13:30 EST, we get together (mix of virtual and in person) for lab teachings. 
On a rotating basis, each member of the lab speaks and teaches about something they know. 
Anything, really. Relevant and interesting topics, good skills to know, nice Python packages,
neuroscientific princples, new findings and literature reviews... whatever!

Get on the listserve for announcements: https://groups.google.com/forum/#!forum/kording-lab-teachings

[Click here for current topics (as of summer 2021)](http://kordinglab.com/2021/01/01/upcoming-lab-teaching.html)

{% assign reference_types = "scientists|students" | split: "|" %}

{% for type in reference_types %}

{% if type == 'scientists' %}
### **For scientists**
 {% elsif type == 'students' %}
### **For students, lab members**
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

### **Older Blog posts from the lab**

<div class="content list">
  {% for post in site.posts %}
    {% if post.categories contains 'blog' %}
    <div class="list-item">
      <p class="list-post-title">
        <a href="{{ site.baseurl }}{{ post.url }}">- {{ post.title }}</a> (<small>{{post.date | date: "%m/%d/%y" }}</small>)
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>

<hr>

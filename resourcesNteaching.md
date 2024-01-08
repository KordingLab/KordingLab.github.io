---
title: Reference
permalink: /resourcesNteaching/
---

### Upcoming lab teachings

Every Friday at 13:30 EST, we get together (mix of virtual and in person) for lab teachings (with food! sometimes). 
On a rotating basis, each member of the lab speaks and teaches about something they know or shares their work. 
Anything, really. Relevant and interesting topics, good skills to know, nice Python packages,
neuroscientific princples, new findings and literature reviews... whatever!

Get on the listserve for announcements: https://groups.google.com/forum/#!forum/kording-lab-teachings

### Spring 2024
| Date | Name | Topic |
|------|------|-------|
| Jan 19 | Konrad K | TBD |
| Jan 26 | K-lab retreat | N/A |
| Feb 2 |  |  |
| Feb 9 |  |  |
| Feb 16 |  |  |
| Feb 23 |   |   |
| Mar 1 | |  |
| Mar 8 |  |  |
| Mar 15 |  |  |
| Mar 22 |  |  |
| Mar 29 |  |  |
| Apr 5 |  |  |
| Apr 12 |  |  |
| Apr 19 |  |  |
| Apr 26 |  |  |
| May 3 |  |  |

<!--[Click here for current topics (as of summer 2021)](http://kordinglab.com/2021/01/01/upcoming-lab-teaching.html)-->

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

---
title: Reference
permalink: /resources/
---

### Upcoming lab teachings

Every Wednesday, we get together (over pizza, sometimes) for lab teachings. 
On a rotating basis, each member of the lab speaks and teaches about something they know. 
Anything, really. Relevant and interesting topics, good skills to know, nice Python packages,
neuroscientific princples, new findings and literature reviews... whatever!

Get on the listserve for announcements: https://groups.google.com/forum/#!forum/kording-lab-teachings

**Spring 2020 topics**

| Date | Name | Topic |
|------|------|-------|
| Jan. 15 | Ari | Variational Inference |
| Jan. 22 | Roozbeh | Why overparameterized deep networks generalize well? |
| Jan. 29 | Pedro | Canonical Correlation Analysis + Update on my research on dimensionality of populations of neurons |
| Feb. 5 |  |  |
| Feb. 12 |  |  |
| Feb. 19 | Brad Wyble | TBA |
| Feb. 26 | Tony | The deconfounder: blessing or curse? |
| Mar. 4 | Nidhi | TBA |
| Mar. 11 | Titipat | Canceled |
| Mar. 18 | Ben | Convex Optimization |
| Mar. 25 | Sebastien Tremblay | TBA |
| Apr. 1 |Rachit | Data Visualization|
| Apr. 8 | Alex Filipowicz | TBA |
| Apr. 15 | Ilenna | TBA |
| Apr. 22 | | |
| Apr. 29 | Ben Baker | Embodied Cognition |
| May 6 | Nachi Stern | Design and learning in physical networks |
| May 13 | | |

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

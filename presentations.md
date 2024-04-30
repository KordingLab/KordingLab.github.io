---
title: Reference
permalink: /presentations/
---

### Upcoming lab meetings

Every Friday at 13:30 EST, we get together (mix of virtual and in person) for lab presentations (with food! sometimes).
On a rotating basis, each member of the lab speaks and teaches about something they know or shares their work. 
Anything, really. Relevant and interesting topics, good skills to know, nice Python packages,
neuroscientific princples, new findings and literature reviews... anything!

Get on the [listserv for announcements](https://groups.google.com/forum/#!forum/kording-lab-teachings)

### Spring 2024
{% raw %}
| Date | Name | Topic |
|------|------|-------|
| Jan 16 [Tues] | Konrad K | TBD |
| Jan 26 [Fri] | K-lab retreat | N/A |
| Feb 2 | Lab business | Discussion |
| Feb 9 |Joey R. | Conformal Prediction |
| Feb 16 | Alessandro Lamacchia | Servers! |
| Feb 23 | Reading club | Episodic Memory |
| Mar 1 | Lab 1-1s | do 'em |
| Mar 8 | Lab 1-1s | do 'em |
| Mar 15 | ... | ... |
| Mar 22 | Tony | "Modern" Causal Inference |
| Mar 29 | ... | ... |
| Apr 5 |Felipe P | sts experiments, tracking |
| Apr 12 | Joey | How to program a brain |
| Apr 19 | 
| Apr 26 | ... | ... |
| May 3 | ... | ... |
| May 10 | Ilenna Jones | 

{% endraw %}

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

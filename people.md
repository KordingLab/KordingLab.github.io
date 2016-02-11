---
title: People
permalink: /people/
---

Visit each member's page to see photos, lists of publications, or to learn something about them.

### Principal Investigator

<div class="content list">
  {% for profile in site.people %}
    {% if profile.position contains 'pi' %}
    <div class="list-item">
      <p class="list-post-title">
        <img width="200" src="{{site.baseurl}}/images/people/{{profile.avatar}}">
        <a href="{{ site.baseurl }}{{ profile.url }}">{{ profile.name }}</a>
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>

<hr>

### Postdoctoral Fellows

<div class="content list">
  {% for profile in site.people %}
    {% if profile.position contains 'postdoc' %}
    <div class="list-item">
      <p class="list-post-title">
        <img width="200" src="{{site.baseurl}}/images/people/{{profile.avatar}}">
        <a href="{{ site.baseurl }}{{ profile.url }}">{{ profile.name }}</a>
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>

<hr>

### Graduate Students

<div class="content list">
  {% for profile in site.people %}
    {% if profile.position contains 'gradstudent' %}
    <div class="list-item">
      <p class="list-post-title">
        <img width="200" src="{{site.baseurl}}/images/people/{{profile.avatar}}">
        <a href="{{ site.baseurl }}{{ profile.url }}">{{ profile.name }}</a>
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>

<hr>

### Visiting Scholars

<div class="content list">
  {% for profile in site.people %}
    {% if profile.position contains 'visiting' %}
    <div class="list-item">
      <p class="list-post-title">
        <img width="200" src="{{site.baseurl}}/images/people/{{profile.avatar}}">
        <a href="{{ site.baseurl }}{{ profile.url }}">{{ profile.name }}</a>
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>

<hr>

### Others

<div class="content list">
  {% for profile in site.people %}
    {% if profile.position contains 'others' %}
    <div class="list-item">
      <p class="list-post-title">
        <img width="200" src="{{site.baseurl}}/images/people/{{profile.avatar}}">
        <a href="{{ site.baseurl }}{{ profile.url }}">{{ profile.name }}</a>
      </p>
    </div>
    {% endif %}
  {% endfor %}
</div>

<hr>

### Alumni

we are updating alumni page. we will put them up soon!

<hr>

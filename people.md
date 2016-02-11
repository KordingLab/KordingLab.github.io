---
title: People
permalink: /people/
---

{% assign people_sorted = (site.people | sort: 'joined' %}
{% assign people_array = "pi|postdoc|gradstudent|visiting|others" | split: "|" %}

{% for item in people_array %}

{% if item == 'postdoc' %}
### Postdoctoral Fellows
 {% elsif item == 'pi' %}
### Principal Investigator
 {% elsif item == 'gradstudent' %}
### Graduate Students
 {% elsif item == 'visiting' %}
### Visiting Scholars
 {% elsif item == 'others' %}
### Honorary Members
{% endif %}

<div class="content list">
  {% for profile in people_sorted %}
    {% if profile.position contains item %}
    <div class="list-item">
      <p class="list-post-title">
        {% if profile.avatar %}
        <a href="{{ site.baseurl }}{{ profile.url }}"><img width="200" src="{{site.baseurl}}/images/people/{{profile.avatar}}"></a>
        {% else %}
        <a href="{{ site.baseurl }}{{ profile.url }}"><img width="200" src="http://evansheline.com/wp-content/uploads/2011/02/facebook-Storm-Trooper.jpg"></a>
        {% endif %}
        <a href="{{ site.baseurl }}{{ profile.url }}">{{ profile.name }}</a>
      </p>
    </div>    
    {% endif %}
  {% endfor %}
</div>
<hr>
{% endfor %}

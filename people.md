---
title: People
permalink: /people/
---

{% assign people_sorted = site.people | sort: 'joined' %}
{% assign role_array = "pi|postdoc|gradstudent|researchstaff|visiting|others|alumni" | split: "|" %}

{% for role in role_array %}

{% assign people_in_role = people_sorted | where: 'position', role %}

<!-- Skip section if there's nobody -->
{% if people_in_role.size == 0 %}
  {% continue %}
{% endif %}

<div class="pos_header">
{% if role == 'postdoc' %}
<h3>Postdoctoral Fellows</h3>
 {% elsif role == 'pi' %}
<h3>Principal Investigator</h3>
 {% elsif role == 'gradstudent' %}
<h3>Graduate Students</h3>
 {% elsif role == 'researchstaff' %}
<h3>Research Staff</h3>
 {% elsif role == 'visiting' %}
<h3>Visiting Scholars</h3>
 {% elsif role == 'others' %}
<h3>Honorary Members</h3>
 {% elsif role == 'alumni' %}
<h3>Alumni</h3>
{% endif %}
</div>

{% if role != 'alumni' %}
<div class="content list people">
  {% for profile in people_sorted %}
    {% if profile.position contains role %}
      <div class="list-item-people">
        <p class="list-post-title">
          {% if profile.avatar %}
            <a href="{{ site.baseurl }}{{ profile.url }}"><img class="profile-thumbnail" src="{{site.baseurl}}/images/people/{{profile.avatar}}"></a>
          {% else %}
            <a href="{{ site.baseurl }}{{ profile.url }}"><img class="profile-thumbnail" src="http://evansheline.com/wp-content/uploads/2011/02/facebook-Storm-Trooper.jpg"></a>
          {% endif %}
          <a class="name" href="{{ site.baseurl }}{{ profile.url }}">{{ profile.name }}</a>
        </p>
      </div>    
    {% endif %}
  {% endfor %}
</div>
<hr>

{% else %}

<br>

| Who are they | When were they here | Where they went |
| :------------- |:-------------| :-----------|
| [David Rolnick](http://kordinglab.com/people/david_rolnick/index.html) | Postdoc (2018 - 2020) | [Assistant Professor](http://www.davidrolnick.com), Computer Science, McGill University and Mila |
| [Ethan Black](http://kordinglab.com/people/ethan_blackwood/index.html) | Rotation Student (2019) | Alex Proekt's Lab at UPenn |
| [Steve Antos](http://kordinglab.com/people/steve_antos/index.html) | Graduate Student (2012 - 2019) | - |
| [Sofia Triantafillou](https://www.dbmi.pitt.edu/node/54091) | Postdoc (2016 - 2018) | Asst Prof. at University of Pittsburgh |
| [Gaiqing Kong](https://gaiqingkong.github.io/) | Visiting Scholar (2016 - 2018) | Postdoc at UCL |
| Claire Chambers | Postdoc (2015 - 2018) | - |
| [Josh Glaser](https://jglaser2.github.io) | Graduate Student (2012 - 2018) | Postdoc at Columbia
| [Daniel Wood](http://kordinglab.com/people/daniel_wood/index.html) | Postdoc (2014 - 2017) | Postdoc at Northwestern |
| [Bahram Yoosefizonooz](http://kordinglab.com/people/bahram_yoosefizonooz/index.html) | Visiting (2017) | Postdoc at U Montreal
| Elahe Arani | Visiting (2017) | Postdoc at U Montreal
| [Luca Lonini](http://kordinglab.com/people/luca_lonini/index.html) | Postdoc (2017) | Postdoc with Arun at Northwestern U
| [Ravi Garg](http://kordinglab.com/people/ravi_garg/index.html) | Undergrad Research | Researcher at Northwestern U
| [Sohrob Saeb](http://kordinglab.com/people/sohrob_saeb/index.html) | Postdoc (2014 - 2017) | Neuroscience in Bay Area
| [Eva Dyer](http://kordinglab.com/people/eva_dyer/index.html) | Postdoc (2017) | Assistant Professor, Dept of Biomedical Engineering at Georgia Tech and Emory U
| [Pavan Ramkumar](http://kordinglab.com/people/pavan_ramkumar/index.html) | Postdoc (2017) | A secret startup in bay area
| [Ted Cybulski](http://kordinglab.com/people/ted_cybulski/index.html) | Graduate Student (2012 - 2017) | Medical resident at Northwestern |
| Xuelong Zhao | Postdoc (2016) | Postdoc at [Brian Litt  lab](http://littlab.seas.upenn.edu/), U Penn
| [Pat Lawlor](http://kordinglab.com/people/pat_lawlor/index.html) | Graduate student (2016) | Northwestern Medical school
| [Hugo Fernandes](http://kordinglab.com/people/hugo_fernandes/index.html) | Postdoc (2016) | [rockets of awesome](https://www.rocketsofawesome.com/)
| [Torben Noto](http://kordinglab.com/people/torben_noto/index.html) | Rotation Student (2016) | Northwestern
| [Vivek Sagar](http://kordinglab.com/people/vivek_sagar/index.html) | Rotation Student (2016) | Northwestern
| [David Brandfonbrener](http://kordinglab.com/people/david_brandfonbrener/index.html) | Visiting Scholar (2016)  | PhD Student, Yale university
| [Daniel E. Acuna](http://kordinglab.com/people/daniel_e_acuna/index.html) | Postdoc (2016) | [iSchool at Syracuse](https://ischool.syr.edu/people/directories/view/deacuna/)
| [Mohammad Azar](http://mgazar.net/academic/) | Postdoc (2016) | Google Deepmind, secret location in London |
| [Cong Yin (Lily)](http://kordinglab.com/people/cong_yin/index.html) | Visiting scholar (2015-2016) | Peking University |
| [Youguo Chen](https://scholar.google.com/citations?user=wZQdEFAAAAAJ&hl=zh-CN) | Visiting scholar (2014 - 2015) | Associate Professor, Southwest University, Chongqing, China
| [Max Berniker](http://sensorimotorcontrolatorium.uic.edu/)   | Postdoc (2014) | Asst Prof, Univ of Illinois at Chicago, Mechanical &amp; Industrial Eng |
| [Mathieu d'Acremont](https://scholar.google.com/citations?user=D7ys4VQAAAAJ&hl=en) | Postdoc (2014) | - |
| [Iris Vilares](https://scholar.google.com/citations?user=Ztwn608AAAAJ&hl=en)   | Graduate Student (2009-2013) | Postdoc, University of Virginia and University College London (w. Peter Dayan) |
| Ben Walker     | Research Engineer (2010-2013) | MS in ME at Northwestern University, Masanet lab |
| Bill Lotter    | Research Scientist (2012-2013)| PhD at MIT |
| Mark Albert	   | (Dec 2009 - Dec 2012) | Asst Prof, Loyola University, Computer Science |
| Yoshiyuki (Yoshi) Sato | Visiting Professor (2012 - 2013) | Asst Prof, Univ of Electro-Communications, Tokyo |
| Petra Conaway	Clinical | Coordinator (2012) | Continuing her work at RIC |
| Rich Li | Rotation Student (Fall 2012) | Continuing Rotations |
| James Ellis | Rotation Student (Fall 2012) | Continuing Rotations |
| Hamid Buini | Summer Intern (2012) | University of Southern Florida |
| AmberLace Moore | Summer Intern (2012) | Spelman College |
| Mayowa Agbaje-Williams | Clinical Coordinator (Summer 2012) | Univ. Illinois Chicago School of Pharmacy |
| Florian Neubauer | Visiting Scholar (2011 - 2012) | PostDoc in Switerland |
| Qiang (Chris) Chen | Rotation Student (Spring 2012) | Raphael Pinaud's lab at Northwestern |
| Ranit Sengupta | Rotation Student (Fall 2011) | Finishing rotations |
| [Ian Stevenson](http://stevenson.lab.uconn.edu/) | Grad Student (2006-2011) | Asst Prof. University of Connecticut |
| Andrew Cichowski | MD rotation student (Summer 2011) | Feinberg Med School MD program |
| James Howard | Rotation Student (Winter 2009) | Jay Gottfried's Lab at Northwestern |
| Kunlin Wei | Postdoc (2006-2009) | Assc Prof, Beijing University, Dept of Psychology |
| Ricardo Ruiz Torres | Rotation Student (Spring 2009) | Lee Miller's Lab at Northwestern |
| Gregory Dam | Grad Student (2006-2009) | Jim Houk's Lab at Northwestern |
| Daniel Wert | SINE Intern (2008) | BME Grad student at LeTourneau University |
| Nicholas Bowman | Rotation Student (Winter 2007) | Jay Gottfried's Lab at Northwestern |
| Taro Kiritani | Rotation Student (Winter 2007) | Gordon Shepard's Lab at Northwestern |
| Rashmi Sarnaik | Rotation Student (Winter 2007) | JC Cang's Lab at Northwestern |
| Emily Oby | Rotation Student (Fall 2006) | Lee Miller's Lab at Northwestern |

{% endif %}
{% endfor %}

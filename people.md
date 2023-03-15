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
| [Ari Benjamin](https://ari-benjamin.com/) | Graduate student (2016-2022) | Postdoc with Tony Zador at Cold Spring Harbor Laboratory |
| [Titipat Achakulvisut](https://kordinglab.com/people/titipat_achakulvisut/.index.html) | Graduate Student (2014 - 2021) | [Biomedical and Data Lab](https://biodatlab.github.io/), Dept of Biomedical Engineering, Mahidol University, Thailand |
| [Pedro Ribeiro](https://www.linkedin.com/in/pedro-ribeiro/) | Graduate Student (2018 - 2021) | Programmer Analyst at Cedars-Sinai Department of Computational Biomedicine|
[Nidhi Seethapathi](https://www.seethapathilab.org) | Postdoc (2018 - 2021) | Assistant Professor at MIT BCS and EECS |
| [Ben Lansdell](http://benlansdell.github.io) | Postdoc (2017 - 2020) | Data Scientist at St. Jude Children's Research Hospital |
| [David Rolnick](http://kordinglab.com/people/david_rolnick/index.html) | Postdoc (2018 - 2020) | [Assistant Professor](http://www.davidrolnick.com), Computer Science, McGill University and Mila |
| [Shaofei Wang](http://kordinglab.com/people/shaofei_wang/index.html) | Researcher (2018 - 2020) | PhD Student, Computer Science, ETH Zurich |
| [Ethan Blackwood](http://kordinglab.com/people/ethan_blackwood/index.html) | Rotation Student (2019) | Alex Proekt's Lab at UPenn |
| [Steve Antos](http://kordinglab.com/people/steve_antos/index.html) | Graduate Student (2012 - 2019) | Analytics Developer |
| [Sofia Triantafillou](https://www.dbmi.pitt.edu/node/54091) | Postdoc (2016 - 2018) | Assistant Professor of Biomedical Informatics at University of Pittsburgh |
| [Gaiqing Kong](https://gaiqingkong.github.io/) | Visiting Scholar (2016 - 2018) | Fyssen Foundation Postdoc at INSERM, France |
| [Claire Chambers](http://kordinglab.com/people/claire_chambers/index.html)  | Postdoc (2015 - 2018) | Data Scientist in Ireland |
| [Josh Glaser](https://jglaser2.github.io) | Graduate Student (2012 - 2018) | Postdoc at Columbia |
| [Daniel Wood](http://kordinglab.com/people/daniel_wood/index.html) | Postdoc (2014 - 2017) | Data Scientist at SharpestMinds |
| [Bahram Yoosefizonooz](http://kordinglab.com/people/bahram_yoosefizonooz/index.html) | Visiting (2017) | NavInfo Europe |
| Elahe Arani | Visiting (2017) | NavInfo Europe |
| [Luca Lonini](http://kordinglab.com/people/luca_lonini/index.html) | Postdoc (2017) | Research Scientist at Shirley Ryan Ability Lab |
| [Ravi Garg](http://kordinglab.com/people/ravi_garg/index.html) | Undergrad Research | MBA Candidate at Kellogg School |
| [Sohrob Saeb](http://kordinglab.com/people/sohrob_saeb/index.html) | Postdoc (2014 - 2017) | Data Scientist at Verily |
| [Eva Dyer](http://kordinglab.com/people/eva_dyer/index.html) | Postdoc (2017) | Assistant Professor of Biomedical Engineering at Georgia Tech and Emory U |
| [Pavan Ramkumar](http://kordinglab.com/people/pavan_ramkumar/index.html) | Postdoc (2017) | Director of ML at Herophilus |
| [Ted Cybulski](http://kordinglab.com/people/ted_cybulski/index.html) | Graduate Student (2012 - 2017) | Internal Medicine Resident at Northwestern |
| Xuelong Zhao | Postdoc (2016) | Postdoc at [Brian Litt  lab](http://littlab.seas.upenn.edu/), U Penn |
| [Pat Lawlor](http://kordinglab.com/people/pat_lawlor/index.html) | Graduate student (2016) | Resident Physician at Children's Hospital of Philadelphia |
| [Hugo Fernandes](http://kordinglab.com/people/hugo_fernandes/index.html) | Postdoc (2016) | [rockets of awesome](https://www.rocketsofawesome.com/) |
| [Torben Noto](http://kordinglab.com/people/torben_noto/index.html) | Rotation Student (2016) | PhD Student w/ Christina Zelano at Northwestern |
| [Vivek Sagar](http://kordinglab.com/people/vivek_sagar/index.html) | Rotation Student (2016) | PhD Student w/ Thorsten Kahnt at Northwestern |
| [David Brandfonbrener](http://kordinglab.com/people/david_brandfonbrener/index.html) | Visiting Scholar (2016)  | PhD Student w/ Joan Bruna at NYU |
| [Daniel E. Acuna](http://kordinglab.com/people/daniel_e_acuna/index.html) | Postdoc (2016) | Assistant Professor of [iSchool at Syracuse](https://ischool.syr.edu/people/directories/view/deacuna/) |
| [Mohammad Azar](http://mgazar.net/academic/) | Postdoc (2016) | Google Deepmind, London |
| [Cong Yin (Lily)](http://kordinglab.com/people/cong_yin/index.html) | Visiting scholar (2015-2016) | Peking University |
| [Youguo Chen](https://scholar.google.com/citations?user=wZQdEFAAAAAJ&hl=zh-CN) | Visiting scholar (2014 - 2015) | Associate Professor, Southwest University, Chongqing, China |
| [Max Berniker](http://sensorimotorcontrolatorium.uic.edu/)   | Postdoc (2014) | Data Scientist at Intuitive |
| [Mathieu d'Acremont](https://scholar.google.com/citations?user=D7ys4VQAAAAJ&hl=en) | Postdoc (2014) | Lead Data Scientist at CVS Health |
| [Iris Vilares](https://scholar.google.com/citations?user=Ztwn608AAAAJ&hl=en)   | Graduate Student (2009-2013) | Assistant Professor of Psychology at University of Minnesota |
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
| Ranit Sengupta | Rotation Student (Fall 2011) | Data Analyst |
| [Ian Stevenson](http://stevenson.lab.uconn.edu/) | Grad Student (2006-2011) | Associate Professor of Psychology at University of Connecticut |
| Andrew Cichowski | MD rotation student (Summer 2011) | Neurologist at Guadalupe Regional Medical Center |
| James Howard | Rotation Student (Winter 2009) | Assistant Professor of Psychology at Brandeis University |
| Kunlin Wei | Postdoc (2006-2009) | Professor of Psychology and Cog Sci at Peking University |
| Ricardo Ruiz Torres | Rotation Student (Spring 2009) | Vicarious Surgical Inc. |
| Gregory Dam | Grad Student (2006-2009) | Assistant Professor of Psychology at Indiana University |
| Daniel Wert | SINE Intern (2008) | ALIVE Industries |
| Nicholas Bowman | Rotation Student (Winter 2007) | Senior Data Scientist at IsoPlexis |
| Taro Kiritani | Rotation Student (Winter 2007) | ExaWizards Inc. in Tokyo |
| Rashmi Sarnaik | Rotation Student (Winter 2007) | Scientific Editor at Neuron |
| Emily Oby | Rotation Student (Fall 2006) | Postdoc w/ Aaron Batista at University of Pittsburgh |

{% endif %}
{% endfor %}

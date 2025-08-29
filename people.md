---
title: People
permalink: /people/
---

### Lab Members

Our research group is remarkably interdisciplinary. Our interests span statistics, physics, biology, applied mathematics, molecular biology, metascience, cognitive science, and many other disciplines. Each person brings unique expertise that contributes to our mission of understanding intelligence, causality, and complex systems.

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
            <a href="{{ site.baseurl }}{{ profile.url }}"><img class="profile-thumbnail" src="https://via.placeholder.com/200x200?text=No+Photo"></a>
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
| [Tony Liu](https://tliutony.github.io/) | Graduate Student (2018-2024) | Assistant Professor of Computer Science, Mount Holyoke College |
| [Xinyue Wang](https://www.charonwangg.com/) | Graduate Student (2021-2023) | PhD Student, Halıcıoğlu Data Science Institute, UCSD |
| [Ilenna Jones](https://www.ilenna.com/) | Graduate Student (2017-2023) | Postdoc, Kemptner Institute, Harvard|
| [Ben Baker](https://www.tbenbaker.com/) | Post-doc (2021-2023) | Assistant Professor of Philosophy at Colby|
| [Richard Lange](https://www.rit.edu/directory/rdlvcs-richard-lange)  | Post-doc (2021-2023) | Assistant Professor at Rochester University|
| Justin Brantley | Post-doc (2021-2023) | Data Scientist, Texas Rangers, yes they did win the super something twice in a row after he joined them |
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
| [Max Berniker](http://sensorimotorcontrolatorium.uic.edu/) | Postdoc (2014) | Senior Data Scientist, Intuitive Surgical |
| [Mathieu d'Acremont](https://scholar.google.com/citations?user=D7ys4VQAAAAJ&hl=en) | Postdoc (2014) | Lead Data Scientist, CVS Health |
| [Iris Vilares](https://scholar.google.com/citations?user=Ztwn608AAAAJ&hl=en) | Graduate Student (2009-2013) | Assistant Professor of Psychology, University of Minnesota |
| Ben Walker | Research Engineer (2010-2013) | M.S. Graduate, Mechanical Engineering, Northwestern University |
| [William Lotter](https://semenovlab.org/) | Research Scientist (2012-2013) | Assistant Professor, Harvard Medical School & Dana-Farber |
| Mark Albert | (Dec 2009-Dec 2012) | Associate Professor, Computer Engineering, University of North Texas |
| Yoshiyuki "Yoshi" Sato | Visiting Professor (2012-2013) | Assistant Professor, University of Electro-Communications, Tokyo |
| Petra Conaway | Clinical Coordinator (2012) | Clinical Coordinator, Shirley Ryan AbilityLab |
| Rich Li | Rotation Student (Fall 2012) | Continuing Rotations |
| James Ellis | Rotation Student (Fall 2012) | Continuing Rotations |
| Hamid Buini | Summer Intern (2012) | University of South Florida |
| AmberLace Moore | Summer Intern (2012) | Spelman College |
| Mayowa Agbaje-Williams | Clinical Coordinator (Summer 2012) | U. of Illinois Chicago, College of Pharmacy |
| Florian Neubauer | Visiting Scholar (2011-2012) | Postdoctoral Researcher, Switzerland |
| Qiang "Chris" Chen | Rotation Student (Spring 2012) | Postdoctoral Researcher, Northwestern (Pinaud Lab) |
| Ranit Sengupta | Rotation Student (Fall 2011) | Data Analyst |
| [Ian Stevenson](http://stevenson.lab.uconn.edu/) | Grad Student (2006-2011) | Associate Professor of Psychology, University of Connecticut |
| Andrew Cichowski | MD rotation student (Summer 2011) | Neurologist, Guadalupe Regional Medical Center (Texas) |
| James Howard | Rotation Student (Winter 2009) | Assistant Professor of Psychology, Brandeis University |
| Kunlin Wei | Postdoc (2006-2009) | Professor of Psychology & Cognitive Science, Peking University |
| Ricardo Ruiz Torres | Rotation Student (Spring 2009) | Engineer (Robotics), Vicarious Surgical, Inc. |
| Gregory Dam | Grad Student (2006-2009) | Assistant Professor of Psychology, Indiana University |
| Daniel Wert | SINE Intern (2008) | ALIVE Industries |
| Nicholas Bowman | Rotation Student (Winter 2007) | Senior Data Scientist, IsoPlexis (now PhenomeX) |
| Taro Kiritani | Rotation Student (Winter 2007) | AI Engineer, ExaWizards, Inc. (Tokyo) |
| Rashmi Sarnaik | Rotation Student (Winter 2007) | Scientific Editor, Neuron |
| Emily Oby | Rotation Student (Fall 2006) | Assistant Professor, Queen's University, Kingston |

{% endif %}
{% endfor %}

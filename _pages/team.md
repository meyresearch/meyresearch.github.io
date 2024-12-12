---
title: "Mey Research group - team"
layout: gridlay
excerpt: "Mey Research group: Team members"
sitemap: false
permalink: /team/
---

# The group

 <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/group_photo.jpg" width="50%" style="float: center" />


## Team Lead

<div>
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/me2.jpg" class="img-responsive" width="20%" style="float: left" />
  <h4>Antonia Mey</h4>
  <i>Chancellor's Fellow, April 2021 -<br>
  <i>Christina Miller Fellow, Jan 2020 - March 2021<br>email: [antonia.mey@ed.ac.uk](mailto:antonia.mey@ed.ac.uk)<br>
    A full CV is available [here]({{ site.url }}{{ site.baseurl }}/downloads/cv.pdf). </i>
  <ul style="overflow: hidden">
  <li> BSc Physics with Chemistry, Keele University </li>
  <li> PhD University of Nottingham with  <a href="https://www.nottingham.ac.uk/~ppzjpg/About.html">Juan Garrahan</a> </li>
  <li>Postdoc Freie Universität Berlin with <a href="https://www.mi.fu-berlin.de/en/math/groups/comp-mol-bio/index.html">Frank Noe</a> </li>
  <li> Postdoc University of Edinburgh with <a href="http://www.julienmichel.net/lab/">Julien Michel</a> </li>
 </ul>

 </div>


## Team Members

{% assign number_printed = 0 %}
{% for member in site.data.team_members %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  {{ member.info }}
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  {% endif %}

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}



## Master, Bachelor Student and Visiting Students
{% assign number_printed = 0 %}
{% for member in site.data.students %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <ul style="overflow: hidden">

  {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %}

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  {% endif %}

  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

# Joining the group

### Open Positions

We have a few open positions in the group:

- [New Methods for Metalloenzyme Modelling](https://www.findaphd.com/phds/project/new-methods-for-metalloenzyme-modelling-to-combat-antimicrobial-resistance/?p180105) (Deadline 17/Jan/2025)
- [Integration of Property Predictions with Molecule Generation using Reinforcement Learning](https://www.ai4biomed.io/research/projects-2025/#accordion-675b166c3f2a3) (Deadline 20/Jan/2025)


And joint with other groups:

- [Design and synthesis of chemical probes to understand the role of glucokinase in pancreatic β-cell function](https://www.findaphd.com/phds/project/eastbio-dtp-design-and-synthesis-of-chemical-probes-to-understand-the-role-of-glucokinase-in-pancreatic-cell-function/?p180041) (Deadline 17/Jan2025 - joint with Chris Coxon's group).  
- [Data-driven Catalyst Optimization for CO2 Utilization Reactions](https://www.findaphd.com/phds/project/e5-dtp-data-driven-catalyst-optimization-for-co2-utilization-reactions/?p180199) (Deadline 06/Jan/2025 joint with Ephrath Solel's group)

**Expression of interest:** Please send an email to [Antonia Mey](mailto:antonia.mey@ed.ac.uk) with the specific title of the project you are interested in. Please attach a brief CV to your email. 

If you want to apply for a prize studentship you will need to register on Euclid prior to 16/12/2024. Please get in touch via email if you are interested as soon as possible. More details are found here:

[Prize Studentships at Edinburgh](https://chem.ed.ac.uk/studying/phd/studentships/prize-phd-scholarships)


### Applications for PhD and Postdoc positions
Are you interested in working on exiting challenges around anticmicrobial resistance looking at ways to combine machine learning and molecular simulations? 

Please get in touch by [email](mailto:antonia.mey@ed.ac.uk) to discuss different opportunities to join the group, or take a look at some of these PhD and Postdoc funding opportunities: 

If you are interested in working with us as a PhD student or postdoc, please send me an [email](mailto:antonia.mey@ed.ac.uk). 
If there is no specific opening advertise take a look at some of the following opportunities for PhD students:   
* [University of Edinburgh Scholarship and Student Funding Services](https://www.ed.ac.uk/student-funding)   
* [Commonwealth Scholarships](http://cscuk.dfid.gov.uk)    
* [Fullbright Scholarships](http://us.fulbrightonline.org/home.html)       
* [Marshall Scholarships](http://www.marshallscholarship.org)     
* [Chevening scholarships](https://www.chevening.org/scholarships/)       
* [Scottish Overseas Research Students Awards Scheme](https://www.gov.uk/government/organisations/foreign-commonwealth-office/about#our-funding-programmes)   


And for Postdocs:   
* [Marie Curie Fellowship](https://ec.europa.eu/research/mariecurieactions/actions/individual-fellowships_en)   
* [Newton Fellowship](https://royalsociety.org/grants-schemes-awards/grants/newton-international/)   
* [Leverhulme fellowship](https://www.leverhulme.ac.uk)   

Generally if you are looking for postdoc funding, there is a great resource for fellowships/fundinding opportunities around the world:
[postdoc funding schemes](https://asntech.github.io/postdoc-funding-schemes/)

   
### Undergraduate student projects
The group is happy to accommodate students from various disciplines, not just Chemistry. Ideally suited candidates are students in Chemistry, Physics, Computer Science, Biochemistry or Biotechnology, provided you have keen interest in exploring the interplay between Biology, Chemistry, and computational modelling and machine learning.  

### Summer student projects
Please send me an [email](mailto:antonia.mey@ed.ac.uk) if you are interested in doing a summer research project to discuss possible available options. 

Deadlines for summer projects are usually quite early in the year (end of January). Here is a none exhaustive list of funding sources:

* [Royal Society of Chemistry](https://www.rsc.org/ScienceAndTechnology/Funding/undergraduate-bursary.asp)
* [Carnegie Trust](https://www.carnegie-trust.org/award-schemes/vacation-scholarships/)
* [Edinburgh University Vacation](https://uoe.sharepoint.com/sites/CSCE/AcademicAffairs/SitePages/College-Vacation-Scholarships.aspx)

### There are no current open positions! 

## Former members
<div class="row">

<div class="col-sm-4 clearfix">
<h4>Postdocs and PhD students</h4>
{% for member in site.data.alumni_members %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Master students</h4>
{% for member in site.data.alumni_msc %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Bachelor Students</h4>
{% for member in site.data.alumni_bsc %}
{{ member.name }}
{% endfor %}
</div>

<div class="col-sm-4 clearfix">
<h4>Visitors</h4>
{% for member in site.data.alumni_visitors %}
{{ member.name }}
{% endfor %}
</div>

</div>

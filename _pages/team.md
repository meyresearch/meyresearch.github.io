---
title: "Team"
layout: gridlay
sitemap: false
permalink: /team/
---

# The group

## Team Lead

<div>
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/me3.jpg" class="img-responsive" width="10%" style="float: left" />
  <h4><a href='https://shuhaozhangtony.github.io/'>Shuhao Zhang</a></h4>  
  <i>Assistant Professor, Nanyang Technological University Nov 2023 - <br>email: [shuhao.zhang@ntu.edu.sg](mailto:shuhao.zhang@ntu.edu.sg)<br>
    A full CV is available [here]({{ site.url }}{{ site.baseurl }}/downloads/cv.pdf). </i>
  <ul style="overflow: hidden">
  <li> BSc Computer Engineering, Nanyang Technological University </li>
  <li> PhD National University of Singapore with 
	<a href="https://www.comp.nus.edu.sg/~hebs/">Bingsheng He</a> 
  </li>
  <li>Postdoc Technische Universität Berlin with 
	<a href="https://www.dima.tu-berlin.de/menue/staff/volker_markl/">Volker Markl</a> 
  </li>
 </ul>
</div>

<br>

## PG Students

{% assign number_printed = 0 %}
{% for member in site.data.phds %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="img-responsive" width="25%" style="float: left" />
  <h4>{{ member.name }}</h4>
  <ul style="overflow: hidden">
  <li> {{ member.info }} </li>
  </ul>
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

## Research Staffs
{% assign number_printed = 0 %}
{% for member in site.data.staffs %}

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

## Visiting Students/Interns
{% assign number_printed = 0 %}
{% for member in site.data.visitors %}

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

<div markdown="0" id="carousel" class="carousel slide" data-ride="carousel" data-interval="3000" data-pause="hover" >
    <!-- Menu -->
    <ol class="carousel-indicators">
        <li data-target="#carousel" data-slide-to="0" class="active"></li>
        <li data-target="#carousel" data-slide-to="1"></li>
        <li data-target="#carousel" data-slide-to="2"></li>
        <li data-target="#carousel" data-slide-to="3"></li>
        <li data-target="#carousel" data-slide-to="4"></li>
        <li data-target="#carousel" data-slide-to="5"></li>
        <li data-target="#carousel" data-slide-to="6"></li>
    </ol>

    <!-- Items -->
<div class="carousel-inner" markdown="0">
    <div class="item active">
        <img src="{{ site.url }}{{ site.baseurl }}/images/outreach/Shuhao_huashi2023.PNG" alt="Slide 1" style="height: 400px; width: 100%; object-fit: contain;" />
        <div class="carousel-caption">
            <p>Shuhao presenting at East China Normal University 2023 December</p>
        </div>
    </div>
    <div class="item">
        <img src="{{ site.url }}{{ site.baseurl }}/images/outreach/Shuhao_tsinghua2023.JPG" alt="Slide 2" style="height: 400px; width: 100%; object-fit: contain;" />
        <div class="carousel-caption">
            <p>Shuhao presenting at Tsinghua University 2023 December</p>
        </div>
    </div>
    <div class="item">
        <img src="{{ site.url }}{{ site.baseurl }}/images/outreach/Shuhao_USTB2023.JPG" alt="Slide 3" style="height: 400px; width: 100%; object-fit: contain;" />
        <div class="carousel-caption">
            <p>Shuhao presenting at University of Science and Technology Beijing 2023 December</p>
        </div>
    </div>
    <div class="item">
        <img src="{{ site.url }}{{ site.baseurl }}/images/outreach/Shuhao_SHJT2023.JPG" alt="Slide 4" style="height: 400px; width: 100%; object-fit: contain;" />
        <div class="carousel-caption">
            <p>Shuhao presenting at Shanghai Jiaotong University 2023 December</p>
        </div>
    </div>
    <div class="item">
        <img src="{{ site.url }}{{ site.baseurl }}/images/outreach/Xianzhi_ICDE2023.jpg" alt="Slide 5" style="height: 400px; width: 100%; object-fit: contain;" />
        <div class="carousel-caption">
            <p>Xianzhi Zeng presenting at ICDE USA 2023 April</p>
        </div>
    </div>
    <div class="item">
        <img src="{{ site.url }}{{ site.baseurl }}/images/outreach/Shuhao_RUC2023.jpg" alt="Slide 6" style="height: 400px; width: 100%; object-fit: contain;" />
        <div class="carousel-caption">
            <p>Shuhao Zhang presenting at Renmin University of China 2023 Sep</p>
        </div>
    </div>	
    <div class="item">
        <img src="{{ site.url }}{{ site.baseurl }}/images/outreach/TeamBBQ2023Nov4.jpg" alt="Slide 7" style="height: 400px; width: 100%; object-fit: contain;" />
        <div class="carousel-caption">
            <p>Team BBQ at East Coast Singapore 2023 November</p>
        </div>
    </div>		
</div>

  <a class="left carousel-control" href="#carousel" role="button" data-slide="prev">
    <span class="glyphicon glyphicon-chevron-left" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="right carousel-control" href="#carousel" role="button" data-slide="next">
    <span class="glyphicon glyphicon-chevron-right" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>


<script>
  function toggleVisibility(id) {
    var x = document.getElementById(id);
    if (x.style.display === "none") {
      x.style.display = "block";
    } else {
      x.style.display = "none";
    }
  }
</script>


<h2 onclick="toggleVisibility('open-position')" style="text-decoration: underline; cursor: pointer;">Open Positions</h2>
<div id="open-position" style="display:none;">
- Currently, we don't hire short-term RA. Positions are reserved for those who will continue their PhDs (e.g., in a part-time manner) in our Lab.
- If you are currently studying at NUS/NTU/SUTD/SMU, short-term intern positions are available.
- We welcome students who want to explore the <i>system research</i> area, particularly ML system, database system, and network system.
- Make sure you have take a look at <a href='https://intellistream.github.io//regulations/'>how our lab works</a>.
- GPA is the least thing we consider. Hands on experience matter more.
- If you are interested in pursuing graduate studies at NTU, please apply at the <a href='https://venus.wis.ntu.edu.sg/GOAL/OnlineApplicationModule/frmOnlineApplication.ASPX'>portal</a>.
- 中国大陆学生: 如果你有参与 "全国大学生电子设计竞赛", "龙芯杯"，“世界大学生超级计算机竞赛”，并获得不错的成绩， 我们将优先考虑录取。
> At any time, we have a limited number of slots available. Unfortunately, we cannot respond to every message we receive. To help manage the process, we are using the <a href='https://forms.office.com/r/NrLZxYjrhg'>questionnaire</a>. We guarantee we will read the responses to this form but cannot guarantee a response. However, an impressive set of answers to this questionnaire is much more likely to result in a response than almost all other forms of contact. 
</div>

<h2 onclick="toggleVisibility('frequent-collaborators')" style="text-decoration: underline; cursor: pointer;">Collaborators in Last 3 Years</h2>
<div id="frequent-collaborators" style="display:none;">
{% assign number_printed = 0 %}
{% for member in site.data.collaborators %}

{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <h4>{{ member.name }}</h4>    
  {{ member.info }}
  <ul style="overflow: hidden">
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
</div>

<h2 onclick="toggleVisibility('former-members')" style="text-decoration: underline; cursor: pointer;">Former Members</h2>
<div id="former-members" style="display:none;">

### Staffs and PhD students
{% for member in site.data.alumni_members %}
   - {{ member.name }} ({{ member.info }})
{% endfor %}

### Master students
{% for member in site.data.alumni_msc %}
   - {{ member.name }} ({{ member.info }})
{% endfor %}

### Bachelor Students
{% for member in site.data.alumni_bsc %}
   - {{ member.name }} ({{ member.info }})
{% endfor %}

### Visitors
{% for member in site.data.alumni_visitors %}
   - {{ member.name }} ({{ member.info }})
{% endfor %}

</div>
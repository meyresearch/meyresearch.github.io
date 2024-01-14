---
title: "IntelliStream Research Group - Home"
layout: homelay
excerpt: "IntelliStream Research Group"
sitemap: false
permalink: /
---
<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/team.jpg" width="50%" style="float: center" />


We are generally interested at system resarch on Machine Learning, Database and their interactions. In particular, the group has the following current research focus. 

<div style="display: flex;">
  <div class="nav-bar">
    <div class="nav-button" onclick="showSection('RAG')">System support for Retrieval Augmented Generation</div>
    <div class="nav-button" onclick="showSection('DSAI')">Data Stream-Centric AI</div>
    <div class="nav-button" onclick="showSection('TSP')">Transactional Stream Processing</div>
    <div class="nav-button" onclick="showSection('HWSP')">Hardware-Conscious Data Stream Processing</div>
    <div class="nav-button" onclick="showSection('ancillaryTopics')">Other Ancillary/Collaborate Topics</div>
  </div>

  <div>
    <div id="RAG" class="content-section">
      <!-- Content for RAG -->
    </div>
    <div id="DSAI" class="content-section">
      <!-- Content for DSAI -->
    </div>
    <!-- Other content sections -->
  </div>
</div>

<!-- Carousel and other content -->

<script>
  function showSection(sectionId) {
    var sections = document.getElementsByClassName('content-section');
    for (var i = 0; i < sections.length; i++) {
      sections[i].style.display = 'none';
    }
    var activeSection = document.getElementById(sectionId);
    activeSection.style.display = 'block';
  }
</script>

<style>
  .nav-bar {
    display: flex;
    flex-direction: column;
    align-items: flex-start;
    padding: 10px;
    border-right: 1px solid #ccc;
    min-height: 200px; /* Adjust as needed */
  }

  .nav-button {
    cursor: pointer;
    color: blue;
    padding: 5px;
    margin-bottom: 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
    text-align: center;
    background-color: #f0f0f0;
  }

  .nav-button:hover {
    background-color: #e0e0e0;
  }

  .content-section {
    display: none;
    margin-left: 20px;
    padding: 10px;
  }

  .active-section {
    display: block;
  }
</style>

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
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider/CStream.png" alt="Slide 1" style="height: 400px; width: 100%; object-fit: contain;" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider/PLStream.png" alt="Slide 2" style="height: 400px; width: 100%; object-fit: contain;" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider/MorphStreamResults.png" alt="Slide 3" style="height: 400px; width: 100%; object-fit: contain;" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider/BriskStream.png" alt="Slide 4" style="height: 400px; width: 100%; object-fit: contain;" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider/IntraStudy.png" alt="Slide 5" style="height: 400px; width: 100%; object-fit: contain;" />
        </div>
        <div class="item">
            <img src="{{ site.url }}{{ site.baseurl }}/images/slider/profiling.png" alt="Slide 6" style="height: 400px; width: 100%; object-fit: contain;" />
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

At any time, we have a limited number of slots available. Unfortunately, we cannot respond to every message we receive. To help manage the process, we are using the <a href='https://forms.office.com/r/NrLZxYjrhg'>questionnaire</a>. We guarantee we will read the responses to this form but cannot guarantee a response. However, an impressive set of answers to this questionnaire is much more likely to result in a response than almost all other forms of contact. 

If you are interested in pursuing graduate studies at NTU, please apply at the <a href='https://venus.wis.ntu.edu.sg/GOAL/OnlineApplicationModule/frmOnlineApplication.ASPX'>portal</a>.
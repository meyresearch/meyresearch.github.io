---
title: "Publications"
layout: gridlay
excerpt: "Publications."
sitemap: false
permalink: /publications/
---
<div style="display: flex; flex-direction: row;">
  <!-- Filter buttons with paper counts -->
  {% assign all_pubs = site.data.publist %}
  <button class="filter-button active-filter" onclick="filterByVenue('All')">Show All ({{ all_pubs | size }})</button>

  {% assign sigmod_pubs = all_pubs | where: 'venue', 'SIGMOD' %}
  <button class="filter-button" onclick="filterByVenue('SIGMOD')">SIGMOD ({{ sigmod_pubs | size }})</button>
  
  {% assign vldb_pubs = all_pubs | where: 'venue', 'VLDB' %}
  <button class="filter-button" onclick="filterByVenue('VLDB')">VLDB ({{ vldb_pubs | size }})</button>
  
  {% assign icde_pubs = all_pubs | where: 'venue', 'ICDE' %}
  <button class="filter-button" onclick="filterByVenue('ICDE')"> ICDE ({{ icde_pubs | size }})</button>  
</div>

# Publications
Author notations: * denotes the author is a student advised by Dr.Shuhao Zhang. # denotes the author is a staff advised by Dr.Shuhao Zhang.

<style>
  .filter-button {
    cursor: pointer;
    padding: 5px 10px;
    margin: 5px;
    border: 1px solid #ccc;
    border-radius: 5px;
    background-color: #f0f0f0;
  }

  .filter-button:hover {
    background-color: #e0e0e0;
  }

  .active-filter {
    background-color: #d0d0d0;
  }
</style>

<script>
  function filterByVenue(venue) {
    var allPublications = document.querySelectorAll('.publication');
    var allYears = document.querySelectorAll('.year-heading');
    allYears.forEach(function(year) {
      year.style.display = 'none'; // Initially hide all year headings
    });

    allPublications.forEach(function(pub) {
      if (venue === 'All' || pub.dataset.venue === venue) {
        pub.style.display = '';
        // Show the year heading if at least one publication is visible
        var yearHeading = document.querySelector('.year-heading[data-year="' + pub.dataset.year + '"]');
        if (yearHeading) {
          yearHeading.style.display = '';
        }
      } else {
        pub.style.display = 'none';
      }
    });

    // Update button styles
    var allButtons = document.querySelectorAll('.filter-button');
    allButtons.forEach(function(btn) {
      if (btn.textContent === venue || (venue === 'All' && btn.textContent === 'Show All')) {
        btn.classList.add('active-filter');
      } else {
        btn.classList.remove('active-filter');
      }
    });
  }
</script>

{% assign pub_years = site.data.publist | map: 'year' | uniq | sort | reverse %}
{% for year in pub_years %}
  <h3 class="year-heading" data-year="{{ year }}">{{ year }}</h3>
  <ol>
    {% for publi in site.data.publist %}
      {% if publi.year == year %}
        <li class="publication" data-venue="{{ publi.venue }}" data-year="{{ year }}">
          [{{ publi.venue }}] <strong>{{ publi.title }}</strong><br />
          <em>{{ publi.authors }}</em><br />
          {{ publi.display }} ({{ year }})<br />
          {% if publi.url %}
            <a href="{{ publi.url }}">PDF</a>
          {% endif %}
        </li>
      {% endif %}
    {% endfor %}
  </ol>
{% endfor %}

## Preprints (Technical Reports)
<ol>
{% for publi in site.data.prelist %}
  <li>{{ publi.title }}
    <em>{{ publi.authors }}</em><br />
    <i class="fa-regular fa-file-pdf"></i><a href="{{ publi.url }}">PDF</a>
  </li>
{% endfor %}
</ol>


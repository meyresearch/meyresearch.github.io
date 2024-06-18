---
title: "Research"
layout: gridlay
sitemap: false
permalink: /research/
---

## Research[^1]

- 2023 - 2026 (PI. $100,000) "Parallelized Stateful Coreset Selection in Continuous Data Streams for Enhanced Stream Learning". Funding from T1 Seed Grant. 
- 2023 - 2026 (PI. $150,000) "Parallel Data Management in Retrieval-based Language Models". Funding from NTU Start-Up Grants. 
- 2023 - 2026 (Co-PI. $1,300,000) "Real-Time Federated Learning on Data Streams". Funding from DTC. 
- 2023 - 2026 (PI. $500,000+) "IntelliStream: Towards Highly-Optimized, Ultra-Scalable, Self-adaptive Data Streaming Analytics in the Heterogeneous Multicore IoT Systems". Funding from Singapore Ministry of Education (MOE) Academic Research Fund (AcRF) Tier 2. 
- 2022 - 2025 (PI - Transferred. ~$500,000) "A Stream Processing based NFV Platform for 5G on Modern Multicore Processors". Funding from National Research Foundation, Singapore and Infocomm Media
Development Authority under its Future Communications Research & Development Programme. 
- 2022 - 2025 (PI - Transferred. ~$500,000) "Energy-efficient, Scalable, and Reliable Distributed Green Streaming
Machine Learning for Edges. Funding from National Research Foundation, Singapore and Infocomm Media Development Authority under its Future Communications Research & Development Programme. 
- 2023 - 2023 (PI - Transferred. $100,000) "Towards Online Continual Pre-Trained Language Model Maintenance". Funding from TL@SUTD.
- 2022 - 2022 (PI - Completed. $67,000) "Online Sentiment Learning of Massive Data Streams". Funding from TL@SUTD. 
- 2022 - 2025 (PI - Terminated. $80,000) "Revisiting the Algorithms for Clustering Evolving Trajectory Streams". Funding from SUTD-ZJU (VP). 
- 2021 - 2024 (PI - Terminated. $100,000) "Efficient Intra-Window Join on the Multicore IoT systems". Funding from SUTD STARTUP RESEARCH GRANT (SRG). 


[^1]: Some grants are transferred or terminated due to PI's move from SUTD to NTU in 2023.

## Project Highlights
{% assign number_printed = 0 %}
{% for publi in site.data.publist %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if publi.highlight == 1 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
 <div class="well">
  <pubtit>{{ publi.title }}</pubtit>
  <img src="{{ site.url }}{{ site.baseurl }}/images/pubpic/{{ publi.image }}" class="img-responsive" width="33%" style="float: left" />
  <p>{{ publi.description }}</p>
  <p><em>{{ publi.authors }}</em></p>
  <p><strong><a href="{{ publi.url }}">{{ publi.venue }} {{ publi.year }}</a></strong></p>
  <p class="text-danger"><strong> {{ publi.news1 }}</strong></p>
  <p> {{ publi.news2 }}</p>
  <p> {{ publi.news2_url }}</p>
    {% if publi.publications %}
      <p><strong>Publications:</strong></p>
      <ul>
        {% for publication in publi.publications %}
          <li>{{ publication }}</li>
        {% endfor %}
      </ul>
    {% endif %}  
 </div>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endif %}
{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}

<p> &nbsp; </p>
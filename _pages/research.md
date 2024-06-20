---
title: "Research"
layout: gridlay
sitemap: false
permalink: /research/
---

## Project Highlights

{% for project in site.data.highlighted_projects %}
### {{ project.project_title }}

<div class="image-container">
  ![Project Image]({{ site.url }}{{ site.baseurl }}/images/pubpic/{{ project.image }}){: .project-image }
</div>

#### Project Description
{{ project.description | markdownify }}

#### Publications
{% if project.publications %}
<ul>
  {% for publication in project.publications %}
    <li>{{ publication.title }} - {{ publication.authors }} ({{ publication.year }})</li>
  {% endfor %}
</ul>
{% endif %}

#### Project News
{% if project.news %}
<ul>
  {% for news_item in project.news %}
    <li>
      <p>{{ news_item.title }} (<a href="{{ news_item.url }}">{{ news_item.url }}</a>)</p>      
    </li>
  {% endfor %}
</ul>
{% endif %}

<hr>
{% endfor %}

## Research Grants[^1]

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

<p> &nbsp; </p>
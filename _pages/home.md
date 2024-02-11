---
title: "IntelliStream Research Group - Home"
layout: homelay
sitemap: false
permalink: /
---
<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/team.jpg" width="50%" style="float: center" />

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

We are a database system group with a focus on <b> data stream management </b>, we also actively explore modern hardware for better management of stream data. 

- **[Data Stream Management for Query Processing]**
  - *Vision/Survey*:
    - [DB] [Survey on TSP (VLDBJ'23)](https://rdcu.be/dncBQ)
    - [DB] [Survey on HW-Conscious Stream Processing (SIGMOD Rec'20)](https://dl.acm.org/doi/10.1145/3385658.3385662)
  - *Benchmarking*:
    - [DB] [Empirical Study of Streaming Join on Multicores (SIGMOD'21)](https://dl.acm.org/doi/10.1145/3448016.3452793)
  - *Algorithm/Query Optimization*:
    - [DB] [Join on Disorder Data Streams with Proactive Error Compensation (SIGMOD'24)](https://tonyskyzeng.github.io/downloads/PECJ_TR.pdf) collaborate with 4Paradigm
    - [DB] [Scalable Streaming Join on Multicores (ICDE'23^b)](https://ieeexplore.ieee.org/document/10184828)
    - [DB] [Multi-Query Optimization for Complex Event Processing with SAP (ICDE'17)](https://doi.org/10.1109/ICDE.2017.166)
  - *System Development/Optimization*:
    - [DB] Scalable Processing of Transactions over Streams (ICDE'24 Demo)
    - [DB] [Scalable TSP on Multicores (SIGMOD'23)](https://intellistream.github.io/downloads/papers/MorphStream_CR.pdf)
    - [DB] [Scalable Transactional Stream Processing on Multicores - Journal Extension (arxiv'23^c)](https://arxiv.org/pdf/2307.12749.pdf)
    - [DB] [Towards Scalable Stateful Stream Processing on Multicores (ICDE'20)](https://doi.org/10.1109/ICDE48307.2020.00136)
    - [DB] [Compression-aware Stream Database with Renmin University of China, Prof.Feng Zhang (ICDE'23)](https://intellistream.github.io/downloads/papers/CompressStreamDB.pdf)
    - [DB] [Stream Processing on CPU-GPU (TPDS'21)](https://doi.org/10.1109/TPDS.2021.3066407)
    - [DB] [Stream Processing on CPU-GPU (USENIX ATC'20)](https://dl.acm.org/doi/abs/10.5555/3489146.3489189)
    - [DB] [NUMA-aware Stream Processing (SIGMOD'19)](https://dl.acm.org/doi/10.1145/3299869.3300067)
    - [DB] [Profiling of Streaming System on Multicore (ICDE'17)](https://doi.org/10.1109/ICDE.2017.119)

- **[Data Stream Management for DM/ML/AI]**
  - *Vision/Survey*:
    - [DB] [Transactional Stream Processing for Large Language Model (LLM) (arxiv'23^b)](https://arxiv.org/pdf/2307.08225.pdf)
  - *Benchmarking*:
    - [AI] [A Benchmark Study of Online Continual Knowledge Learning of Large Language Models (arxiv'24^b)](https://intellistream.github.io/downloads/papers/preprints/OCKL.pdf)
    - [DB] [An In-Depth Study of Data Stream Clustering (SIGMOD'23)](https://dl.acm.org/doi/abs/10.1145/3589307)
    - [AI] High Performance ML Inference on Modern Hardware (reviewing)
    - [DB] Revisit Approximate Nearest​ Neighbour Search under Online Ingestion (preparing)
  - *Algorithm/Query Optimization*:
    - [DB] [Self-Optimizing Data Stream Clustering Algorithm (arxiv'23^a)](https://arxiv.org/abs/2309.04799)
  - *System Development/Optimization*:
    - [DB] View Materialization in Video Databases, driven by Zhejiang University Prof.Dongxiang Zhang (SIGMOD'24)
    - [AI] [Stream Learning for Sentiment Analysis (EMNLP'23, *Main*)](https://intellistream.github.io/downloads/papers/sentistream_EMNLP.pdf)
    - [AI] [A Framework of Scalable Polarity Labelling over Data Streams (arxiv'22)](https://arxiv.org/abs/2203.12368)
    - [DB] [Progressive Trajectory Exploration (BigMM'19)](https://dl.acm.org/doi/abs/10.5555/3489146.3489189)

- **[Data Stream Management for Network and Communication]**
  - *Vision/Survey*:
    - [DB] [HW-Conscious Stream Compression (DEBS'23)](https://dl.acm.org/doi/abs/10.1145/3583678.3596885)
  - *System Development/Optimization*:
    - [DB] [A Database System for Network Function Virtualization (NFV) (arxiv'23^a)](https://arxiv.org/pdf/2307.10732.pdf)
    - [DB] [Data Stream Compression on AMP (ICDE'23^a)](https://ieeexplore.ieee.org/document/10184703)
    - [DB] [HW-Conscious Stream Compression Framework (arxiv'23)](https://arxiv.org/pdf/2306.10228.pdf)

- <span onclick="toggleVisibility('ancillaryTopics')" style="cursor: pointer; color: blue; text-decoration: underline;">click to see our other ancillary/collaborate topics</span>
<div id="ancillaryTopics" style="display:none; margin-left: 20px;">
  <ul>	
 	<li>[ML] <a href="">Novel Retrival Paradigam/Algorithm for Large Language Models (preparing)</a> collaborate with SUTD Prof.Wei Lu</li>
    <li>[AI/DB] <a href="https://www.ijcai.org/proceedings/2020/610">Parking Prediction</a> with Renmin Univeristy of China, Prof.Feng Zhang (IJCAI'20, TKDE'21, VLDBJ'22)</li>    
    <li>[HPC] <a href="https://ieeexplore.ieee.org/document/7877153">Cloud Resource Mgmt</a> with Tianjin Univeristy, Prof.Shanjiang Tang (SC'16)</li>
	<li>[DB] <a href="https://dl.acm.org/doi/10.14778/2536274.2536319">DB on APU Systems (VLDB'13, VLDB'14, MASCOTS'15, TPDS'17)</a></li>
	<li>[DB] <a href="https://ieeexplore.ieee.org/document/7425227">MapReduce on FPGA Systems (TPDS'16)</a></li>	
  </ul>
</div>

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

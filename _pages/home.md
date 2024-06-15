---
title: "IntelliStream Research Group - Home"
layout: homelay
sitemap: false
permalink: /
---

<!--<img src="{{ site.url }}{{ site.baseurl }}/images/teampic/team.jpg" width="50%" style="float: center" />-->

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

Our group thrives at the intersection of data-intensive applications and systems. We navigate the complex landscape defined by the three Vs of data: Volume, Velocity, and Variety (see our briefying [slides](https://intellistream.github.io/downloads/talks/ResearchRoadmap.pdf)). Our recent focus is on pioneering in the dual realms of _Data Management on New Hardware_ and _Database meets Artificial Intelligence (DB4AI & AI4DB)_. If you like to join our team, please first answer a few questions in <a href='https://forms.office.com/r/NrLZxYjrhg'>questionnaire</a>.

### Data Management on New Hardware (DaMoN)

- _Vision/Survey_:  
  - [VLDBJ'23] [A Survey on Transactional Stream Processing](https://rdcu.be/dncBQ)
  - [DEBS'23] [A Hardware-Conscious Stateful Stream Compression Framework for IoT Applications (Vision)](https://dl.acm.org/doi/abs/10.1145/3583678.3596885) 
  - [SIGMOD Rec'20] [Hardware-Conscious Stream Processing: A Survey](https://dl.acm.org/doi/10.1145/3385658.3385662)
  - [OJIOT'20] [NebulaStream: Complex Analytics Beyond the Cloud](https://intellistream.github.io/downloads/papers/OJIOT_2020v6i1n07_Zeuch.pdf)

- _Benchmarking_:
  - [SIGMOD'21] [Parallelizing Intra-Window Join on Multicores: An Experimental Study](https://dl.acm.org/doi/10.1145/3448016.3452793)
  - [ICDE'17] [Revisiting the Design of Data Stream Processing Systems on Multi-Core Processors](https://www.comp.nus.edu.sg/~hebs/pub/shuhaoICDE17a.pdf)
  - [TPDS'17] [Understanding Co-Running Behaviors on Integrated CPU/GPU Architectures](https://doi.org/10.1109/TPDS.2016.2586074)
  - [MASCOTS'15] [To Co-run, or Not to Co-run: A Performance Study on Integrated Architectures](https://doi.org/10.1109/MASCOTS.2015.27) 

- _Algorithm/Query Optimization_: 
  - [ICDE'23] [Scalable Online Interval Join on Modern Multicore Processors in OpenMLDB](https://intellistream.github.io/downloads/papers/Zhang-2023-OIJ-OpenMLDB_CR.pdf) 
  - [MDPI'22] [Revisiting the Design of Parallel Stream Joins on Trusted Execution Environments](https://www.mdpi.com/1999-4893/15/6/183)
  - [ICDE'17] [Multi-Query Optimization for Complex Event Processing in SAP ESP](https://www.comp.nus.edu.sg/~hebs/pub/shuhaoICDE17b.pdf)

- _System Development/Optimization_:
  - [TKDE'24] [CStream: Parallel Data Stream Compression on Multicore Edge Devices](https://arxiv.org/pdf/2306.10228.pdf)  
  - [ICDE'24] [Fast Parallel Recovery for Transactional Stream Processing on Multicores](https://intellistream.github.io/downloads/papers/ICDE24_MorphStreamR.pdf)  
  - [ICDE'24 Demo] [MorphStream: Scalable Processing of Transactions over Streams on Multicores](https://intellistream.github.io/downloads/papers/ICDE24_Demo_MorphStream.pdf)
  - [ICDE'23] [Parallelizing Stream Compression for IoT Applications on Asymmetric Multicores](https://intellistream.github.io/downloads/papers/CStream_CR.pdf)
  - [SIGMOD'23] [MorphStream: Adaptive Scheduling for Scalable Transactional Stream Processing on Multicores](https://intellistream.github.io/downloads/papers/MorphStream_CR.pdf)
  - [ICDE'20] [Towards Concurrent Stateful Stream Processing on Multicore Processors](https://doi.org/10.1109/ICDE48307.2020.00136)
  - [TPDS'21] [Fine-Grained Multi-Query Stream Processing on Integrated Architectures](https://doi.org/10.1109/TPDS.2021.3066407)
  - [USENIX ATC'20] [FineStream: Fine-Grained Window-Based Stream Processing on CPU-GPU Integrated Architectures](https://www.comp.nus.edu.sg/~hebs/pub/atc20-finestream.pdf)
  - [SIGMOD'19] [BriskStream: Scaling Data Stream Processing on Shared-Memory Multicore Architectures](https://dl.acm.org/doi/10.1145/3299869.3300067)
  - [SC'16] <a href="https://ieeexplore.ieee.org/document/7877153">Elastic Multi-resource Fairness: Balancing Fairness and Efficiency in Coupled CPU-GPU Architectures</a>
  - [TPDS'16] <a href="https://wangzeke.github.io/doc/melia-tpds-16.pdf">Melia: A MapReduce Framework on OpenCL-Based FPGAs</a>
  - [VLDB'14] [In-Cache Query Co-Processing on Coupled CPU-GPU Architectures](https://doi.org/10.14778/2735496.2735497)
  - [VLDB'13] <a href="https://dl.acm.org/doi/10.14778/2536274.2536319">OmniDB: towards portable and efficient query processing on parallel CPU/GPU architectures</a>

### Database meets Artificial Intelligence (DB4AI & AI4DB)

- _Benchmarking_:
  - [SIGMOD'23] [Data Stream Clustering: An In-depth Empirical Study](https://dl.acm.org/doi/abs/10.1145/3589307)
 
- _System Development/Optimization_:
  - [SIGMOD'24] [PECJ: Stream Window Join on Disorder Data Streams with Proactive Error Compensation](https://tonyskyzeng.github.io/downloads/PECJ_TR.pdf)
  - [SIGMOD'24] [Predictive and Near-Optimal Sampling for View Materialization in Video Databases]()
  - [EMNLP'23, _Main_] [SentiStream: A Co-Training Framework for Adaptive Online Sentiment Analysis in Evolving Data Streams](https://intellistream.github.io/downloads/papers/sentistream_EMNLP.pdf)
  - [ICDE'23] [CompressStreamDB: Fine-Grained Adaptive Stream Processing without Decompression](https://ieeexplore.ieee.org/document/10184565/)
  - [VLDBJ'22] [Payment behavior prediction on shared parking lots with TR-GCN](https://doi.org/10.1007/s00778-021-00722-0)
  - [TKDE'21] [Periodic Weather-Aware LSTM with Event Mechanism for Parking Behavior Prediction](https://doi.org/10.1109/TKDE.2021.3070202)
  - [IJCAI'20] [PewLSTM: Periodic LSTM with Weather-Aware Gating Mechanism for Parking Behavior Prediction](https://www.ijcai.org/proceedings/2020/610)

- <span onclick="toggleVisibility('ancillaryTopics')" style="cursor: pointer; color: blue; text-decoration: underline;">click to see our other ancillary topics or preprints</span>
<div id="ancillaryTopics" style="display:none; margin-left: 20px;">
  - [IWQoS'24] [Low-Latency Video Conferencing via Optimized Packet Routing and Reordering](https://arxiv.org/abs/2310.05054)
  - [BigMM'19] [TraV: an Interactive Trajectory Exploration System for Massive Data Sets](https://ieeexplore.ieee.org/abstract/document/8919445) 
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

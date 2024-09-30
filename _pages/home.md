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

**Our Research Focus**

The PI, Dr. Zhang, will join the School of Computer Science and Technology at Huazhong University of Science and Technology (HUST) as a Professor in November 2024. We welcome talented students to join our research endeavors. Our team concentrates on three core research directions:

### 1. **Vector Database with Streaming Capabilities**  
We are pioneering a novel vector database system designed to handle both high-throughput streaming data and complex similarity searches. This system supports continuous vector data ingestion and real-time processing, addressing the scalability challenges inherent in dynamic and evolving datasets. Our research focuses on optimizing retrieval efficiency for applications demanding rapid vector updates and queries in a streaming context.
 
- **[arXiv'24]** [CANDY: A Benchmark for Continuous Approximate Nearest Neighbor Search with Dynamic Data Ingestion](https://arxiv.org/pdf/2406.19651)
- **[NIPS'24]** [LibAMM: Empirical Insights into Approximate Computing for Accelerating Matrix Multiplication]()

### 2. **Retrieval-Augmented Generation (RAG)**  
We are building a next-generation RAG system that leverages our cutting-edge vector database. The integration with our vector database provides a high-performance foundation for large-scale retrieval tasks, facilitating dynamic data ingestion and updating while improving the retrieval quality in RAG applications.

- **[arXiv'24]** [Online Continual Knowledge Learning for Language Models](http://arxiv.org/abs/2311.09632)
- **[arXiv'24]** [StreamPrompt: Learnable Prompt-guided Data Selection for Efficient Stream Learning](http://arxiv.org/abs/2406.07590)

### 3. **Stream Processing System**  
Our extensive work on stream processing systems has resulted in significant technological advancements. We are open to collaborations for real-world deployments. Our innovations in stream processing techniques include concurrency control, adaptive scheduling, and fine-grained optimizations for handling high-velocity (out-of-order) data streams.

##### **Stream Learning**
- **[arXiv'24]** [SRTFD: Scalable Real-Time Fault Diagnosis through Online Continual Learning](https://arxiv.org/abs/2408.05681v1)
- **[EMNLP'23]** [SentiStream: A Co-Training Framework for Adaptive Online Sentiment Analysis in Evolving Data Streams](https://aclanthology.org/2023.emnlp-main.380)

##### **Transactional Stream Processing**
- **[ICDE'24]** [Fast Parallel Recovery for Transactional Stream Processing on Multicores](https://intellistream.github.io/downloads/papers/ICDE24_MorphStreamR.pdf)
- **[ICDE'24]** [MorphStream: Scalable Processing of Transactions over Streams](https://intellistream.github.io/downloads/papers/ICDE24_Demo_MorphStream.pdf)
- **[arXiv'24]** [TransNFV: Scalable State Management in NFV with Adaptive Transactional Concurrency Control](http://arxiv.org/abs/2312.01066)
- **[VLDBJ'23]** [A Survey on Transactional Stream Processing](https://rdcu.be/dncBQ)

##### **Stream Compression**
- **[TKDE'24]** [CStream: Parallel Data Stream Compression on Multicore Edge Devices](https://ieeexplore.ieee.org/document/10506068)
- **[ICDE'23]** [CompressStreamDB: Fine-Grained Adaptive Stream Processing without Decompression](https://ieeexplore.ieee.org/document/10184565)
- **[ICDE'23]** [Parallelizing Stream Compression for IoT Applications on Asymmetric Multicores](https://ieeexplore.ieee.org/document/10184703)
- **[DEBS'23]** [A Hardware-Conscious Stateful Stream Compression Framework for IoT Applications (Vision)](https://doi.org/10.1145/3583678.3596885)

##### **Stream Window Join**
- **[SIGMOD'25]** [Enabling Adaptive Sampling for Intra-Window Join: Simultaneously Optimizing Quantity and Quality]()
- **[SIGMOD'24]** [PECJ: Stream Window Join on Disorder Data Streams with Proactive Error Compensation](https://doi.org/10.1145/3639268)
- **[ICDE'23]** [Scalable Online Interval Join on Modern Multicore Processors in OpenMLDB](https://ieeexplore.ieee.org/document/10184828)
- **[SIGMOD'21]** [Parallelizing Intra-Window Join on Multicores: An Experimental Study](https://doi.org/10.1145/3448016.3452793)

##### **Stream Processing Systems**
- **[TPDS'21]** [Fine-Grained Multi-Query Stream Processing on Integrated Architectures](https://ieeexplore.ieee.org/document/9380479)
- **[SIGMOD Record'20]** [Hardware-Conscious Stream Processing: A Survey](https://doi.org/10.1145/3385658.3385662)
- **[VLIoT'20]** [NebulaStream: Complex Analytics Beyond the Cloud](https://www.ronpub.com/ojiot/OJIOT_2020v6i1n07_Zeuch.html)
- **[ATC'20]** [FineStream: Fine-Grained Window-Based Stream Processing on CPU-GPU Integrated Architectures](https://www.usenix.org/system/files/atc20-zhang-feng.pdf)
- **[SIGMOD'19]** [Briskstream: Scaling Data Stream Processing on Multicore Architectures](https://doi.acm.org/10.1145/3299869.3300067)
- **[ICDE'17]** [Revisiting the Design of Data Stream Processing Systems on Multi-Core Processors](https://doi.org/10.1109/ICDE.2017.119)

<span onclick="toggleVisibility('ancillaryTopics')" style="cursor: pointer; color: blue; text-decoration: underline;">click to see our other ancillary topics</span>
<div id="ancillaryTopics" style="display:none; margin-left: 20px;">
 - **[SIGMOD'24]** [Predictive and Near-Optimal Sampling for View Materialization in Video Databases](https://doi.org/10.1145/3639274)
 - **[IWQoS'24]** [Low-Latency Video Conferencing via Optimized Packet Routing and Reordering](http://arxiv.org/abs/2310.05054) 
 - **[TPDS'17]** [Understanding Co-Running Behaviors on Integrated CPU/GPU Architectures](https://ieeexplore.ieee.org/document/7501903)
 - **[SC'16]** [Elastic Multi-resource Fairness: Balancing Fairness and Efficiency in Coupled CPU-GPU Architectures](https://ieeexplore.ieee.org/document/7877153)
 - **[TPDS'16]** [Melia: A MapReduce Framework on OpenCL-Based FPGAs](https://ieeexplore.ieee.org/document/7425227)
 - **[MASCOTS'15]** [To Co-run, or Not to Co-run: A Performance Study on Integrated Architectures](https://doi.org/10.1109/MASCOTS.2015.27)
 - **[VLDB'14]** [In-cache query co-processing on coupled CPU-GPU architectures](https://doi.org/10.14778/2735496.2735497)
 - **[VLDB'13]** [OmniDB: towards portable and efficient query processing on parallel CPU/GPU architectures](https://dl.acm.org/doi/10.14778/2536274.2536319)
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

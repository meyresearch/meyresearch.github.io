---
title: "IntelliStream Research Group - Home"
layout: homelay
excerpt: "IntelliStream Research Group"
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


- <b>2023 - present</b>: We are now working towards building the next generation <i>Data Stream-Centric Retrieval-augmented Generation (RAG) System</i>. Join us and change the world.

- <b>2013 - 2023</b>: We have been focus on three key stream-centric research directions:

<span onclick="toggleVisibility('TenYears')" style="cursor: pointer; color: blue; text-decoration: underline;">Last Ten Years' topics</span>
<div id="TenYears" style="display:none;">
- <b>[Hardware-Conscious Data Stream Processing]</b> Multicore NUMA, GPU accelerated stream query processing, AMP-aware data stream compression, etc.
	- <i>Algorithms</i>: 
		- [Stream Compression on AMP (ICDE'23<sup>a</sup>)](https://ieeexplore.ieee.org/document/10184703)
		- [Scalable Streaming Join on Multicores (ICDE'23<sup>b</sup>)](https://ieeexplore.ieee.org/document/10184828)
		- [HW-Conscious Stream Compression (DEBS'23)](https://dl.acm.org/doi/abs/10.1145/3583678.3596885)
		- [HW-Conscious Stream Compression (arxiv'23)](https://arxiv.org/pdf/2306.10228.pdf)
		- [Empirial Study of Streaming Join on Multicores (SIGMOD'21)](https://dl.acm.org/doi/10.1145/3448016.3452793) 
	- <i>Systems</i>: 
		- [Stream Processing on CPU-GPU (TPDS'21)](https://doi.org/10.1109/TPDS.2021.3066407)
		- [Survey on HW-Conscious Stream Processing (SIGMOD Rec'20)](https://dl.acm.org/doi/10.1145/3385658.3385662) 
		- [Stream Processing on CPU-GPU (USENIX ATC'20)](https://dl.acm.org/doi/abs/10.5555/3489146.3489189)
		- [NUMA-aware Stream Processing (SIGMOD'19)](https://dl.acm.org/doi/10.1145/3299869.3300067)
		- [Profiling of Streaming System on Multicore (ICDE'17)](https://doi.org/10.1109/ICDE.2017.119)
	- <i>Non-Streaming Systems</i>:
		- <a href="https://dl.acm.org/doi/10.14778/2536274.2536319">APU Systems</a> (VLDB'13, VLDB'14, MASCOTS'15, TPDS'17)
		- <a href="https://ieeexplore.ieee.org/document/7425227">FPGA Systems</a> (TPDS'16)

- <b>[Transactional Stream Processing]</b> Transactional stream processing (TSP) frameworks and its applications in LLM, NFV etc. 
	- <i>TSP System</i>: 
		- [Scalable TSP on Multicores (SIGMOD'23)](https://intellistream.github.io/downloads/papers/MorphStream_CR.pdf) 
		- [Survey on TSP (VLDBJ'23)](https://rdcu.be/dncBQ) 
		- [More Scalable TSP on Multicores (arxiv'23<sup>c</sup>)](https://arxiv.org/pdf/2307.12749.pdf)
		- [Towards Scalable TSP on Multicores (ICDE'20)](https://doi.org/10.1109/ICDE48307.2020.00136)
	- <i>Its Applications</i>: 
		- [TSP for Network Function virtualization (NFV) (arxiv'23<sup>a</sup>)](https://arxiv.org/pdf/2307.10732.pdf) 
		- [TSP for Large Language Model (LLM) (arxiv'23<sup>b</sup>)](https://arxiv.org/pdf/2307.08225.pdf)

- <b>[Data Stream-Centric AI]</b> High performance online machine learning, data stream mining, data stream preprocessing algorithms/systems 
	- <i>Data Stream Mining</i>: 
		- [In-Depth Study of Data Stream Clustering (SIGMOD'23)](https://dl.acm.org/doi/abs/10.1145/3589307) 
		- [Self-Optimizing Data Stream Clustering (arxiv'23<sup>a</sup>)](https://arxiv.org/abs/2309.04799)
		- [Progressive Trajectory Exploration (BigMM'19)](https://dl.acm.org/doi/abs/10.5555/3489146.3489189) 
	- <i>Online Machine Learning</i>: 
		- [Co-Training-based Online Sentiment Analysis (EMNLP'23, <i>Main</i>)](https://intellistream.github.io/downloads/papers/sentistream_EMNLP.pdf) 
		- [Online Continual Knowledge Learning (arxiv'23<sup>b</sup>)](https://intellistream.github.io/downloads/papers/preprints/OCKL.pdf)
		- [Scalable Polarity Labelling (arxiv'22)](https://arxiv.org/abs/2203.12368)

<span onclick="toggleVisibility('ancillaryTopics')" style="cursor: pointer; color: blue; text-decoration: underline;">Other ancillary topics</span>
<div id="ancillaryTopics" style="display:none;">
  <ul>
    <li><a href="https://doi.org/10.1109/ICDE.2017.166">MQO in CEP</a> (ICDE'17)</li>
    <li><a href="https://intellistream.github.io/downloads/papers/CompressStreamDB.pdf">CompressDB</a> (ICDE'23)</li>
    <li><a href="https://www.ijcai.org/proceedings/2020/610">Parking Prediction</a> (IJCAI'20, TKDE'21, VLDBJ'22)</li>
    <li><a href="https://ieeexplore.ieee.org/document/7877153">Cloud Resource Mgmt</a> (SC'16)</li>
  </ul>
</div>

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


At any time, we have a limited number of slots available. Unfortunately, we cannot respond to every message we receive. To help manage the process, we are using the <a href='https://forms.gle/CANbWnxG6Ep61tXf9'>questionnaire</a>. We guarantee we will read the responses to this form but cannot guarantee a response. However, an impressive set of answers to this questionnaire is much more likely to result in a response than almost all other forms of contact. 

If you are interested in pursuing graduate studies at NTU, please apply at the <a href='https://venus.wis.ntu.edu.sg/GOAL/OnlineApplicationModule/frmOnlineApplication.ASPX'>portal</a>.
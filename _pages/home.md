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

We are generally interested at system resarch on Machine Learning, Database and their interactions. In particular, the group has the following current research focus. 

- <b>[System support for Retrieval Augmented Generation]</b> We are now working towards building the next generation Data Stream-Centric Retrieval-augmented Generation (RAG) System

	- <span onclick="toggleVisibility('RAG')" style="cursor: pointer; color: blue; text-decoration: underline;">click to see our related publications</span>
	<div id="RAG" style="display:none; margin-left: 20px;">
	<ul>
	  <li><a href="">visionary preprint</a> (preparing)</li>
	</ul>
	</div>

- <b>[Data Stream-Centric AI]</b> High performance online machine learning, data stream mining, data stream preprocessing algorithms/systems 

	- <span onclick="toggleVisibility('DSAI')" style="cursor: pointer; color: blue; text-decoration: underline;">click to see our related publications</span>
	<div id="DSAI" style="display:none; margin-left: 20px;">
	<ul>
		  <li><i>AI for Data Stream Management</i>:
		<ul>
		  <li><a href="https://tonyskyzeng.github.io/downloads/PECJ_TR.pdf">Join on Disorder Data Streams with Proactive Error Compensation (SIGMOD'24)</a></li>
		</ul>
	  </li>
	  <li><i>Data Stream Mining</i>:
		<ul>
		  <li><a href="https://dl.acm.org/doi/abs/10.1145/3589307">In-Depth Study of Data Stream Clustering (SIGMOD'23)</a></li>
		  <li><a href="https://arxiv.org/abs/2309.04799">Self-Optimizing Data Stream Clustering (arxiv'23<sup>a</sup>)</a></li>
		  <li><a href="https://dl.acm.org/doi/abs/10.5555/3489146.3489189">Progressive Trajectory Exploration (BigMM'19)</a></li>
		</ul>
	  </li>
	  <li><i>Online Machine Learning</i>:
		<ul>
		  <li><a href="https://intellistream.github.io/downloads/papers/sentistream_EMNLP.pdf">Co-Training-based Online Sentiment Analysis (EMNLP'23, <i>Main</i>)</a></li>
		  <li><a href="https://intellistream.github.io/downloads/papers/preprints/OCKL.pdf">Online Continual Knowledge Learning (arxiv'23<sup>b</sup>)</a></li>
		  <li><a href="https://arxiv.org/abs/2203.12368">Scalable Polarity Labelling (arxiv'22)</a></li>
		</ul>
	  </li>
	</ul>
	</div>

- <b>[Transactional Stream Processing]</b> Transactional stream processing (TSP) frameworks and its applications in LLM, NFV etc. 

	- <span onclick="toggleVisibility('TSP')" style="cursor: pointer; color: blue; text-decoration: underline;">click to see our related publications</span>
	<div id="TSP" style="display:none; margin-left: 20px;">
	<ul>
	  <li><i>TSP System</i>:
		<ul>
		  <li><a href="">Scalable Processing of Transactions over Streams (ICDE'24 Demo)</a></li>
		  <li><a href="https://intellistream.github.io/downloads/papers/MorphStream_CR.pdf">Scalable TSP on Multicores (SIGMOD'23)</a></li>
		  <li><a href="https://rdcu.be/dncBQ">Survey on TSP (VLDBJ'23)</a></li>
		  <li><a href="https://arxiv.org/pdf/2307.12749.pdf">More Scalable TSP on Multicores (arxiv'23<sup>c</sup>)</a></li>
		  <li><a href="https://doi.org/10.1109/ICDE48307.2020.00136">Towards Scalable TSP on Multicores (ICDE'20)</a></li>
		</ul>
	  </li>
	  <li><i>Its Applications</i>:
		<ul>
		  <li><a href="https://arxiv.org/pdf/2307.10732.pdf">TSP for Network Function virtualization (NFV) (arxiv'23<sup>a</sup>)</a></li>
		  <li><a href="https://arxiv.org/pdf/2307.08225.pdf">TSP for Large Language Model (LLM) (arxiv'23<sup>b</sup>)</a></li>
		</ul>
	  </li>
	</ul>
	</div>

- <b>[Hardware-Conscious Data Stream Processing]</b> Multicore NUMA, GPU accelerated stream query processing, AMP-aware data stream compression, etc.

	- <span onclick="toggleVisibility('HWSP')" style="cursor: pointer; color: blue; text-decoration: underline;">click to see our related publications</span>
	<div id="HWSP" style="display:none; margin-left: 20px;">
	<ul>
	  <li><i>Algorithms</i>:
		<ul>
		  <li><a href="https://ieeexplore.ieee.org/document/10184703">Stream Compression on AMP (ICDE'23<sup>a</sup>)</a></li>
		  <li><a href="https://ieeexplore.ieee.org/document/10184828">Scalable Streaming Join on Multicores (ICDE'23<sup>b</sup>)</a></li>
		  <li><a href="https://dl.acm.org/doi/abs/10.1145/3583678.3596885">HW-Conscious Stream Compression (DEBS'23)</a></li>
		  <li><a href="https://arxiv.org/pdf/2306.10228.pdf">HW-Conscious Stream Compression (arxiv'23)</a></li>
		  <li><a href="https://dl.acm.org/doi/10.1145/3448016.3452793">Empirical Study of Streaming Join on Multicores (SIGMOD'21)</a></li>
		</ul>
	  </li>
	  <li><i>Systems</i>:
		<ul>
		  <li><a href="https://doi.org/10.1109/TPDS.2021.3066407">Stream Processing on CPU-GPU (TPDS'21)</a></li>
		  <li><a href="https://dl.acm.org/doi/10.1145/3385658.3385662">Survey on HW-Conscious Stream Processing (SIGMOD Rec'20)</a></li>
		  <li><a href="https://dl.acm.org/doi/abs/10.5555/3489146.3489189">Stream Processing on CPU-GPU (USENIX ATC'20)</a></li>
		  <li><a href="https://dl.acm.org/doi/10.1145/3299869.3300067">NUMA-aware Stream Processing (SIGMOD'19)</a></li>
		  <li><a href="https://doi.org/10.1109/ICDE.2017.119">Profiling of Streaming System on Multicore (ICDE'17)</a></li>
		</ul>
	  </li>
	  <li><i>Non-Streaming Systems</i>:
		<ul>
		  <li><a href="https://dl.acm.org/doi/10.14778/2536274.2536319">APU Systems (VLDB'13, VLDB'14, MASCOTS'15, TPDS'17)</a></li>
		  <li><a href="https://ieeexplore.ieee.org/document/7425227">FPGA Systems (TPDS'16)</a></li>
		</ul>
	  </li>
	</ul>
	</div>	

- <span onclick="toggleVisibility('ancillaryTopics')" style="cursor: pointer; color: blue; text-decoration: underline;">click to see our other ancillary/collaborate topics</span>
<div id="ancillaryTopics" style="display:none; margin-left: 20px;">
  <ul>
    <li><a href="">View Materialization in Video Databases</a> (SIGMOD'24)</li>
    <li><a href="https://doi.org/10.1109/ICDE.2017.166">MQO in CEP</a> (ICDE'17)</li>
    <li><a href="https://intellistream.github.io/downloads/papers/CompressStreamDB.pdf">CompressDB</a> (ICDE'23)</li>
    <li><a href="https://www.ijcai.org/proceedings/2020/610">Parking Prediction</a> (IJCAI'20, TKDE'21, VLDBJ'22)</li>
    <li><a href="https://ieeexplore.ieee.org/document/7877153">Cloud Resource Mgmt</a> (SC'16)</li>
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
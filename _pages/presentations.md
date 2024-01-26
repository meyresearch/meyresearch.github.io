---
title: "Presentations"
layout: textlay
excerpt: "Presentations"
sitemap: false
permalink: /presentations/
---

# Meetings and Presentations

We organize a bi-weekly presentation (3PM every Friday) on presenting an interesting research paper by a team member. It is open to public, and you are free to attend and join the discussion.

---

<script>
  // Embed the JSON data using Liquid for all categories
  const presentations = {{ site.data.presentations | jsonify }};
</script>

<div class="presentation-section">
  <div id="system_next" class="next-presentation"></div>
  <button onclick="toggleVisibility('system_past')">📅 Show/Hide Past Presentations</button>
  <div id="system_past" style="display:none"></div>
  <button onclick="toggleVisibility('system_future')">📅 Show/Hide Future Presentations</button>
  <div id="system_future" style="display:none"></div>
</div>

#### Search Presentations

<div class="presentation-section">
  <input type="text" id="search-input" placeholder="Search for presentations..." oninput="searchPresentations()">
  <div id="search-results"></div>
</div>

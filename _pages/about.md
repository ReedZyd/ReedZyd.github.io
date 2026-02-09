---
permalink: /
title: ""
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
---
<!-- I am a fourth-year Ph.D. student at <a href="https://www.tue.nl/en/" target="_blank">Eindhoven University of Technology</a>,
    under the supervision of <a href="https://www.win.tue.nl/~mpechen/?_gl=1*iopzok*_ga*NTk4Mzc5NDExLjE2ODA3NzUyNjU.*_ga_JN37M497TT*MTY5ODMzMjE2My4yOC4xLjE2OTgzMzIxODEuNDIuMC4w" 
    target="_blank">Mykola Pechenizkiy</a> and <a href="https://mengf1.github.io/" target="_blank">Meng Fang</a>. I am also very fortunate to work closely with <a href="https://yalidu.github.io/" target="_blank">Prof. Yali Du</a> at <a herf="https://www.kcl.ac.uk/" target="_blank">King’s College London</a>, and <a href="https://biweihuang.com/" target="_blank">Prof. Biwei Huang</a> at <a href="https://ucsd.edu/" target="_blank">University of California San Diego</a>. 

Prior to joining TU/e, I was a master student in <a href="https://www.en.sdu.edu.cn/" target="_blank">Shandong University</a> (SDU), supervised by <a href="http://www.vsislab.com/" target="_blank">Prof. Wei Zhang</a>. I also obtained my bachelor's degree from Shandong University.

My current research interests lie in reinforcement learning (RL), especially RL for LLMs and causal RL.
 -->


<style>
  /* ===== Theme variables (scoped) ===== */
  :root{
    --bg: #ffffff;
    --text: #111827;
    --muted: #374151;
    --border: #e5e7eb;

    --btn-border: #717272;
    --btn-bg: #98abbe;
    --btn-text: #111827;
    --btn-hover-bg: #111827;
    --btn-hover-text: #c7d2fe;

    --link: #0f766e; /* optional: link tint */
  }

  /* Dark mode triggers: system + common theme toggles */
  @media (prefers-color-scheme: dark){
    :root{
      --bg: #0b1220;
      --text: #e5e7eb;
      --muted: #a3a3a3;
      --border: #243042;

      --btn-border: #39485f;
      --btn-bg: #1f2a3a;
      --btn-text: #e5e7eb;
      --btn-hover-bg: #e5e7eb;
      --btn-hover-text: #0b1220;

      --link: #5eead4;
    }
  }
  /* If your site uses a manual toggle that adds a class/attribute */
  html[data-theme="dark"],
  html.dark,
  body.dark{
    --bg: #0b1220;
    --text: #e5e7eb;
    --muted: #a3a3a3;
    --border: #243042;

    --btn-border: #39485f;
    --btn-bg: #1f2a3a;
    --btn-text: #e5e7eb;
    --btn-hover-bg: #e5e7eb;
    --btn-hover-text: #0b1220;

    --link: #5eead4;
  }

  /* ===== About (scoped) ===== */
  .about { max-width: 980px; margin: 0 auto; }
  .about p{
    margin: 0 0 12px;
    line-height: 1.75;
    color: var(--text);
  }
  .about p:last-child{ margin-bottom: 0; }

  .about a{ text-decoration: none; color: var(--link); }
  .about a:hover{ text-decoration: underline; }

  .about .btn{
    display: inline-flex;
    align-items: center;
    padding: 6px 10px;
    border-radius: 10px;
    border: 1px solid var(--btn-border);
    background: var(--btn-bg);
    color: var(--btn-text);
    font-size: 0.92rem;
    line-height: 1;
    margin-left: 6px;
    white-space: nowrap;
  }
  .about .btn:hover{
    background: var(--btn-hover-bg);
    color: var(--btn-hover-text);
    border-color: var(--btn-hover-bg);
    transition: background .15s ease, color .15s ease, border-color .15s ease;
    text-decoration: none;
  }

  /* Make the scholar badge look okay on dark bg (optional) */
  .about img[alt*="Google Scholar citations"]{
    vertical-align: middle;
    margin-left: 6px;
    height: 22px;
    width: auto;
    /* If your SVG is dark-on-light, this can help in dark mode */
    filter: none;
  }
  html[data-theme="dark"] .about img[alt*="Google Scholar citations"],
  html.dark .about img[alt*="Google Scholar citations"],
  body.dark .about img[alt*="Google Scholar citations"]{
    /* If badge becomes hard to read in dark mode, uncomment: */
    /* filter: brightness(1.15) contrast(1.05); */
  }

  /* ===== Unified sections (scoped) ===== */
  .cv { max-width: 980px; margin: 0 auto; }

  .cv h2{
    font-size: 1.35rem;
    margin: 22px 0 10px;
    padding-bottom: 6px;
    border-bottom: 1px solid var(--border);
    color: var(--text);
  }

  .cv ul{
    margin: 0;
    padding-left: 1.2em;
    line-height: 1.8;
    color: var(--text);
  }
  .cv li{ margin: 8px 0; }

  .cv a{ text-decoration: none; color: var(--link); }
  .cv a:hover{ text-decoration: underline; }

  .cv .muted{ color: var(--muted); }

  /* News: align date for better readability */
  .cv .news li{ margin: 10px 0; }
  .cv .news .date{
    display: inline-block;
    min-width: 90px;
    color: var(--muted);
    font-weight: 600;
  }
/* === Dark-mode fix for your custom blocks (put at VERY END) === */

/* 1) Default: follow the site theme (do NOT force black text) */
.about, .about p,
.cv, .cv ul, .cv li,
.cv .news .date,
.cv h2 {
  color: inherit;
}

/* If you previously set these, override them back to inherit */
.about p { color: inherit; }
.cv ul { color: inherit; }
.cv .muted { color: inherit; } /* we'll define muted per mode below */

/* 2) When dark mode is active: force readable colors */
@media (prefers-color-scheme: dark) {
  .about, .about p,
  .cv, .cv ul, .cv li {
    color: #e5e7eb !important;          /* main text */
  }
  .cv .news .date,
  .cv .muted {
    color: #a3a3a3 !important;          /* muted text */
  }
  .cv h2 {
    border-bottom-color: #243042 !important;
  }
  .about a, .cv a {
    color: #5eead4 !important;          /* links */
  }
  .about .btn{
    background: #1f2a3a !important;
    border-color: #39485f !important;
    color: #e5e7eb !important;
  }
  .about .btn:hover{
    background: #e5e7eb !important;
    border-color: #e5e7eb !important;
    color: #0b1220 !important;
  }
}

/* 3) Also support manual toggles some sites use */
html[data-theme="dark"] .about, html[data-theme="dark"] .about p,
html[data-theme="dark"] .cv,    html[data-theme="dark"] .cv ul, html[data-theme="dark"] .cv li,
html.dark .about, html.dark .about p,
html.dark .cv,    html.dark .cv ul, html.dark .cv li,
body.dark .about, body.dark .about p,
body.dark .cv,    body.dark .cv ul, body.dark .cv li{
  color: #e5e7eb !important;
}
html[data-theme="dark"] .cv .news .date, html[data-theme="dark"] .cv .muted,
html.dark .cv .news .date,               html.dark .cv .muted,
body.dark .cv .news .date,               body.dark .cv .muted{
  color: #a3a3a3 !important;
}
html[data-theme="dark"] .about a, html[data-theme="dark"] .cv a,
html.dark .about a,               html.dark .cv a,
body.dark .about a,               body.dark .cv a{
  color: #5eead4 !important;
}
</style>


<div class="about">
  <p>
    I am a fourth-year Ph.D. student at
    <a href="https://www.tue.nl/en/" target="_blank" rel="noopener noreferrer">Eindhoven University of Technology</a>,
    under the supervision of
    <a href="https://www.win.tue.nl/~mpechen/?_gl=1*iopzok*_ga*NTk4Mzc5NDExLjE2ODA3NzUyNjU.*_ga_JN37M497TT*MTY5ODMzMjE2My4yOC4xLjE2OTgzMzIxODEuNDIuMC4w"
       target="_blank" rel="noopener noreferrer">Mykola Pechenizkiy</a>
    and
    <a href="https://mengf1.github.io/" target="_blank" rel="noopener noreferrer">Meng Fang</a>.
    I am also very fortunate to work closely with
    <a href="https://yalidu.github.io/" target="_blank" rel="noopener noreferrer">Prof. Yali Du</a>
    at
    <a href="https://www.kcl.ac.uk/" target="_blank" rel="noopener noreferrer">King’s College London</a>,
    and
    <a href="https://biweihuang.com/" target="_blank" rel="noopener noreferrer">Prof. Biwei Huang</a>
    at
    <a href="https://ucsd.edu/" target="_blank" rel="noopener noreferrer">University of California San Diego</a>.
    Prior to joining TU/e, I was a master student in
    <a href="https://www.en.sdu.edu.cn/" target="_blank" rel="noopener noreferrer">Shandong University</a> (SDU),
    supervised by
    <a href="http://www.vsislab.com/" target="_blank" rel="noopener noreferrer">Prof. Wei Zhang</a>.
    I also obtained my bachelor's degree from Shandong University.
  </p>

  <p>
    My research focuses on reinforcement learning, especially RL for LLMs and causal RL. And I have published 10+ papers at the top AI conferences. <a href="https://scholar.google.com/citations?user=YOUR_ID&hl=en" target="_blank" rel="noopener noreferrer">
  <img src="/assets/badges/scholar_citations.svg" alt="Google Scholar citations">
</a>

  </p>
  <p>
    I am currently on the job market and actively looking for collaboration and visiting opportunities. If you are interested, feel free to contact me.
    <a class="btn" href="mailto:y.zhang5@tue.nl">Email</a>
  </p>
</div>
<style>
  /* ===== Unified sections (scoped) ===== */
  .cv { max-width: 980px; margin: 0 auto; }

  .cv h2{
    font-size: 1.35rem;
    margin: 22px 0 10px;
    padding-bottom: 6px;
    border-bottom: 1px solid #e5e7eb;
  }

  .cv ul{
    margin: 0;
    padding-left: 1.2em;
    line-height: 1.8;
    color: #111827;
  }
  .cv li{ margin: 8px 0; }

  .cv a{ text-decoration: none; }
  .cv a:hover{ text-decoration: underline; }

  /* nicer separators than <hr> */
  /* divider: make it spacing only (no line) */
  .cv .divider{
    height: 0;            /* no extra line */
    background: none;     /* no extra line */
    margin: 18px 0;       /* keep spacing between sections */
    border: 0;
  }
  .cv .muted{ color: #374151; }

  /* News: align date for better readability */
  .cv .news li{ margin: 10px 0; }
  .cv .news .date{
    display: inline-block;
    min-width: 90px;      /* aligns month-year */
    color: #374151;
    font-weight: 600;
  }
</style>

<div class="cv">
  <h2>✨ News</h2>
  <ul class="news">
    <li><span class="date">Feb 2026</span>I’m co-organizing a tutorial on reward modeling for LLMs at CAPL — see you in Tübingen!</li>
    <li><span class="date">Oct 2025</span>One paper was accepted to NeurIPS 2025 as spotlight. ✨</li>
    <li><span class="date">May 2025</span>I will give a tutorial at the OxML Summer School. 🧑‍🏫</li>
    <li><span class="date">May 2025</span>Two papers were accepted by TMLR. </li>
    <li><span class="date">Jan 2025</span>RuAG was accepted to ICLR 2025. 🚀</li>
    <li><span class="date">Oct 2024</span>MACCA and CAST were accepted to the NeurIPS 2024 CRL Workshop. </li>
    <li><span class="date">Oct 2024</span>I will give a talk at the Women in AI &amp; Robotics Reading Group. </li>
    <li><span class="date">Dec 2023</span>One paper was accepted to AAAI 2024. </li>
    <li><span class="date">Oct 2023</span>I will give a talk at RLChina. 💬</li>
    <li><span class="date">Sep 2023</span>Two papers were accepted to NeurIPS 2023. 🎉</li>
    <li><span class="date">Oct 2022</span>I started my PhD journey at TU/e. 🌱</li>
  </ul>

  <!-- <div class="divider"></div> -->

  <h2>📚 Service</h2>
  <ul>
    <li>Journal Reviewer: Transactions on Machine Learning Research, IEEE Transactions on Artificial Intelligence.</li>
    <li>Conference Reviewer: NeurIPS 2024-2025, ICML 2024-2026, ICLR 2025-2026, AAAI 2025-2026, AAMAS 2024-2025, AISTATS 2025.</li>
    <li>Teaching Assistant: Generative AI in OxML 2024, 2IIG0 Data Mining and Machine Learning.</li>
    <li>Supervised MSc students: Schipper Olivier, Beuningen Niels van, Dirk Michielsen, Xie Lan.</li>
  </ul>

  <h2>🧑‍💻 Internship</h2>
  <ul>
    <li>
      Microsoft Research Asia, mentored by
      <a href="https://scholar.google.com/citations?user=hqlU92YAAAAJ" target="_blank" rel="noopener noreferrer">Dr. Lu Wang</a>,
      2024.
    </li>
  </ul>

  <!-- <div class="divider"></div> -->


  <h2>🌟 Awards</h2>
  <ul>
    <li>NeurIPS 2023 Travel Award</li>
    <li>Outstanding Graduates of Shandong Province (2019)</li>
    <li class="muted">
      Competitions: Second Prize in the Chinese Graduate Mathematical Modeling Competition (2019),
      First Prize in the National Electronic Design Competition, Shandong Province (2017),
      International Aquatic Robot Competition Champion (2018, 2019)
    </li>
    <li class="muted">
      Scholarships: Shandong University first-class scholarship, Shandong University outstanding students special scholarship, etc.
    </li>
  </ul>

  <!-- <div class="divider"></div> -->


</div>

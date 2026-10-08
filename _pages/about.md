---
permalink: /
title: ""
excerpt: "About me"
author_profile: true
redirect_from:
  - /about/
  - /about.html
  - /publications/
---

I am a postdoctoral researcher at [Delft University of Technology](https://www.tudelft.nl/en/), working with [Frans A. Oliehoek](https://fransoliehoek.net/) and [Jan-Willem van de Meent](https://amlab-amsterdam.github.io/people/JanWillemVanDeMeent/).

I obtained my Ph.D. from [Eindhoven University of Technology](https://www.tue.nl/en/), supervised by [Mykola Pechenizkiy](https://www.win.tue.nl/~mpechen/) and [Meng Fang](https://mengf1.github.io/). I am also very fortunate to work closely with [Yali Du](https://yalidu.github.io/) at [King’s College London](https://www.kcl.ac.uk/) and [Biwei Huang](https://biweihuang.com/) at [University of California San Diego](https://ucsd.edu/). I am currently a visiting student at the [Max Planck Institute for Intelligent Systems](https://is.mpg.de), supervised by [Shiwei Liu](https://shiweiliuiiiiiii.github.io), where I work at the intersection of reinforcement learning (RL) and large language models (LLMs). Previously, I was a research intern at Microsoft, mentored by [Lu Wang](https://scholar.google.com/citations?user=hqlU92YAAAAJ&hl=en), and I obtained my Master's and Bachelor's degrees at [Shandong University](https://www.en.sdu.edu.cn/), supervised by [Wei Zhang](http://www.vsislab.com/).

My research focuses on reinforcement learning, especially RL for LLMs and causal RL.

<span style="color:#b91c1c">I am currently on the job market and actively looking for my next position, as well as visiting and collaboration opportunities. If you are interested, feel free to contact me.</span> [Email](mailto:yudizhangzhang@tudelft.nl)

## 🎓 Education

**Ph.D. in Computer Science**, Eindhoven University of Technology, Netherlands<br>
*Sep 2022 – Sep 2026 · Supervisors: [Mykola Pechenizkiy](https://mpechen.win.tue.nl/), [Meng Fang](https://mengfn.github.io/)*

**M.Sc. in Control Science and Engineering**, Shandong University, China<br>
*Sep 2019 – Sep 2022 · Supervisor: [Wei Zhang](http://www.vsislab.com/)*

**B.Sc. in Automation**, Shandong University, China<br>
*Sep 2015 – Jul 2019*

## 🧑‍💻 Experience

**Delft University of Technology** — Postdoctoral researcher, Delft, Netherlands<br>
*Sep 2026 – present · Working with [Frans A. Oliehoek](https://fransoliehoek.net/) and [Jan-Willem van de Meent](https://amlab-amsterdam.github.io/people/JanWillemVanDeMeent/)*

**Max Planck Institute for Intelligent Systems** — Visiting student, Tübingen, Germany<br>
*Apr 2026 – present · Supervisor: [Shiwei Liu](https://shiweiliuiiiiiii.github.io)*

- RL from verifiable rewards (RLVR) and the learning dynamics of LLMs.
- Benchmarking LLM data filtering for post-training.
- Agentic RL with harnesses and skills.

**Microsoft** — Research intern, Beijing, China<br>
*Mar – Oct 2024 · Mentor: [Lu Wang](https://scholar.google.com/citations?user=hqlU92YAAAAJ&hl=en)*

- LLM reasoning: built **RuAG**, which learns interpretable logic rules from offline data via LLM-aided MCTS and injects them into prompts (ICLR 2025).
- LLM distillation: a pipeline that distills both responses and reward signals into smaller models.
- Large Action Models (LAMs): contributed to the supervised fine-tuning phase (TMLR 2025).

## ✨ News

{% for n in site.data.news limit:5 %}
- **{{ n.date }}** — {{ n.text }}
{% endfor %}

[All news &rarr;](/news/)

## 📄 Publications {#publications}

{% include publications.html %}

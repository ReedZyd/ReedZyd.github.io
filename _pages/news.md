---
layout: archive
title: "News"
permalink: /news/
author_profile: true
---

{% for n in site.data.news %}
- **{{ n.date }}** — {{ n.text }}
{% endfor %}

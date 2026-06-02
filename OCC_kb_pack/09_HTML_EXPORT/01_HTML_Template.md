---
title: HTML Export Template
doc_id: 09_HTML_001
version: 1.0
owner: Sales Training Lead
last_updated: 2026-06-01
priority_tier: 7
applies_to: [html_export]
tags: [html, template, elevenlabs]
---

# HTML Export Template

## Purpose

This file provides the standard HTML template for ElevenLabs-ready knowledge base exports.

Use this template for every exported Markdown source file.

---

# Standard HTML Template

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>{{title}}</title>
  <meta name="doc_id" content="{{doc_id}}">
  <meta name="version" content="{{version}}">
  <meta name="owner" content="{{owner}}">
  <meta name="last_updated" content="{{last_updated}}">
  <meta name="priority_tier" content="{{priority_tier}}">
  <meta name="applies_to" content="{{applies_to}}">
  <meta name="tags" content="{{tags}}">
  <meta name="source_path" content="{{source_path}}">
</head>
<body>
  <article>
    <header>
      <h1>{{title}}</h1>
      <section class="metadata">
        <p><strong>Doc ID:</strong> {{doc_id}}</p>
        <p><strong>Version:</strong> {{version}}</p>
        <p><strong>Owner:</strong> {{owner}}</p>
        <p><strong>Last Updated:</strong> {{last_updated}}</p>
        <p><strong>Priority Tier:</strong> {{priority_tier}}</p>
        <p><strong>Applies To:</strong> {{applies_to}}</p>
        <p><strong>Tags:</strong> {{tags}}</p>
        <p><strong>Source:</strong> {{source_path}}</p>
      </section>
    </header>

    {{converted_body}}
  </article>
</body>
</html>
```

---

# Minimal Styling Rule

Do not add heavy design styling.

If basic readability styling is needed, use inline semantic HTML only, not external CSS.

Allowed:

- `<article>`
- `<section>`
- `<header>`
- `<h1>` through `<h4>`
- `<p>`
- `<strong>`
- `<em>`
- `<ul>` / `<ol>`
- `<table>`
- `<blockquote>`
- `<pre><code>`

Avoid:

- JavaScript
- External stylesheets
- Images
- Decorative HTML
- Hidden content
- Complex layouts

---

# Word Track Formatting

Use blockquotes for approved rep or customer-facing language.

Example:

```html
<blockquote>
  <p>Mr./Mrs. Customer, did the office explain what we are going to do today?</p>
</blockquote>
```

---

# Scoring Format Formatting

Use code blocks for scoring templates.

Example:

```html
<pre><code>Score: __ / 5
Missed Step:
KPI Impact:
Corrected Move:
Practice Drill:</code></pre>
```

---

# Final Rule

The template should make retrieval easier, not prettier.

ElevenLabs needs clear structure more than visual design.

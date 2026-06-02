---
title: HTML Export Rules
doc_id: 09_HTML_000
version: 1.0
owner: Sales Training Lead
last_updated: 2026-06-01
priority_tier: 7
applies_to: [html_export]
tags: [html, export, elevenlabs, knowledge_base]
---

# HTML Export Rules

## Purpose

This document controls how rebuilt Markdown knowledge-base files should be converted into ElevenLabs-ready HTML.

Markdown is the editable source of truth.

HTML is the upload format.

Do not edit exported HTML directly unless the change is formatting-only. If content changes are needed, update the Markdown source first and re-export.

---

# Export Philosophy

The HTML export should make the knowledge base easier for ElevenLabs to retrieve and use.

The export should preserve:

- Clear headings
- Short sections
- Tables
- Lists
- Required word tracks
- Required disclosures
- Step numbers
- Guardrails
- Scoring formats
- Roleplay templates
- Source-of-truth hierarchy

The export should avoid:

- Styling clutter
- Decorative design
- JavaScript
- External CSS
- Images
- Hidden content
- Unused old DOCX references
- `[VERIFY]` placeholders
- Duplicate old scripts
- Conflicting Step 8 or Step 9 language
- Conflicting warranty claims

---

# HTML Structure Standard

Each exported HTML file should use this structure:

```html
<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Document Title</title>
  <meta name="doc_id" content="DOC_ID">
  <meta name="version" content="VERSION">
  <meta name="source_path" content="SOURCE_MARKDOWN_PATH">
</head>
<body>
  <article>
    <header>
      <h1>Document Title</h1>
      <p><strong>Doc ID:</strong> DOC_ID</p>
      <p><strong>Version:</strong> VERSION</p>
      <p><strong>Source:</strong> SOURCE_MARKDOWN_PATH</p>
    </header>
    <!-- Converted content -->
  </article>
</body>
</html>
```

---

# Metadata Rules

The YAML front matter from each Markdown file should be converted into visible or meta content.

Required metadata to preserve:

- title
- doc_id
- version
- owner
- last_updated
- priority_tier
- applies_to
- tags

Recommended visible metadata block:

```html
<section class="metadata">
  <p><strong>Doc ID:</strong> ...</p>
  <p><strong>Version:</strong> ...</p>
  <p><strong>Owner:</strong> ...</p>
  <p><strong>Last Updated:</strong> ...</p>
  <p><strong>Priority Tier:</strong> ...</p>
  <p><strong>Applies To:</strong> ...</p>
  <p><strong>Tags:</strong> ...</p>
</section>
```

---

# Heading Rules

Use semantic HTML headings.

| Markdown | HTML |
|---|---|
| `#` | `<h1>` |
| `##` | `<h2>` |
| `###` | `<h3>` |
| `####` | `<h4>` |

Do not skip heading levels unless inherited from the source Markdown.

---

# Table Rules

Convert Markdown tables into real HTML tables.

Use:

```html
<table>
  <thead>
    <tr><th>...</th></tr>
  </thead>
  <tbody>
    <tr><td>...</td></tr>
  </tbody>
</table>
```

Do not convert tables into images.

---

# Word Track Rules

Approved word tracks must remain exact.

Use `<blockquote>` for customer-facing language and rep word tracks.

Example:

```html
<blockquote>
  <p>The total investment for the full project comes to $List Price...</p>
</blockquote>
```

Do not paraphrase locked Step 8 or Step 9 language during export.

---

# Code Block Rules

Keep diagnostic formats, scoring formats, and templates in `<pre><code>` blocks.

Example:

```html
<pre><code>Score: __ / 5
Missed Step:
KPI Impact:
Corrected Move:
Practice Drill:</code></pre>
```

---

# Compliance and Disclosure Rules

Required legal or compliance language must remain exact.

Do not shorten:

- GreenSky / Synovus disclosure
- Deferred-interest disclosure
- Range-rate disclosure
- Prohibited-claims language
- Missing-information response
- Safe default warranty answer

---

# File Naming Rules

Exported HTML files should keep the same base filename as the Markdown source.

Example:

```text
01_CORE_RULES_PROMPT_MODE/00_Hope_System_Prompt_v5.md
```

Exports to:

```text
09_HTML_EXPORT/html/01_CORE_RULES_PROMPT_MODE/00_Hope_System_Prompt_v5.html
```

---

# Export Folder Standard

Use this output structure:

```text
09_HTML_EXPORT/
  00_HTML_Export_Rules.md
  01_HTML_Template.md
  02_Conversion_Checklist.md
  03_File_Export_Index.md
  html/
    01_CORE_RULES_PROMPT_MODE/
    02_APPROVED_LANGUAGE/
    03_OBJECTION_HANDLING/
    04_PRODUCT_KNOWLEDGE/
    05_FINANCING/
    06_WARRANTIES/
    07_CUSTOMER_PERSONAS/
    08_ROLEPLAY_SCENARIOS/
```

---

# Do Not Export

Do not export audit-only admin files into ElevenLabs unless the admin file is intentionally used as a knowledge-base control file.

Default: do not export:

```text
00_ADMIN/*_AUDIT.md
00_ADMIN/FINAL_KB_REBUILD_STATUS.md
```

These are project management files, not rep-facing KB files.

---

# Required Pre-Export Checks

Before exporting, confirm:

1. Hope System Prompt v5 is approved.
2. Step 8 language is approved.
3. Step 9 language is approved.
4. Current financing programs are accurate.
5. Warranty simplified coaching model is approved.
6. 9-customer persona model is approved.
7. Roleplay scenario engine is approved.
8. No `[VERIFY]` placeholders remain in export files.

---

# Final Rule

Do not let formatting edits change sales meaning.

The HTML export must preserve the system exactly, not improve, rewrite, or reinterpret it.

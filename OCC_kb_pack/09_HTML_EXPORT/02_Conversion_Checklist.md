---
title: HTML Conversion Checklist
doc_id: 09_HTML_002
version: 1.0
owner: Sales Training Lead
last_updated: 2026-06-01
priority_tier: 7
applies_to: [html_export]
tags: [html, checklist, qa, elevenlabs]
---

# HTML Conversion Checklist

## Purpose

This checklist must be used before, during, and after Markdown-to-HTML conversion.

The goal is to prevent content drift, formatting loss, or accidental upload of incomplete material into ElevenLabs.

---

# 1. Pre-Conversion Checklist

Before converting, confirm:

- [ ] Markdown source file is final or approved for export.
- [ ] YAML metadata exists.
- [ ] `title` is present.
- [ ] `doc_id` is present.
- [ ] `version` is present.
- [ ] `owner` is present.
- [ ] `last_updated` is present.
- [ ] `priority_tier` is present.
- [ ] `applies_to` is present.
- [ ] `tags` are present.
- [ ] No `[VERIFY]` placeholders remain.
- [ ] No old warranty claims conflict with simplified warranty model.
- [ ] No old Step 8 language conflicts with approved Step 8.
- [ ] No old Step 9 language conflicts with approved Step 9.
- [ ] No prohibited financing claims are presented as approved language.
- [ ] No unsupported product claims remain.

---

# 2. Conversion Checklist

During conversion, confirm:

- [ ] YAML metadata converts to visible metadata block.
- [ ] Document title becomes `<title>` and `<h1>`.
- [ ] Headings convert to proper `<h1>`, `<h2>`, `<h3>`, `<h4>`.
- [ ] Markdown tables convert to HTML tables.
- [ ] Word tracks convert to blockquotes.
- [ ] Code blocks remain in `<pre><code>`.
- [ ] Lists remain lists.
- [ ] Required disclosures remain exact.
- [ ] Step numbers remain intact.
- [ ] Scoring templates remain readable.
- [ ] Roleplay setup templates remain readable.
- [ ] No scripts, images, or external CSS are added.

---

# 3. Post-Conversion QA Checklist

After conversion, confirm:

- [ ] HTML opens correctly in a browser.
- [ ] Metadata is visible and correct.
- [ ] File name matches Markdown source base name.
- [ ] Folder path matches export standard.
- [ ] Tables are readable.
- [ ] Required word tracks are exact.
- [ ] Required disclosures are exact.
- [ ] Locked Step 8 language is exact.
- [ ] Locked Step 9 language is exact.
- [ ] Safe warranty default answer is exact.
- [ ] GreenSky / Synovus disclosure is exact.
- [ ] No audit-only files were exported by accident.

---

# 4. Spot-Check Priority Files

Always manually spot-check these high-risk files after conversion:

```text
01_CORE_RULES_PROMPT_MODE/00_Hope_System_Prompt_v5.md
01_CORE_RULES_PROMPT_MODE/01_Sales_System_Master.md
02_APPROVED_LANGUAGE/05_Financing_Presentation_Language.md
02_APPROVED_LANGUAGE/07_Close_Ask_Language.md
05_FINANCING/02_Current_Financing_Programs.md
05_FINANCING/05_Prohibited_Financing_Statements.md
06_WARRANTIES/01_Company_Workmanship_Warranty.md
06_WARRANTIES/02_Manufacturer_Warranties.md
08_ROLEPLAY_SCENARIOS/04_Closing_Roleplay_Step8_Step9.md
```

---

# 5. ElevenLabs Upload Checklist

Before uploading to ElevenLabs:

- [ ] Confirm final HTML folder only includes intended files.
- [ ] Confirm file names are readable and organized by folder.
- [ ] Confirm HTML files are not empty.
- [ ] Confirm no admin audit files are included unless intentionally added.
- [ ] Confirm Hope System Prompt v5 has been separately applied as the agent system prompt.
- [ ] Confirm KB HTML files do not duplicate the system prompt unnecessarily unless desired.
- [ ] Confirm file count matches File Export Index.

---

# 6. Change Management Rule

After export, if content needs to change:

1. Update Markdown source.
2. Re-export HTML.
3. Replace the HTML file in ElevenLabs.
4. Log the change in the relevant audit or status file.

Do not directly edit HTML for content changes.

---

# Final Rule

Conversion is not rewriting.

The HTML should say exactly what the Markdown says, only in upload-ready structure.

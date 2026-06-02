---
title: Final KB Rebuild Status
version: 1.0
owner: Sales Training Lead
last_updated: 2026-06-01
status: export_triggered
---

# Final KB Rebuild Status

## Purpose

This file summarizes the rebuilt OneCallCloser.ai / Hope knowledge base before ElevenLabs HTML export.

Markdown files are the editable source of truth.

HTML files will be the upload format for ElevenLabs.

---

# Current Export State

HTML export has been approved and triggered.

The repository contains an automated exporter at:

```text
OCC_kb_pack/09_HTML_EXPORT/convert_markdown_to_html.py
```

The GitHub Actions workflow that performs the export is located at:

```text
.github/workflows/export-elevenlabs-html.yml
```

Expected HTML output folder:

```text
OCC_kb_pack/09_HTML_EXPORT/html/
```

---

# Rebuild Status Summary

| Section | Status | Notes |
|---|---|---|
| 01_CORE_RULES_PROMPT_MODE | Complete | Core rules, system prompt, modes, scoring, coaching, compliance |
| 02_APPROVED_LANGUAGE | Complete | Step-specific approved language and drift control |
| 03_OBJECTION_HANDLING | Complete | 9 core objections tied to system step and KPI |
| 04_PRODUCT_KNOWLEDGE | Complete | Product files rebuilt with warranty drift removed |
| 05_FINANCING | Complete | Financing rebuilt with strict compliance and Step 8 alignment |
| 06_WARRANTIES | Complete | Simplified, low-interruption warranty coaching model |
| 07_CUSTOMER_PERSONAS | Complete | 9 total personas across Easy, Medium, Hard |
| 08_ROLEPLAY_SCENARIOS | Complete | Modular roleplay simulator engine |
| 09_HTML_EXPORT | Triggered | Automated exporter and workflow installed |

---

# Source-of-Truth Order

Hope should follow this authority order:

1. Compliance and prohibited claims
2. Conflict Priority Hierarchy
3. Hope System Prompt v5
4. Sales System Master
5. Approved Step 8 and Step 9 language
6. Financing files
7. Warranty files
8. Product files
9. Approved language files
10. Objection handling files
11. Customer persona files
12. Roleplay scenario files

If sources conflict, the higher source wins.

---

# Core System Files

Folder:

```text
01_CORE_RULES_PROMPT_MODE/
```

Current rebuilt files:

```text
00_Hope_System_Prompt_v5.md
01_Sales_System_Master.md
02_Sales_Process_Checklist.md
03_Appointment_Call_Flow.md
04_Coaching_Rules.md
05_Scoring_Rubric.md
06_Compliance_Prohibited_Claims.md
07_Mode_Definitions.md
08_Conflict_Priority_Hierarchy.md
```

---

# Final Rule

Markdown is the editable source of truth.

HTML is the ElevenLabs upload format.

Do not edit the HTML directly unless it is a formatting-only correction. Update Markdown first, then re-export.

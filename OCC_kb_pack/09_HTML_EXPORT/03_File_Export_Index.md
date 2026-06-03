---
title: File Export Index
doc_id: 09_HTML_003
version: 1.1
owner: Sales Training Lead
last_updated: 2026-06-02
priority_tier: 7
applies_to: [html_export]
tags: [html, export_index, elevenlabs, file_list]
---

# File Export Index

## Purpose

This document defines which Markdown source files should be exported to ElevenLabs-ready HTML.

Markdown files are the source of truth.

HTML files are the upload format.

---

# Export Root

HTML output should be written to:

```text
OCC_kb_pack/09_HTML_EXPORT/html/
```

Each source folder should be mirrored inside the HTML output folder.

---

# Do Not Export By Default

Do not export admin audit files by default:

```text
00_ADMIN/*_AUDIT.md
00_ADMIN/FINAL_KB_REBUILD_STATUS.md
```

These are project-control files, not rep-facing knowledge base files.

---

# Export Set - 01 Core Rules Prompt Mode

Source folder:

```text
01_CORE_RULES_PROMPT_MODE/
```

Export these files:

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
09_ElevenLabs_Voice_Mapping.md
```

Note:

Hope System Prompt v5.1 should be applied as the agent system prompt. Exporting it as a KB file is optional, but it is included in this index for completeness.

---

# Export Set - 02 Approved Language

Source folder:

```text
02_APPROVED_LANGUAGE/
```

Export these files:

```text
01_Opening_and_Setting_Expectations.md
02_Discovery_Questions.md
03_Demo_and_Education_Language.md
04_Price_Conditioning_Language.md
05_Financing_Presentation_Language.md
06_Objection_Response_Language.md
07_Close_Ask_Language.md
08_Rehash_and_Follow_Up_Language.md
```

---

# Export Set - 03 Objection Handling

Source folder:

```text
03_OBJECTION_HANDLING/
```

Export these files:

```text
01_Price_Too_High.md
02_Need_To_Think_About_It.md
03_Need_To_Talk_To_Spouse.md
04_Getting_Other_Estimates.md
05_Not_Ready.md
06_No_Time_Today.md
07_Dont_Want_Financing.md
08_Trust_Reputation_Concern.md
09_Same_Day_Close_Resistance.md
```

---

# Export Set - 04 Product Knowledge

Source folder:

```text
04_PRODUCT_KNOWLEDGE/
```

Export these files:

```text
00_Product_Overview.md
01_Fiber_Cement_Siding.md
02_Exterior_Painting.md
03_Windows_and_Doors.md
04_Gutters_and_Guards.md
05_Stucco.md
06_Competitor_Comparisons.md
```

---

# Export Set - 05 Financing

Source folder:

```text
05_FINANCING/
```

Export these files:

```text
00_FinancingOverview.md
01_FinancingPlans.md
02_FinancingObjectionHandling.md
03_ProhibitedFinancingClaims.md
```

---

# Export Set - 06 Warranties

Source folder:

```text
06_WARRANTIES/
```

Export these files:

```text
01_Company_Workmanship_Warranty.md
02_Manufacturer_Warranties.md
03_Warranty_Comparison_FAQ.md
04_Warranty_Claim_Limits.md
```

---

# Export Set - 07 Customer Personas

Source folder:

```text
07_CUSTOMER_PERSONAS/
```

Export these files:

```text
00_Persona_Index.md
01_Easy_Personas.md
02_Medium_Personas.md
03_Hard_Personas.md
```

---

# Export Set - 08 Roleplay Scenarios

Source folder:

```text
08_ROLEPLAY_SCENARIOS/
```

Export these files:

```text
00_Roleplay_Rules.md
01_Roleplay_Setup_Templates.md
02_Full_Appointment_Scenarios.md
03_Single_Step_Roleplay_Templates.md
04_Closing_Roleplay_Step8_Step9.md
05_First_Half_Roleplay_Steps1_6.md
06_Second_Half_Roleplay_Steps6_10.md
07_Objection_Drill_Bank.md
08_Follow_Up_Call_Drills.md
09_Pressure_Modifiers.md
```

---

# Export Set - 80 Coaching

Source folder:

```text
80_COACHING/
```

Export these files:

```text
00_Roleplay_Scoring_Rubric.md
01_Coaching_Rules.md
02_KPI_Definitions.md
03_Quick_Drill_Scoring_Rubric.md
04_Upstream_Diagnosis.md
05_Hope_Coaching_Protocol.md
06_Manager_Drill_Sheet.md
```

---

# Export Count

Total default export files:

| Section | Count |
|---|---:|
| 01 Core Rules Prompt Mode | 10 |
| 02 Approved Language | 8 |
| 03 Objection Handling | 9 |
| 04 Product Knowledge | 7 |
| 05 Financing | 4 |
| 06 Warranties | 4 |
| 07 Customer Personas | 4 |
| 08 Roleplay Scenarios | 10 |
| 80 Coaching | 7 |
| Total | 63 |

---

# Optional Export Files

Optional admin/control files:

```text
00_ADMIN/FINAL_KB_REBUILD_STATUS.md
09_HTML_EXPORT/00_HTML_Export_Rules.md
09_HTML_EXPORT/01_HTML_Template.md
09_HTML_EXPORT/02_Conversion_Checklist.md
09_HTML_EXPORT/03_File_Export_Index.md
```

These are useful for documentation but should not be uploaded as rep-facing KB unless intentionally desired.

---

# Final Rule

Only export files listed in the default export set unless there is a clear reason to include admin files.

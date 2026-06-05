---
title: File Export Index
doc_id: 09_HTML_003
version: 1.2
owner: Sales Training Lead
last_updated: 2026-06-04
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
10_Hope_Voice_Mapping_Guide.md
```

---

# Export Set - 02 Approved Language

```text
02_APPROVED_LANGUAGE/01_Opening_and_Setting_Expectations.md
02_APPROVED_LANGUAGE/02_Discovery_Questions.md
02_APPROVED_LANGUAGE/03_Demo_and_Education_Language.md
02_APPROVED_LANGUAGE/04_Price_Conditioning_Language.md
02_APPROVED_LANGUAGE/05_Financing_Presentation_Language.md
02_APPROVED_LANGUAGE/06_Objection_Response_Language.md
02_APPROVED_LANGUAGE/07_Close_Ask_Language.md
02_APPROVED_LANGUAGE/08_Rehash_and_Follow_Up_Language.md
```

---

# Export Set - 03 Objection Handling

```text
03_OBJECTION_HANDLING/01_Price_Too_High.md
03_OBJECTION_HANDLING/02_Need_To_Think_About_It.md
03_OBJECTION_HANDLING/03_Need_To_Talk_To_Spouse.md
03_OBJECTION_HANDLING/04_Getting_Other_Estimates.md
03_OBJECTION_HANDLING/05_Not_Ready.md
03_OBJECTION_HANDLING/06_No_Time_Today.md
03_OBJECTION_HANDLING/07_Dont_Want_Financing.md
03_OBJECTION_HANDLING/08_Trust_Reputation_Concern.md
03_OBJECTION_HANDLING/09_Same_Day_Close_Resistance.md
```

---

# Export Set - 04 Product Knowledge

```text
04_PRODUCT_KNOWLEDGE/00_Product_Overview.md
04_PRODUCT_KNOWLEDGE/01_Fiber_Cement_Siding.md
04_PRODUCT_KNOWLEDGE/02_Exterior_Painting.md
04_PRODUCT_KNOWLEDGE/03_Windows_and_Doors.md
04_PRODUCT_KNOWLEDGE/04_Gutters_and_Guards.md
04_PRODUCT_KNOWLEDGE/05_Stucco.md
04_PRODUCT_KNOWLEDGE/06_Competitor_Comparisons.md
```

---

# Export Set - 05 Financing

```text
05_FINANCING/00_FinancingOverview.md
05_FINANCING/01_FinancingPlans.md
05_FINANCING/02_FinancingObjectionHandling.md
05_FINANCING/03_ProhibitedFinancingClaims.md
```

---

# Export Set - 06 Warranties

```text
06_WARRANTIES/01_Company_Workmanship_Warranty.md
06_WARRANTIES/02_Manufacturer_Warranties.md
06_WARRANTIES/03_Warranty_Comparison_FAQ.md
06_WARRANTIES/04_Warranty_Claim_Limits.md
```

---

# Export Set - 07 Customer Personas

```text
07_CUSTOMER_PERSONAS/00_Persona_Index.md
07_CUSTOMER_PERSONAS/01_Easy_Personas.md
07_CUSTOMER_PERSONAS/02_Medium_Personas.md
07_CUSTOMER_PERSONAS/03_Hard_Personas.md
```

---

# Export Set - 08 Roleplay Scenarios

```text
08_ROLEPLAY_SCENARIOS/00_Roleplay_Rules.md
08_ROLEPLAY_SCENARIOS/01_Roleplay_Setup_Templates.md
08_ROLEPLAY_SCENARIOS/02_Full_Appointment_Scenarios.md
08_ROLEPLAY_SCENARIOS/03_Single_Step_Roleplay_Templates.md
08_ROLEPLAY_SCENARIOS/04_Closing_Roleplay_Step8_Step9.md
08_ROLEPLAY_SCENARIOS/05_First_Half_Roleplay_Steps1_6.md
08_ROLEPLAY_SCENARIOS/06_Second_Half_Roleplay_Steps6_10.md
08_ROLEPLAY_SCENARIOS/07_Objection_Drill_Bank.md
08_ROLEPLAY_SCENARIOS/08_Follow_Up_Call_Drills.md
08_ROLEPLAY_SCENARIOS/09_Pressure_Modifiers.md
```

---

# Export Set - 08 Coaching

```text
08_Coaching/00_Roleplay_Scoring_Rubric.md
08_Coaching/01_Coaching_Rules.md
08_Coaching/02_KPI_Definitions.md
08_Coaching/03_Quick_Drill_Scoring_Rubric.md
08_Coaching/04_Upstream_Diagnosis.md
08_Coaching/05_Hope_Coaching_Protocol.md
08_Coaching/06_Manager_Drill_Sheet.md
```

---

# Export Set - 09 FAQ

```text
09_FAQ/00_Customer_FAQ.md
09_FAQ/01_Rep_FAQ.md
09_FAQ/02_Product_FAQ.md
09_FAQ/03_Financing_FAQ.md
09_FAQ/04_Warranty_FAQ.md
09_FAQ/05_Hope_FAQ.md
```

---

# Export Count

| Section | Count |
|---|---:|
| 01 Core Rules Prompt Mode | 11 |
| 02 Approved Language | 8 |
| 03 Objection Handling | 9 |
| 04 Product Knowledge | 7 |
| 05 Financing | 4 |
| 06 Warranties | 4 |
| 07 Customer Personas | 4 |
| 08 Roleplay Scenarios | 10 |
| 08 Coaching | 7 |
| 09 FAQ | 6 |
| Total | 70 |

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

---

# Final Rule

Only export files listed in the default export set unless there is a clear reason to include admin files.

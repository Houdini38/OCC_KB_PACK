---
title: Final KB Rebuild Status
version: 1.0
owner: Sales Training Lead
last_updated: 2026-06-01
status: ready_for_html_export_planning
---

# Final KB Rebuild Status

## Purpose

This file summarizes the rebuilt OneCallCloser.ai / Hope knowledge base before ElevenLabs HTML export.

Markdown files are the editable source of truth.

HTML files will be the upload format for ElevenLabs.

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
| 09_HTML_EXPORT | Not Started | Next phase |

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

## Core Rules Locked

- Hope is a rep-practice machine, not a lecture machine.
- Coach short, drill fast.
- Step 8 and Step 9 must not blend.
- Compliance overrides everything.
- Financing requires hard compliance interruption.
- Warranty uses low-interruption coaching unless the rep clearly overpromises.
- Roleplay should not rescue the rep from losing unless compliance or severe confusion requires it.

---

# Approved Language Files

Folder:

```text
02_APPROVED_LANGUAGE/
```

Current rebuilt files:

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

## Approved Language Rules Locked

- Step 1 controls appointment expectations.
- Step 4 conditions value before price.
- Step 5 explains complete-project value.
- Step 8 controls affordability.
- Step 9 closes the decision.
- Follow-up call language is flexible but outcome-based.

---

# Objection Handling Files

Folder:

```text
03_OBJECTION_HANDLING/
```

Current rebuilt files:

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

## Objection Rule Locked

Every objection should follow:

```text
Acknowledge → Isolate → Clarify → Respond → Tie Back → Close Back
```

Objections must tie to:

- Missed step
- Customer signal
- Corrected move
- KPI impact
- Close-back question

---

# Product Knowledge Files

Folder:

```text
04_PRODUCT_KNOWLEDGE/
```

Current rebuilt files:

```text
00_Product_Overview.md
01_Fiber_Cement_Siding.md
02_Exterior_Painting.md
03_Windows_and_Doors.md
04_Gutters_and_Guards.md
05_Stucco.md
06_Competitor_Comparisons.md
```

## Product Rule Locked

Product docs teach product value.

Warranty docs control warranty.

Financing docs control financing.

Do not invent product specs, ratings, energy savings, ROI, or competitor claims.

---

# Financing Files

Folder:

```text
05_FINANCING/
```

Current rebuilt files:

```text
01_Financing_Master_Policy.md
02_Current_Financing_Programs.md
03_Financing_Presentation_Framework.md
04_Financing_FAQ.md
05_Prohibited_Financing_Statements.md
```

## Financing Rule Locked

```text
Payment isolation first. Promotion second. Compliance always.
```

Hard interrupt for prohibited financing claims, including:

- Guaranteed approval
- Everyone gets approved
- Free financing / free money
- Guaranteed APR, term, or payment
- SuperiorPRO approves the loan
- Pressure into application without consent

---

# Warranty Files

Folder:

```text
06_WARRANTIES/
```

Current rebuilt files:

```text
01_Company_Workmanship_Warranty.md
02_Manufacturer_Warranties.md
03_Warranty_Comparison_FAQ.md
04_Warranty_Claim_Limits.md
```

## Warranty Rule Locked

Warranty coaching is low-interruption.

Use soft correction unless the rep clearly overpromises.

Safe default warranty answer:

> SuperiorPRO warranties vary by product. We cover installation issues for 24 months on most jobs. Some products also have longer manufacturer coverage where we help with labor if the manufacturer approves. Your signed contract and warranty document are the final word.

---

# Customer Persona Files

Folder:

```text
07_CUSTOMER_PERSONAS/
```

Current rebuilt files:

```text
00_Persona_Index.md
01_Easy_Personas.md
02_Medium_Personas.md
03_Hard_Personas.md
```

## Persona Rule Locked

Exactly 9 customer personas:

| Difficulty | Personas |
|---|---|
| Easy | Enthusiastic Emma, Ready Randy, Retired Ruth |
| Medium | Hesitant Helen, Budget Brenda, Comparison Carl |
| Hard | Skeptical Steve, Bargain Betty, Angry Arnold |

Do not use Beginner, Intermediate, Advanced, or Expert as active difficulty labels.

---

# Roleplay Scenario Files

Folder:

```text
08_ROLEPLAY_SCENARIOS/
```

Current rebuilt files:

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

## Roleplay Rule Locked

Roleplay engine formula:

```text
Customer + Service Line + Roleplay Scope + Difficulty + Pressure Modifier + Win Condition
```

Roleplay scopes:

1. Full Appointment
2. Single Step
3. Closing Roleplay, Steps 8 and 9
4. First Half, Steps 1 through 6
5. Second Half, Steps 6 through 10
6. Objection Drill
7. Follow Up Call Mode

---

# Audit Files Created

Folder:

```text
00_ADMIN/
```

Current audit files:

```text
02_APPROVED_LANGUAGE_AUDIT.md
03_OBJECTION_HANDLING_AUDIT.md
04_PRODUCT_KNOWLEDGE_AUDIT.md
05_FINANCING_AUDIT.md
06_WARRANTIES_AUDIT.md
07_CUSTOMER_PERSONAS_AND_ROLEPLAY_AUDIT.md
FINAL_KB_REBUILD_STATUS.md
```

---

# Files Ready for HTML Export

All rebuilt Markdown files in these folders are ready for HTML export planning:

```text
01_CORE_RULES_PROMPT_MODE/
02_APPROVED_LANGUAGE/
03_OBJECTION_HANDLING/
04_PRODUCT_KNOWLEDGE/
05_FINANCING/
06_WARRANTIES/
07_CUSTOMER_PERSONAS/
08_ROLEPLAY_SCENARIOS/
```

Before converting, create the HTML export rules folder:

```text
09_HTML_EXPORT/
```

---

# HTML Export Requirements

The export system should preserve:

- Metadata
- Headings
- Tables
- Code blocks where needed
- Step numbers
- Required word tracks
- Guardrails
- Source-of-truth hierarchy
- Required disclosures
- Scoring formats
- Roleplay templates

The export system should remove or avoid:

- Unused old DOCX references
- `[VERIFY]` placeholders
- Duplicate old scripts
- Conflicting warranty claims
- Conflicting Step 8 / Step 9 language
- Any content marked audit-only

---

# Final Pre-Export Gate

Before HTML export, confirm:

1. Hope System Prompt v5 is approved.
2. Step 8 language is approved.
3. Step 9 language is approved.
4. Financing plan table is current.
5. Warranty simplified coaching model is approved.
6. 9-persona model is approved.
7. Roleplay simulator structure is approved.

---

# Final Rule

Markdown is the editable source of truth.

HTML is the ElevenLabs upload format.

Do not edit the HTML directly unless it is a formatting-only correction. Update Markdown first, then re-export.

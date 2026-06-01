---
title: Phase 2 Audit - Approved Language
version: 1.0
owner: Sales Training Lead
last_updated: 2026-06-01
status: active
---

# Phase 2 Audit - 02_APPROVED_LANGUAGE

## Purpose

This audit controls the approved language folder before ElevenLabs HTML conversion.

Approved language files are high-risk because old scripts can easily conflict with the Sales System Master, Step 8, Step 9, financing compliance, or follow-up call rules.

## Folder Under Audit

```text
OCC_kb_pack/02_APPROVED_LANGUAGE/
```

Expected source files:

```text
01_Opening_and_Setting_Expectations.docx
02_Discovery_Questions.docx
03_Demo_and_Education_Language.docx
04_Price_Conditioning_Language.docx
05_Financing_Presentation_Language.docx
06_Objection_Response_Language.docx
07_Close_Ask_Language.docx
08_Rehash_and_Follow_Up_Language.docx
```

## Replacement Strategy

Do not edit old DOCX files directly as the KB source.

Create clean `.md` source files that become the editable single source of truth. Convert final approved `.md` files into ElevenLabs-ready HTML later.

## Priority Table

| File | Risk Level | Action |
|---|---|---|
| `01_Opening_and_Setting_Expectations.docx` | Medium | Replace from Appointment Call Flow and Step 1 master |
| `02_Discovery_Questions.docx` | Medium | Replace from Step 2 and discovery library |
| `03_Demo_and_Education_Language.docx` | Medium | Replace from Step 5 and product docs |
| `04_Price_Conditioning_Language.docx` | High | Replace from Step 4 approved language |
| `05_Financing_Presentation_Language.docx` | Critical | Replace from Step 8 approved sequence and compliance rules |
| `06_Objection_Response_Language.docx` | High | Replace after objection handling folder is rebuilt |
| `07_Close_Ask_Language.docx` | Critical | Replace from Step 9 approved sequence |
| `08_Rehash_and_Follow_Up_Language.docx` | High | Replace from Follow Up Call Mode outcome framework |

## Non-Negotiable Rules

1. Compliance overrides approved language.
2. The Sales System Master controls step order and purpose.
3. Step 8 language must not drift.
4. Step 9 language must not drift.
5. Financing language must not promise approval, terms, rate, or payment.
6. Follow-up call language is flexible by wording but strict by outcome.
7. Objection language must tie back to a step and KPI.
8. Product and warranty facts must not be invented inside sales scripts.

## Step 8 / Step 9 Separation

Step 8 controls payment isolation.

Step 9 controls closing sequence.

Do not blend them.

| Step | Owns | Does Not Own |
|---|---|---|
| Step 8 | List Price, monthly payment, payment target, trial close, Monthly Promotion, Add/Subtract/Sharp Angle | Promo Home / Marketing Opportunity close |
| Step 9 | Physical disarm, timeline question, WOW line, Promo Home / Marketing Opportunity, adjusted offer, direct close | Monthly isolation or Add/Subtract/Sharp Angle |

## Completion Checklist

Before HTML export, each approved-language file must have:

- Metadata block
- Purpose
- When to use
- Approved structure or script
- What not to say
- KPI impact
- Compliance guardrail
- Source-of-truth note

## Immediate Files Created / Replaced

Create the following Markdown replacements first:

```text
04_Price_Conditioning_Language.md
05_Financing_Presentation_Language.md
07_Close_Ask_Language.md
```

Reason: these three files protect Step 4, Step 8, and Step 9. These are the highest revenue and language-drift risk areas.

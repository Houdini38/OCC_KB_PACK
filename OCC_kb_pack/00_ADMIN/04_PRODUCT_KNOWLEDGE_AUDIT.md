---
title: Phase 6 Audit - Product Knowledge
version: 1.0
owner: Operations Lead / Sales Training Lead
last_updated: 2026-06-01
status: active
---

# Phase 6 Audit - Product Knowledge

## Purpose

This audit controls the product knowledge folder before ElevenLabs HTML conversion.

Product knowledge should help the AI coach teach product value, answer customer questions, and run realistic roleplay without inventing technical specs, warranty terms, or competitor claims.

## Current Source Files Provided

The current product source set consists of:

```text
00_ProductOverview.md
01_FiberCementSiding.md
02_ExteriorPainting.md
03_WindowsAndDoors.md
04_GuttersAndGuards.md
05_Stucco.md
06_CompetitorComparisons.md
```

These are being converted into the `04_PRODUCT_KNOWLEDGE` folder as clean Markdown source files.

## Product Knowledge Philosophy

Product files should teach product value and approved talking points.

They should not control:

- Warranty terms
- Financing terms
- Discount authority
- Step 8 pricing language
- Step 9 closing language
- Unsupported competitor claims

Warranty information should live in `06_WARRANTIES`.

Financing information should live in `05_FINANCING`.

Competitor positioning should live in the approved competitor comparison file.

## Authority Rules

1. Compliance overrides product language.
2. Warranty files control warranty details.
3. Product files control product features, demo points, install process, and customer-facing product explanations.
4. Competitor comparison file controls competitive positioning.
5. Any `[VERIFY]` item is not approved for customer-facing use until confirmed.
6. If a product fact is not confirmed, use the missing-information response.

## Critical Cleanup Items

The uploaded product files include several warranty-related fields that conflict with the updated simplified warranty documents.

Examples:

- `[VERIFY: 10 years on workmanship]`
- `[VERIFY: 7-year workmanship]`
- `[VERIFY: 5–10 years]`

These should not be used as product facts.

Replacement rule:

> Warranty questions should be answered from `06_WARRANTIES`, not product sheets.

## Product Folder Target

```text
04_PRODUCT_KNOWLEDGE/
  00_Product_Overview.md
  01_Fiber_Cement_Siding.md
  02_Exterior_Painting.md
  03_Windows_and_Doors.md
  04_Gutters_and_Guards.md
  05_Stucco.md
  06_Competitor_Comparisons.md
```

## Completion Gates

Before HTML export, product files must pass these gates:

- No unverified specs are taught as facts.
- Warranty questions route to warranty files.
- Financing questions route to financing files.
- Competitor comparisons are category-based and non-defamatory.
- Banned claims are clearly listed.
- Every product feature connects to a homeowner benefit.
- Install-process language is homeowner-facing and practical.

## Revenue Rule

Product knowledge should make Step 5 stronger.

The goal is not trivia. The goal is to help the rep explain why the complete project is worth the investment.

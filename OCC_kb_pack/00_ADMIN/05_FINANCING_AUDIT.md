---
title: Phase 4 Audit - Financing
version: 1.0
owner: Sales Training Lead / Finance Manager
last_updated: 2026-06-01
status: active
---

# Phase 4 Audit - 05_FINANCING

## Purpose

This audit controls the financing folder before ElevenLabs HTML conversion.

Financing is high-risk because it affects affordability, Step 8 payment control, discount discipline, and consumer-credit compliance.

## Current Source Files Provided

The current financing source set consists of:

```text
00_FinancingOverview.md
01_FinancingPlans.md
02_FinancingObjectionHandling.md
03_ProhibitedFinancingClaims.md
```

These are being converted into the `05_FINANCING` folder as clean Markdown source files.

## Replacement Strategy

Expected KB folder structure:

```text
05_FINANCING/
  01_Financing_Master_Policy.md
  02_Current_Financing_Programs.md
  03_Financing_Presentation_Framework.md
  04_Financing_FAQ.md
  05_Prohibited_Financing_Statements.md
```

## Authority Rules

1. Compliance and prohibited financing claims override every other financing file.
2. Current financing programs control plan numbers, terms, payment factors, max discount allowances, and required disclosures.
3. Step 8 approved language controls the order of price and payment presentation.
4. Financing objection handling must not rewrite locked Step 8 or Step 9 language.
5. The AI coach must not invent approval, APR, term, payment, credit result, lender decision, prepayment rule, or discount authority.
6. Any unknown financing detail must be treated as unconfirmed.

## Source Strengths

The uploaded files provide:

- Active GreenSky plan categories
- Plan numbers
- Terms
- APR/rate ranges
- Payment factors
- Maximum discount allowances
- Required deferred-interest disclosures
- Required range-rate disclosures
- Synovus Bank / GreenSky lender language
- Banned phrase index
- Compliance interrupt protocol
- Financing objection examples

## Drift / Compliance Items to Clean While Converting

Some objection wording must be tightened before final KB use:

1. Replace any Step 8 wording that differs from the final approved sequence.
2. Avoid saying financing is "free money" because prohibited-claims guidance bans "free financing" and no-cost framing.
3. Avoid saying a soft credit pull "doesn't affect your score" unless confirmed as approved lender language.
4. Avoid telling reps to "let them leave only after running the application" because the customer controls consent.
5. Avoid "lock in our current promotion" unless tied to approved promotion policy.
6. Keep Step 9 Promo Home language out of Step 8 financing objection handling.
7. Never quote a specific payment as guaranteed. Use payment-factor examples only as estimates.

## Required Final Financing Files

| New File | Source | Purpose |
|---|---|---|
| `01_Financing_Master_Policy.md` | Financing Overview | Financing philosophy, rules, discount authority, Hope triggers |
| `02_Current_Financing_Programs.md` | Financing Plans | Exact active plans, factors, terms, disclosures |
| `03_Financing_Presentation_Framework.md` | Financing Overview + Step 8 + Objection Handling | How financing should be presented inside Step 8 |
| `04_Financing_FAQ.md` | All financing files | Field-ready FAQ for reps and coach |
| `05_Prohibited_Financing_Statements.md` | Prohibited Financing Claims | Tier 1 banned language and interrupt protocol |

## Completion Gates

Before HTML export, financing files must pass these gates:

- All plan terms match the approved plan table.
- Required disclosure language is preserved.
- Step 8 sequence matches the Sales System Master.
- No banned phrases remain as recommended language.
- Any risky examples are either removed or clearly marked as prohibited.
- Discount authority is clearly internal and not customer-facing.
- Plan 6160 incompatibility with discount is clearly marked.
- The lender relationship is stated correctly.

## Revenue Rule

Financing is an affordability tool, not a substitute for value or an excuse to discount early.

Step 8 must isolate payment before promotion.

---
title: Financing FAQ
doc_id: 05_FINANCING_004
version: 1.0
owner: Finance Manager
last_updated: 2026-06-01
priority_tier: 3
applies_to: [coach_mode, financing_mode, roleplay_mode, faq_mode]
tags: [financing, faq, greensky, step_8, disclosures]
---

# Financing FAQ

## Purpose

This file gives the AI coach quick answers to common financing questions.

Answers must stay inside approved financing terms, disclosures, and prohibited-claims rules.

If a question requires a fact not confirmed in the knowledge base, the agent must say it is not confirmed.

---

# FAQ Guardrail

Do not invent financing facts.

If the answer is not confirmed, say:

> I do not have that confirmed in the knowledge base. Do not quote it on a kitchen table. Flag it to your manager so we can get an approved answer.

For customer-facing uncertainty, say:

> I want to make sure I give you the exact number. Let me confirm that and follow up.

---

# Who provides the financing?

Financing is provided through GreenSky and made by Synovus Bank.

Required disclosure:

> GreenSky® program consumer loans are made by Synovus Bank, Member FDIC, NMLS #408043.

SuperiorPRO is not the lender.

All credit decisions and loan terms are determined by program lenders.

---

# Can SuperiorPRO approve the customer?

No.

SuperiorPRO does not approve financing.

Approved language:

> Financing is available for qualified customers, and the lender determines approval and terms.

---

# Can reps tell customers they will be approved?

No.

Do not say:

- "You will be approved."
- "Everyone gets approved."
- "Your credit is fine."
- "I can get you approved."

Approved replacement:

> We can submit the application and see what you qualify for. The lender makes the final decision.

---

# What plans are currently available?

Current plans are controlled by:

```text
05_FINANCING/02_Current_Financing_Programs.md
```

The plan categories are:

1. 0% APR plans
2. Fixed interest rate plans
3. No interest, no payments deferred-interest plans
4. No interest, with payments deferred-interest plans

Use only the approved current plan table.

---

# How does the rep calculate monthly payment?

Use the approved payment factor.

Formula:

```text
Project Amount x Payment Factor = Monthly Payment Estimate
```

Do not present the result as guaranteed approval, guaranteed terms, or guaranteed final payment.

---

# What is the lowest possible payment plan?

Based on the current financing programs file, Plan 9998 has a 180-month term and a 0.96% payment factor.

It is a fixed rate range plan with APR from 8.14% to 20.20% and rate from 7.99% to 19.99%.

Required disclosure for range-rate plans:

> Your specific APR within this range is determined by the lender based on your application.

---

# What is the strongest 0% APR plan?

Plan 6160 provides 0% APR for 60 months.

Important guardrail:

Plan 6160 has 0% max discount allowance.

Do not combine Plan 6160 with a discount request.

---

# Which plans allow the highest discount authority?

Current highest discount authority is 25% max discount off List Price for these plans:

- 2511
- 2720
- 2832
- 9991

This is internal guidance and must not be volunteered to the customer.

Discounts beyond listed maximum require manager approval.

---

# Can reps volunteer the max discount?

No.

Reps must not volunteer the maximum discount.

Use the approved sales sequence:

1. Build value.
2. Present List Price.
3. Isolate monthly comfort.
4. Offer Monthly Promotion.
5. Use Add/Subtract/Sharp Angle only if still needed.
6. Use Step 9 Promo Home / Marketing Opportunity only in Step 9.

---

# What is deferred interest?

Deferred interest means interest accrues during the promotional period but is waived if the full balance is paid before the promotional period ends.

Required disclosure:

> Interest is waived if the full amount is paid before the promotional period ends. If not paid in full, interest that accrued during the promo period will be charged.

Do not call deferred interest a 0% loan.

---

# What is no interest with payments?

Plan 4069 has deferred interest with required payments.

Required disclosure:

> Monthly payments are required during and after the promotional period. Interest is waived only if the full balance is paid before the promo period ends.

---

# Can reps say financing is free?

No.

Do not say:

- "Free financing"
- "No-cost financing"
- "There's no catch"
- "Free money"

Use accurate plan language instead.

---

# When should financing be discussed?

Financing should be discussed during Step 8 after List Price is presented.

The rep should present List Price first, then monthly payment, then isolate monthly comfort.

Do not use financing early as a shortcut around value building.

---

# What if the customer does not want financing?

Respect the preference.

Approved response:

> I understand. Some homeowners prefer not to finance. If you do not want to use our financing, are you comfortable putting 35% down and paying the balance upon completion?

If they hesitate, return to payment isolation without promising approval.

---

# Can reps tell customers the credit pull will not affect their score?

Only use credit-pull language that is confirmed by approved lender documentation.

If not confirmed, do not say it.

Use the missing-information response if needed.

---

# Can reps tell customers to apply just to compare?

Reps must not pressure customers into an application.

The customer controls consent.

The rep may explain financing options and ask whether the customer wants to apply, but must not mislead or coerce.

---

# Can reps compare GreenSky to outside lenders?

Reps may explain the approved GreenSky options.

Do not disparage other lenders.

Do not claim GreenSky will beat another lender unless confirmed by approved documentation.

---

# KPI Impact

Financing affects:

- Financing Attachment
- Close Rate
- Same-Day Close Rate
- Margin
- Discount Discipline
- Average Ticket

---

# Final Rule

When financing is unclear, verify before speaking.

A clean answer protects the customer, the rep, the company, and the sale.

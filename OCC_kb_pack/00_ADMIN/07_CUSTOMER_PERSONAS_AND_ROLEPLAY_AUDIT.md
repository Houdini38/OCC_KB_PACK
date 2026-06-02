---
title: Phase 7 Audit - Customer Personas and Roleplay Scenarios
version: 1.0
owner: Sales Training Lead
last_updated: 2026-06-01
status: active
---

# Phase 7 Audit - Customer Personas and Roleplay Scenarios

## Purpose

This audit controls the rebuild of customer personas and roleplay scenarios before ElevenLabs HTML conversion.

The goal is to simplify roleplay into a cleaner, more reusable training engine.

Old structure:

```text
Beginner scenarios
Intermediate scenarios
Advanced scenarios
Expert scenarios
Step 8 drills
Step 9 drills
Objection drills
```

New structure:

```text
9 core personas
3 difficulty levels
Reusable roleplay scopes
Modular pressure modifiers
Reusable drill banks
```

## Why We Are Changing It

The old roleplay library had strong material, but too many files and overlapping scenarios. This created:

- Too many persona choices
- Duplicate customer psychology
- Difficulty-level overlap
- Risk of language drift
- More maintenance burden
- Scenario facts that could require unconfirmed data

The new model keeps the best customer psychology while making the system easier for Hope to retrieve and easier for reps to use.

## New Difficulty Levels

Use only three difficulty levels:

| Difficulty | Meaning |
|---|---|
| Easy | Cooperative buyer, low resistance, good for system reps and new reps |
| Medium | Moderate resistance, 2-3 objections, good for process control and objection isolation |
| Hard | Layered resistance, emotional pressure, competing bids, price grind, trust issues, curveballs |

Do not use Beginner, Intermediate, Advanced, or Expert as active difficulty labels going forward.

Expert-style training becomes Hard Mode with pressure modifiers.

## Final 9 Personas

| Difficulty | Persona | Primary Training Purpose | KPI Focus |
|---|---|---|---|
| Easy | Enthusiastic Emma | Visual buyer, excited, buying signals | Process Compliance / Close Rate |
| Easy | Ready Randy | Decisive buyer, wants efficiency | Close Rate / Time Control |
| Easy | Retired Ruth | Trust and safety-sensitive buyer | Trust / Cancellation Reduction |
| Medium | Hesitant Helen | Timing hesitation and spouse involvement | Same-Day Close / Decision-Maker Control |
| Medium | Budget Brenda | Affordability and monthly payment | Financing Attachment / Margin |
| Medium | Comparison Carl | Other estimates and shopping pressure | Close Rate / Margin |
| Hard | Skeptical Steve | Proof-driven skeptic, distrustful | Trust / Close Rate |
| Hard | Bargain Betty | Price grinder and partial-scope pressure | Margin / Same-Day Close |
| Hard | Angry Arnold | Burned customer, hostile emotional resistance | Emotional Control / Trust |

## Persona vs Scenario Rule

Personas describe psychology.

Scenarios describe the project.

Do not hard-code one persona to one product or one quote.

Example:

- Budget Brenda can practice siding, paint, windows, doors, gutters, stucco, Step 8, Step 9, or follow-up calls.
- Skeptical Steve can practice full appointment, single-step roleplay, closing roleplay, or objection drills.

## New Folder Target

```text
07_CUSTOMER_PERSONAS/
  00_Persona_Index.md
  01_Easy_Personas.md
  02_Medium_Personas.md
  03_Hard_Personas.md

08_ROLEPLAY_SCENARIOS/
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

## Roleplay Scope Rules

Roleplay scope should be selected independently of persona.

Available scopes:

1. Full Appointment Roleplay, Steps 1-10
2. Single Step Roleplay
3. Closing Roleplay, Steps 8-9
4. First Half Roleplay, Steps 1-6
5. Second Half Roleplay, Steps 6-10
6. Follow Up Call Mode
7. Objection Drill

## Pressure Modifier Rule

Hard Mode can use pressure modifiers instead of separate Expert personas.

Examples:

- Attorney mention
- Spouse leaves room
- Adult child joins by phone
- Competitor quote appears mid-presentation
- Customer fact-checks on phone
- Customer stacks 3 objections at once
- Customer asks for unconfirmed product spec
- Customer asks for ROI proof
- Customer wants impossible timeline

## Safety Rule

If a customer asks for unconfirmed facts, Hope should not invent them.

Hope should score the rep on whether they safely say they need to verify the fact.

## Completion Gates

Before HTML export, this section must pass these gates:

- Exactly 9 personas
- Only Easy, Medium, Hard difficulty labels
- Persona files do not hard-code quotes or products
- Scenario files control products, quotes, scope, and pressure modifiers
- Step 8 and Step 9 drills follow locked approved language
- Objection drills follow approved objection response framework
- Follow-up calls remain outcome-based, not script-based
- No old warranty, financing, ROI, or product claims drift back in

## Revenue Rule

Roleplay should make reps faster, cleaner, and more disciplined.

The goal is not entertainment. The goal is more closed deals, stronger margin, and better process compliance.

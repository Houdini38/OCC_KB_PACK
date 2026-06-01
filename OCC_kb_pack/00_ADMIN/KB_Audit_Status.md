# OneCallCloser.ai KB Audit Status

**Status:** Active rebuild
**Repository folder:** `OCC_kb_pack/`
**Purpose:** Track the cleanup and completion of the OneCallCloser.ai / Hope knowledge base before HTML conversion for ElevenLabs.

## Primary Goal

Create one clean source of truth for:

- Sales process
- Approved scripted language
- Individual step sequences
- Objection handling
- Financing rules
- Product knowledge
- Warranty rules
- Customer personas
- Roleplay scenarios
- Coaching diagnostics
- FAQs

## Completion Rule

Do not improve files randomly. Work folder by folder in priority order. Each file should have:

- One clear purpose
- One source of truth
- One owner
- One version number
- No conflicting language
- No placeholders left unresolved unless marked for review

## Audit Priority Order

1. `01_CORE_RULES_PROMPT_MODE`
2. `02_APPROVED_LANGUAGE`
3. `03_OBJECTION_HANDLING`
4. `05_FINANCING`
5. `06_WARRANTIES`
6. `04_PRODUCT_KNOWLEDGE`
7. `07_CUSTOMER_PERSONAS`
8. `08_ROLEPLAY_SCENARIOS`
9. `09_COACHING_DIAGNOSTICS`
10. `10_FAQS`
11. `HTML_EXPORT`

## Phase 1 - Core Rules Audit

Folder: `01_CORE_RULES_PROMPT_MODE`

| File | Status | Action Needed |
|---|---|---|
| `01_Sales_System_Master.docx` | Needs review | Replace or update from final approved manager-training guide |
| `02_Sales_Process_Checklist.docx` | Needs review | Align with final 10-step sequence |
| `03_Appointment_Call_Flow.docx` | Needs review | Confirm timing, appointment flow, and expectation language |
| `04_Coaching_Rules.docx` | Needs review | Keep manager and AI coach behavior clean and specific |
| `05_Scoring_Rubric.docx` | Needs review | Tie scoring to KPIs and process compliance |
| `06_Compliance_Prohibited_Claims.docx` | High priority | Must override all scripts and roleplay behavior |
| `07_Mode_Definitions.docx` | Needs review | Confirm Coach, Roleplay, Demo, Product, Financing, and FAQ modes |
| `08_Conflict_Priority_Hierarchy.docx` | High priority | Must define exact source-of-truth order |

## Phase 2 - Approved Language Audit

Folder: `02_APPROVED_LANGUAGE`

Highest-risk files:

| File | Risk |
|---|---|
| `04_Price_Conditioning_Language.docx` | Step 4 drift risk |
| `05_Financing_Presentation_Language.docx` | Step 8 drift and compliance risk |
| `06_Objection_Response_Language.docx` | Closing language drift risk |
| `07_Close_Ask_Language.docx` | Step 9 drift risk |

Rule: Step 8 and Step 9 must match the final approved rep and manager guides. Do not blend old wording into these files.

## Phase 3 - Objection Handling Audit

Folder: `03_OBJECTION_HANDLING`

Every objection file should follow this structure:

- Customer says
- What it usually means
- Where it belongs in the 10-step system
- Approved response
- Close-back question
- KPI impact
- Do not say
- AI coach note

## Phase 4 - Financing Audit

Folder: `05_FINANCING`

Rules:

- Financing terms must stay exact.
- Do not promise approval.
- Do not invent APR, payment factor, term, lender decision, or discount authority.
- Step 8 payment-control sequence must be protected.
- Prohibited financing claims override scripts.

## Phase 5 - HTML Export

Final approved source files will be converted into ElevenLabs-ready HTML under:

`HTML_EXPORT/`

HTML requirements:

- Clean semantic HTML only
- No scripts
- No complex CSS
- Preserve doc ID, title, version, owner, priority, and tags
- Use headings, lists, tables, and blockquotes for retrieval clarity

## Immediate Next Action

Audit and replace the `01_CORE_RULES_PROMPT_MODE` folder first, beginning with:

1. `01_Sales_System_Master.docx`
2. `08_Conflict_Priority_Hierarchy.docx`
3. `07_Mode_Definitions.docx`
4. `06_Compliance_Prohibited_Claims.docx`

## Revenue Rule

Fix the sales-process brain first. Step 8 and Step 9 drift costs money every day because it weakens payment control, same-day close rate, and discount discipline.

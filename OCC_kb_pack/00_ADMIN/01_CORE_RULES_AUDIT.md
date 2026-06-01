# Phase 1 Audit - 01_CORE_RULES_PROMPT_MODE

**Status:** In progress
**Folder audited:** `OCC_kb_pack/01_CORE_RULES_PROMPT_MODE/`
**Audit purpose:** Determine which core prompt-mode files should be kept, replaced, rewritten, or split before final HTML conversion for ElevenLabs.

## Executive Summary

The core rules folder is the control tower for the agent. These files should be cleaned before product, warranty, financing, persona, scenario, FAQ, or diagnostic files are finalized.

The current pack uses `.docx` templates. That is fine as a working format, but the final ElevenLabs upload should be clean HTML generated from finalized source files.

The biggest risk in this folder is language conflict. If the Sales System Master, Checklist, Coaching Rules, Mode Definitions, or Approved Language files disagree, the agent will blend old scripts with new approved scripts.

## Core Audit Decision Table

| File | Current Role | Audit Status | Recommended Action | Reason |
|---|---|---|---|---|
| `01_Sales_System_Master.docx` | Main sales process source | High priority | Replace from final approved manager-training guide | This must be the single sales process source of truth, especially for Step 8 and Step 9. |
| `02_Sales_Process_Checklist.docx` | Rep/process checklist | Needs review | Rewrite after Sales System Master is finalized | Checklist should be derived from the master, not compete with it. |
| `03_Appointment_Call_Flow.docx` | Timing and appointment flow | Needs review | Update and keep | Should align with the appointment flow and expectation-setting language. |
| `04_Coaching_Rules.docx` | AI coach behavior rules | Needs review | Rewrite after Mode Definitions and Hierarchy are finalized | Coaching rules should tell the agent how to correct reps without inventing language. |
| `05_Scoring_Rubric.docx` | Roleplay and coaching scoring | Needs review | Rewrite around KPIs | Scoring should connect to Close Rate, Same-Day Close, ATS, financing attachment, process compliance, and margin. |
| `06_Compliance_Prohibited_Claims.docx` | Compliance restrictions | Tier 1 | Keep as highest authority and verify against final financing/compliance docs | Compliance must override scripts, roleplay behavior, product claims, financing claims, and warranty claims. |
| `07_Mode_Definitions.docx` | Agent mode behavior | High priority | Update and keep | Mode confusion causes poor coaching quality. This file should define Coach, Roleplay, Demonstration, Product, Financing, FAQ, and Diagnostics behavior. |
| `08_Conflict_Priority_Hierarchy.docx` | Source-of-truth hierarchy | Tier 1 | Replace or rewrite as a locked authority file | This decides what wins when documents conflict. It must be explicit and easy for the agent to follow. |

## Immediate Replacement Strategy

### Replace first

1. `01_Sales_System_Master.docx`
2. `08_Conflict_Priority_Hierarchy.docx`
3. `07_Mode_Definitions.docx`
4. `06_Compliance_Prohibited_Claims.docx`

### Rewrite second

5. `02_Sales_Process_Checklist.docx`
6. `04_Coaching_Rules.docx`
7. `05_Scoring_Rubric.docx`
8. `03_Appointment_Call_Flow.docx`

## Source-of-Truth Rules to Add

The rebuilt core folder should make these rules impossible to miss:

1. Compliance overrides everything.
2. Company policy overrides sales preference.
3. Final approved Step 8 and Step 9 language overrides any older script.
4. Product facts must come from approved product files only.
5. Warranty facts must come from approved warranty files only.
6. Financing facts must come from approved financing files only.
7. Roleplay personas can change behavior, but not facts, policies, or compliance.
8. If the agent does not know, it must say the information is not confirmed instead of inventing.

## Step 8 / Step 9 Drift Control

The new core files must protect the following separation:

| Step | Job | Do Not Blend With |
|---|---|---|
| Step 8 - Price Presentation | Anchor List Price, isolate monthly payment, confirm payment target, trial-close List Price, offer Monthly Promotion, use Add/Subtract/Sharp Angle only if still needed | Step 9 Promo Home language |
| Step 9 - Closing Sequence | Disarm, timeline question, WOW line, justified Promo Home / Marketing Opportunity, adjusted offer, direct close | Step 8 payment isolation language |

## Recommended Final File Format

For source management:

```text
.md source files for editing and version control
.html export files for ElevenLabs upload
.docx only when a printable human training guide is needed
```

Recommended final structure inside this folder:

```text
01_CORE_RULES_PROMPT_MODE/
  01_Sales_System_Master.md
  02_Sales_Process_Checklist.md
  03_Appointment_Call_Flow.md
  04_Coaching_Rules.md
  05_Scoring_Rubric.md
  06_Compliance_Prohibited_Claims.md
  07_Mode_Definitions.md
  08_Conflict_Priority_Hierarchy.md
```

## Quality Gates Before HTML Conversion

Each core file must pass these gates:

- No bracketed placeholders unless intentionally marked `[VERIFY]`.
- No conflicting Step 8 or Step 9 language.
- No prohibited financing, warranty, or product claims.
- Every rule has one owner and one authority level.
- Every mode tells the agent exactly what to do and what not to do.
- Every coaching rule connects to process compliance or a KPI.

## Next Action

Create the replacement draft for:

```text
01_CORE_RULES_PROMPT_MODE/08_Conflict_Priority_Hierarchy.md
```

Reason: the hierarchy should be locked before replacing the sales system and coaching rules. It prevents the agent from blending new approved language with old template language.

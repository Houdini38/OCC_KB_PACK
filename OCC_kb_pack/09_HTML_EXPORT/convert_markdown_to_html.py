#!/usr/bin/env python3
"""Convert approved Hope KB Markdown files to simple ElevenLabs-ready HTML."""

from __future__ import annotations

import html
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
KB_ROOT = ROOT / "OCC_kb_pack"
OUT_ROOT = KB_ROOT / "09_HTML_EXPORT" / "html"

EXPORT_FILES = [
    "01_CORE_RULES_PROMPT_MODE/00_Hope_System_Prompt_v5.md",
    "01_CORE_RULES_PROMPT_MODE/01_Sales_System_Master.md",
    "01_CORE_RULES_PROMPT_MODE/02_Sales_Process_Checklist.md",
    "01_CORE_RULES_PROMPT_MODE/03_Appointment_Call_Flow.md",
    "01_CORE_RULES_PROMPT_MODE/04_Coaching_Rules.md",
    "01_CORE_RULES_PROMPT_MODE/05_Scoring_Rubric.md",
    "01_CORE_RULES_PROMPT_MODE/06_Compliance_Prohibited_Claims.md",
    "01_CORE_RULES_PROMPT_MODE/07_Mode_Definitions.md",
    "01_CORE_RULES_PROMPT_MODE/08_Conflict_Priority_Hierarchy.md",
    "01_CORE_RULES_PROMPT_MODE/09_ElevenLabs_Voice_Mapping.md",
    "01_CORE_RULES_PROMPT_MODE/10_Hope_Voice_Mapping_Guide.md",
    "02_APPROVED_LANGUAGE/01_Opening_and_Setting_Expectations.md",
    "02_APPROVED_LANGUAGE/02_Discovery_Questions.md",
    "02_APPROVED_LANGUAGE/03_Demo_and_Education_Language.md",
    "02_APPROVED_LANGUAGE/04_Price_Conditioning_Language.md",
    "02_APPROVED_LANGUAGE/05_Financing_Presentation_Language.md",
    "02_APPROVED_LANGUAGE/06_Objection_Response_Language.md",
    "02_APPROVED_LANGUAGE/07_Close_Ask_Language.md",
    "02_APPROVED_LANGUAGE/08_Rehash_and_Follow_Up_Language.md",
    "03_OBJECTION_HANDLING/01_Price_Too_High.md",
    "03_OBJECTION_HANDLING/02_Need_To_Think_About_It.md",
    "03_OBJECTION_HANDLING/03_Need_To_Talk_To_Spouse.md",
    "03_OBJECTION_HANDLING/04_Getting_Other_Estimates.md",
    "03_OBJECTION_HANDLING/05_Not_Ready.md",
    "03_OBJECTION_HANDLING/06_No_Time_Today.md",
    "03_OBJECTION_HANDLING/07_Dont_Want_Financing.md",
    "03_OBJECTION_HANDLING/08_Trust_Reputation_Concern.md",
    "03_OBJECTION_HANDLING/09_Same_Day_Close_Resistance.md",
    "04_PRODUCT_KNOWLEDGE/00_Product_Overview.md",
    "04_PRODUCT_KNOWLEDGE/01_Fiber_Cement_Siding.md",
    "04_PRODUCT_KNOWLEDGE/02_Exterior_Painting.md",
    "04_PRODUCT_KNOWLEDGE/03_Windows_and_Doors.md",
    "04_PRODUCT_KNOWLEDGE/04_Gutters_and_Guards.md",
    "04_PRODUCT_KNOWLEDGE/05_Stucco.md",
    "04_PRODUCT_KNOWLEDGE/06_Competitor_Comparisons.md",
    "05_FINANCING/00_FinancingOverview.md",
    "05_FINANCING/01_FinancingPlans.md",
    "05_FINANCING/02_FinancingObjectionHandling.md",
    "05_FINANCING/03_ProhibitedFinancingClaims.md",
    "06_WARRANTIES/01_Company_Workmanship_Warranty.md",
    "06_WARRANTIES/02_Manufacturer_Warranties.md",
    "06_WARRANTIES/03_Warranty_Comparison_FAQ.md",
    "06_WARRANTIES/04_Warranty_Claim_Limits.md",
    "07_CUSTOMER_PERSONAS/00_Persona_Index.md",
    "07_CUSTOMER_PERSONAS/01_Easy_Personas.md",
    "07_CUSTOMER_PERSONAS/02_Medium_Personas.md",
    "07_CUSTOMER_PERSONAS/03_Hard_Personas.md",
    "08_ROLEPLAY_SCENARIOS/00_Roleplay_Rules.md",
    "08_ROLEPLAY_SCENARIOS/01_Roleplay_Setup_Templates.md",
    "08_ROLEPLAY_SCENARIOS/02_Full_Appointment_Scenarios.md",
    "08_ROLEPLAY_SCENARIOS/03_Single_Step_Roleplay_Templates.md",
    "08_ROLEPLAY_SCENARIOS/04_Closing_Roleplay_Step8_Step9.md",
    "08_ROLEPLAY_SCENARIOS/05_First_Half_Roleplay_Steps1_6.md",
    "08_ROLEPLAY_SCENARIOS/06_Second_Half_Roleplay_Steps6_10.md",
    "08_ROLEPLAY_SCENARIOS/07_Objection_Drill_Bank.md",
    "08_ROLEPLAY_SCENARIOS/08_Follow_Up_Call_Drills.md",
    "08_ROLEPLAY_SCENARIOS/09_Pressure_Modifiers.md",
    "08_Coaching/00_Roleplay_Scoring_Rubric.md",
    "08_Coaching/01_Coaching_Rules.md",
    "08_Coaching/02_KPI_Definitions.md",
    "08_Coaching/03_Quick_Drill_Scoring_Rubric.md",
    "08_Coaching/04_Upstream_Diagnosis.md",
    "08_Coaching/05_Hope_Coaching_Protocol.md",
    "08_Coaching/06_Manager_Drill_Sheet.md",
    "09_FAQ/00_Customer_FAQ.md",
    "09_FAQ/01_Rep_FAQ.md",
    "09_FAQ/02_Product_FAQ.md",
    "09_FAQ/03_Financing_FAQ.md",
    "09_FAQ/04_Warranty_FAQ.md",
    "09_FAQ/05_Hope_FAQ.md",
]


def parse_front_matter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        return {}, text
    end = text.find("\n---\n", 4)
    if end == -1:
        return {}, text
    raw = text[4:end]
    body = text[end + 5 :]
    meta: dict[str, str] = {}
    for line in raw.splitlines():
        if not line.strip() or ":" not in line:
            continue
        key, value = line.split(":", 1)
        meta[key.strip()] = value.strip().strip('"')
    return meta, body


def inline_md(text: str) -> str:
    escaped = html.escape(text)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"\*([^*]+)\*", r"<em>\1</em>", escaped)
    return escaped


def convert_table(lines: list[str]) -> tuple[str, int]:
    rows = []
    consumed = 0
    for line in lines:
        if not line.strip().startswith("|") or "|" not in line.strip()[1:]:
            break
        rows.append(line.strip())
        consumed += 1
    if len(rows) < 2:
        return "", 0
    header = [cell.strip() for cell in rows[0].strip("|").split("|")]
    body_rows = rows[2:]
    out = ["<table>", "<thead><tr>"]
    out.extend(f"<th>{inline_md(cell)}</th>" for cell in header)
    out.append("</tr></thead>")
    out.append("<tbody>")
    for row in body_rows:
        cells = [cell.strip() for cell in row.strip("|").split("|")]
        out.append("<tr>")
        out.extend(f"<td>{inline_md(cell)}</td>" for cell in cells)
        out.append("</tr>")
    out.append("</tbody></table>")
    return "\n".join(out), consumed


def markdown_to_html(md: str) -> str:
    lines = md.splitlines()
    out: list[str] = []
    i = 0
    in_ul = False
    in_ol = False
    in_blockquote = False

    def close_lists() -> None:
        nonlocal in_ul, in_ol
        if in_ul:
            out.append("</ul>")
            in_ul = False
        if in_ol:
            out.append("</ol>")
            in_ol = False

    def close_blockquote() -> None:
        nonlocal in_blockquote
        if in_blockquote:
            out.append("</blockquote>")
            in_blockquote = False

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()
        if not stripped:
            close_lists(); close_blockquote(); i += 1; continue
        if stripped.startswith("```"):
            close_lists(); close_blockquote(); code_lines = []; i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i]); i += 1
            if i < len(lines): i += 1
            out.append(f"<pre><code>{html.escape(chr(10).join(code_lines))}</code></pre>"); continue
        if stripped.startswith("|"):
            close_lists(); close_blockquote(); table_html, consumed = convert_table(lines[i:])
            if consumed:
                out.append(table_html); i += consumed; continue
        heading_match = re.match(r"^(#{1,4})\s+(.*)$", stripped)
        if heading_match:
            close_lists(); close_blockquote(); level = len(heading_match.group(1)); text = inline_md(heading_match.group(2))
            out.append(f"<h{level}>{text}</h{level}>"); i += 1; continue
        if stripped == "---":
            close_lists(); close_blockquote(); out.append("<hr>"); i += 1; continue
        if stripped.startswith(">"):
            close_lists()
            if not in_blockquote:
                out.append("<blockquote>"); in_blockquote = True
            quote = stripped.lstrip(">").strip()
            if quote: out.append(f"<p>{inline_md(quote)}</p>")
            i += 1; continue
        if re.match(r"^[-*]\s+", stripped):
            close_blockquote()
            if not in_ul:
                close_lists(); out.append("<ul>"); in_ul = True
            item = re.sub(r"^[-*]\s+", "", stripped); out.append(f"<li>{inline_md(item)}</li>"); i += 1; continue
        if re.match(r"^\d+\.\s+", stripped):
            close_blockquote()
            if not in_ol:
                close_lists(); out.append("<ol>"); in_ol = True
            item = re.sub(r"^\d+\.\s+", "", stripped); out.append(f"<li>{inline_md(item)}</li>"); i += 1; continue
        close_lists(); close_blockquote(); out.append(f"<p>{inline_md(stripped)}</p>"); i += 1
    close_lists(); close_blockquote()
    return "\n".join(out)


def render_html(meta: dict[str, str], body_html: str, source_path: str) -> str:
    title = meta.get("title") or Path(source_path).stem.replace("_", " ")
    keys = ["doc_id", "version", "owner", "last_updated", "priority_tier", "applies_to", "tags"]
    meta_tags = [f'  <meta name="{k}" content="{html.escape(meta.get(k, ""))}">' for k in keys]
    visible_meta = "\n".join(f"        <p><strong>{k.replace('_', ' ').title()}:</strong> {html.escape(meta.get(k, ''))}</p>" for k in keys)
    return f"""<!doctype html>
<html lang=\"en\">
<head>
  <meta charset=\"utf-8\">
  <title>{html.escape(title)}</title>
{chr(10).join(meta_tags)}
  <meta name=\"source_path\" content=\"{html.escape(source_path)}\">
</head>
<body>
  <article>
    <header>
      <h1>{html.escape(title)}</h1>
      <section class=\"metadata\">
{visible_meta}
        <p><strong>Source:</strong> {html.escape(source_path)}</p>
      </section>
    </header>
{body_html}
  </article>
</body>
</html>
"""


def main() -> None:
    OUT_ROOT.mkdir(parents=True, exist_ok=True)
    missing: list[str] = []
    converted = 0
    for rel in EXPORT_FILES:
        src = KB_ROOT / rel
        if not src.exists():
            missing.append(rel); continue
        text = src.read_text(encoding="utf-8")
        if "[VERIFY" in text:
            raise SystemExit(f"Blocked export: [VERIFY] placeholder found in {rel}")
        meta, body = parse_front_matter(text)
        body_html = markdown_to_html(body)
        out_path = OUT_ROOT / rel.replace(".md", ".html")
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(render_html(meta, body_html, rel), encoding="utf-8")
        converted += 1
    if missing:
        raise SystemExit("Missing export sources:\n" + "\n".join(missing))
    print(f"Converted {converted} Markdown files to HTML in {OUT_ROOT}")


if __name__ == "__main__":
    main()

---
name: consulting-proposal-designer
description: "Render approved proposal copy and commercial terms as a branded two-page HTML/PDF document. Use after proposal drafting and pricing, when the user needs the final visual artifact."
---

# Consulting Proposal Designer

Use the selected workspace and its `DESIGN.md`. Read the deal's approved copy, actual pricing,
scope, and agreement before rendering. `consulting-proposal-drafting` and
`consulting-pricing-builder` can prepare those inputs; this skill owns layout and rendering.

1. Read `assets/copy-and-design-frameworks.md` relative to this installed skill.
2. Copy `assets/proposal-template.html` into the deal's existing `02-proposals/` folder. Preserve the
   installed template; generated files and environments belong in the selected workspace.
3. Fill every slot, including `DOC_TITLE`, all `TIER_1_*` through `TIER_3_*` fields, steps, commercial
   terms, and brand fields. Escape text values. Use only reviewed markup in rich-content slots.
   All prices, service promises, and ownership claims require actual approval/source evidence.
4. Supply approved brand fonts through `BRAND_CSS` and `--brand-body-font`. The default system sans
   works without a font download. Font changes can affect pagination.
5. Prepare a Python environment outside the plugin. Install Playwright and its Chromium browser,
   or an available WeasyPrint environment. These are alternative renderers, not hidden dependencies:
   `python3 -m venv <workspace-env>`; use that environment's Python for `-m pip install playwright`
   and `-m playwright install chromium`. WeasyPrint is optional and needs its platform libraries.
6. Run the installed helper with absolute paths:
   `"<workspace-env>/bin/python" "<installed-skill>/assets/render.py" "<workspace>/.../proposal.html"`.
   `--check` validates slots without rendering. `--engine chromium|weasyprint|auto` selects the engine.
   `CHROMIUM_PATH` optionally names an existing browser executable.
7. Inspect both pages, verify prices/terms and text overflow, and retain the editable HTML alongside
   the PDF. Target two pages; the renderer does not certify page count or visual fit.
8. Prepare delivery according to the agreed process. Do not invent a deadline, require a video,
   or send the proposal without authorization.

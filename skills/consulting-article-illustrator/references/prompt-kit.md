# Prompt kit — hand-drawn whiteboard explainers

Every prompt = **STYLE BLOCK** (always identical, the locked look) + **ARCHETYPE BLOCK** (the layout,
filled with the concept's real labels). Generate with **gpt-image-2** (the `GenerateImage` tool
in-session, or Higgsfield `gpt-image-2`). Keep labels short (≤3–4 words) — gpt-image-2 garbles long text.

---

## STYLE BLOCK — paste verbatim into every prompt
> Hand-drawn whiteboard explainer infographic in a friendly doodle/marker style. Soft **LIGHT GREY
> background (#e9ebee)** — never white, never a gradient. All boxes, arrows, and hand-lettered labels in
> **BLACK marker**; the **only** accent color is a single **BLUE (#2a5bd0)**, used for highlighter
> swashes, underlines, numbered circles, checkmarks, and small accent ticks. Slightly wobbly hand-drawn
> rounded-rectangle boxes, hand-drawn arrows, simple line-doodle icons, clean legible hand-lettering,
> lots of whitespace, high craft, flat — no photorealism, no gradient, no drop shadows.

Then add **one** archetype block:

---

## FLOW / pipeline
> Layout: a left-to-right flow of [N] slightly-wobbly hand-drawn rounded boxes joined by hand-drawn
> arrows. Box 1 (solid): "[LABEL]" with a small [icon] doodle. Box 2 (dashed, with a BLUE highlighter
> swash behind the word): "[PIVOTAL LABEL]" with a small [icon] doodle. Box [N] (solid): "[LABEL]" with
> a small checkmark doodle. Hand-lettered title across the top with a BLUE underline: "[TITLE]". Small
> blue caption under the pivotal box: "[caption]".

## COMPARISON (X vs Y)
> Layout: a two-column comparison split by a thin vertical hand-drawn line. Left heading (BLUE underline):
> "[LEFT]"; under it [2–3] small doodle-icon boxes ([icons]); a BLUE highlighted caption pill at the
> bottom: "[verdict]". Right heading (BLUE underline): "[RIGHT]"; under it [2–3] small doodle-icon boxes
> ([icons] with tiny blue checkmarks); a BLUE highlighted caption pill at the bottom: "[verdict]".

## CYCLE / loop
> Layout: a circular loop of [4–6] slightly-wobbly hand-drawn rounded boxes joined by curved hand-drawn
> arrows clockwise, each with a small BLUE numbered circle and a tiny doodle icon: 1 "[L]" ([icon]),
> 2 "[L]" ([icon]), … A hand-lettered title in the center with a BLUE highlighter swash behind it:
> "[TITLE]". Balanced composition.

## STACK / layers
> Layout: [3–4] stacked hand-drawn rounded rows, a hand-drawn left brace spanning them labelled "[STACK
> NAME]". Each row: a doodle icon on the left, a BLUE-highlighted label + a short "→ [note]" on the
> right. Highlight the key row's label with a blue swash.

## HUB-AND-SPOKE
> Layout: a central hand-drawn circle "[CORE]" (with a [icon]/mascot), [3–4] satellite hand-drawn boxes
> around it on hand-drawn connector lines, each a doodle icon + short label: "[L]" ([icon]) … Optional
> hand-lettered title with BLUE underline at top: "[TITLE]".

## FRAMEWORK (inputs → N rows → output)
> Layout: left = a loose cluster of doodle "messy inputs" (sticky notes, notebook, docs) with a small
> label "[messy inputs]"; a hand-drawn arrow to center = [N] stacked hand-drawn rows, each with a BLUE
> numbered circle, a doodle icon, a bold "[NAME]" and a small sub-line "[detail]"; a hand-drawn arrow to
> right = a clean "output" doodle (checklist/sparkle) with a BLUE-highlighted "[OUTCOME]" and a short
> checklist. Hand-lettered title on top with BLUE underline: "[TITLE]".

---

## Higgsfield CLI route (alternative to the GenerateImage tool)
For tighter style-matching, generate via Higgsfield `gpt-image-2` with an uploaded **style-reference
image** (one of the `samples/`):
```bash
higgsfield auth login
higgsfield upload samples/flow.png        # → save the UUID as REF
higgsfield generate cost gpt-image-2 --prompt "..."   # check cost first
higgsfield generate create gpt-image-2 \
  --prompt "$STYLE  <archetype block, filled with real labels>" \
  --image $REF --wait
# output → integrations/higgsfield/_work/  → copy keepers into the article's images/ folder
```
`$STYLE` = the STYLE BLOCK above. The reference image anchors the hand-drawn look; the prompt drives
layout + labels. (Cap at ~6 elements per diagram — more than that garbles.)

## Tips
- **Short labels only.** 1–3 words per box. Put nuance in a tiny caption, not inside the box.
- **One pivotal element** gets the blue highlight — don't blue-wash everything.
- **Aspect:** in-article ~3:2 landscape; if it doubles as a post, also render 1:1 / 4:5.
- **If a label must be long or exact** (product names, numbers): shorten it, or split it into a short
  label + a tiny caption — gpt-image-2 garbles long strings.
- **Regenerate on:** white (not grey) background, garbled/misspelled text, a vector-clean (not
  hand-drawn) look, or more than one accent color.

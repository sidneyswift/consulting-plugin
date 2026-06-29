---
name: consulting-article-illustrator
description: Generate hand-drawn "whiteboard / excalidraw"-style explainer images for articles and posts — the doodle-marker diagrams that sit inside a pillar to explain a concept (a flow, a comparison, a loop, a stack, a hub-and-spoke, a numbered framework). Made with gen AI (gpt-image) in the brand palette: light-grey background, black marker line work + hand-lettering, a single blue accent (no yellow). Use when asked to "make an article image / diagram / explainer / infographic", a "hand-drawn / sketch / whiteboard / excalidraw" visual, or a concept diagram to drop into a blog post / LinkedIn article / pillar. NOT for clean HTML social graphics (use consulting-graphics) or anything animated (use consulting-hyperframes-video).
---

# Consulting Article Illustrator

Hand-drawn **whiteboard explainer diagrams** for articles — the friendly doodle-marker visuals that
make a concept legible inside a pillar post. Produced with **gen AI** (the reference look is itself
AI-generated, not literal Excalidraw), so this skill is a **prompt + style system**, not an HTML kit.

> **Lineage.** A first version of this skill (built on another machine) used `gpt-image-2` via the
> Higgsfield CLI but a **white background + yellow badges**. Sid rejected the yellow → this version
> locks the palette to **light grey / black marker / one blue** (below). It also absorbed the duplicate
> `consulting-article-images`. The parent pipeline (nightly-content density rules) refers to this skill
> by name — keep it `consulting-article-illustrator`.

- **This skill** = hand-drawn, doodle, marker — concept *explainers* inside articles.
- **`consulting-graphics`** = clean **HTML→PNG** social graphics (statement / stat / framework-blocks).
- **`consulting-hyperframes-video`** = anything animated/motion.

Style lineage + Sid's decoded preference: `swipe/article-image-referances/_index.md` (the references and
the palette correction that defines this skill).

## The locked look (Sid, 2026-06-29)
> "light grey background, black marker, and blue highlights." (Explicitly **not** the references' yellow.)

| Role | Value | Notes |
|---|---|---|
| Background | **light grey** `#e9ebee` | soft, flat — never pure white, never a gradient |
| Line work + lettering | **black marker** | wobbly hand-drawn boxes/arrows; legible hand-lettering |
| Accent / highlight | **one blue** (riso-blue, currently `#2a5bd0`) | highlighter swashes, underlines, numbered circles, checkmarks, accent ticks |
| Yellow | **never** | the single most important correction — no yellow anywhere |

Everything else is the doodle vocabulary: slightly-wobbly rounded-rectangle boxes, hand-drawn solid +
dashed arrows, simple line-doodle icons (brain, gears, laptop, clock, lightbulb, magnet, file, server…),
optional friendly mascot, lots of whitespace, flat — no photoreal, no gradients. Defer exact brand
tokens to the project **`DESIGN.md`**; this skill only fixes the *article-image* palette + style.

## Workflow
1. **Find the concept.** One idea per image — the thing the article's reader needs to *see* (a process,
   a contrast, a loop, a structure). Pull it from the draft/insight.
2. **Pick an archetype** that fits the idea (see table). One archetype = one layout.
3. **Write the prompt** = the **style block** + the **archetype block**, filled with the concept's real
   labels. Full templates in [references/prompt-kit.md](references/prompt-kit.md).
4. **Generate** — two routes, both `gpt-image`-class: **(a)** the **`GenerateImage` tool** (fastest,
   in-session); or **(b)** the **Higgsfield CLI** with an uploaded **style-reference image** for tighter
   control: `higgsfield generate create gpt-image-2 --prompt "$STYLE …" --image $REF --wait` (output →
   `integrations/higgsfield/_work/`). Landscape (~3:2) for in-article; 1:1 or 4:5 if it's also a post.
5. **Run the bar** (below). Regenerate if it fails — especially **any yellow**, garbled text, or a white
   (not grey) background. Text fidelity is gen-AI's weak spot → keep every label **short (≤3–4 words)**.
6. **Save into the piece's bundle:** `content/03-drafts/<YYYY-MM-DD-slug>/images/<concept>.png` (the
   article's own folder — see `content/AGENTS.md`). Scratch/tests → `content/_work/article-images/`.

## Layout archetypes
| Archetype | Use for | Shape |
|---|---|---|
| **Flow / pipeline** | a process, before→after, a path | 2–4 boxes left→right joined by arrows; dash + blue-highlight the pivotal box |
| **Comparison** | X vs Y, old vs new, tool vs system | vertical split; two headings (blue underline); blue-highlight pill verdict under each |
| **Cycle / loop** | a compounding/repeating system | 4–6 boxes in a ring, curved arrows, blue numbered circles |
| **Stack / layers** | a layered architecture | stacked rows + a left brace label; blue-highlight the key layer |
| **Hub-and-spoke** | one core + its parts | center node + satellite boxes on connectors |
| **Framework** | a named N-part model, inputs→output | numbered rows (blue circles) between a "messy inputs" cluster and a clean "output" |

## The bar — check every render before showing
- [ ] **Light-grey** background (not white), flat?
- [ ] **Black marker** line work + legible hand-lettering (labels spelled correctly)?
- [ ] **Blue** the *only* accent — and **zero yellow**?
- [ ] Hand-drawn doodle feel (wobbly boxes, doodle icons), not a clean vector/HTML chart?
- [ ] One clear idea, lots of whitespace, reads at article width?
- [ ] On-brand vibe vs the references (`swipe/article-image-referances/`) and `samples/`?

Fail any box → don't ship it; fix the prompt and regenerate.

## Samples (locked exemplars)
`samples/` holds three approved renders — one per core archetype — to match against:
`flow.png`, `compare.png`, `cycle.png`.

> **Taste authority:** `consulting-tasteful-design` + `DESIGN.md` govern brand look across every medium;
> this skill is their hand-drawn-explainer implementation. Keep it bold and friendly, never yellow.

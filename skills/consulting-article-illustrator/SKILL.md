---
name: consulting-article-illustrator
description: Generate hand-drawn "whiteboard / excalidraw"-style explainer images for articles and posts — the doodle-marker diagrams that sit inside a pillar to explain a concept (a flow, a comparison, a loop, a stack, a hub-and-spoke, a numbered framework). Made with gpt-image-2 in the brand palette: light-grey background, black marker line work + hand-lettering, a single blue accent. Plans a figure set — a hero thumbnail at the top (above the first line; doubles as the social/OG preview) plus ~1 diagram per section — and embeds them inline. Use when asked to "make an article image / diagram / explainer / infographic / hero / thumbnail", a "hand-drawn / sketch / whiteboard" visual, or to illustrate a blog post / LinkedIn article / pillar. NOT for clean HTML social graphics (use consulting-graphics) or anything animated (use consulting-hyperframes-video).
---

# Consulting Article Illustrator

Hand-drawn **whiteboard explainer diagrams** for articles — the friendly doodle-marker visuals that make
a concept legible inside a pillar post. Made with **gpt-image-2**, so this is a **prompt + style system**.

- **This skill** = hand-drawn, doodle, marker — concept *explainers* inside articles.
- **`consulting-graphics`** = clean HTML→PNG social graphics (statement / stat / framework-blocks).
- **`consulting-hyperframes-video`** = anything animated/motion.

## The look
| Role | Value | Notes |
|---|---|---|
| Background | **light grey** `#e9ebee` | soft, flat — not pure white, no gradient |
| Line work + lettering | **black marker** | wobbly hand-drawn boxes/arrows; legible hand-lettering |
| Accent | **one blue** `#2a5bd0` | highlighter swashes, underlines, numbered circles, checkmarks, ticks |

Doodle vocabulary: slightly-wobbly rounded-rectangle boxes, hand-drawn solid + dashed arrows, simple
line-doodle icons (brain, gears, laptop, clock, lightbulb, magnet, file, server…), an optional friendly
mascot, lots of whitespace, flat — no photoreal, no gradients. Match the bundled `samples/`. Defer brand
tokens to the project **`DESIGN.md`**.

## Density & placement
- **Open with a hero.** Every article gets a **hero thumbnail** — the title concept as **one bold metaphor (a cover, not a diagram)** — at the **very top, above the first line**. Save it as the bundle `thumbnail.png` (the pillar convention); it doubles as the social/OG preview.
- **Then ~1 diagram per major section/concept.** A 4-section pillar → a hero + ~4 section figures. Cap section figures at **~4–6**.
- **Place each section figure at its break**, right after that section's point lands.
- **Lead with the strongest archetype** (a comparison or a flow usually reads fastest).

## Workflow
1. **Plan the figure set.** Read the draft; list its major sections; per **Density & placement** pick a
   **hero** (the title concept, for the top) plus the concept + archetype for each section. One idea per figure.
2. **Write the prompt** = the **style block** + the **archetype block**, filled with the concept's real
   labels (templates: [references/prompt-kit.md](references/prompt-kit.md)). Keep labels short (≤3–4 words)
   — gpt-image-2 garbles long text.
3. **Generate with gpt-image-2.** *Attended / local:* the `GenerateImage` tool in-session, or the
   Higgsfield CLI (`gpt-image-2 --image $REF`, a `samples/` image as the style reference). *Unattended /
   cloud pipeline:* the **Higgsfield MCP** connector with model **`gpt-image-2`** (the CLI's browser auth
   can't run there) — don't substitute another model. Landscape ~3:2 in-article; 1:1 or 4:5 if it also
   runs as a post.
4. **Run the bar** (below); regenerate on any miss.
5. **Save + embed.** Write each to the piece's own bundle `…/images/<concept>.png` (see `content/AGENTS.md`).
   Embed the **hero at the very top, above the first line** (the bundle `thumbnail.png`); embed each section
   figure at its break: `![alt](images/<concept>.png)`. Scratch/tests → `content/_work/article-images/`.

## Layout archetypes
| Archetype | Use for | Shape |
|---|---|---|
| **Hero / title card** | the lead image (top of the article) + social thumbnail | a COVER, not a diagram: ONE central doodle (the core metaphor) + the hand-lettered TITLE with a blue underline, nothing else — no steps, lists, panels, or flow arrows. Wide 16:9, poster-like, mostly empty space |
| **Flow / pipeline** | a process, before→after, a path | 2–4 boxes left→right joined by arrows; dash + blue-highlight the pivotal box |
| **Comparison** | X vs Y, old vs new, tool vs system | vertical split; two headings (blue underline); blue-highlight pill verdict under each |
| **Cycle / loop** | a compounding/repeating system | 4–6 boxes in a ring, curved arrows, blue numbered circles |
| **Stack / layers** | a layered architecture | stacked rows + a left brace label; blue-highlight the key layer |
| **Hub-and-spoke** | one core + its parts | center node + satellite boxes on connectors |
| **Framework** | a named N-part model, inputs→output | numbered rows (blue circles) between a "messy inputs" cluster and a clean "output" |

## The bar — check every render before showing
- [ ] **Light-grey** background, flat?
- [ ] **Black marker** line work + legible hand-lettering (labels spelled correctly)?
- [ ] **Blue** the only accent?
- [ ] Hand-drawn doodle feel (wobbly boxes, doodle icons), not a clean vector chart?
- [ ] One clear idea, lots of whitespace, reads at article width?
- [ ] Matches the bundled `samples/`?

Fail any box → don't ship it; fix the prompt and regenerate.

## Samples
`samples/` holds approved exemplars to match: `flow.png`, `compare.png`, `cycle.png`.

## Nightly pipeline hook
`consulting-nightly-content` can **auto-illustrate** a staged pillar: generate every image via the
**Higgsfield MCP** connector with model **`gpt-image-2`** (never the in-session `GenerateImage` tool or a
fallback model), apply **Density & placement**, save into the draft's `images/` (+ `thumbnail.png`), embed
inline, and leave it staged for review (never auto-publish). If the MCP or `gpt-image-2` is unavailable,
stage without figures and flag — don't swap models.

> **Taste authority:** `consulting-tasteful-design` + `DESIGN.md` govern brand look across every medium;
> this is their hand-drawn-explainer implementation.

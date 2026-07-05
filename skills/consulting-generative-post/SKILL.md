---
name: consulting-generative-post
description: Produce a finished, post-ready branded VISUAL by compositing a Higgsfield-generated background (photoreal / cinematic / illustrative imagery) with an on-brand HTML text overlay. This is "the power move." Use on "make a post image / hero image / banner / OG card with a real/cinematic/AI background and a headline", "put a headline on a generated image", "branded visual over a photo/AI background", or whenever a social asset needs BOTH generative imagery AND clean, on-brand type. Orchestrates consulting-higgsfield (the background) + consulting-graphics (the overlay) and defers aesthetics to consulting-tasteful-design. NOT for a pure typographic graphic on a solid/gradient field (no generated photo) → consulting-graphics; NOT for raw generation with no text overlay → consulting-higgsfield.
---

# Consulting Generative Post

The power move: **generate imagery neither HTML nor a stock library can give you (Higgsfield), then
lay pixel-perfect on-brand type over it (consulting-graphics).** Each tool does the half it's best at —
AI makes the photoreal/cinematic field; HTML makes legible, on-brand text. Neither alone produces this.

> **This skill locks the WORKFLOW; the DESIGN is a living layer.** The steps below are stable. The
> *visual treatment* — scrim recipe, type placement, which template, composition — is intentionally
> kept malleable: it lives in `references/overlay-shell.html` and defers to `consulting-tasteful-design`
> (`DESIGN.md`). Iterate the look there without touching the process here.

## Prerequisites
- `consulting-higgsfield` usable (CLI authed — `higgsfield account status` shows credits).
- `consulting-graphics` rendering path available (`npx playwright screenshot`).
- Brand canon: `DESIGN.md` (via `consulting-tasteful-design`); voice via `consulting-copy-writer`.

## Workflow (stable)

1. **Pick the canvas.** Default LinkedIn feed **1080×1350 (4:5)**; use 1:1, 9:16, or 1.91:1 (OG) per the
   destination. Sizes/safe-zones → `consulting-graphics` (`references/dimensions.md`).
2. **Generate the background** with `consulting-higgsfield`. Encode the brand *mood/palette* from
   `DESIGN.md` into the prompt; **reserve negative space** where the headline will sit (e.g. "generous
   empty space, upper-left"); demand **no text/words** in the image. Preview cost, generate, and land the
   raw file in `integrations/higgsfield/_work/`.
3. **Inspect the actual result — don't trust the prompt.** Open the generated image and find the real
   darkest / emptiest region; AI rarely honors "negative space on the left" exactly. *That* region is
   where the text goes, and the focal element (a streak, a subject) is what the text must not collide with.
4. **Compose the overlay** with `consulting-graphics`. Start from `references/overlay-shell.html` (or a
   `consulting-graphics` template like `statement`): swap the template's CSS color field for the generated
   image (`background-size:cover`) and add a **directional legibility scrim** darkening only the text side
   (keep the focal element visible). Brand tokens from `DESIGN.md`; **never bake text into the AI image** —
   that's the whole point of overlaying it here.
5. **Render + review.** `npx playwright screenshot --viewport-size="W,H" "file:///…/overlay.html" "…/out.png"`.
   Then **look at the PNG**: does the headline read at thumbnail scale, clear of the focal element, footer
   present, one signal accent? Iterate the overlay (not the workflow) until clean.
6. **Promote + hand off.** Move the keeper into `content/` (raw stays gitignored in `_work/`). For LinkedIn,
   pass the final asset + caption to `consulting-linkedin-publisher` — **drafts only, never auto-send.**

## The overlay technique (what's new vs. consulting-graphics)

`consulting-graphics` templates sit on a CSS color field; here the field is a **photo + scrim**:

- **`background-size:cover; background-position:center`** fits a square generation into a 4:5 / 9:16 canvas.
- **Scrim** = layered gradients that darken only the headline side (and the footer strip) so white type
  reads, while leaving the generated focal element bright. The current recipe lives in the shell file.
- Reuse a `consulting-graphics` template's *type treatment* (e.g. `statement`: Space Grotesk hook + one
  `Instrument Serif` italic signal accent); only the field changes.

## Cost discipline (inherits consulting-higgsfield)
Preview every generation (`higgsfield generate cost …`) and **cite the actual credits** after. The overlay
render is free (local Playwright). Gate video/Soul backgrounds behind explicit go-ahead.

## Don't
- Don't bake headline/marketing **text into the AI image** — overlay it.
- Don't **commit raw media** — `_work/` is gitignored; promote only keepers to `content/`.
- Don't **invent Higgsfield model names** — `higgsfield model list` is the source of truth.
- Don't **auto-publish** — confirm the final creative + caption first.

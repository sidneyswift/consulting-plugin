---
name: consulting-tasteful-design
description: >
  The house authority on visual TASTE — the look-and-feel north star every skill defers to when
  making something seen: a video or motion graphic, a social graphic or carousel, a slide/pitch
  deck, a proposal, a landing page, the metrics dashboard, an email header — any rendered artifact.
  Use whenever the goal is "make it look good / on-brand / bold / not AI slop", or when choosing
  palette, type, layout, or motion. It does NOT redefine the brand tokens — those are canonical in
  the project's root /DESIGN.md; this skill carries
  the cross-medium PRINCIPLES (the "bold, not boring" stance), the anti-AI-slop checklist, and the
  rules for translating the brand into MOTION/video that the still-graphics kit doesn't cover.
metadata: { "tags": "design, taste, brand, visual, motion, look-and-feel, anti-slop, house-authority" }
---

# Consulting Tasteful Design — the look-and-feel north star

The **shared visual-taste authority** for the practice. Other skills make the artifact; this skill
decides whether it looks like us and whether it looks *good*. `consulting-graphics` (stills),
`consulting-hyperframes-video` (motion), `consulting-proposal-designer`, and the dashboard all
**defer here** for principles, and to the brand canon below for exact tokens.

It's the visual counterpart to our writing voice — same DNA (**specificity, conviction,
say-it-out-loud, no hype**), translated from sentences to pixels. The stance is **bold, not boring.**

## Canon — read these, never invent brand facts

1. **The project's root `/DESIGN.md`** — the **brand source of truth**: the exact
   palette (`--ink` / `--navy` / `--accent` / `--signal` / `--tint` …), the type roles, and the
   standard footer signature (Recoup mark · Sidney Swift · recoupable.com), plus the "bold, not
   boring" principles. **Pull exact colors, fonts, the logo, and the footer from here — don't restate
   or guess them.** For stills it also owns the template set (`framework-blocks`, `statement`, `stat`,
   `editorial`). For anything it doesn't cover (e.g. audience) — or if the project has no `DESIGN.md` at all (e.g. this plugin installed in another repo) — ask the user for brand values, or scaffold one; never invent.
2. **`consulting-copywriting/references/voice-principles.md`** — governs every word that appears
   (headlines, captions, labels, CTAs).

**Brand character at a glance** (exact values live in `DESIGN.md`): deep **ink/navy color
fields** with **one electric "signal" blue** as the energy accent; **Space Grotesk** for display,
**Plus Jakarta Sans** for body, **Instrument Serif italic** for the occasional editorial moment;
every piece closes with the **Recoup mark + "Sidney Swift" · recoupable.com** footer.

## Principles — bold, not boring

These match `DESIGN.md` and extend across every medium. (They deliberately retire the old
"no color / 40% empty / decoration is a sin" rules — those made work forgettable.)

1. **Commit to a color field.** Each artifact has a dominant field — full-bleed dark (`--ink`/`--navy`,
   high-conviction) or crisp light (`--paper`/`--tint`, scannable). **Pale, washed-out gradients are
   banned** — they read as generic. Go all the way dark, or keep it crisp-light.
2. **One thing is huge.** A hook, a number, or a framework — legible as a thumbnail. Display type
   runs big; the focal element dwarfs everything else.
3. **Color carries meaning.** `--accent` for structure (rules, labels, numbers); `--signal` for *one*
   energy pop per piece — the word/number you want the eye to hit. Never rainbow it.
4. **Make it saveable.** Real numbers, named frameworks, worked examples with receipts. Build things
   people screenshot and re-share — the specificity *is* the design (mirrors "specificity as proof").
5. **Vary expression across a series.** Same DNA, different composition. If two pieces look
   interchangeable, the brief failed — vary the field, layout, and dominant element.
6. **Texture is allowed; clutter isn't.** A dotwave motif or a single signal glow adds depth.
   Decoration that carries no meaning still gets cut — but "interesting" is a goal, not a sin.
7. **Mobile-first.** If the hook doesn't land at phone-thumbnail scale, it fails. Test small.

## Translating it to motion & video

What `DESIGN.md` doesn't cover — how the brand moves. `consulting-hyperframes-video` reads
this section.

- **The color field is the scene.** Commit each scene to a dark or light field; carry it through.
  One saturated `--signal` glow for depth is on-brand — a *washed-out* gradient with nothing to say
  is the slop tell. Don't confuse the two.
- **One thing huge per beat.** A scene shows one idea — a hook line, a count-up number, a framework
  reveal. Don't crowd a frame; let beats sequence the story.
- **Signal accent is the motion focal.** A line wipe, a highlighted word, a number ticking up — *one*
  energy moment per scene, not everything moving. Motion directs the eye to the signal.
- **Type in motion.** Space Grotesk display animates in with intent — **ease, stagger, one timeline;
  never bounce-everything or spin for its own sake.** (Mechanics: `consulting-hyperframes-video/
  engine/hyperframes-animation`.)
- **Close on the signature.** End on the footer lockup (Recoup mark + Sidney Swift · recoupable.com)
  as the endcard, adapted to the field's light/dark.
- **Deterministic + validated.** Respect the render rules (`npx hyperframes lint && validate`).

## The anti-AI-slop checklist (the tells to avoid)

- [ ] A **pale, washed-out** purple→blue gradient hero with a generic glowing orb and no focal point.
      (Our look commits to a saturated field + **one** signal glow behind a huge focal element — not this.)
- [ ] Glassmorphism / frosted cards stacked everywhere.
- [ ] Emoji as bullets; emoji in headlines.
- [ ] 4+ font families, or default system-font soup (we use Space Grotesk + Plus Jakarta + Instrument Serif).
- [ ] Rainbow / 6-color palettes with no `--accent` vs `--signal` discipline.
- [ ] Fake/placeholder numbers, lorem ipsum, generic "synergy" stock imagery.
- [ ] Every element the same visual weight — no clear hook, no "one thing huge".
- [ ] Motion: everything sliding/spinning/zooming at once.
- [ ] A series where every piece looks interchangeable (sameness).

Hit any? Fix before shipping.

## Pre-ship checklist (run on every visual)

1. **Tokens pulled from `DESIGN.md`** — palette, type, logo, footer not invented.
2. **Committed color field** (fully dark or crisp light); no pale gradient.
3. **One huge focal element**; hierarchy obvious in a 1-second glance.
4. **`--accent` for structure, one `--signal` pop**; AA contrast on text.
5. **Real content / real numbers**; copy passes `voice-principles.md` (no hype, say-it-out-loud).
6. **Footer signature present**; reads at phone scale.
7. Within a series, **this piece looks distinct** from its siblings.
8. **Motion** (if any) serves meaning, one timeline, closes on the signature.

## How a skill should use this

Read this skill → pull exact tokens from `DESIGN.md` → pick a
composition that fits the *content* (a graphics template, or a HyperFrames frame-preset curated to
brand) → design to the bold-not-boring principles → run the pre-ship checklist before calling it
done. Keep the DNA consistent across a set, vary the expression within it.

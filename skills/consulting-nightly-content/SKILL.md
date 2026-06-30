---
name: consulting-nightly-content
description: Phase 3 of the nightly pipeline — the content engine. After capture + janitor, pick a topic from the day's new insights and produce a pillar ARTICLE, a LinkedIn post derived from it, and an on-brand thumbnail — all staged for review, never published. Uses consulting-copywriting for prose and consulting-article-illustrator for the hero thumbnail + inline diagrams. Article-first: one pillar -> many platform posts. Use on "run the nightly content", "draft today's article", or as the nightly content ritual.
---

# Consulting Nightly Content (article-first flywheel engine)

Capture turns calls into insights; this turns the day's strongest insight into a **pillar article**, then
derives a **LinkedIn post** from it and an **on-brand thumbnail**. Article-first, because one good article
becomes many platform posts later (LinkedIn, X, newsletter) — write the pillar once, atomize forever.

The engine drafts; **Sid publishes.** Quality over cadence.

## Output — one pillar bundle (slug folder) in drafts/
```
content/03-drafts/<YYYY-MM-DD>-<topic-slug>/
  <article-slug>.md    the pillar article (hero + figures embedded inline)
  linkedinpost.md      the LinkedIn post derived from / promoting the article
  thumbnail.png        the hand-drawn hero (also the social/OG preview)
  images/              the inline section figures (~1 per section)
```
(A pillar is the *folder* shape of a draft; a one-off post/graphic is a single file in `content/03-drafts/`.
See `content/AGENTS.md`.)

## Rails
1. **Never auto-publish.** Drafts only; Sid reviews + publishes via `consulting-linkedin-publisher` (Postbridge).
2. **Grounded, not fabricated.** Every claim traces to a real captured insight/transcript — carry the
   citation. Never invent a client name, number, or result; confirm before naming a client, or write generically.
3. **Voice = `consulting-copywriting`** (no exceptions): no em-dashes, anti-slop list, specific, human. Read it.
4. **Quality over volume.** One strong article a night (occasionally a second). A thin day → one-line report, no article.

## Steps
0. **Orient + find what's new.** Read the day's `business/ops/nightly-digests/<date>.md`. Gather insights
   newer than `content/_work/LAST_DRAFTED` (`knowledge/insights/`, `content/02-ideas/`). `git log` for today.

1. **Pick ONE topic** — the strongest, most specific fresh insight with a real story / POV from an actual
   call. Dedup vs `content/04-published/` and existing `content/03-drafts/` (never rewrite a published pillar).
   Slugify the topic and make the bundle folder `content/03-drafts/<YYYY-MM-DD>-<topic-slug>/` (date-first, so `drafts/` sorts chronologically).

2. **Write the ARTICLE** (the pillar). Read **`consulting-copywriting`** first (voice-principles, anti-slop,
   formats §blog/articles, and long-form-essay architecture for 1,000+ words). Lead with the counterintuitive,
   concrete before abstract, grounded + cited. Aim 800–1,400 words. Save as `<article-slug>.md` with
   frontmatter: `title`, `source` (insight/transcript path), `audience`, `status: draft`.

3. **Derive the LinkedIn POST from the article.** Read `consulting-copywriting` §social. A standalone hook
   that teases/promotes the article (don't just paste the intro). Save as `linkedinpost.md` (frontmatter:
   `source` = the article path, `hook`, `status: draft`).

4. **Illustrate the article.** Read **`consulting-article-illustrator`** (the house article-image skill;
   brand taste via **`consulting-tasteful-design`** / `DESIGN.md`). Per its density rule, produce the
   **hero thumbnail** — saved as the bundle `thumbnail.png` and embedded above the first line — **plus
   ~1 inline figure per major section**, saved in `images/` and embedded at each section break (pick the
   archetype that fits each concept). Hand-drawn whiteboard palette; generate with **gpt-image-2** (this
   run is a cloud worker with the Higgsfield connector → use the illustrator's Higgsfield `gpt-image-2`
   route). Run the illustrator's bar on each image. If image generation isn't available, stage the
   article without figures and flag it in the report — don't block the article.

5. **Report + score + commit.** Write `business/ops/content-reports/<date>.md` (**Article · Post · Hero + figures ·
   Skipped (why) · Needs Sid**), run `python evals/content/score_run.py` (composite + flags at top), commit
   each draft why-first, stamp `content/_work/LAST_DRAFTED`, then stop.

## Notes
- **Article-first is the leverage.** The pillar gets atomized later into X threads, a newsletter, more LinkedIn
  angles. Spend the effort on the pillar.
- **Mine, don't manufacture.** Nothing worth a pillar → say nothing. The flywheel rewards signal, not cadence.
- Scored by `evals/content/score_run.py`: completeness (article + post + thumbnail), grounding, voice, non-dup.

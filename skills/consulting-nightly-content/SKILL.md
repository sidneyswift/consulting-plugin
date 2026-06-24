---
name: consulting-nightly-content
description: Phase 3 of the nightly pipeline — the content engine. After capture + janitor, pick a topic from the day's new insights and produce a pillar ARTICLE, a LinkedIn post derived from it, and an on-brand thumbnail — all staged for review, never published. Uses consulting-copywriting for prose and consulting-graphics for the image. Article-first: one pillar -> many platform posts. Use on "run the nightly content", "draft today's article", or as the nightly content ritual.
---

# Consulting Nightly Content (article-first flywheel engine)

Capture turns calls into insights; this turns the day's strongest insight into a **pillar article**, then
derives a **LinkedIn post** from it and an **on-brand thumbnail**. Article-first, because one good article
becomes many platform posts later (LinkedIn, X, newsletter) — write the pillar once, atomize forever.

The engine drafts; **Sid publishes.** Quality over cadence.

## Output — one pillar bundle (slug folder) in drafts/
```
content/03-drafts/<YYYY-MM-DD>-<topic-slug>/
  <article-slug>.md    the pillar article
  linkedinpost.md      the LinkedIn post derived from / promoting the article
  thumbnail.png        the on-brand graphic
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

4. **Make the THUMBNAIL.** Read **`consulting-graphics`** (+ the taste north star **`consulting-tasteful-design`**, whose
   `DESIGN.md` holds the brand tokens). Pick the template that fits the piece — `statement` for a
   hook/POV, `framework-blocks` for a teaching breakdown, `stat` for a proof number, `editorial` for a
   restrained one — and **vary it run to run** so the feed isn't samey (bold is the default, not the pale
   editorial look). Compose from the brand tokens in `DESIGN.md` and render via Playwright
   (`npx playwright screenshot --viewport-size="W,H" file.html thumbnail.png`). Save `thumbnail.png` (keep the
   `.html` alongside). If graphics config isn't set up, save the HTML and flag the PNG step — don't block the article.

5. **Report + score + commit.** Write `business/ops/content-reports/<date>.md` (**Article · Post · Thumbnail ·
   Skipped (why) · Needs Sid**), run `python evals/content/score_run.py` (composite + flags at top), commit
   each draft why-first, stamp `content/_work/LAST_DRAFTED`, then stop.

## Notes
- **Article-first is the leverage.** The pillar gets atomized later into X threads, a newsletter, more LinkedIn
  angles. Spend the effort on the pillar.
- **Mine, don't manufacture.** Nothing worth a pillar → say nothing. The flywheel rewards signal, not cadence.
- Scored by `evals/content/score_run.py`: completeness (article + post + thumbnail), grounding, voice, non-dup.

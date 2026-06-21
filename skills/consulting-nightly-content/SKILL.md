---
name: consulting-nightly-content
description: Phase 3 of the nightly pipeline — the content engine. After capture + janitor, pick a topic from the day's new insights and produce a pillar ARTICLE, a LinkedIn post derived from it, and an on-brand thumbnail — all staged for review, never published. Uses consulting-copywriting for prose and consulting-graphics for the image. Article-first: one pillar -> many platform posts. Use on "run the nightly content", "draft today's article", or as the nightly content ritual.
---

# Consulting Nightly Content (article-first flywheel engine)

Capture turns calls into insights; this turns the day's strongest insight into a **pillar article**, then
derives a **LinkedIn post** from it and an **on-brand thumbnail**. Article-first, because one good article
becomes many platform posts later (LinkedIn, X, newsletter) — write the pillar once, atomize forever.

The engine drafts; **Sid publishes.** Quality over cadence.

## Output — one folder per article
```
content/articles/drafts/<topic-slug>-<YYYY-MM-DD>/
  <article-slug>.md    the pillar article
  linkedinpost.md      the LinkedIn post derived from / promoting the article
  thumbnail.png        the on-brand graphic
```

## Rails
1. **Never auto-publish.** Drafts only; Sid reviews + publishes via `consulting-linkedin-publisher` (Postbridge).
2. **Grounded, not fabricated.** Every claim traces to a real captured insight/transcript — carry the
   citation. Never invent a client name, number, or result; confirm before naming a client, or write generically.
3. **Voice = `consulting-copywriting`** (no exceptions): no em-dashes, anti-slop list, specific, human. Read it.
4. **Quality over volume.** One strong article a night (occasionally a second). A thin day → one-line report, no article.

## Steps
0. **Orient + find what's new.** Read the day's `business/ops/nightly-digests/<date>.md`. Gather insights
   newer than `content/_work/LAST_DRAFTED` (`knowledge/insights/`, `content/ideas/`). `git log` for today.

1. **Pick ONE topic** — the strongest, most specific fresh insight with a real story / POV from an actual
   call. Dedup vs `content/published/` and `content/articles/` (never rewrite a published pillar). Slugify
   the topic and make the folder `content/articles/drafts/<topic-slug>-<YYYY-MM-DD>/`.

2. **Write the ARTICLE** (the pillar). Read **`consulting-copywriting`** first (voice-principles, anti-slop,
   formats §blog/articles, and long-form-essay architecture for 1,000+ words). Lead with the counterintuitive,
   concrete before abstract, grounded + cited. Aim 800–1,400 words. Save as `<article-slug>.md` with
   frontmatter: `title`, `source` (insight/transcript path), `audience`, `status: draft`.

3. **Derive the LinkedIn POST from the article.** Read `consulting-copywriting` §social. A standalone hook
   that teases/promotes the article (don't just paste the intro). Save as `linkedinpost.md` (frontmatter:
   `source` = the article path, `hook`, `status: draft`).

4. **Make the THUMBNAIL.** Read **`consulting-graphics`** — pick the thumbnail/landscape format + the brand
   template (`elegant-founder`), compose the HTML from identity (`~/.config/sid/identity.md`), and render via
   Playwright (`npx playwright screenshot --viewport-size="W,H" file.html thumbnail.png`). Save `thumbnail.png`
   in the folder (keep the `.html` alongside). If the graphics config isn't set up, save the thumbnail HTML and
   flag the PNG step in the report — don't block the article on it.

5. **Report + score + commit.** Write `business/ops/content-reports/<date>.md` (**Article · Post · Thumbnail ·
   Skipped (why) · Needs Sid**), run `python evals/content/score_run.py` (composite + flags at top), commit
   each draft why-first, stamp `content/_work/LAST_DRAFTED`, then stop.

## Notes
- **Article-first is the leverage.** The pillar gets atomized later into X threads, a newsletter, more LinkedIn
  angles. Spend the effort on the pillar.
- **Mine, don't manufacture.** Nothing worth a pillar → say nothing. The flywheel rewards signal, not cadence.
- Scored by `evals/content/score_run.py`: completeness (article + post + thumbnail), grounding, voice, non-dup.

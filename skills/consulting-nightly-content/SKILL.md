---
name: consulting-nightly-content
description: Phase 3 of the nightly pipeline — the demand engine's insight lane (Engine A, article-first). After capture + janitor, pick a signal from the day's reservoir and produce a copy-edited pillar ARTICLE, a copy-edited LinkedIn post derived from it, and an on-brand image set — staged as one role-named idea bundle (article.md + linkedin.md + meta.yml + images/) for review, never published. Uses consulting-copywriting for prose, consulting-copy-reviewer (the customer's eyes) then consulting-copy-editor on the article, and consulting-article-illustrator for the hero image + inline diagrams. Article-first: one pillar -> many platform posts. Use on "run the nightly content", "draft today's article", or as the nightly content ritual.
---

# Consulting Nightly Content (article-first flywheel engine)

Capture turns calls into insights; this turns the day's strongest insight into a **pillar article**, runs it
past the customer's eyes and the editor's, derives and edits a **LinkedIn post**, then makes an **on-brand image set (hero + figures)**. Article-first,
because one good article becomes many platform posts later (LinkedIn, X, newsletter) — write the pillar
once, atomize forever.

The engine drafts; **Sid publishes.** Quality over cadence.

## Output — one idea bundle (slug folder) in drafts/
```
content/03-drafts/<YYYY-MM-DD>-<topic-slug>/    ← the idea is the unit (date + slug = identity)
  meta.yml         the bundle manifest / approval state machine (source + per-format status)
  article.md       the pillar article (hero + figures embedded inline)
  linkedin.md      the LinkedIn post derived from / promoting the article
  images/          image1.png = hero (also the social/OG preview), then image2.png… (~1 per section)
```
Children are **role-named** (`article.md`, `linkedin.md`; later `x.md` / `email.md` as the idea warrants) —
the folder carries the title, so every bundle is structurally identical and the approval queue is uniform.
(A pillar is the *folder* shape of a draft; a one-off post/graphic is a single file in `content/03-drafts/`.
See `content/AGENTS.md`.)

## Rails
1. **Never auto-publish.** Drafts only; Sid reviews + publishes via `consulting-linkedin-publisher` (Postbridge).
2. **Grounded, not fabricated.** Every claim traces to a real captured insight/transcript — carry the
   citation. Never invent a client name, number, or result; confirm before naming a client, or write generically.
3. **Voice = `consulting-copywriting`** (no exceptions): no em-dashes, anti-slop list, specific, human. Read it.
4. **Two gates on the article: reader, then editor.** Run `consulting-copy-reviewer` (the customer's eyes) and rewrite from its notes, *then* `consulting-copy-editor`, before deriving the post; edit the post before illustration + scoring.
5. **Quality over volume.** One strong article a night (occasionally a second). A thin day → one-line report, no article.

## Steps
0. **Orient + find what's new.** Read the day's `business/ops/nightly-digests/<date>.md`. Gather unused
   **signals** — the **dated `signals/<YYYY-MM-DD>-*.md` files** with `status: new` (plus `evergreen` POVs
   not yet drafted into a published pillar); skip `used`/`archived` **and the meta files** (`AGENTS.md`,
   `_template.md`, `_index.md`, `_archive/` are NOT signals). (`content/_work/LAST_DRAFTED` is just a
   run-log now; per-signal `status` is the truth.) `git log` for today.

1. **Pick ONE signal** — the strongest, most specific unused signal (`status: new`, or an `evergreen` POV
   not yet published) with a real story / POV from an actual source. Dedup vs `content/04-published/` and
   existing `content/03-drafts/` (never rewrite a published pillar). Carry its `source` so the draft stays
   grounded. Slugify the topic and make the bundle folder `content/03-drafts/<YYYY-MM-DD>-<topic-slug>/`
   (date-first, so `drafts/` sorts chronologically).

2. **Write the ARTICLE** (the pillar). Read **`consulting-copywriting`** first: voice-principles,
   anti-slop, formats §blog/articles, and **`references/social-article-style.md`**. Use the social-article
   structure by default: thesis first, purpose sentence, thought experiment, fair comparison, pragmatic
   verdict. Aim 800–1,400 words. Save as `article.md` with frontmatter: `title`, `source`
   (insight/transcript path), `audience`, `status: draft`.

3. **Reader review (customer POV) + rewrite.** Read **`consulting-copy-reviewer`** and run it on
   `article.md`: a fresh-context subagent role-plays Sid's ICP customer and returns reader-reaction
   notes (unclear jargon, where they tune out, trust, whether they'd share). Rewrite the article from the
   accepted notes — clearer, less technical, worth the reader's time, every fact intact. This is the
   **customer** gate; the editor gate is next.

4. **Edit the ARTICLE.** Read **`consulting-copy-editor`** and run its editorial pass on the rewritten
   `article.md`. Implement accepted edits in place. Defer score/report/commit to step 8 because this
   parent workflow scores the full bundle once. Use the edited article as the source for every downstream step.

5. **Derive the LinkedIn POST.** Read `consulting-copywriting` §social + **`consulting-linkedin-post-architect`**.
   Write a **stand-alone** post that delivers complete value on its own (don't just paste the article intro) —
   phone-first formatting, value above the fold. The article link is **optional**: add it only as a bonus after
   an already-complete post, never a forced "read the article" / "link in comments." Save as `linkedin.md`
   (frontmatter: `source` = the article path, `hook`, `status: draft`).

6. **Edit the LinkedIn POST.** Run **`consulting-copy-editor`** on `linkedin.md`. Implement accepted edits
   in place before illustration and scoring. Defer score/report/commit to step 8.

7. **Illustrate the edited article.** Read **`consulting-article-illustrator`** (the house article-image skill;
   brand taste via **`consulting-tasteful-design`** / `DESIGN.md`). Per its density rule, produce the
   **hero** — saved as `images/image1.png` and embedded above the first line — **plus ~1 inline figure per
   major section**, saved as `images/image2.png`, `image3.png`, … (reading order) and embedded at each
   section break (pick the archetype that fits each concept). Hand-drawn whiteboard palette; generate with **gpt-image-2** (this
   run is a cloud worker with the Higgsfield connector → use the illustrator's Higgsfield `gpt-image-2`
   route). Run the illustrator's bar on each image. If image generation isn't available, stage the
   article without figures and flag it in the report — don't block the article.

8. **Write the manifest, mark the signal, report, score, commit.** Write the bundle **`meta.yml`** — the
   approval state machine: `id` (the folder), `title`, `date`, `engine: A`, `source` (the signal path), a
   `formats:` list (one row per artifact — `article`/`linkedin`, each with `file:` + `status: draft`), and
   `images:`. This is the row Sid approves per format. Then set the consumed signal's `status: used` + `used_by:`
   the bundle path, and regenerate `signals/_index.md` (an `evergreen` insight stays evergreen — append
   the bundle to its `used_by` history instead). Write `business/ops/content-reports/<date>.md` (**Article ·
   Reader review · Article edit · Post · Post edit · Hero + figures · Skipped (why) · Needs Sid**), run
   `python evals/content/score_run.py` (composite + flags at top), commit each draft why-first, stamp
   `content/_work/LAST_DRAFTED`, then stop.

## Notes
- **Article-first is the leverage.** The pillar gets atomized later into X threads, a newsletter, more LinkedIn
  angles. Spend the effort on the pillar.
- **Mine, don't manufacture.** Nothing worth a pillar → say nothing. The flywheel rewards signal, not cadence.
- Scored by `evals/content/score_run.py`: completeness (edited article + edited post + images), grounding, voice, non-dup.

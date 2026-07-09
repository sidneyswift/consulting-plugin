---
name: consulting-friday-review
description: The weekly content + system review ritual. Use on "run the Friday review", weekly cadence, or "what should I write this week". Good candidate to wire as a scheduled task.
---

# Consulting Friday Review

## Steps
1. Scan `signals/` for unused signals — the dated `<YYYY-MM-DD>-*.md` files (`status: new`; skip the meta files `AGENTS.md`/`_template.md`/`_index.md`/`_archive/`; target 15–20 candidates).
2. Detect repeated questions across the week's calls and `knowledge/` — repeats are the strongest content signal.
3. Scan published posts + `integrations/linkedin/engagement/` for winners/outliers → run
   `consulting-content-recycler` (repost with a fresh hook · re-share with context · fan an outlier
   into new formats). A winner not recycled is shelf inventory.
4. Run `consulting-content-extraction` on any un-processed transcripts in `content/01-raw/`.
5. Run `consulting-research-miner` if the research wiki advanced since `integrations/research/_work/LAST_MINED` — harvest fresh agent/skill/compound-engineering ideas into `signals/` (delta-guarded; no-ops if nothing's new).
6. Propose the top 1–3 ideas to test (→ `consulting-content-idea-generator`) or draft (→ `consulting-content-drafter`).
7. Surface knowledge-base gaps (questions answered 2+ times but not yet an FAQ).
8. Report a short weekly content plan.

Source: Ch. 4 (the Friday Review).

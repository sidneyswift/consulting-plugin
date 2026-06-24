---
name: consulting-friday-review
description: The weekly content + system review ritual. Use on "run the Friday review", weekly cadence, or "what should I write this week". Good candidate to wire as a scheduled task.
---

# Consulting Friday Review

## Steps
1. Scan `content/02-ideas/` (target 15–20 candidates).
2. Detect repeated questions across the week's calls and `knowledge/` — repeats are the strongest content signal.
3. Run `consulting-content-extraction` on any un-processed transcripts in `content/01-raw/`.
4. Run `consulting-research-miner` if the research wiki advanced since `integrations/research/_work/LAST_MINED` — harvest fresh agent/skill/compound-engineering ideas into `content/02-ideas/` (delta-guarded; no-ops if nothing's new).
5. Propose the top 1–3 ideas to test (→ `consulting-content-idea-generator`) or draft (→ `consulting-content-drafter`).
6. Surface knowledge-base gaps (questions answered 2+ times but not yet an FAQ).
7. Report a short weekly content plan.

Source: Ch. 4 (the Friday Review).

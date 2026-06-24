---
name: consulting-research-miner
description: Mine the external AI & Agents research wiki for content. Use on "harvest research", "content ideas from research", "mine the research wiki", on the Friday cadence, or whenever the research wiki (../research) has new material. Turns its cited analysis into content/02-ideas/ cards that show the practice's agent/skill expertise — read-only; never copies wiki pages in.
---

# Consulting Research Miner

Harvest the research wiki (a read-only, **content-only** source) into the content backlog. The
**mining protocol, path config, and boundary rules live in `integrations/research/AGENTS.md`** —
read that first; this skill is only the harvest loop layered on top of it.

## When to run
Friday cadence (via `consulting-friday-review`), on demand ("harvest research"), or whenever the
wiki's `log.md` has advanced since `integrations/research/_work/LAST_MINED`.

## Steps
1. **Follow the protocol.** Read `integrations/research/AGENTS.md` → resolve the wiki path, then read
   the wiki's `for-builders.md` + `CLAUDE.md` QUERY operation. You are running a QUERY against the wiki.
2. **Find the delta.** Read the wiki's `log.md`; select pages added/changed since `_work/LAST_MINED`.
   First run (`never`): seed from the highest-signal pages — everything under `patterns/` plus the
   paged `artifacts/` + `concepts/` (skip `sources/`, `meta/`, and tooling).
3. **Read whole pages.** For each selected page read the *entire* page — especially `## What we'd
   steal` and `## Patterns demonstrated`. Don't skim only the steal bullets (the wiki's own anti-rule).
4. **Translate analysis → angles.** Turn each portable idea into a first-person content angle that
   shows *your* expertise (teach it / argue it / show the receipts), not a third-person book report.
   Keep the strongest ~5–10 across the delta — quality over a dump (the weekly target is 15–20 ideas).
5. **Write the card file** at `content/02-ideas/YYYY-MM-DD-research-<topic>-ideas.md`, in the house format
   (match any existing `content/02-ideas/*-call-ideas.md`):
   - `# Content candidates — Research wiki: <topic> (YYYY-MM-DD)`
   - a `Source:` line naming the wiki pages mined;
   - `## LinkedIn post candidates` — numbered; each a **bold hook**, a `Hook:` body, an
     `*(Intent: <audience / TAM>)*` tag, **and the `[[wiki page]]` citation** it came from;
   - `## Blog / long-form topics` — bullets, each with its `[[citation]]`.
6. **Promote durable POVs.** If a page yields a reusable explanation/framework (not just a hook), also
   drop it into `knowledge/insights/` with its citation.
7. **Stamp + report.** Update `_work/LAST_MINED` to the newest harvested `log.md` date. Report: pages
   mined · ideas written · POVs promoted · any **gaps** (topics you expected but the wiki lacked).

## Discipline
- **Cite or omit.** Every claim/figure/quote in a card carries its `[[wiki page]]` (and load-bearing
  `[[sources/…]]`). Anything you can't trace → label `[UNVERIFIED]`, or leave it out.
- **Read-only.** Never write to the wiki; never copy its pages into this repo — only distilled cards
  + cited POVs cross the boundary.
- **Content only.** This never touches `clients/` or `pipeline/`. Research is a content source.

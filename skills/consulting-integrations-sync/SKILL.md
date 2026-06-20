---
name: consulting-integrations-sync
description: The anti-staleness engine for external integrations. Use on the Friday cadence, on "sync the integrations", "is the CRM in sync", "refresh granola/attio/linkedin/gmail/slack", or whenever the repo might have drifted from Attio/Granola/LinkedIn/Gmail/Slack. Reconciles live sources against the repo and reports what changed and what's stale.
---

# Consulting Integrations Sync

Keep `integrations/` (Granola, Attio, LinkedIn, Gmail) and the curated repo from going stale.
Run end-to-end, then report. API keys are in repo-root `.env.local`.

## Steps
1. **Attio (query live — system of record).** Per `integrations/attio/crm-sync.md`, query deals via REST
   (`POST /v2/objects/deals/records/query`). For each deal, compare its **stage** to its
   filesystem location. On mismatch: move the folder (`pipeline/**` ↔ `clients/**`), fix the deal
   `AGENTS.md` status line, and regenerate `pipeline/_board.md`. Attio wins on stage; repo wins on artifacts.
2. **Granola (re-pull deltas — mirror).** If new meetings exist since `integrations/granola/_work` was
   last built, re-run the pull pipeline (or note it's due). File new consulting meetings under the right
   `clients/`/`pipeline/` folder and flag any **new prospect** for `consulting-lead-intake`.
3. **LinkedIn (pull signal).** Refresh follower/engagement snapshots if stale; if new engagement exists,
   chain into `consulting-linkedin-audience`. Update `integrations/linkedin/_work/LAST_SYNCED`.
4. **Gmail (if auth configured).** Pull deal/client threads; flag any **awaiting my reply**. If auth
   isn't set up yet, skip and note it.
5. **Slack (if auth configured — log + channel, like Gmail).** Pull deal-tied conversations only
   (never the whole workspace), and pull each one **complete — every top-level message AND every thread
   reply** (`--days 0 --threads`); a bounded window silently drops new replies on older threads, so don't
   use one. Run `integrations/slack/_work/list_access.py` to confirm read access, then for each row of the
   **Deal channel routing** table in `integrations/slack/AGENTS.md` run
   `integrations/slack/_work/pull_conversation.py --channel <id> --token user --days 0 --threads
   --out <dest>/<YYYY-MM-DD>-<channel>.md`. File each keeper next to its client, mine the internal
   product DM into `knowledge/product/`, and flag threads **awaiting my reply**. Mine only the lines new
   since `integrations/slack/_work/LAST_SYNCED` (so insights don't duplicate), then stamp it. No `SLACK_*`
   keys set → skip and note it.
6. **Research wiki (read-only content source).** Mined by `consulting-research-miner` (delta-guarded
   via `integrations/research/_work/LAST_MINED`) and pulled at draft time by `consulting-content-drafter`
   — see `integrations/research/AGENTS.md`. The Friday harvest lives in `consulting-friday-review`;
   trigger the miner here too if the wiki's `log.md` advanced since `LAST_MINED`.
7. **Mine fresh material.** New won deals → `consulting-case-study-builder`; recurring answers →
   `knowledge/faqs/`; reusable insights → `knowledge/insights/` + `content/ideas/`.
8. **Stamp + report.** Update each integration's `LAST_SYNCED`, the crm-sync "Last full reconcile"
   note, and write a short report: **what changed · what drifted · what's stale · what needs me**.

Confirm before inventing client facts. Do the routine filing/reconciling without asking.

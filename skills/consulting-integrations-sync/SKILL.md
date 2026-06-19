---
name: consulting-integrations-sync
description: The anti-staleness engine for external integrations. Use on the Friday cadence, on "sync the integrations", "is the CRM in sync", "refresh granola/attio/linkedin", or whenever the repo might have drifted from Attio/Granola/LinkedIn. Reconciles live sources against the repo and reports what changed and what's stale.
---

# Consulting Integrations Sync

Keep `integrations/` (Granola, Attio, LinkedIn, Gmail) and the curated repo from going stale.
Run end-to-end, then report. API keys are in repo-root `.env.local`.

## Steps
1. **Attio (query live — system of record).** Per `operating/crm-sync.md`, query deals via REST
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
5. **Mine fresh material.** New won deals → `consulting-case-study-builder`; recurring answers →
   `knowledge/faqs/`; reusable insights → `knowledge/insights/` + `content/ideas/`.
6. **Stamp + report.** Update each integration's `LAST_SYNCED`, the crm-sync "Last full reconcile"
   note, and write a short report: **what changed · what drifted · what's stale · what needs me**.

Confirm before inventing client facts. Do the routine filing/reconciling without asking.

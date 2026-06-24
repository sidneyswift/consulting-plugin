---
name: consulting-system-auditor
description: Reconcile and health-check the whole workspace. Use on "audit the system", "is everything up to date", or periodically.
---

# Consulting System Auditor

## Steps
1. Reconcile filesystem ↔ Attio CRM: deals in the right stage, no drift (`integrations/attio/crm-sync.md`).
2. Find stale client `AGENTS.md` dashboards (status/next-action out of date).
3. Find un-processed transcripts in `content/01-raw/` and `*/meetings/` (→ run `consulting-call-processor`).
4. Find wins missing a case study or testimonial; recurring answers missing an FAQ.
5. Check the dashboard and metrics are current.
6. Report a prioritized punch list (don't auto-change client facts without confirming).

Source: CLAUDE.md auto-manage discipline.

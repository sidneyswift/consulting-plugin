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
2. **Granola (capture VERBATIM transcripts — the primary source, not the summary).** List new notes:
   `python integrations/granola/_work/list_new_notes.py` (id/title/created_at/attendees for notes newer
   than `_work/LAST_SYNCED`). Classify each by job + attendee domain: **in scope** = Recoup consulting (a
   won client or an open prospect/lead); **skip** SwiftResponse/Flex, personal, and internal standups
   (note skips in the report, don't fetch them). For each in-scope note capture the transcript —
   `python integrations/granola/_work/pull_transcript.py --note <id> --stage --out <dest>` — where `<dest>`
   is `clients/<client>/meetings/transcripts/<YYYY-MM-DD>-<slug>.md` (won) or
   `pipeline/<stage>/<deal>/meetings/transcripts/<YYYY-MM-DD>-<slug>.md` (open). The file holds the AI
   summary (labelled *not evidence*) **and the verbatim transcript** — cite the transcript downstream,
   never the summary. New prospect with no folder → `consulting-lead-intake` first. Stamp
   `integrations/granola/_work/LAST_SYNCED` with today's ISO datetime.
3. **LinkedIn (pull signal).** Refresh follower/engagement snapshots if stale; if new engagement exists,
   chain into `consulting-linkedin-audience`. Update `integrations/linkedin/_work/LAST_SYNCED`.
4. **Gmail (capture FULL threads for real relationships — Attio-gated).** Scope = people who matter:
   query Attio live for **Customers + Warm Leads + Target Accounts + open-pipeline contacts**, collect their
   email domains/addresses (the 1,041 `relationship = product-user` are quarantined — exclude). For each
   client/deal, archive the **full thread history** (every message, untruncated):
   `python integrations/gmail/_work/export_thread_bodies.py --query "from:<domain> OR to:<domain>"
   --title "<Name>" --out <clients|pipeline>/<entity>/emails/email-archive-<YYYY-MM-DD>.md`. Then layer the
   triage on top — `pull_threads.py` for **awaiting-my-reply** — as derived signal, not a replacement for
   the archive. A **human, non-automated sender NOT in Attio** → don't archive; flag it in the report as a
   possible new lead. Never archive the whole mailbox (automated/no-reply/newsletters excluded). Stamp
   `integrations/gmail/_work/LAST_SYNCED`. No auth → skip + note.
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
   `knowledge/faqs/`; reusable insights → `knowledge/insights/` + `content/02-ideas/`.
8. **Stamp + report.** Update each integration's `LAST_SYNCED`, the crm-sync "Last full reconcile"
   note, and write a short report: **what changed · what drifted · what's stale · what needs me**.

Confirm before inventing client facts. Do the routine filing/reconciling without asking.

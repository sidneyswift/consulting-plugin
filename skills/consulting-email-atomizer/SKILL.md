---
name: consulting-email-atomizer
description: Fan one source insight into several scheduled, segment-routed email touches (trend-jack, proof, insight, build-in-public, 1:1 nudge) staged as drafts, never one-offs. Use after a call/extraction, on "turn this into emails", "atomize for email", "what should I send the list", or when a notable industry event lands. Powers the top-of-funnel email engine.
---

# Consulting Email Atomizer

Turn one source (a `knowledge/insights/` entry, a fresh call, or an industry event) into several
email touches. Second consumer of the insight reservoir (LinkedIn is the first).
Full design: `docs/plans/2026-06-19-email-engine-design.md` · templates: `library/email-templates/` (06-11) ·
staging + frontmatter + routing: `content/email/AGENTS.md`.
**Voice + gate (always):** write in `consulting-copywriting` voice, then run every draft through the `consulting-outbound-email` skill (read context, route to the right person, reader-POV check, names verified) before staging.

## Steps
1. **Take one source.** Prefer an existing `knowledge/insights/` file. If it is a raw call, run
   `consulting-content-extraction` first so the insight exists. Record its path. It becomes `source:`.
   *No source, no email.*
2. **Atomize.** Decide which of the 6 formats this source can *honestly* yield (most yield 2-4, not
   all 6). A weak fit is a skip. Don't pad.
3. **Route.** For each chosen format, apply the default routing (`content/email/AGENTS.md`):
   trend-jack → cold/warm/targets · proof → everyone · insight → warm/targets/customers ·
   build-in-public → customers/warm · nudge → one named person · newsletter → whole list.
4. **Resolve segments live.** Query Attio (`ATTIO_API_KEY`) for current membership of each target
   segment. Reconcile-on-touch, never a copied list. For a 1:1 nudge, pick the one named contact.
5. **Draft each touch.** Fill the matching `library/email-templates/` skeleton in Sid's voice.
   Always apply `consulting-copywriting` (the voice) and the `consulting-outbound-email` gate (names
   verified against real context). Borrow `consulting-content-drafter`'s AIDA and "you over I". Ground
   every claim in the source. No invented numbers, streams, or chart positions.
6. **Stage.** Write each to `content/email/outbox/<send_date>-<format>-<segment>.md` with the
   instance frontmatter (format · source · audience/recipient · send_date · `status: draft` · `channel: gmail`).
7. **Report the fan-out** (1 source into N drafts) with proposed send_dates spread across the week.
   **Never send.** Offer to stage Gmail drafts via `integrations/gmail/_work/create_draft.py` only on confirmation.

Output: N staged email drafts in `content/email/outbox/`, each tracing to one source.
Source: Ch. 3/5 (atomization plus the multi-format test) plus `docs/plans/2026-06-19-email-engine-design.md`.

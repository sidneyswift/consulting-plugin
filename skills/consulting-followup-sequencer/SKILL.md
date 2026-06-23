---
name: consulting-followup-sequencer
description: Generate the timed follow-up cadence for a deal, personalized to the client's stated stakes. Use after a call or proposal, on "draft follow-ups", "they went quiet", "what do I send next".
---

# Consulting Follow-Up Sequencer

> Voice + gate: write in `consulting-copywriting` voice, then run every draft through `consulting-outbound-email` (read context, route, reader-POV check) before staging.

## Steps
1. Pull the deal's specifics: the outcome discussed, the stakes in their words, the next-meeting date.
2. Fill the templates in `library/email-templates/`:
   - Same-day thank-you
   - 24h value-add (attach a relevant resource/case study)
   - Proposal delivery (within 48h, suggest a Loom)
3. If silent, generate the Day 5 / 10 / 15 sequence (max 3 touches), each referencing *their* stakes, not your proposal.
4. **Stage in Gmail (optional).** Offer to drop each touch into Gmail as a draft via
   `integrations/gmail/_work/create_draft.py --to <addr> --subject "..." --body-file <file>`
   (creates a draft; only sends with `--send` + a typed confirmation). Save drafts next to the deal
   (e.g. `pipeline/01-leads/<deal>/followups.md`).
5. Offer to set reminders / a scheduled task for the cadence.

Output: ready-to-send emails (optionally staged as Gmail drafts). Source: Ch. 14 (48-Hour Rule + follow-up sequence).

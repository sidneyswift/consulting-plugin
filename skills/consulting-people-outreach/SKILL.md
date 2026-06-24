---
name: consulting-people-outreach
description: Draft the FIRST direct touch to a new person — a warm engager or fresh lead with no prior interaction — grounded in the specific post/context that surfaced them, in Sid's voice, on the right channel (LinkedIn connection note/DM, or email). Use on "draft outreach to this new lead", "reach out to who engaged", "first message to X", or when consulting-linkedin-audience surfaces a new high-fit person. Drafts only, never auto-send/auto-connect.
---

# Consulting People Outreach

> The first-touch skill. This owns the cold/warm **opening** message to someone you have **no prior
> interaction** with. Once they reply (a real interaction exists), hand the cadence to
> `consulting-followup-sequencer`. For *commenting* to warm someone first, that's
> `consulting-linkedin-engage` (queue only — it never DMs).

> Voice: run every draft through `consulting-email-voice` (its rules are the house voice — no
> em-dashes, short and direct, value over neediness, evidence over authority, names verified).

## Steps
1. **Gather the real context — never open from a snippet.** Pull what actually surfaced them and
   anything known about them:
   - The **specific post/comment** they engaged with (`integrations/linkedin/engagement/*.json` or the
     post URL) — this is the genuine hook.
   - Their **ICP tier + signal** (`score_lead.score_fit`; `positioning/icp.md` for the angle).
   - Any **prior history** (usually none for a new engager — say so explicitly): live Gmail
     (`search_threads`), `integrations/granola/`, the Attio record. If there's real history, this
     isn't a first touch — use `consulting-followup-sequencer` instead.
2. **Pick the channel by what you can verify:**
   - **Verified email on file** (from `enrich.py` / `enrich_getleads.py`) → draft an **email** and run
     it through `consulting-email-voice` (then stage per step 5).
   - **No email** (most LinkedIn engagers) → draft a **LinkedIn connection note** (≤ ~300 chars) or, if
     already connected, a short **DM**. LinkedIn has no safe send API — like `consulting-linkedin-engage`,
     this stays human-in-the-loop: Sid sends it himself.
3. **Draft in first-touch posture.** Open with something specific to *their* post (a genuine point of
   view, not generic praise). Lead with value; the ask is soft or absent (first touch ≈ cold: pure
   value, no close). One idea, short, confident not needy. Make the angle Sid's positioning (turn
   scattered AI experimentation into coordinated capability), tied to their actual context.
4. **Ground every claim (evidence discipline).** Never invent a shared connection, a mutual, or a
   result. Reference only real, named examples; if you don't have one, drop the claim and just ask the
   genuine question. Get every name/title/company right.
5. **Stage as a draft — never auto-send, never auto-connect.**
   - Email → `integrations/gmail/_work/create_draft.py --to <addr> --subject "..." --body-file <file>`
     (draft only; sends solely with `--send` + a typed confirmation).
   - LinkedIn note/DM → write it to `integrations/linkedin/engagement/<date>-outreach.md` (one block per
     person: who, why they fit, the post URL, the message) for Sid to send manually.
6. **Close the loop.** Note the outreach on the Attio lead record (a touch was made). When they reply,
   the relationship is live → hand to `consulting-followup-sequencer` for the timed cadence.

## Chains with
- **Upstream:** `consulting-linkedin-audience` (new high-fit engagers → leads) · `consulting-linkedin-engage`
  (comments that warmed them) · `consulting-lead-intake` (a fresh inbound).
- **Voice:** `consulting-email-voice`. **Downstream (after a reply):** `consulting-followup-sequencer`.

Output: a staged first-touch message (Gmail draft or a LinkedIn note in `engagement/`), grounded and
in voice, ready for Sid to send. Never sent automatically.

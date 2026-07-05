---
name: consulting-progress-report
description: Write and ship the recurring client-facing progress report — the contractual bi-weekly/monthly "what did I get for my money" update to the engagement sponsor (often the payment condition). Use on "write the progress report / bi-weekly update for {client}", when a report due-date hits, or after a delivery period closes. Assembles from the client's activity log, verifies every claim against primary sources, drafts in the locked house format (TLDR of before→after arrows, quick notes, next two weeks, saving-for-{platform}, needs, per-stakeholder goals), gates through consulting-copy-reviewer role-playing the actual sponsor plus a fresh-eyes condense pass, then Sid's critique loop. NOT the light session recap (consulting-stakeholder-update) and NOT the quarterly value review (consulting-quarterly-value-review) — this is the contractual cadence deliverable between them.
---

# Consulting Progress Report

The report's job, in order: (1) a busy non-technical sponsor reads ALL of it and understands it, (2) they
feel the hire is paying off (trust up, "I'd repeat this to a peer"), (3) they start wanting the next,
bigger scope — seeded by the deferred list, never pitched. Every choice below serves those three.

Voice: `consulting-copy-writer` (no em-dashes, plain words, digits). Process guardrails here are the
lessons from the 2026-07-03 Seeker report #1 build (exemplar: as-sent verbatim + Sid's final-edit notes
in `clients/seeker-music/04-delivery/progress-reports/2026-07-03-report-1.md`).

## Inputs (gather before drafting)

1. `clients/{client}/04-delivery/account-activity-log.md` — the canonical session-by-session source. If
   sessions are missing from it (nightlies sometimes only update the dashboard), backfill entries first.
2. Verbatim transcripts in `clients/{client}/meetings/transcripts/` — verify every number, count, quote,
   and state-claim against these, not against AI summaries.
3. The client `AGENTS.md` Reality section — reconcile; Sid's confirmed POV outranks inference.
4. `04-delivery/running-lists.md` (client-surfaceable) — the deferred list feeds "Saving for {platform}".
5. **Never** pull from `## Expansion watch` or any internal-only strategy file into a client artifact.

## Evidence rules (non-negotiable)

- **No unaudited numbers.** If the only figure is the client's own qualitative estimate, publish it as an
  attributed quote: `Time saved so far: "days of work" (Darren's estimate)`.
- **No promises you can't guarantee.** "The next report opens with the measured number" got cut by Sid:
  never commit a future deliverable/number in a client artifact.
- **Don't overclaim state.** In-build stays "(still in build)"; local-only stays "(on {name}'s machine for
  now)"; org-level install ≠ per-user install — say which.
- **Client-corrected facts outrank derived ones.** When Sid corrects a count (sessions, workflows), his
  number ships and the resolution gets logged back to the activity log/dashboard.
- **Unreconciled facts stay out.** Conflicting counts (e.g. 3 catalog numbers on file) → write around the
  number. Ambiguous names (Steven vs Stefan) → address the group ("you and the exec team").
- **Money always carries its control context** ("caps with request-based top-ups, Darren at $1,000/mo.
  Spend stays visible as more people come on"), so the sponsor never discovers run-rate one bullet at a time.

## The format (locked with Sid, 2026-07-03)

Internal front matter (To/From/Period/Date + a DRAFT line deleted on send), then the email body:

1. **Greeting** — "Hey {sponsor}," + logistics note only if needed (e.g. work-email-down). One-line
   framing: "Below is the progress report of the last two weeks: where things were, where things are now,
   what's next, etc." + "Quick video: {Loom URL}" (1-minute walkthrough).
2. **TLDR (two weeks ago → today)** — 5–7 bullets, each a readable `before → after` phrase around a
   literal `→`. **No category labels** ("Darren:", "Owned AI:" — banned; the compartments read as
   ambiguous). Backticks on system names (`Finance OS`). Lead with the person/adoption story ("{champion}
   typing into chat → building in Code"), put ownership on the deliverables ("15 {Client}-owned finance
   skills"), end on the value line (time saved).
3. **Quick notes** — 2–3 one-line items that matter but need no explanation (spend policy, dashboard).
4. **The next two weeks** — only real commitments, named people, one line each ("Continue weekly sessions
   with X to improve `{OS}`", "Start weekly sessions with Y...", "Plan sessions next month with Z...").
   Attribute claims ("per Nicole, he's one of the heaviest users").
5. **Saving for {platform}** — the expansion seed. "Work outside the current scope, worth doing when we
   take over {platform}. Not building these yet; keeping a running-list:" then plain-named connection
   bullets (no "MCP"/"write-back" jargon). This is restraint-framed value, never a pitch.
6. **Needs from {client}** — only asks they must act on NOW, each routed to a named owner, "when you're
   ready" on the non-urgent, gloss unknown tools ("Granola (meeting notes)"). After the asks, the
   no-pressure line: "Nothing above needs a decision yet, but if I can get my hands on {docs/APIs} now, I
   can start mapping how {platform} will connect to everything we're building."
7. **What we're working towards** — the closer: one goal per named stakeholder, quoted-style, the
   sponsor's goal LAST ("Evan's Goal: '...increases speed and revenue without adding headcount.'"). This
   ends the read on where everyone is headed, in the sponsor's own success language.

Length bar: the sponsor finishes it. One page. If a bullet needs a paragraph, it's the Loom's job.

## Process

1. **Backfill + verify.** Update the activity log from any unlogged sessions; verify the load-bearing
   claims against transcripts (quote timestamps in your working notes).
2. **Draft** to `clients/{client}/04-delivery/progress-reports/{date}-report-{N}.md` with the DRAFT
   status line. Commit (drafts are episodic memory too).
3. **Gate 1 — the sponsor's eyes.** Run `consulting-copy-reviewer` with the persona tightened to the
   actual sponsor (never technical), loaded with engagement context (fee, why they hired, their board's
   priorities, team names, how busy they are). Add the report-specific questions: too long / where would
   you stop? was the month's fee well spent, which line? 0–10 would you recommend, what raises it? what
   makes you want to expand scope? Triage: accept jargon flags, buried wins, trust dips; reject any note
   that needs an invented number.
4. **Gate 2 — fresh-eyes condense.** A zero-context subagent sweeps for combinable bullets,
   redundancies, and state contradictions (the "installed org-wide" vs "team installs next" class). Merge;
   keep every fact.
5. **Sid critique loop.** His corrections are ground truth (they often carry NEW facts — log those to the
   dashboard/lists). Iterate in place; commit each round with a why-first message.
6. **Ship kit.** On request: a white-background HTML paste source next to the report (dark-theme rich-text
   copies carry background colors into Gmail; the HTML file pastes clean — delete it after send), a
   ~90-second Loom script (repo → skills → dashboard → design system → deferred list + asks), and the
   Slack variant (a one-line "dropping the report I emailed @here too" wrapper; the email-logistics
   opener stays email-only).
7. **After send — file it.** Replace the file body with the **as-sent verbatim** (+ an internal-notes
   section recording Sid's final edits as skill feedback), mark ✅ SENT in the title and the schedule
   table, add a sent entry to the activity log, refresh the dashboard (report due-date, new commitments,
   new asks/balls, any new facts Sid introduced), sync the running lists, and commit.
8. **Compound.** Diff Sid's sent version against the last draft; fold recurring edits back into this
   skill and the client's `_TEMPLATE.md`.

## Instance vs. skill (keep the boundary)

Client specifics (the champion's name, the platform name, which connections are deferred, the $ cap)
live in the client's `_TEMPLATE.md` and reports. This skill owns the process, the format shape, the
evidence rules, and the voice — improve the skill when the lesson generalizes, the template when it's
client-shaped.

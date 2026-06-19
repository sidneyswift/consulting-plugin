---
name: consulting-account-reality
description: Build or refresh the "Reality (Sid's POV)" section for a client or lead by traversing every comms channel holistically, then synthesizing — explicitly flagging missing data. Use before any big account move, on "what's really going on with X", "refresh the reality for X", when a dashboard looks stale or assumed, or before drafting outreach to a customer/lead.
---

# Consulting Account Reality

Produce an **evidence-grounded, honestly-caveated picture** of where one account actually stands — and
keep the agent from mistaking *activity* for *outcomes*. The output is the `## Reality (Sid's POV)`
block at the top of the entity's `AGENTS.md` (canonical shape: `clients/rostrum/AGENTS.md`).

> Why this exists: we once read 39 GitHub PRs and concluded Recoup "built Rostrum's backbone" — true
> for *build*, false for *adoption* (the usage data was simply missing). This skill forces the
> holistic look + the missing-data flag **before** any assumption. **build ≠ usage · CRM stage ≠ health.**

## Steps
1. **Scope to ONE entity (deal-scoped).** Load only that account's `clients/<client>/` or
   `pipeline/<stage>/<deal>/` folder + its `AGENTS.md`. Never load the whole lake.
2. **Traverse every channel — collect, don't conclude.** Fan out (parallel subagents for speed), one
   per source, each on a strict *"cite source + quote; do NOT interpret"* brief:
   - **Granola** notes (`integrations/granola/Recoup/clients|prospects/<entity>/`) — verify any figure
     against the **verbatim transcript** (`?include=transcript`), not the AI summary.
   - **Gmail** thread (`integrations/gmail/threads/<entity>.json`) — who owes the reply, last ball.
   - **Slack** deal channel(s) (routing table in `integrations/slack/AGENTS.md`) — async delivery state.
   - **Attio** live (`ATTIO_API_KEY`) — stage, $, people (reconcile-on-touch).
   - **GitHub** (only if we build product for them) — *build* activity, explicitly NOT adoption.
   Each subagent returns cited facts **and a list of what that channel could NOT tell you.**
3. **Synthesize + separate activity from outcome.** Reconcile across channels. Distinguish build/commits
   from adoption, CRM stage from health, a plan from a commitment. Anything not directly evidenced →
   **[MISSING]**; never infer success from volume. Re-verify any subagent's numbers against the source.
4. **Write the `## Reality (Sid's POV)` block** at the top of the entity `AGENTS.md`: where it stands,
   what the customer actually values, the highest-leverage next move, risks, and an explicit
   **[MISSING]** list. If Sid hasn't confirmed it, label it **DRAFT — agent-reconstructed, Sid to
   confirm** (never present a reconstruction as Sid's stated view). Keep a dated _Challenge log_.
5. **Apply the value ladder.** Flag whether the best next move is communication / an artifact / a
   proactive update / presence / aggressive execution — *before* defaulting to building product (slow,
   expensive). Match the move to what THIS account values right now.
6. **Report what needs Sid.** Surface the [MISSING] gaps + any money/dates to confirm. Never auto-send;
   confirm before writing client facts into the dashboard.

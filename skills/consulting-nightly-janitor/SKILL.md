---
name: consulting-nightly-janitor
description: Phase 2 of the nightly pipeline — the workspace reconciler. Runs after the ingestion sweep, reads the digest's "Needs you" queue, and does the higher-judgment MUTATIONS capture deliberately skips: create prospect dashboards (lead-intake), reconcile Attio↔folder drift, move deals across funnel stages (evidence-gated), refresh stale dashboards, regenerate indexes, archive dead files. Use on "run the janitor", "reconcile the workspace", "clear the digest queue", or as the nightly post-capture ritual. Mutating + evidence-gated — never the capture step.
---

# Consulting Nightly Janitor (workspace reconciler)

Capture (`consulting-nightly-ingestion`) gets raw in and writes the digest. **This is phase 2:** read
that digest + scan the workspace and do the structural maintenance capture deliberately doesn't —
turning clean raw + flags into a maintained, drift-free, navigable workspace. The digest's **"Needs
you"** section is your **work queue**.

Capture is additive and safe; the janitor **mutates** (creates dashboards, moves deals, edits the CRM,
archives files), so it runs under stricter rails.

## The janitor rails (mutation is the difference)
1. **Evidence-gate every mutation.** A stage move, a `$`/date into a dashboard, or a CRM write must quote
   a **primary source** — a captured transcript/email line, the contract, or a live Attio field. Can't
   quote it → **don't do it**; stage it in the report.
2. **Ambiguous → recommend, don't act.** When the signal is unclear (is this deal really at "proposal"?),
   write the recommendation to the report for Sid to confirm — never guess a stage or a fact.
3. **Archive, never delete.** Stale/dead *local* files move to `_archive/` (dated); never `rm`. **Never**
   delete or bulk-edit an external record (Attio/Gmail/Slack) — add/update only, only IDs you created.
4. **Idempotent.** Don't re-create a dashboard that exists, don't re-move a deal already at its stage,
   don't duplicate a prospect. Check before you act.
5. **Never auto-send** (inherited): any outbound stays a draft.

## Steps
0. **Orient + load the queue.** Read the latest `business/ops/nightly-digests/<date>.md` — its **Needs
   you** is the work list. `git log --oneline -20`. Read each touched deal/client `AGENTS.md` first.

1. **New prospects → dashboards.** For each "new prospect, no dashboard/CRM" flagged: run
   `consulting-lead-intake` to build `pipeline/<stage>/<deal>/AGENTS.md` (stakeholders, stakes, $, status,
   next action) grounded in the captured transcript/email, add the deal to `pipeline/_board.md`, and
   **stage** the Attio record write for confirmation (CRM write = evidence-gated). Skip if the dashboard
   already exists (idempotent).

2. **Reconcile Attio ↔ folder drift.** Query Attio live for each active deal; compare its **stage** to
   its folder location. On mismatch, move the folder (`pipeline/**` ↔ `clients/**`), fix the dashboard
   status line, and regenerate `pipeline/_board.md` (Attio wins on stage; repo wins on artifacts). This is
   the "Won in Attio but stuck in pipeline" catch.

3. **Funnel moves (evidence-gated).** Where a captured primary source shows a stage change ("we signed",
   "send the proposal", "they passed"), move the deal via `consulting-deal-stage-mover` (folder + board +
   Attio in lockstep) — **with the quote logged**. Ambiguous → recommend in the report, don't move.

4. **Refresh stale dashboards.** A dashboard older than its folder's **newest captured artifact** has
   un-incorporated material → refresh its status / stakes / next-action (or its `## Reality (Sid's POV)`
   via `consulting-account-reality`) from the new transcript/email. Don't invent — cite.

5. **Navigability + dedup.** Regenerate indexes
   (`python integrations/granola/_work/build_transcript_indexes.py`); resolve any duplicate artifacts
   (same note-id / thread in two files) by keeping one and noting it.

6. **Archive dead files + sweep used signals.** Stale scratch / superseded local files → `_archive/<area>/`
   dated (never delete). **Sweep the reservoir:** move `signals/*.md` whose `status` is `used` or `archived`
   (**content-type only — never evergreen insights**) into `signals/_archive/`, then regenerate
   `signals/_index.md`. This keeps `signals/` the live queue (new + evergreen).

7. **Report + score + commit.** Write `business/ops/janitor-reports/<date>.md` with sections **Done ·
   Drift fixed · Staged for confirmation · Deferred**, run `python evals/janitor/score_run.py` and put the
   composite + flags at the top, commit each change why-first, then stop. "Staged for confirmation" is the
   handoff to Sid.

## Notes
- **Reads the digest; doesn't re-pull.** No fresh digest → run capture first (or note it).
- **Quiet queue is fine.** Empty "Needs you" + no drift → one-line report, no commits. Don't invent work.
- Scored by `evals/janitor/score_run.py` against `evals/janitor/RUBRIC.md` (drift → 0, queue-clearance,
  mis-action = 0). The funnel-move is the highest-risk action — don't autopilot until a supervised run
  has validated it.

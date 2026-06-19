---
name: consulting-call-processor
description: The auto-manage orchestrator. Use whenever new client/deal material lands — a transcript, meeting note, email, or result — or when the user says "process this call", "ingest this", "handle this transcript". Runs the full keep-the-system-current loop end to end.
---

# Consulting Call Processor

The CLAUDE.md auto-manage loop as one skill. Don't stop after a single step — run the whole loop, then report what changed.

## Steps
1. **Place the raw file.** Save to the right home (`content/raw/`, `clients/{client}/meetings/`, or `pipeline/{stage}/{deal}/`), dated `YYYY-MM-DD`.
2. **Read it.**
3. **Extract.** Run `consulting-content-extraction`. If it's a discovery/sales call, also run `consulting-discovery-analysis`; if the deal is qualified, chain into `consulting-proposal-drafting`.
4. **Scan the related folder.** Open the client/deal folder, read its `AGENTS.md` dashboard, reconcile against the new info.
5. **Update affected files.** Refresh the client `AGENTS.md` dashboard (status, stakes, $, next action), `pipeline/_board.md`, and `operating/dashboard.html`. Capture new stakeholders, decisions, dates.
6. **Move files to match reality.** If the deal changed stage, run `consulting-deal-stage-mover`.
7. **Mine for content + proof.** Recurring answers → `knowledge/faqs/`; wins → trigger `consulting-case-study-builder` / `consulting-testimonial-capture`.
8. **Report** a short summary of everything changed.

Confirm before inventing client facts; otherwise do the routine filing without asking.

---
name: consulting-deal-stage-mover
description: Advance a deal cleanly when its state changes. Use on "move X to proposal", "we won/lost the deal", "X signed", or any pipeline stage change. Keeps folders, the board, and the CRM in sync.
---

# Consulting Deal Stage Mover

## Steps
1. Locate the deal folder under `pipeline/{current-stage}/{deal}/`.
2. Move it to the new stage:
   - Forward through `pipeline/01-leads → 02-qualifying → 03-discovery → 04-proposal → 05-negotiation`.
   - On **win**: run `consulting-client-onboarding` (move into `clients/{client}/`).
   - On **loss**: move to `pipeline/closed-lost/` and write a short post-mortem (why, what to learn).
3. Update `pipeline/_board.md`.
4. Update the Attio CRM stage to match (`operating/crm-sync.md` mapping).
5. Update `operating/dashboard.html` funnel counts.

Rule: never let the filesystem and CRM drift. Report the move.

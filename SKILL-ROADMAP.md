# Skill Roadmap

Every repeatable workflow in the playbook, mapped to a skill we can author with `/skill-creator`.
Rule of the practice: **anything done more than once becomes a skill.** Each skill lives in
`skills/<name>/SKILL.md`, then gets packaged into a plugin and installed so it triggers
non-deterministically (see `skills/_packaging/README.md`).

Status legend: ✅ built (all 26 now authored). Priority: **P0** = highest leverage. Next step: package + install so they auto-trigger (consulting-skill-packager).

---

## P0 — The spine of the operating system (build first)

### 1. consulting-call-processor ✅ (P0) — the auto-manage orchestrator
The CLAUDE.md ingest loop as a single skill. Drop in any transcript/note/email and it runs the
whole loop end-to-end.
- **Trigger:** new transcript/note/email added, or "process this call", "ingest this".
- **Does:** place raw file (dated) → read → run content-extraction + (if discovery) discovery-analysis → scan the related client/deal folder → update client README, `pipeline/_board.md`, `operating/dashboard.html` → move folders if stage changed → mine for content/proof → report changes.
- **Reads → writes:** `content/raw/`, `clients/*`, `pipeline/*` → updates dashboards, boards, KB.
- **Source:** CLAUDE.md auto-manage loop (synthesizes Ch. 4, 11, 17).

### 2. consulting-content-extraction ✅ (P0)
Mine a transcript into insights + content candidates. *Already built.* Ch. 4, 6.

### 3. consulting-discovery-analysis ✅ (P0)
Analyze a discovery call: stakes, pain, metrics, objections, qualification. *Already built.* Ch. 11, 12.

### 4. consulting-proposal-drafting ✅ (P0)
Draft a situational-assessment proposal with 3 options. *Already built.* Ch. 13, 14.

### 5. consulting-lead-intake ✅ (P0)
Triage a brand-new lead the moment it arrives.
- **Trigger:** "new lead", a fresh prospect transcript/email, or pasting an inbound inquiry.
- **Does:** create `pipeline/01-leads/<deal>/` + README, run the qualification checklist (stakes / timeline / ROI-measurability / decision-maker), flag red flags, recommend qualify-or-pass, create/update the Attio CRM record.
- **Reads → writes:** raw inquiry → `pipeline/01-leads/`, CRM record.
- **Source:** Ch. 10 (Qualifying Buyers).

---

## P1 — Sales & pipeline acceleration

### 6. consulting-pricing-builder ✅ (P1)
Generate three-tier options for a deal.
- **Trigger:** "build pricing", "what should I charge", during proposal drafting.
- **Does:** produce Advisory / Comprehensive (recommended) / Premium tiers at a 5–10x spread, anchored to the cost of *not* solving it; attach a payment structure (50/50, prepay, milestone, success-based); run the Simplicity Test.
- **Source:** Ch. 7, 8, 9 + `library/pricing/`.

### 7. consulting-followup-sequencer ✅ (P1)
Generate the timed follow-up cadence for a deal, personalized to the client's stated stakes.
- **Trigger:** proposal sent, or "draft follow-ups", "they went quiet".
- **Does:** fill the same-day / 24h / proposal-delivery / Day 5-10-15 templates with the deal's specifics; schedule reminders.
- **Source:** Ch. 14 + `library/email-templates/`.

### 8. consulting-objection-handler ✅ (P1)
Turn a raw objection into a tailored response.
- **Trigger:** "they said [objection]", "how do I respond to…".
- **Does:** match to the 4 core objection scripts (+ internal-buy-in, bad-experiences), personalize with the deal's stakes/ROI, surface "what would need to be true?", and produce stakeholder one-pagers when buy-in is the blocker.
- **Source:** Ch. 9, 15 + `library/scripts/`.

### 9. consulting-deal-stage-mover ✅ (P1)
Advance a deal cleanly when its state changes.
- **Trigger:** "move X to proposal", "we won/lost X".
- **Does:** move the folder between `pipeline/` stages (or → `clients/` on win, → `closed-lost/` with a post-mortem), update `_board.md` and the CRM stage, never letting them drift.
- **Source:** `operating/crm-sync.md` + Ch. 10–15.

---

## P1 — Content flywheel

### 10. consulting-content-drafter ✅ (P1)
Turn an idea/insight into a publish-ready draft.
- **Trigger:** "draft a post/blog about X", promoting an item from `content/ideas/`.
- **Does:** apply AIDA + the title formula ("[N] steps to [outcome] by [%] using [tool]"), "you" framing, specificity ladder; output a draft to `content/drafts/`.
- **Source:** Ch. 5.

### 11. consulting-content-idea-generator ✅ (P1)
Produce test variants to find what resonates before investing.
- **Trigger:** "ideas for X", "test this angle".
- **Does:** generate 3–5 multi-tweet framings of one idea + candidate titles, tag by intent/TAM, log to `content/experiments/`.
- **Source:** Ch. 3, 5.

### 12. consulting-friday-review ✅ (P1) — weekly ritual
- **Trigger:** scheduled weekly, or "run the Friday review".
- **Does:** scan `content/ideas/` (15–20 candidates), detect repeated questions, propose which to test/draft, run content-extraction on the week's new calls, surface KB gaps.
- **Source:** Ch. 4 (the Friday Review ritual). *Good candidate for a scheduled task.*

### 13. consulting-faq-builder ✅ (P2)
- **Trigger:** a question answered for the 2nd time, "add this to the FAQ".
- **Does:** write a canonical answer to `knowledge/faqs/`, link related content, flag it for a content piece.
- **Source:** Ch. 4 ("never answer the same question twice").

---

## P1 — Client success, retention & expansion

### 14. consulting-client-onboarding ✅ (P1)
Stand up a won client in one move.
- **Trigger:** deal won, "onboard <client>".
- **Does:** copy `clients/_TEMPLATE/` → `clients/<client>/`, fill the dashboard README, generate the kickoff checklist (SOW signed, first invoice, Slack Connect, repo, designated contacts, 48h-decision SLA), move the pipeline folder in.
- **Source:** Ch. 16 + `clients/_TEMPLATE/`.

### 15. consulting-quarterly-value-review ✅ (P1)
The connective tissue between delivery, renewals, and proof.
- **Trigger:** quarterly per client, "build the QBR for <client>".
- **Does:** assemble problems solved / value created / time saved / opportunities opened from the delivery log; output a review doc to `clients/<client>/05-retention/`; tee up a renewal/expansion proposal and a testimonial ask.
- **Source:** Ch. 17. *Good candidate for a scheduled task per client.*

### 16. consulting-testimonial-capture ✅ (P1)
- **Trigger:** milestone hit, 30–60 days in, after a QBR.
- **Does:** draft the testimonial *for* the client + the request email, log to `proof/testimonials/`, request logo rights.
- **Source:** Ch. 14, 21.

### 17. consulting-case-study-builder ✅ (P2)
- **Trigger:** engagement milestone/completion, "write a case study".
- **Does:** convert delivery docs into a problem → approach → quantified-outcome case study in `proof/case-studies/`; feed it back into content as a 24h value-add asset.
- **Source:** Ch. 21.

### 18. consulting-expansion-spotter ✅ (P2)
- **Trigger:** during/after delivery, QBR time.
- **Does:** scan a client's notes for adjacent problems, recommend Land → Expand → Transform moves and a tier upgrade, draft the expansion proposal to `06-expansion/`.
- **Source:** Ch. 17.

---

## P2 — Business operations

### 19. consulting-sow-generator ✅ (P2)
- **Does:** generate a SOW (deliverables, milestones, payment terms, resource requirements, success criteria) under the existing MSA; save to `clients/<client>/03-contracts/`.
- **Source:** Ch. 19 + `library/contracts/`.

### 20. consulting-invoice-generator ✅ (P2)
- **Does:** produce an invoice per the selected payment structure; log to `business/finance/`; track W-9 / terms.
- **Source:** Ch. 20.

### 21. consulting-metrics-updater ✅ (P2)
- **Trigger:** monthly, or after a deal changes state.
- **Does:** recompute win rate, avg deal size, cycle length, MRR, conversations/week; refresh `operating/dashboard.html`; append history to `business/metrics/`.
- **Source:** Ch. 21. *Good candidate for a scheduled task.*

### 22. consulting-ip-register-updater ✅ (P3)
- **Does:** log new frameworks/methodologies/OSS tools to the IP register in `business/legal/` to strengthen the Pre-Existing IP clause on future deals.
- **Source:** Ch. 19.

---

## P2 — Positioning & market

### 23. consulting-positioning-refiner ✅ (P3)
- **Does:** sharpen the "I help [X] achieve [Y] by [Z]" statement, audit assets for the resume trap, update `positioning/`.
- **Source:** Ch. 1, 2.

### 24. consulting-market-scanner ✅ (P3)
- **Does:** capture niche notes, buying signals ("hungry crowd"), and market-rate references into `positioning/market-research/`.
- **Source:** Ch. 3.

---

## Meta — the skill system itself

### 25. consulting-skill-packager ✅ (P1)
- **Trigger:** "package the skills", new skill authored.
- **Does:** bundle `skills/` into a plugin (plugin.json + skills), produce the `.plugin`, and guide the GitHub publish + install so skills trigger non-deterministically.
- **Source:** `skills/_packaging/README.md` + the `create-cowork-plugin` skill.

### 26. consulting-system-auditor ✅ (P2)
- **Trigger:** "audit the system", periodically.
- **Does:** reconcile filesystem ↔ CRM, find stale client READMEs, deals in the wrong stage, un-extracted transcripts, missing proof; report a punch list.
- **Source:** CLAUDE.md auto-manage discipline.

---

## Recommended build order
1. **P0 spine:** `consulting-call-processor` + `consulting-lead-intake` (the 3 existing P0 skills already cover extraction/discovery/proposal).
2. **P1 sales:** pricing-builder, followup-sequencer, objection-handler, deal-stage-mover.
3. **P1 content + client:** content-drafter, friday-review, client-onboarding, quarterly-value-review, testimonial-capture.
4. **P1 meta:** skill-packager (so everything above can be installed and auto-trigger).
5. **P2/P3:** ops, positioning, system-auditor as the practice scales.

Skills marked "scheduled task" candidates (friday-review, quarterly-value-review, metrics-updater)
can also be wired to run automatically on a cadence.

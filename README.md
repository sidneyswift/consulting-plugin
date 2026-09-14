# Skills — Reusable Capabilities

> Rule of the practice: **anything we do more than once becomes a skill.**

Each skill is a folder with a `SKILL.md` (frontmatter `name` + `description`, then steps).
Authored here → installed as a plugin → selected by the task and each skill's description.
See `_packaging/README.md` for setup, dependencies, and the editing lifecycle.

## Workspace and examples

The plugin contains procedures and illustrative assets. Business records, account credentials,
pricing, client limits, sender identity, and brand choices belong to the workspace using it.
Choose the workspace explicitly, or use the current project when that is unambiguous. Follow its
`AGENTS.md` and keep the existing `clients/`, `pipeline/`, `integrations/`, `signals/`, `content/`,
`library/`, and `business/` structure. Never search for another private checkout to fill gaps.

Resolve a skill's scripts, references, and assets from that installed skill's directory. Resolve
business inputs and generated outputs from the selected workspace. An installed plugin may be
read-only; write drafts, renders, dependency environments, and temporary work into the project or
a dedicated temporary directory instead.

Examples labeled **fictional** or **synthetic** teach format and reasoning. Their companies,
people, numbers, and commercial terms are invented and must not become claims in real work.
Real reports require primary evidence; real pricing, spending limits, and promises come from
the relevant account and executed agreement.

Brand fonts, colors, and signatures come from the workspace's `DESIGN.md` or the user's selected
brand brief. Existing theme assets are optional examples, with their original notices preserved.
Add your own approved fonts to your workspace's brand assets and reference them from that brief;
no change to the plugin's folder structure is required.

## Capability groups

**Spine / orchestration**
- `consulting-call-processor` — auto-manage loop: ingest any new material end to end
- `consulting-system-auditor` — reconcile filesystem ↔ CRM, surface a punch list

**Sales & pipeline**
- `consulting-lead-intake` — triage + qualify a new lead
- `consulting-discovery-analysis` — analyze a discovery call, qualify the buyer
- `consulting-pricing-builder` — three-tier options, 5-10x anchor
- `consulting-proposal-drafting` — situational-assessment proposal (content/structure)
- `consulting-proposal-designer` — branded 2-page proposal HTML→PDF (design + copy frameworks)
- `consulting-followup-sequencer` — timed follow-up cadence
- `consulting-objection-handler` — tailored objection responses
- `consulting-deal-stage-mover` — advance a deal, keep folders/board/CRM in sync

**Content flywheel**
- `consulting-content-extraction` — mine transcripts into insights + content
- `consulting-content-idea-generator` — multi-tweet test variants
- `consulting-content-drafter` — idea → publish-ready draft (AIDA + title formula)
- `consulting-content-recycler` — reuse winners: repost, re-share with context, fan an outlier into new formats
- `consulting-friday-review` — weekly content + system ritual
- `consulting-faq-builder` — recurring answer → canonical FAQ

**Client success**
- `consulting-client-onboarding` — stand up a won client
- `consulting-quarterly-value-review` — QBR that drives renewals + proof
- `consulting-testimonial-capture` — draft + request testimonials
- `consulting-case-study-builder` — delivered work → case study
- `consulting-expansion-spotter` — land-and-expand opportunities

**Business ops**
- `consulting-sow-generator` — SOW under the MSA
- `consulting-invoice-generator` — invoice per payment structure
- `consulting-metrics-updater` — refresh dashboard + metrics
- `consulting-ip-register-updater` — log reusable IP

**Positioning & meta**
- `consulting-positioning-refiner` — sharpen the message
- `consulting-market-scanner` — niche intel + buying signals
- `consulting-skill-packager` — bundle skills into an installable plugin

**Visual & video**
- `consulting-tasteful-design` — house look-and-feel north star (palette, type, spacing, anti-AI-slop) that every visual skill defers to
- `consulting-hyperframes-video` — make any video / animation / motion graphic; HeyGen's HyperFrames toolkit folded into one house skill (11 workflow `modes/` + 6 `engine/` packs), renders video from HTML via `npx hyperframes`

## Updating and sharing

This repository is already an installable `consulting-os` plugin. Editing these files updates
this checkout. Installed copies update through their plugin manager; vendored copies in another
repository need a separate reviewed update. Neither a skill edit nor a version bump publishes it.

The `consulting-*` names remain stable so existing workspace routines keep resolving them.
Moving capabilities into another plugin is a separate packaging step, including that repository's
manifest, naming, dependency, and publication checks.

## Recoup media identity

Version 1.8.0 binds house media to Recoup Sky. The canonical reviewed distribution lives in
`skills/consulting-tasteful-design/brand/`, with source revision, exact asset hashes, font notices,
Finals references and a portable staging helper. Six independent media skills carry generated copies.
After updating the canonical package, run `python3 scripts/sync_brand.py`; verification uses
`python3 scripts/sync_brand.py --check` and `node --test tests/brand.test.mjs`.
See the brand GUIDE.md for client overrides and private output ownership. No history or private
business evidence belongs in a public brand package. Existing optional vendor fonts are retained.

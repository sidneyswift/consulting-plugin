---
name: consulting-product-engine
description: Engine B of the demand engine — turn shipped, user-facing product work (merged PRs / releases) into a staged idea bundle (article + LinkedIn post + email + image(s) + meta.yml, same shape as Engine A), grounded and cited to the PRs, never auto-sent. This is the build->content half of the flywheel (Engine A is calls->content). It rides the nightly pipeline: the extract half (PRs -> product-update signals) runs in ingestion, the draft half (signal -> gated bundle) runs in the content phase. Source = the public recoupable org, tokenless (B1 resolved). Use on "turn our shipped PRs into content", "announce what we shipped", "run the product engine".
---

# Consulting Product Engine (Engine B — product → feature content)

Engine A turns calls/insights into thought leadership. **Engine B turns shipped product work into
demand.** Every PR that ships a user-facing change is a **signal** (`source.type: pr`); this skill
turns those signals into the feature-announcement formats Sid sent by hand to Recoup users in 2025
(`library/email-templates/email-feature-announcement.md` — 7 real, proven sends), now automated and
**staged for approval, never auto-sent**.

Same **idea-bundle shape** and same **approval queue** as Engine A — a product update is just a bundle
whose `source` is a PR/release instead of a call.

> **Status:** 🟡 logic scaffolded; **source connector ✅ built** (`integrations/github/_work/pull_prs.py`,
> tokenless; **B1 resolved** — public `recoupable` org). Engine B rides the
> existing 3-phase pipeline: its **extract half** (pull → filter → cluster → cite → write `product-update`
> signals) runs in **ingestion (phase 1)**; its **draft half** (signal → gated bundle) runs in the
> **content phase (phase 3)**, where a fresh product-update jumps the queue. One sample bundle built + gated
> (`content/03-drafts/2026-07-01-agent-sends-email`). Design: `docs/plans/2026-06-30-demand-engine-restructure-spec.md` §"Engine B".

## Prerequisite — the source connector (built; runs in ingestion)
The **extract half** runs inside `consulting-nightly-ingestion` (phase 1): reads merged PRs from the
**public `recoupable` org** via `integrations/github/_work/pull_prs.py` (GitHub Search API,
**unauthenticated — no token**; optional read-only `GITHUB_TOKEN` only for rate-limit headroom). GitHub owns
truth; the repo keeps only the distilled `product-update` signals + a `LAST_SYNCED`. **Watches the product
org, not this consulting-os repo.** See `integrations/github/AGENTS.md` (B1 resolved).

## The flow (two halves, two phases)
**Extract half — runs in INGESTION (phase 1); writes signals:**
```text
pull merged PRs since integrations/github/_work/LAST_SYNCED   (pull_prs.py — tokenless)
  → FILTER to user-facing changes   (drop refactors/chores/deps/tests/infra; keep feat(...))
  → CLUSTER related PRs into ONE feature   (5 PRs building one capability = one announcement, not five)
  → JUDGE "shippable to users" + write a cited "what shipped, for users" line   (traces to PR/commit)
  → write a `product-update` SIGNAL to signals/   (type: product-update, source.type: pr, locator: PR#/sha)
```
**Draft half — runs in the CONTENT phase (phase 3); consumes a product-update signal:**
```text
pick a product-update signal   (fresh ones JUMP THE QUEUE — feature news is perishable)
  → fan the FULL bundle (same shape as Engine A):
       meta.yml · article.md (feature story + lesson) · linkedin.md · email.md (feature-announcement, deep-link CTA)
       · images/ (hero image1.png leads the email) · video/ (optional)
  → gate every text format (reviewer then editor), then stage in content/03-drafts/<date>-<feature-slug>/
  → STOP for Sid approval (never auto-send)
```

## The hard part: PR → "user-facing feature" (do in order)
Most PRs are not announceable. The judgment, in order:
1. **Filter out** refactors, chores, dependency bumps, tests, infra, internal-only changes.
2. **Cluster** related PRs into one feature — don't announce the same capability five times.
3. **Judge "shippable to users"** — is it live / flag-on, and does it change what a user can *do*? Tie
   to release notes / tags when present.
4. **Write one line: "what shipped, for users," cited to the PRs.** Evidence discipline (root
   `CLAUDE.md`): the claim traces to the PR/commit (PR #, commit sha, or a verbatim title), never
   invented — same bar as Engine A's grounding. **Build/commit activity ≠ adoption** — announce what
   shipped, not usage you can't prove.

`⟡ DECISION B2: the filter signal — a `user-facing` label we add in the product repo (cleanest) vs
title/path heuristics vs only release tags.`

## Per-feature formats (reuse what exists)
- **`article.md`** — the pillar: the feature story + the portable lesson (blog-length, `consulting-copy-writer`
  social-article style). The post + email derive from it, same as Engine A. (The "agent sends email" sample
  is a good template: the 38%-empty war story → the fix → the general lesson.)
- **`linkedin.md`** (+ optional `x.md`) — build-in-public / demo post.
- **`email.md`** — the **feature-announcement format** (`library/email-templates/email-feature-announcement.md`):
  subject = the outcome ("It booked a guest in 5 minutes"), open with the new power, **prove it** (a live
  test / demo / 2-3 copy-paste prompts), **one deep-link CTA into the product**, founder sign-off. Strip
  em-dashes/hype per `consulting-copy-writer`.
- **`images/`** — `consulting-article-illustrator` (gpt-image-2 via the Higgsfield MCP when unattended):
  a **hero `image1.png`** the email leads with and the article uses, plus inline figures as the article warrants.
- **`video/`** — optional: `consulting-hyperframes-video` explainer/demo (or a provided screen capture).
- Edit gates — **every audience-facing text format.** Run `consulting-copy-reviewer` **then**
  `consulting-copy-editor` on **each** of `article.md` / `linkedin.md` / `email.md` (+ `x.md` if used),
  reviewer before editor. Use the right ICP per format: the **Recoup customer** for `email.md`; **Sid's
  operator/builder ICP** for `article.md` / `linkedin.md` / `x.md`. Record which gates ran in the bundle's
  `gates:` field. (Scored ≠ gated — the automated scorer is the floor; the reader/editor passes are the bar.)

## Audience & dispatch (reuses the email engine)
- The feature-email is **broadcast/nurture** → routes via the existing matrix (`email/AGENTS.md`):
  product updates → customers + warm + (gated) targets; segments resolve via live Attio **at dispatch**.
- Dispatch rail = `integrations/gmail/_work/create_draft.py` (drafts only). **Never auto-send.**
- `⟡ DECISION B3: add feature-announcement as email-atomizer format #12, or Engine B owns it directly
  (today the atomizer has formats 06-11; feature-announcement is a swipe file being promoted to a format).`

## Output — one idea bundle (same shape as Engine A)
```
content/03-drafts/<YYYY-MM-DD>-<feature-slug>/
  meta.yml     id · title · date · engine: B · source (the PRs) · formats[] each status: draft · gates
  article.md   the pillar — the feature story + the lesson
  linkedin.md  build-in-public / demo post (x.md optional)
  email.md     the feature-announcement (deep-link CTA into the product)
  images/      image1.png = hero (leads the email + article), then image2.png…
  video/       optional explainer / demo clip
```

## Rails
1. **Never auto-send / auto-publish.** Everything stages at `status: draft`; Sid approves per format.
2. **Grounded, cited to the PR.** Every "what shipped" claim carries a PR #/commit sha; unproven → don't
   ship it. Announce shipped capability, never claimed adoption.
3. **One feature = one bundle.** Cluster; don't spam a bundle per PR.
4. **Voice = `consulting-copy-writer`**; edit gates before staging.
5. **Watches the product repo, not consulting-os.**

## Open decisions
- **B1 — ✅ RESOLVED (2026-06-30):** watch the **public `recoupable` org**, read **tokenless** via
  `pull_prs.py`. No PAT/App needed (optional read-only token only for rate-limit headroom).
- **B2** — the user-facing filter signal. Grounded default from the real PR stream: **conventional-commit
  prefix** — keep `feat(...)`; drop `chore`/`test`/`ci`/`build`/`refactor`/`docs` + bare "Test" PRs; treat
  `fix:` as user-facing only if it names a user-visible symptom. Confirm, or add a `user-facing` PR label.
- **B3** — feature-announcement as email-atomizer format #12 vs. Engine B owns it directly.

## New pieces (build order)
1. `integrations/github/` — the merged-PR pull (`pull_prs.py`) + `LAST_SYNCED`. **✅ built + verified.**
2. This skill. **✅ scaffolded.**
3. Promote the feature-announcement swipe file → a reusable format. **✅ done.**
4. **Wired into the pipeline:** extract half in `consulting-nightly-ingestion`,
   draft half in `consulting-nightly-content`. First sample bundle done (`2026-07-01-agent-sends-email`).
   **Next:** lock B2 (filter heuristic) + B3 (atomizer format).

## Connection to `products/` (distinct, adjacent)
`products/` decides *what to build* (demand → score → ship); Engine B announces *what shipped*. They
meet at `source:` — a `products/05-shipped/` card or its PRs trigger Engine B; Engine B's engagement
(demo clicks, replies) feeds **revealed-demand signals back into `products/_signals.md`**. Neither owns
the other.

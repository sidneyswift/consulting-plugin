---
name: consulting-nightly-content
description: "Phase 3 of the nightly pipeline — the demand engine's post-first LinkedIn lane. After capture + janitor, pick a strong signal and stage one evidence-backed, LinkedIn-only post for review. Default to a failure, build-in-public scene, or concrete mechanism; never require an article, email, or image. Pillars are an optional weekly authority lane after a post has proved useful. Never publishes. Use on \"run the nightly content\", \"draft today's LinkedIn post\", or as the nightly content ritual."
---

# Consulting Nightly Content (post-first demand engine)

## Visual handoff

When this workflow creates or requests a rendered artifact, use `consulting-tasteful-design` and
the selected workspace DESIGN.md. House identity is Recoup Sky; explicit client/artist branding wins.
Pass brand/version, expression, format, reference IDs and output folder to the media skill. Its bundled
package supplies exact fonts/logos. Keep new derivatives in the current identity while preserving
historical evidence. Save editable source and brand.lock.json with the deliverable. Ordinary text
outputs stay text; a script is not a rendered video. Existing data dashboards retain their canonical
Recoup CSS during data updates. Do not publish private client work to the public Brand Studio.


**Workspace:** use the selected project and its `AGENTS.md`; keep existing entity folders and
Reality headings. Business paths below are relative to that project. Bundled resources are relative
to this installed skill; sibling capabilities resolve by their installed names. Never search another
private checkout for missing inputs. Use workspace identity, audience, pricing, and `DESIGN.md` fonts.
Local `_work` adapters and `evals` are optional workspace tools, not bundled dependencies. Check
presence and current help first; otherwise use an available connector for the same scoped operation.
If neither exists, report that step incomplete. For missing scorers, perform the stated checks and
label the result manual/unscored; never invent a numeric score or successful provider action.

Capture turns calls, product work, and failures into signals. This skill turns the strongest signal into
one **native LinkedIn post** that a buyer can understand and forward without an article. Long-form is
optional and downstream: write a pillar only after a post proves the idea deserves expansion, or during
the separate weekly authority lane.

The engine drafts; **the owner publishes.** Quality over cadence.

## Default output — one LinkedIn-only bundle in drafts/
```
content/03-drafts/<YYYY-MM-DD>-<topic-slug>/    ← the idea is the unit (date + slug = identity)
  brief.md         the scene, evidence, mechanism, takeaway, and reader exit
  linkedin.md      the complete native post
  meta.yml         source, format, review state, and gates
```
The folder carries the identity. `article.md`, `email.md`, and `images/` are optional additions, never
prerequisites for a LinkedIn draft. Product-update signals may use their own announcement variant, but
must still produce a complete native post.

## Rails
1. **Never auto-publish.** Drafts only; the owner reviews + publishes via `consulting-linkedin-publisher` (Postbridge).
2. **Grounded, not fabricated.** Every claim traces to a real captured insight/transcript — carry the
   citation. Never invent a client name, number, or result; confirm before naming a client, or write generically.
3. **Voice = `consulting-copy-writer`** (no exceptions): no em-dashes, anti-slop list, specific, human. Read it.
4. **One reader gate, one edit maximum.** Run `consulting-copy-reviewer`, accept only clarity/evidence fixes, then one `consulting-copy-editor` pass. Prefer kill over a second rewrite; raw specificity beats polished abstraction.
5. **One post, not a compulsory fan-out.** Default output is `brief.md` + `linkedin.md` + `meta.yml`.
6. **Quality over volume.** One strong post on a weekday; a thin day → one-line report, no bundle.

## Steps
0. **Orient + find what's new.** Read the day's `business/ops/nightly-digests/<date>.md`. Gather unused
   **signals** — the **dated `signals/<YYYY-MM-DD>-*.md` files** with `status: new` (plus `evergreen` POVs
   not yet drafted into a published pillar); skip `used`/`archived` **and the meta files** (`AGENTS.md`,
   `_template.md`, `_index.md`, `_archive/` are NOT signals). (`content/_work/LAST_DRAFTED` is just a
   run-log now; per-signal `status` is the truth.) `git log` for today.

1. **Pick ONE signal** — the strongest, most specific unused signal (`status: new`, or an `evergreen` POV
   not yet published) with a real story / POV from an actual source. Dedup vs `content/04-published/` and
   existing `content/03-drafts/` (never rewrite a published pillar). Carry its `source` so the draft stays
   grounded. Slugify the topic and make the bundle folder `content/03-drafts/<YYYY-MM-DD>-<topic-slug>/`
   (date-first, so `drafts/` sorts chronologically).
   - **Fresh `product-update` signals jump the queue.** Ingestion writes `type: product-update` signals
     (cited to PRs) from the GitHub capture. Feature news is **perishable** — announce it while it's new —
     so a fresh product-update outranks evergreen insights for tonight's slot; insights fill otherwise.
   - **Branch on the signal's `type`.** Product updates use `consulting-product-engine` for the factual
     announcement shape. Insight signals default to one of: failure story, build-in-public result, or
     concrete mechanism. Both branches produce a native post first.

2. **Write `brief.md`.** Use the repository template. Name the buyer, live problem, scene, what broke or
   changed, primary evidence, mechanism, practical takeaway, and native reader exit. If the source cannot
   support a concrete scene or mechanism, stop with `Needs owner`; do not inflate it into prose.

3. **Write the LinkedIn POST.** Read `consulting-copy-writer` §social and
   `consulting-linkedin-post-architect`. Start at the beginning of the scene, not in the middle of an
   article argument. Deliver the full mechanism and takeaway in the post. Default to no outbound URL,
   no raw Calendly, no `recoupable.dev`, and no “read the article.” A native close may make the consulting
   relevance explicit or point to the owner's profile.

4. **Reader review + one edit.** Run `consulting-copy-reviewer` through the buyer named in `brief.md`.
   Require clear answers to: Who is this for? What changed? Why believe it? What can the reader do with
   it? Would a CEO forward it internally without an article link? Apply accepted clarity/evidence notes,
   then run one `consulting-copy-editor` pass. Kill rather than entering a second revision loop.

5. **Write the manifest, mark the signal, report, score, commit.** Write `meta.yml` with `id`, `title`,
   `date`, `engine`, source signal, `format: linkedin`, `status: draft`, and the two completed gates.
   Then set the consumed signal's `status: used` + `used_by:`
   the bundle path, and regenerate `signals/_index.md` (an `evergreen` insight stays evergreen — append
   the bundle to its `used_by` history instead). Write `business/ops/content-reports/<date>.md` (**Post ·
   Post gates · Skipped (why) · Needs owner**), run
   `python evals/content/score_run.py` (composite + flags at top), commit each draft why-first, stamp
   `content/_work/LAST_DRAFTED`, then stop.

## Notes
- **Post-first is the sales lane.** Expand proven posts into pillars; do not make pillars the price of admission.
- **Mine, don't manufacture.** Nothing worth a post → say nothing. The flywheel rewards signal, not cadence.
- Use the current scorer as a mechanical floor only. Booked ICP conversations and attributed meeting
  mentions are the learning signal; draft approval and likes are not revenue proxies.

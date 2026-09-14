# Packaging: this repo IS an installable plugin

This repo is a self-contained plugin **and** its own single-plugin marketplace, so it installs
directly from its GitHub URL — there's no build step and no `.plugin` artifact to produce.

## How it's wired
- `skills/<name>/SKILL.md` — one folder per skill (frontmatter `name` + `description`, then steps).
  The `SKILL.md` format is the same open standard across all three tools, so the skills are shared.
- `.cursor-plugin/marketplace.json` + `.cursor-plugin/plugin.json` — make it installable in **Cursor**.
- `.claude-plugin/marketplace.json` + `.claude-plugin/plugin.json` — make it installable in **Claude Code**.
- `.codex-plugin/plugin.json` + `.agents/plugins/marketplace.json` — make it installable in **Codex**.
  Codex uses a different layout: the manifest lives in `.codex-plugin/` and the marketplace catalog
  lives in `.agents/plugins/` (Codex also reads `.claude-plugin/marketplace.json` as a legacy fallback).
- All three manifests expose one plugin, **`consulting-os`** ("Consulting OS"), whose skills live in `skills/`.

## Add or change a skill
1. Create/edit `skills/<name>/SKILL.md` (rule of the practice: anything done 2+ times becomes a skill).
   Use `/skill-creator` to scaffold the frontmatter + steps.
2. Validate the changed helpers and run `python3 scripts/validate_plugin.py` from the plugin root.
3. When changing the package version, keep the three plugin manifests and the two marketplace
   metadata versions aligned. The Codex marketplace has no separate version field.
4. Commit. Publish the intended branch when authorized, then update installed or vendored copies
   through their own lifecycle. A private source commit does not update another repository.

## Install it
- **Cursor:** add the repo URL (`https://github.com/sidneyswift/consulting-plugin`) as a plugin
  source (plugins panel, or Team/Enterprise → Settings → Plugins → Import from Repo), then install
  **`consulting-os`**.
- **Claude Code:** add the same repo as a marketplace, then install the **`consulting-os`** plugin.
- **Codex:** use the plugin manager to add this repository's marketplace and install
  **`consulting-os`**. This repository supplies `.agents/plugins/marketplace.json` and
  `.codex-plugin/plugin.json`; use the installation interface supported by your installed app.
- Once installed, each skill auto-triggers by its `description` — no need to point at the file.

## Naming
Prefix practice skills with `consulting-` so they group together.

## Runtime inputs and dependencies

Text-only skills need the selected workspace and the sources relevant to their task. They do not
require a copy of the author's personal workspace. Read that project's operating instructions
before changing its records. Sibling skills are installed capabilities addressed by name, not
hardcoded paths into another computer's plugin cache.

Integration helpers under a workspace's `integrations/<provider>/_work/` are optional local
adapters, not files shipped by this plugin. Check the helper's presence and current command-line
interface before invoking it. Otherwise use an available authenticated connector for the same
scoped operation. If neither exists, identify the missing integration and leave the affected
step incomplete. Never substitute a bulk import for a missing scoped operation, or mark a send,
publish, ingestion, or sync successful without a provider receipt.

Provider credentials remain in the selected account's connector or project-scoped environment.
Do not request secret values in chat or commit them into skills. Account IDs, sender identity,
client limits, CRM schema, research sources, and privacy exclusions are runtime configuration.
Incoming material must satisfy that workspace's intake rules before it is saved or summarized.

Executable skills document their own requirements. Proposal rendering uses an explicitly prepared
Python renderer environment; video helpers require their declared Node/browser/media tools.
Install those environments outside the installed plugin. Run only the helpers needed for the task;
installing this plugin does not grant access to third-party accounts or trigger ingestion.

## Validation

`python3 scripts/validate_plugin.py` checks all discovered skill entrypoints, local package
metadata, manifest version parity, and Python/JavaScript/shell syntax. It does not execute provider
actions, install dependencies, or establish that a business example is safe to publish. Run the
focused behavioral checks supplied with changed executable helpers as well.

Before sharing a new snapshot, review the final file contents and any bundled asset terms.
Existing private Git history is not sanitized by editing today's examples. Publish reviewed
files through the destination's established process rather than exposing this repository's history.

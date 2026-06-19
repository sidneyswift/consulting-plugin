---
name: consulting-skill-packager
description: Publish or refresh the consulting-os plugin so it installs from its GitHub URL. Use on "package the skills", "publish the plugin", "ship the skills", or after authoring/editing a skill so the change goes live.
---

# Consulting Skill Packager

This repo is already a plugin **and** its own marketplace (`.cursor-plugin/` and `.claude-plugin/`
manifests). "Packaging" just means validating and pushing — there is no `.plugin` artifact to build.

## Steps
1. Validate each `skills/{name}/SKILL.md` has valid frontmatter (`name` + `description`) and clear steps.
2. Confirm the manifests still list the plugin and point `skills` at `skills/`
   (`.cursor-plugin/` for Cursor, `.claude-plugin/` for Claude Code).
3. Bump `version` in the `plugin.json` + `marketplace.json` files if you're publishing a change.
4. Commit and push to GitHub — the repo URL is the install source.
5. Tell the user how to install/refresh: add the repo URL as a plugin source (Cursor) or marketplace
   (Claude Code) and install `consulting-os`; existing installs pick up changes on refresh.

Full lifecycle: `_packaging/README.md`.

# Skills — Reusable Capabilities

> Rule of the practice: **anything we do more than once becomes a skill.**

Each skill is a folder with a `SKILL.md` (frontmatter `name` + `description`, then steps).
Skills replace one-off prompts — they can trigger automatically once installed as a plugin.

## Current skills
- `consulting-content-extraction/` — mine transcripts into insights + content
- `consulting-discovery-analysis/` — analyze a discovery call, qualify the buyer
- `consulting-proposal-drafting/` — draft a situational-assessment proposal

## Authoring → installing
Author here → package with the `create-cowork-plugin` skill → push to GitHub → install into the
workspace → it triggers non-deterministically. Full lifecycle: `_packaging/README.md`.

When you notice a repeated task, propose turning it into a skill (use `/skill-creator`).

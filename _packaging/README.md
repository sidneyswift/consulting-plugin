# Packaging skills into an installable plugin

These skills live in the workspace as plain folders so they're easy to author and version.
To make them trigger **non-deterministically** inside the Claude workspace, they must be
packaged as a plugin and installed.

## Lifecycle
1. **Author** a skill here: `skills/<skill-name>/SKILL.md` (frontmatter `name` + `description`, then steps).
   Trigger to create one: anything you've done 2+ times. Use `/skill-creator` (or the
   `create-cowork-plugin` skill) to scaffold it.
2. **Bundle** the `skills/` folder into a plugin (a `plugin.json` + the skills).
   Use the `create-cowork-plugin` skill to produce a `.plugin` file.
3. **Publish** to GitHub as a plugin/marketplace repo (so it's versioned and shareable).
4. **Install** the plugin into the Claude workspace from the marketplace.
5. Once installed, the skill auto-triggers by its `description` — no need to point at the file.

## Naming
Prefix practice skills with `consulting-` so they group together in the marketplace.

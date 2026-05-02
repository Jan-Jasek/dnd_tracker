# DND Tracker Agent Rules

This repository is a source-of-truth workspace for a custom DND world, campaign management, lore, faction simulation, session preparation, maps, encounters, and generated assets.

## Source Of Truth

- `.rulesync/` is the source of truth for agent-facing rules and skills.
- `AGENTS.md`, `CLAUDE.md`, `.codex/`, and `.claude/` are generated from `.rulesync/`.
- Campaign canon lives in repository Markdown under `data/<WorldName>/`.
- `data/` is the Obsidian vault root and may contain multiple worlds.
- Tooling, imports, generators, templates, and agent configuration stay outside `data/`.
- Drafts, imported notes, and generated ideas are not canon until promoted.

## Campaign Content Rules

- Use Markdown with YAML frontmatter for campaign content.
- Every canon file should have `id`, `type`, and `status`.
- Prefer stable lowercase dotted IDs like `world.veiled-sun`, `campaign.city-of-ash`, or `faction.crimson-ledger`.
- Preserve contradictions as notes instead of silently overwriting them.
- Separate public belief, hidden truth, and contested interpretation when useful.
- Favor playable consequences over encyclopedia prose.

## Workflow Rules

- Put OneNote exports under `imports/onenote/raw/` before classification.
- Put brainstorming under `ideas/` unless it is being promoted into canon.
- Put polished world material under `data/<WorldName>/`, organized into sections such as `History/`, `Places/`, `Factions/`, `Organisations/`, `Campaigns/`, `People/`, `Pantheon/`, and `Notes/`.
- Major player choices should create timeline events and consequences.
- Faction changes should update relevant faction files, campaign state, and timeline events.
- Generated maps, images, and other assets should include a nearby Markdown brief explaining purpose, prompts, and canon status.

## Validation

- Run `make static` before publishing broad structural changes.
- Run `make ai_generate` after editing `.rulesync/`.
- Run `make ai_check` to detect drift between `.rulesync/` and generated agent files.

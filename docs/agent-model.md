# Agent Model

Agents and skills should support the campaign workflow without becoming the source of truth for lore.

## Proposed Skills

- `world-builder`: Develops custom world canon from questions, constraints, themes, and existing notes.
- `campaign-librarian`: Maintains structure, IDs, links, duplicate detection, and canon hygiene.
- `session-prep`: Builds session plans from campaign state, active clocks, NPCs, and locations.
- `faction-simulator`: Advances factions and clocks based on goals, pressure, and player actions.
- `lore-consistency`: Checks new material against accepted canon.
- `encounter-builder`: Creates combat, social, exploration, and investigation encounters.
- `map-brief-generator`: Creates map prompts, edit briefs, room keys, and detail passes.
- `import-onenote`: Classifies OneNote exports into structured Markdown drafts.
- `obsidian-export`: Adds Obsidian-oriented tags, links, indexes, and graph-friendly organization.

## Source Of Truth

- Campaign lore lives in repository Markdown under `data/<WorldName>/`.
- Agent behavior and workflow rules live in `.rulesync/` and generate via `make ai_generate`:
  - `AGENTS.md` (open standard)
  - `CLAUDE.md`, `.claude/` (Claude Code)
  - `.codex/` (OpenAI Codex CLI)
  - `.cursor/` (Cursor / Grok)
- Generated content is a proposal until promoted.

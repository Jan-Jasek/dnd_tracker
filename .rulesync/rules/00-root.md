---
root: true
targets:
  - "*"
globs:
  - "**/*"
---

# DND Tracker Agent Rules

This repository is a source-of-truth workspace for a custom DND world, campaign management, lore, faction simulation, session preparation, maps, encounters, and generated assets.

## Source Of Truth

- `.rulesync/` is the source of truth for agent-facing rules and skills.
- Generated from `.rulesync/` via `make ai_generate`:
  - `AGENTS.md` — open Agents.md standard
  - `CLAUDE.md`, `.claude/` — Claude Code
  - `.codex/` — OpenAI Codex CLI
  - `.cursor/` — Cursor / Grok
- Campaign canon lives in repository Markdown under `data/<WorldName>/`.
- `data/` is the Obsidian vault root and may contain multiple worlds.
- Tooling, imports, generators, templates, and agent configuration stay outside `data/`.
- Drafts, imported notes, and generated ideas are not canon until promoted.

## Setting Identity

- **Universe:** Weaving (_Tkaní_) — the whole woven from the Weave, the primal energy that flows through all planes via the Paths
- **Material plane:** Eloran — largely sealed from the Weave since Orion's working; primary campaign setting
- **Fey plane:** name TBD — dominated by Erathon; saturated with tainted Weave
- **Shadow plane:** The Hollow — a hollow reflection of Eloran, created as a byproduct of Erathon's attempted merger
- **Primal energy:** the Weave (_Předivo_) — the underlying substance of all things; once unified across the Weaving; shattered by the Sundering into isolated, hungry pockets
- **The Paths:** channels that carry Weave between planes; broken or corrupted since the Sundering
- **The Accord:** the pre-Sundering era when the Weave flowed freely and the universe was harmonious
- **The Sundering:** the cataclysm that shattered the Weave; cause unknown
- **Erathon:** a pre-Sundering being, trapped in a pocket of Weave overlapping the Fey plane; imprisoned on Eloran by Orion; now fragmenting back into the world
- See `data/Eloran/Cosmology.md` for the full cosmological account

## Universe Ontology

The setting is organized as a strict hierarchy. Every content file belongs to exactly one layer:

```
Universe (e.g. Eloran)
└── Planes (Material World, Feywild, Shadowfell, Divine Realms…)
    └── Regions (geographic areas within a plane)
        └── Places (cities, towns, dungeons, landmarks)
            └── Districts / Sub-locations
Pantheon (gods; spans all planes; child of Universe)
Factions (political/military groups; child of a Plane or Region)
Organisations (guilds, orders, companies; child of a Plane or Region)
People (NPCs; linked to their plane, faction/org, and primary location)
Campaigns (narrative arcs; child of Universe; reference Planes/Places/People)
└── Sessions
└── Player Characters
└── Timeline (campaign-specific events)
Timeline (also exists at Universe level and per-Plane level)
```

- **Universe hub** (`data/<Universe>/<Universe>.md`) is the graph root. Everything links back to it.
- The material world/planet and each additional plane each have their own hub file under `Planes/`.
- `README.md` should not be used as a hub or index inside `data/`. Use `<Universe>.md` or `<PlaneName>.md` instead.

## Content File Rules

- Use Markdown with YAML frontmatter for campaign content.
- Every canon file must have `id`, `type`, `status`, and `universe` fields.
- Plane-specific files must also have a `plane` field. Location files add `region`. People files add `faction` or `org` where applicable.
- Prefer stable lowercase dotted IDs: `universe.weaving`, `plane.eloran`, `faction.triple-coalition`, `place.orestor`, `character.eirys`.
- Preserve contradictions as notes instead of silently overwriting them.
- Separate public belief, hidden truth, and contested interpretation when useful.
- Favor playable consequences over encyclopedia prose.
- Czech is the language of narration at the table. Write canon prose in English, but give every proper name (people, places, organisations, epithets) its Czech form, e.g. `# Darkenwold (Temnohvozd)` or an `aliases:` entry.
- Write in-character quotes, citations, and in-world texts (letters, newsletters, inscriptions) in Czech.

## Present-State Writing

Canon files describe the **current state of the world**. They are not a changelog of DM or agent decisions.

When a fact is updated:

- Rewrite the passage as the new present truth.
- Do not keep traces of the discarded draft: `no longer`, `rather than X`, `used to be`, `this replaces`, `previously`, `not TBD anymore`, `**Resolved:** Y rather than X`.
- In-world historical change (wars, schisms, coups, deaths) belongs in Timeline and origin sections — that is story. Editorial memory of "we used to say X" does not.
- If a superseded draft must be kept, move it to `ideas/` or mark `status: contradicted`. Do not leave a palimpsest in canon prose.

`Notes/Open Questions` lists **unresolved** items only. Once decided, delete the question and write the answer as present fact in the relevant file.

## Obsidian Graph Linking Conventions

These rules ensure the Obsidian graph is navigable and centers on the right nodes:

1. **Hub files link down.** The universe hub links to each Plane hub, Pantheon, and Campaigns index. Each Plane hub links to its Regions, Factions, Organisations, People, and Timeline.
2. **Content files link up.** Every file includes a `> Part of: [[Parent]]` line (or `parent:` frontmatter) pointing one level up the hierarchy.
3. **People link sideways.** People files link to their primary location, faction or org, and any campaigns they appear in.
4. **Factions and Orgs link to their key people and key locations.**
5. **Timeline entries link to all people, places, and factions involved in that event.**
6. **Campaigns link to the universe hub, the planes/places they occur in, and all key NPCs and factions.**
7. **Do not create orphan files.** Every new file must link to at least one existing file and be linked from at least one existing file on creation.

## Timeline Structure

There are three timeline scopes — all three may coexist and cross-reference each other:

- **Universe timeline** (`data/<Universe>/History/Timeline.md`): cosmological and world-age events spanning all planes — creation, god-wars, extinction events, planar rifts.
- **Plane timeline** (`data/<Universe>/Planes/<Plane>/History/Timeline.md`): events scoped to that plane — wars, empires, migrations, magical catastrophes.
- **Campaign timeline** (`data/<Universe>/Campaigns/<Campaign>/Timeline.md`): events from play — session outcomes, player decisions, NPC state changes.

Timeline entries should link to the people, places, and factions they involve.

## Workflow Rules

- Put OneNote exports under `imports/onenote/raw/` before classification.
- Put brainstorming under `ideas/` unless it is being promoted into canon.
- Put polished world material under `data/<Universe>/`, organized by: `Planes/`, `Pantheon/`, `Factions/`, `Organisations/`, `People/`, `Campaigns/`, `History/`, `Notes/`. Place-specific content lives under `Planes/<PlaneName>/Places/` and `Planes/<PlaneName>/Regions/`.
- Major player choices should create timeline events and consequences.
- Faction changes should update the faction file, any linked campaign state, and the relevant timeline.
- Generated maps, images, and other assets should include a nearby Markdown brief explaining purpose, prompts, and canon status.
- Images referenced from canon must live inside `data/` (e.g. `data/<Universe>/Maps/`) and be embedded with `![[file]]` so Obsidian displays them; files under `imports/` are outside the vault.

## Validation

- Run `make static` before publishing broad structural changes.
- Run `make ai_generate` after editing `.rulesync/`.
- Run `make ai_check` to detect drift between `.rulesync/` and generated agent files.

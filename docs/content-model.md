# Content Model

The repository uses Markdown for readable content and frontmatter for structured metadata.

`data/` is the Obsidian vault root. Each world should be organized under `data/<WorldName>/`.

## Core Types

- `world`
- `campaign`
- `adventure`
- `session`
- `scene`
- `faction`
- `person`
- `location`
- `item`
- `event`
- `rumor`
- `quest`
- `encounter`
- `map`
- `timeline`
- `clock`
- `decision`
- `consequence`

## Frontmatter Conventions

Use stable IDs:

```yaml
id: faction.example
type: faction
status: draft
```

Prefer lowercase dotted IDs:

```text
world.veiled-sun
campaign.city-of-ash
faction.crimson-ledger
person.captain-varek
location.eastgate
event.ledger-spy-killed
```

## Linking

Use Markdown links for human navigation and IDs for agent-readable references.

```md
See [Captain Varek](../characters/captain-varek.md).
```

```yaml
related:
  - person.captain-varek
  - faction.ivory-watch
```

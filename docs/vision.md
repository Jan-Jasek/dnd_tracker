# DND Campaign Manager Vision

This repository is the canonical workspace for building, managing, simulating, and preparing a custom DND world and its campaigns.

The frontend is intentionally secondary. Obsidian, OneNote exports, a future web app, or a Codex workflow should all read from and write back to the same durable campaign files.

`data/` is the Obsidian-facing vault root. Each world lives under its own folder, such as `data/Eloran/`.

## Goals

- Preserve campaign canon in readable Markdown under `data/<WorldName>/`.
- Keep generated ideas separate from accepted canon.
- Support structured worldbuilding for a custom setting.
- Track player actions and their consequences.
- Simulate active factions, clocks, timelines, and city-scale change.
- Prepare sessions, encounters, maps, rumors, NPCs, and locations from current campaign state.
- Make future export to Obsidian straightforward.

## Non-Goals For Now

- Building the final frontend.
- Fully automating world simulation before the lore model exists.
- Importing OneNote content before templates and canon policy are defined.
- Treating generated content as canon without review.

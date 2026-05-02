---
name: map-generate
description: Use when generating a visual map image from a completed map brief — city, district, region, or continent — using Gemini image generation. Run after /map-design has produced a brief.
---

# Map Generate

Use this skill to turn a finished map brief into a visual asset and attach it back to the canon file.

## Prerequisites

- A map brief file must exist at `data/<World>/Maps/<name>.md` with a filled `## Generation Prompt` section.
- If no brief exists, run `/map-design` first.

## Workflow

1. Read the map brief. Extract the `## Generation Prompt` and the `## Required Features` sections.
2. Select a visual style appropriate to the map scope:
   - **City / district**: top-down ink illustration, labelled districts, hand-drawn cartographic style
   - **Region**: painted parchment map, terrain features, road network, city markers
   - **Continent**: full political map, color-coded territories, coastlines, mountain ranges, major cities
3. Build the final image prompt (see Prompt Construction below).
4. Generate the image using the `compound-engineering:gemini-imagegen` skill.
5. Save the asset to `data/<World>/Maps/assets/<name>.<ext>`.
6. Update the map brief frontmatter: add the path to `asset_paths`.
7. Add an `## Edit Notes` entry recording the prompt used and the date.

## Prompt Construction

Combine three elements into one dense paragraph:

1. **Style anchor** — art style, medium, color palette, rendering quality
2. **Scene content** — extracted from the brief's Generation Prompt verbatim, then tightened
3. **Technical constraints** — orientation, label style, compass rose if needed, what to exclude

Example structure:
> "Top-down hand-drawn ink map on aged parchment, slightly yellowed, fine crosshatching. [Scene content from brief]. No grid lines. Labelled in a serif font. Compass rose in lower-right corner. No modern elements."

## Style Reference by Scope

| Scope | Style Anchor |
|-------|-------------|
| City | Top-down ink illustration, isometric optional, aged parchment |
| District / neighborhood | Street-level perspective map, detail-dense, faction colors |
| Region | Painted watercolor terrain map, illustrated mountains and forests |
| Continent | Classical political map, solid territory colors, coastline focus |

## Asset Naming

`data/<World>/Maps/assets/<world-id>-<location-id>-<scope>.<ext>`

Examples:
- `eloran-orestor-city.png`
- `eloran-meredie-region.png`
- `eloran-continent.png`

## After Generation

- If the image has errors or missing features, note them in `## Edit Notes` and regenerate with a revised prompt.
- Do not overwrite the previous asset — append a version suffix (`-v2`, `-v3`).
- Promote the brief to `status: canon` only after the DM reviews and approves the image.

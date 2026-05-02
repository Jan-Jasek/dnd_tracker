---
name: map-design
description: >-
  Use when designing the content of a city, region, or continent map —
  districts, geography, faction control zones, landmarks, secrets, encounter
  areas, and canon gaps — from existing world lore or from scratch.
---
# Map Design

Use this skill to produce a structured map brief: the authoritative written description of a place that drives both play and future visual generation.

## Workflow

1. Identify the map scope: city, district, region, or continent.
2. Read all relevant canon files — location, factions, history, timeline — before inventing anything.
3. Separate what is canon, what is candidate, and what is an open question the DM must decide.
4. Build the map in layers (see below). Do not collapse unknown areas into invented detail.
5. Flag every gap explicitly rather than filling it with generic fantasy content.
6. Write or update a map brief file using `templates/map.md` under `data/<World>/Maps/`.
7. Mark the file `candidate` until the DM promotes it to `canon`.

## Map Layers

Work through each layer in order. A layer can be left partial if the canon does not support it yet.

### 1. Geography
- Natural features: rivers, coastlines, hills, forests, roads, walls
- Scale and orientation
- What terrain shapes movement, trade, and conflict

### 2. Zones / Districts
- Named areas with distinct character, function, or control
- Who lives here, who passes through, what activity is normal
- Boundaries — hard (walls, rivers) or soft (culture, fear, class)

### 3. Faction Control
- Which faction controls or contests each zone
- Visible presence: guards, signs, colors, checkpoints, shrines
- Hidden presence: safe houses, informants, tunnels, dead drops
- Contested or transitional zones — mark explicitly

### 4. Key Locations
- Named buildings, squares, landmarks with playable purpose
- Each location should have: a function, who is here, and one hook or secret
- Do not list generic locations (taverns, markets) unless they have a specific name or role

### 5. Secrets and Hidden Layer
- Things a player could discover through investigation or faction trust
- Underground, rooftop, or off-map extensions
- What public belief is wrong about this place

### 6. Encounter Density
- Where combat, social tension, or chase scenes naturally happen
- Patrol routes, choke points, crowd density, sightlines
- This feeds directly into the Generation Prompt

## Output

Produce or update a map brief at `data/<World>/Maps/<name>.md` with:

- Filled frontmatter: `id`, `type: map`, `status: candidate`, `world`, `location`, `asset_paths: []`
- All six layers above, even if some sections are marked `# Open Questions`
- A `## Generation Prompt` section with a dense, scene-setting paragraph ready for `/map-generate`
- An `## Open Questions` section listing every gap that blocks canon promotion

## Output Bias

Favor:
- Specific named places over generic zone descriptions
- Faction tension visible in the geography
- Secrets that reward player investigation
- Terrain that creates tactical or social constraints
- Contradictions preserved, not resolved

Avoid:
- Inventing canon the DM has not confirmed
- Symmetric or "balanced" layouts that feel designed rather than grown
- Filling open questions with placeholder fantasy content
- Maps that have no faction pressure or hidden layer

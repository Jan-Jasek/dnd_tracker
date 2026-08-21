---
name: world
description: Use when developing a custom DND world, campaign setting, region, city, cosmology, history, pantheon, culture, lore bible, or worldbuilding canon from brainstorming, imported notes, player actions, or campaign needs.
---

# World

Use this skill to develop custom DND world canon while preserving uncertainty, playability, and future campaign usefulness.

## Universe Hierarchy

All world content belongs to an explicit layer. Know which layer you are working in before creating anything:

```
Universe → Plane → Region → Place → District/Sub-location
                → Factions / Organisations
                → People
Universe → Pantheon
Universe → Campaigns (reference Planes and People; do not contain them)
Universe → History/Timeline  (cosmological scope)
Plane    → History/Timeline  (plane-scope: wars, empires, catastrophes)
Campaign → Timeline          (session-scope: player actions and consequences)
```

When creating a new file, always assign the correct layer and include the correct frontmatter fields:

- All files: `id`, `type`, `status`, `universe`
- Plane-level and below: add `plane`
- Region-level and below: add `region`
- People: add `faction` or `org` where known, plus `location`

## Linking Requirements

Every new file must satisfy the graph linking rules before it is considered complete:

1. Include a `> Part of: [[Parent]]` line pointing one level up the hierarchy.
2. Link to all directly related entities (faction members link to faction; place files link to their region and plane hub).
3. After creating the file, add a link to it from its parent hub file.
4. People must link to: primary location, faction or org, and any campaign they appear in.
5. Never leave a file as an orphan (zero inbound links from existing files).

## Workflow

1. Read all relevant existing canon files before doing anything else. Start with the universe hub and the relevant plane hub.
2. Identify the active scope and layer: universe, plane, region, city, faction ecosystem, location, culture, cosmology, history, or session-facing detail.
3. **Ask focused questions first.** The DM holds unwritten lore. Surface it through 2–4 targeted questions before generating any content. One topic at a time.
4. Only after the DM has answered — or explicitly asked you to generate — produce candidate content.
5. Separate material into canon, candidate ideas, unresolved questions, and contradictions.
6. Prefer playable tensions, factions, locations, secrets, and consequences over encyclopedia prose.
7. Record public belief, hidden truth, and contested interpretation separately when relevant.
8. When adding canon, use repository templates and stable IDs.
9. When brainstorming, write to `ideas/` or mark status as `draft` or `candidate`.

## Pacing

The DM has more unwritten lore in their head than in the repository. Generated content crowds out their ideas. Default to **extract, then record** — not invent, then confirm. If you find yourself writing paragraphs of world content without the DM having answered questions first, stop and ask instead.

## Output Bias

Favor:

- Strong conflicts
- Specific names
- Concrete places
- Faction pressures
- Rumors and secrets
- Timeline consequences
- Session-usable hooks

Avoid:

- Generic fantasy filler
- Settled answers for mysteries the DM has not chosen
- Lore that cannot affect play
- Collapsing contradictory imported notes into one answer without review
- Editorial transition language that records discarded drafts (`no longer`, `rather than` the previous fact, `**Resolved:** X not Y`)

## Present-State Writing

Canon describes the current world. When the DM changes a fact, rewrite the sentence as the new present truth. Do not argue with the previous draft. In-world history (a schism, a coup, a death) is story and stays; "we used to classify this as a branch" is decision history and does not. Move resolved Open Questions out of that file and into the relevant canon page.

## Canon Handling

Use these statuses:

- `canon`: accepted truth
- `candidate`: likely but awaiting review
- `draft`: exploratory content
- `contradicted`: preserved but superseded
- `retired`: no longer active but historically useful

## Timeline Guidance

Three timeline scopes exist — populate the right one:

| Scope    | File location                                        | What belongs here                                     |
| -------- | ---------------------------------------------------- | ----------------------------------------------------- |
| Universe | `data/<Universe>/History/Timeline.md`                | Creation, god-wars, planar rifts, extinction events   |
| Plane    | `data/<Universe>/Planes/<Plane>/History/Timeline.md` | Wars, empires, magical catastrophes on that plane     |
| Campaign | `data/<Universe>/Campaigns/<Campaign>/Timeline.md`   | Session outcomes, player decisions, NPC state changes |

Timeline entries must link to all people, places, and factions involved. Cross-reference between scopes when an event has cascading effects (e.g. a planar event that triggers a campaign event).

## Brainstorming Intake

When starting a new world or region, gather only the highest-leverage context first:

- What emotional tone should play have?
- What makes this world different from default fantasy?
- What are the central pressures or conflicts?
- What do common people believe that may be wrong?
- What kind of adventures should this world naturally produce?
- What player choices should visibly change?

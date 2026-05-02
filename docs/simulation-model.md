# Simulation Model

Simulation should begin with simple, reviewable state changes before becoming automated.

## Main Concepts

- Factions have goals, resources, enemies, allies, and clocks.
- Player actions create events and consequences.
- Time passing advances clocks.
- Visible consequences become rumors, scene changes, NPC behavior, and location updates.
- Hidden consequences remain tracked for future reveals.

## Faction Turn Output

A faction turn should produce:

- Player inputs considered
- Faction moves
- Clock changes
- New rumors
- Visible consequences
- Hidden consequences
- Hooks for the next session

## Simulation Principle

The simulator proposes changes. The DM accepts, edits, or rejects them before they become canon.

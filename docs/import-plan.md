# OneNote Import Plan

The OneNote import should happen after the content model and templates are stable enough to classify notes.

## Proposed Flow

1. Export OneNote notebooks or sections into a local format.
2. Store raw exports under `imports/onenote/raw/`.
3. Extract readable text and attachments into `imports/onenote/extracted/`.
4. Classify notes into `imports/onenote/classified/`.
5. Review and promote accepted content into `data/<WorldName>/`.

## Classification Buckets

- Canon candidate
- Draft idea
- Contradiction
- Duplicate
- Session note
- NPC
- Location
- Faction
- Adventure seed
- Timeline event
- Map or asset
- Rule or table

## Open Questions

- Which OneNote export formats are available locally?
- Are attachments, images, and maps important to preserve?
- Should imported notes keep their original notebook hierarchy?
- Should dates from OneNote metadata become timeline evidence?

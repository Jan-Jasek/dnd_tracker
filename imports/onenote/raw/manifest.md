---
id: import.onenote.manifest
type: import-manifest
status: draft
---

# OneNote Backup Manifest

Raw OneNote backups are kept in the local OneNote backup directory for now instead of being copied into this repository.

## Source Directories

- `/Users/janjasek/Library/Containers/com.microsoft.onenote.mac/Data/Library/Application Support/Microsoft User Data/OneNote/15.0/Backup/DnD_Eloran_Campaigns`
- `/Users/janjasek/Library/Containers/com.microsoft.onenote.mac/Data/Library/Application Support/Microsoft User Data/OneNote/15.0/Backup/DnD_Eloran_World`
- `/Users/janjasek/Library/Containers/com.microsoft.onenote.mac/Data/Library/Application Support/Microsoft User Data/OneNote/15.0/Backup/DnD_5E_Erebor`

## Notes

- `.one` files are binary MS-ONESTORE format backups.
- Text is stored as UTF-16LE; the original `strings`-based extraction missed most content.
- Use `generators/extract-onenote-images.py` for proper extraction (UTF-16LE text + JPEG/PNG carving).
- The 2026 `Dračí nezavislost` backup is the most current (21 images, 872 text strings).
- Old `strings`-based extractions use the `dnd-eloran-campaigns-*` filename prefix; new extractions use shorter slugs.

## Extraction status (DnD_Eloran_Campaigns)

| Section                        | Extracted                              | Images |
| ------------------------------ | -------------------------------------- | ------ |
| Dračí nezavislost (2026-04-26) | `dra-nezavislost-one-on-26-04-2026.md` | 21     |
| Dračí nezavislost (2023-03-01) | `dra-nezavislost-one-on-01-03-2023.md` | 11     |
| Lore                           | `lore-one-on-01-03-2023.md`            | 0      |
| Meredie                        | `meredie-one-on-01-03-2023.md`         | 0      |
| Orestor                        | `orestor-one-on-01-03-2023.md`         | 0      |
| Quick Notes                    | `quick-notes-one-on-01-03-2023.md`     | 0      |

Images are in `imports/onenote/images/`.

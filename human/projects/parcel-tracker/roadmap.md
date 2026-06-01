# parcel-tracker Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
| source | fact |
|---|---|
| `dev/legacy/dev/TROUBLESHOOTING.md` | ParcelsApp puo cambiare markup o rendere fragile il parsing diretto. Il tracker prova prima dati strutturati JSON/Next data. Se non trova un evento affidabile, usa un fallback sicuro su HTML/title/meta e crea una chiave stabi |
| `parcel_tracker.py` | status = clean_text(next((x for x in text_fields if clean_text(x)), "")) |

## Deferred Or Risky Work
- dev/legacy/dev/TROUBLESHOOTING.md: ParcelsApp puo cambiare markup o rendere fragile il parsing diretto. Il tracker prova prima dati strutturati JSON/Next data. Se non trova un evento affidabile, usa un fallback sicuro su HTML/title/meta e crea una chiave stabi

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.

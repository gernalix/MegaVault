# SuperContacts Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
| source | fact |
|---|---|
| `dev/legacy/dev/NEODOC.md` | ## Future Docs Rule |
| `dev/legacy/dev/NEODOC.md` | - No duplicate AI/human doc trees. No stale roadmap copies. Keep this file token-efficient. |
| `dev/legacy/dev/INDEX.md` | - Append future notes under the matching section in `dev/NEODOC.md`. |
| `tools/build-finalize.ps1` | push = "pending" |
| `tools/build-finalize.ps1` | telegram_apk = "pending" |
| `tools/build-finalize.ps1` | telegram_zip = "pending" |
| `tools/build-finalize.sh` | local current next |
| `tools/build-finalize.sh` | next=$((current + 1)) |
| `tools/build-finalize.sh` | printf '%s' "$next" > "$version_file" |
| `tools/build-finalize.sh` | log "Versione patch aggiornata: $next" |
| `tools/build-finalize.sh` | printf '%s\n' "$next" |
| `tools/guardrails/engine.py` | database_file = next( |
| `tools/guardrails/engine.py` | state_index = next((index for index, token in enumerate(columns[1:], start=1) if token in ADB_DEVICE_STATES), None) |
| `tools/tests/test_guardrails_engine.py` | device_test = next( |

## Deferred Or Risky Work
- tools/guardrails/engine.py: code="adb-ddmlib-timeout-non-blocking",
- tools/tests/test_guardrails_engine.py: self.assertEqual(warnings[0]["code"], "adb-ddmlib-timeout-non-blocking")
- dev/legacy/dev/NEODOC.md: - Pixel validation uses debug/deviceTest packages only; never overwrite the personal `com.supercontacts.app` install.
- dev/legacy/dev/NEODOC.md: - SQLite is primary storage. Core tables: `contacts`, `contact_fields`; related tables: events, initiatives, tags, backup metadata.
- dev/legacy/dev/NEODOC.md: - New contacts get `public_id = c-<uuid>`; migration v8 backfills old rows and indexes `public_id`.
- dev/legacy/dev/NEODOC.md: - Home search never displays photo path/filename/URI/storage internals. Photo field values are excluded from match metadata; phone matches are not rendered on Home.
- dev/legacy/dev/NEODOC.md: - v17: Real nationality field with local versioned country/nationality asset, live autocomplete, free-text fallback, ISO country code persistence, flag display, Room v10 migration, and wider field-description verification across displ
- dev/legacy/dev/NEODOC.md: - v15: Generic field descriptions with parent-bound add/edit/remove UI, localized EN/IT strings, Room v9 migration, parent-aware history events, and backup/import preservation.
- dev/legacy/dev/NEODOC.md: - Distance sorting still depends on saved coordinates and current device location permission.
- dev/legacy/dev/NEODOC.md: - Deep links use generated app-local `public_id`; old rows get public ids during Room migration v8 or when restored through supported migrations.
- dev/legacy/dev/NEODOC.md: - Device smoke package for manual adb flows: `com.supercontacts.app.debug`.
- dev/legacy/dev/NEODOC.md: - Instrumentation target clone when used: `com.supercontacts.app.devicetest`; runner `com.supercontacts.app.devicetest.test/androidx.test.runner.AndroidJUnitRunner`.

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.

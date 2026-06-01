# android-sdk-auto-update Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
| source | fact |
|---|---|
| `dev/legacy/dev/human/ANDROID_SDK_UPDATE_TOOL.md` | Questo tool non aggiorna roadmap o file interni di app Android come MultiTimeTracker o SuperContacts. |
| `android_sdk_auto_update.sh` | --dry-run Show and log the planned mutation without installing/removing. |
| `android_sdk_auto_update.sh` | /^Available Updates:/ { in_updates=1; next } |
| `android_sdk_auto_update.sh` | /^Installed packages:/ // /^Installed Packages:/ { in_installed=1; next } |
| `android_sdk_auto_update.sh` | /^Available Updates:/ { in_updates=1; print; next } |
| `android_sdk_auto_update.sh` | info "Accepting pending Android SDK licenses non-interactively" |

## Deferred Or Risky Work
- UNKNOWN: no risk/deferred list found.

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.

# remote-codex-phone AI OPERATIONS

PROJECT
- name: remote-codex-phone
- slug: remote-codex-phone
- purpose: Prompt #438 setup for controlling Codex from an Android phone through:
- current_status: Working tree has 7 non-clean entries; do not mix unrelated changes. First entries: ?? .codexmeta, ?? .codexmeta.bak.20260528_191731, ?? .codexmeta.bak.20260528_191758, ?? .codexmeta.bak.20260528_191912, ?? .codexmeta.bak.20260528_193715
- repo_path: `/home/daniele/codex-workspace/remote-codex-phone`
- remote: `none`
- branch: `master`
- last_verified_commit/date: `e1280bc` / `2026-06-01T13:20:29+02:00`

STACK
- languages: UNKNOWN
- frameworks: UNKNOWN
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: UNKNOWN

CODE_MAP
entrypoints:
- UNKNOWN
important_folders:
- `dev`
important_files:
- `dev/README.md`
tests:
- UNKNOWN
scripts:
- UNKNOWN
generated/runtime/avoid_touch_casually:
- `dev/legacy`

ARCH
summary:
- dev/legacy/README.md: Prompt #438 setup for controlling Codex from an Android phone through:
- dev/legacy/TROUBLESHOOTING.md: systemctl status ssh --no-pager
- dev/legacy/OPERATIONS.md: - Termius, or Termux with `openssh`
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # Remote Codex From Phone |
| `dev/legacy/README.md` | ## PC State |
| `dev/legacy/README.md` | ## Manual Tailscale Login |
| `dev/legacy/TROUBLESHOOTING.md` | # Troubleshooting |
| `dev/legacy/TROUBLESHOOTING.md` | ## Tailscale Needs Login |
| `dev/legacy/TROUBLESHOOTING.md` | ## SSH Does Not Connect |
| `dev/legacy/TROUBLESHOOTING.md` | ## tmux Basics |
| `dev/legacy/TROUBLESHOOTING.md` | ## Firewall |
| `dev/legacy/OPERATIONS.md` | # Operations |
| `dev/legacy/OPERATIONS.md` | ## Phone Apps |
| `dev/legacy/OPERATIONS.md` | ## Connect From Phone |
| `dev/legacy/OPERATIONS.md` | ## tmux Sessions |
| `dev/legacy/README.md` | Prompt #438 setup for controlling Codex from an Android phone through: |
| `dev/legacy/TROUBLESHOOTING.md` | systemctl status ssh --no-pager |
| `dev/legacy/OPERATIONS.md` | - Termius, or Termux with `openssh` |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `UNKNOWN` | no verified invariants found in read sources. |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
| source | fact |
|---|---|
| `dev/legacy/TROUBLESHOOTING.md` | systemctl status ssh --no-pager |
| `dev/legacy/TROUBLESHOOTING.md` | systemctl status tailscaled --no-pager |
test_targets:
- UNKNOWN
known_test_flakiness_or_requirements:
- UNKNOWN

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `UNKNOWN` | no verified versioning/release rules found in read sources. |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `UNKNOWN` | no verified data storage policy found in read sources. |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `UNKNOWN` | no verified bugs/troubleshooting facts found in read sources. |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- UNKNOWN: no verified do-not-break rules found in read sources.

RECENT_DECISIONS
| source | fact |
|---|---|
| `UNKNOWN` | no verified recent decisions found in read sources. |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `UNKNOWN` | no verified roadmap found in read sources. |

LEGACY_SUMMARY
- legacy_docs_read_count: 4
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/README.md`
- `dev/legacy/TROUBLESHOOTING.md`
- `dev/legacy/OPERATIONS.md`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../remote-codex-phone/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/remote-codex-phone/overview.md)
- human_folder: [human folder](../../human/projects/remote-codex-phone)
- legacy_docs: [dev/legacy](../../../remote-codex-phone/dev/legacy)
- repo_path: [repo](../../../remote-codex-phone)

OPEN_QUESTIONS
- none detected in extracted sources

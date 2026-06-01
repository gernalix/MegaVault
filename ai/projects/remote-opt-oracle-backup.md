# remote_opt_oracle_backup AI OPERATIONS

PROJECT
- name: remote_opt_oracle_backup
- slug: remote-opt-oracle-backup
- purpose: Remote Oracle backup script set for restic backup/prune/systemd units under the Oracle backup runtime path; source docs are sparse, so verify remote runtime before edits.
- current_status: Working tree has 10 non-clean entries; do not mix unrelated changes. First entries: M backup.sh, M prune.sh, M prune_local_snapshots.sh, ?? backup.sh.bak.20260331_220235, ?? backup.sh.bak.20260502_025422
- repo_path: `/home/daniele/codex-workspace/projects/vm_oracle/remote_opt_oracle_backup`
- remote: `none`
- branch: `main`
- last_verified_commit/date: `62254c3` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Python, Shell
- frameworks: UNKNOWN
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: systemd

CODE_MAP
entrypoints:
- `check_backup_health.py`
important_folders:
- `dev`
important_files:
- `dev/README.md`
tests:
- UNKNOWN
scripts:
- `backup.sh`
- `backup.sh.bak.20260331_220235`
- `backup.sh.bak.20260502_025422`
- `check_backup_health.py`
- `prune.sh`
- `prune.sh.bak.20260331_220235`
- `prune.sh.bak.20260502_032503`
- `prune_local_snapshots.sh`
- `prune_local_snapshots.sh.bak.20260502_025422`
generated/runtime/avoid_touch_casually:
- `dev/legacy`

ARCH
summary:
- backup.sh: ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- check_backup_health.py: import os, time, sys, traceback
- prune.sh: ENV_FILE="/etc/oracle_backup/oracle_backup.env"
- prune_local_snapshots.sh: STATE_DIR="/var/lib/oracle_backup"
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `backup.sh` | #!/usr/bin/env bash |
| `backup.sh` | # shellcheck disable=SC1090 |
| `backup.sh` | # Create sqlite snapshots (consistent even with WAL + active writers) |
| `backup.sh` | # Use sqlite online backup API |
| `backup.sh` | # Compute relative path from its root |
| `backup.sh` | # Now run restic backup to each repo |
| `backup.sh` | # Note: first-time remote init is manual (see README) |
| `backup.sh` | # Success marker (epoch seconds) |
| `check_backup_health.py` | #!/usr/bin/env python3 |
| `check_backup_health.py` | # v1 |
| `prune.sh` | #!/usr/bin/env bash |
| `prune.sh` | # shellcheck disable=SC1090 |
| `prune_local_snapshots.sh` | #!/usr/bin/env bash |
| `backup.sh` | ENV_FILE="/etc/oracle_backup/oracle_backup.env" |
| `check_backup_health.py` | import os, time, sys, traceback |
| `prune.sh` | ENV_FILE="/etc/oracle_backup/oracle_backup.env" |
| `prune_local_snapshots.sh` | STATE_DIR="/var/lib/oracle_backup" |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `backup.sh` | echo "[*] oracle-backup @ $ts" |
| `backup.sh` | echo "[!] Another oracle-backup restic job is already running." |
| `backup.sh` | # Use sqlite online backup API |
| `backup.sh` | sqlite3 "$src" ".timeout 5000" ".backup '$dst'" |
| `backup.sh` | # Now run restic backup to each repo |
| `backup.sh` | echo "[*] Restic backup..." |
| `backup.sh` | if ! rclone copyto "$preflight_file" "$remote_path/.oracle-backup-write-test" --retries 1 --low-level-retries 1; then |
| `backup.sh` | rclone deletefile "$remote_path/.oracle-backup-write-test" // true |
| `backup.sh` | restic -r "$repo" backup \ |
| `backup.sh` | echo "[!] all backup repos failed" |
| `backup.sh` | echo "[!] backup OK with repo_success=$repo_success repo_fail=$repo_fail" |
| `check_backup_health.py` | def notify(msg: str, title: str = "Backup alert"): |
| `check_backup_health.py` | telegram_notify.notify(msg, title=title, prefix="oracle-backup") |
| `check_backup_health.py` | f"⚠️ Nessun marker di backup trovato ({STATE_FILE}). " |
| `check_backup_health.py` | f"Probabile che i backup non siano mai partiti o che ci sia un errore di permessi.\n" |
| `check_backup_health.py` | f"🚨 Backup NON eseguito da {age_min:.1f} minuti (soglia {threshold_min} min).\n" |
| `check_backup_health.py` | f"Controlla: journalctl -u oracle-backup.service -n 200 --no-pager\n" |
| `check_backup_health.py` | notify("❌ Errore monitor backup:\n" + traceback.format_exc(), title="Backup monitor error") |
| `prune.sh` | echo "[*] oracle-backup prune @ $ts" |
| `prune.sh` | echo "[!] Could not acquire backup lock for prune." |
| `prune_local_snapshots.sh` | echo "[!] Backup is running; skip local snapshot prune." |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
| source | fact |
|---|---|
| `backup.sh` | #!/usr/bin/env bash |
| `backup.sh` | sqlite3 "$src" ".timeout 5000" ".backup '$dst'" |
| `check_backup_health.py` | #!/usr/bin/env python3 |
| `check_backup_health.py` | f"Controlla: journalctl -u oracle-backup.service -n 200 --no-pager\n" |
| `prune.sh` | #!/usr/bin/env bash |
| `prune_local_snapshots.sh` | #!/usr/bin/env bash |
test_targets:
- UNKNOWN
known_test_flakiness_or_requirements:
- backup.sh: sqlite3 "$src" ".timeout 5000" ".backup '$dst'"

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `UNKNOWN` | no verified versioning/release rules found in read sources. |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `backup.sh` | echo "[*] oracle-backup @ $ts" |
| `backup.sh` | echo "[!] Another oracle-backup restic job is already running." |
| `backup.sh` | # Use sqlite online backup API |
| `backup.sh` | sqlite3 "$src" ".timeout 5000" ".backup '$dst'" |
| `backup.sh` | # Now run restic backup to each repo |
| `backup.sh` | echo "[*] Restic backup..." |
| `backup.sh` | if ! rclone copyto "$preflight_file" "$remote_path/.oracle-backup-write-test" --retries 1 --low-level-retries 1; then |
| `backup.sh` | rclone deletefile "$remote_path/.oracle-backup-write-test" // true |
| `backup.sh` | restic -r "$repo" backup \ |
| `backup.sh` | echo "[!] all backup repos failed" |
| `backup.sh` | echo "[!] backup OK with repo_success=$repo_success repo_fail=$repo_fail" |
| `check_backup_health.py` | def notify(msg: str, title: str = "Backup alert"): |
| `check_backup_health.py` | telegram_notify.notify(msg, title=title, prefix="oracle-backup") |
| `check_backup_health.py` | f"⚠️ Nessun marker di backup trovato ({STATE_FILE}). " |
| `check_backup_health.py` | f"Probabile che i backup non siano mai partiti o che ci sia un errore di permessi.\n" |
| `check_backup_health.py` | f"🚨 Backup NON eseguito da {age_min:.1f} minuti (soglia {threshold_min} min).\n" |
| `check_backup_health.py` | f"Controlla: journalctl -u oracle-backup.service -n 200 --no-pager\n" |
| `check_backup_health.py` | notify("❌ Errore monitor backup:\n" + traceback.format_exc(), title="Backup monitor error") |
| `prune.sh` | echo "[*] oracle-backup prune @ $ts" |
| `prune.sh` | echo "[!] Could not acquire backup lock for prune." |
| `prune_local_snapshots.sh` | echo "[!] Backup is running; skip local snapshot prune." |
| `backup.sh` | #!/usr/bin/env bash |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `backup.sh` | sqlite3 "$src" ".timeout 5000" ".backup '$dst'" |
| `check_backup_health.py` | notify("❌ Errore monitor backup:\n" + traceback.format_exc(), title="Backup monitor error") |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- backup.sh: echo "[*] oracle-backup @ $ts"
- backup.sh: echo "[!] Another oracle-backup restic job is already running."
- backup.sh: # Use sqlite online backup API
- backup.sh: sqlite3 "$src" ".timeout 5000" ".backup '$dst'"
- backup.sh: # Now run restic backup to each repo
- backup.sh: echo "[*] Restic backup..."
- backup.sh: if ! rclone copyto "$preflight_file" "$remote_path/.oracle-backup-write-test" --retries 1 --low-level-retries 1; then
- backup.sh: rclone deletefile "$remote_path/.oracle-backup-write-test" // true
- backup.sh: restic -r "$repo" backup \
- backup.sh: echo "[!] all backup repos failed"
- backup.sh: echo "[!] backup OK with repo_success=$repo_success repo_fail=$repo_fail"
- check_backup_health.py: def notify(msg: str, title: str = "Backup alert"):
- check_backup_health.py: telegram_notify.notify(msg, title=title, prefix="oracle-backup")
- check_backup_health.py: f"⚠️ Nessun marker di backup trovato ({STATE_FILE}). "
- check_backup_health.py: f"Probabile che i backup non siano mai partiti o che ci sia un errore di permessi.\n"
- check_backup_health.py: f"🚨 Backup NON eseguito da {age_min:.1f} minuti (soglia {threshold_min} min).\n"

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
- legacy_docs_read_count: 6
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/lib/README.txt`
- `backup.sh`
- `check_backup_health.py`
- `prune.sh`
- `prune_local_snapshots.sh`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../projects/vm_oracle/remote_opt_oracle_backup/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/remote-opt-oracle-backup/overview.md)
- human_folder: [human folder](../../human/projects/remote-opt-oracle-backup)
- legacy_docs: [dev/legacy](../../../projects/vm_oracle/remote_opt_oracle_backup/dev/legacy)
- repo_path: [repo](../../../projects/vm_oracle/remote_opt_oracle_backup)

OPEN_QUESTIONS
- none detected in extracted sources

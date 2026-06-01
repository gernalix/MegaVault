# os-observer Troubleshooting

## Problemi e sintomi rilevati nel codice
- os_observer_export.sh:3:set -euo pipefail
- os_observer_export.sh:120:except sqlite3.DatabaseError:
- os_observer_export.sh:132:"UPDATE codex_sessions SET transcript_excerpt=substr(coalesce(transcript_excerpt,''),1,2000), recent_errors=substr(coalesce(recent_errors,''),1,2000), tou
- os_observer_export.sh:137:except sqlite3.DatabaseError:
- os_observer_export.sh:149:timeout 90 nice -n 19 ionice -c3 python3 "${PROJECT_DIR}/os_observer_ai_diagnostics.py" \
- os_observer_export.sh:156:"${SQLITE_BIN}" -cmd '.timeout 10000' "${telemetry_copy}" "VACUUM; PRAGMA optimize;" >/dev/null 2>&1 // true
- os_observer_export.sh:157:"${SQLITE_BIN}" -cmd '.timeout 10000' "${knowledge_copy}" "VACUUM; PRAGMA optimize;" >/dev/null 2>&1 // true
- os_observer_export.sh:160:"${SQLITE_BIN}" -cmd '.timeout 5000' "${DB_PATH}" "PRAGMA wal_checkpoint(FULL);" >/dev/null 2>&1 // true
- codex_freeze_runner.py:48:DEFAULT_RUN_NEXT_TIMEOUT_SECONDS = 2 * 3600
- codex_freeze_runner.py:51:QUEUE_BUSY_TIMEOUT_MS = 1000
- codex_freeze_runner.py:53:QUEUE_RETRY_BACKOFF_SECONDS = 0.25
- codex_freeze_runner.py:70:PHASE_FAILED = "failed"
- codex_freeze_runner.py:82:retry_count INTEGER NOT NULL DEFAULT 0,
- codex_freeze_runner.py:260:def failure(self, now: float) -> None:
- codex_freeze_runner.py:399:except (OSError, json.JSONDecodeError) as exc:
- codex_freeze_runner.py:400:raise SystemExit(f"invalid_resource_config path={config_path} error={exc}") from exc
- docs/prompt_683_knowledge_patch.sql:3:'pattern:transfer_rsync_stalled_dest_sdc_io_error',
- docs/prompt_683_knowledge_patch.sql:5:'transfer rsync stalled with DEST sdc transport error',

## Comandi/verifiche utili trovati
- UNKNOWN: nessun comando rilevato in build/script/CI.

## Safety prima di correggere
- os_observer_export.sh:48:trap 'rm -rf "${tmp}"' EXIT
- os_observer_export.sh:98:conn.execute("PRAGMA journal_mode=DELETE")
- os_observer_export.sh:202:"${SQLITE_BIN}" -readonly -cmd '.timeout 5000' "${DB_PATH}" "SELECT ts // ' table=' // table_name // ' deleted=' // deleted_rows // ' cutoff=' // cutoff_t
- systemd/user/home-backup-kuma-push.service:12:PrivateTmp=true
- systemd/user/home-backup-retention-kuma-push.service:13:PrivateTmp=true
- codex_freeze_runner.py:84:last_block_reason TEXT NOT NULL DEFAULT '',
- codex_freeze_runner.py:372:def emit_progress(message: str, *, trace: bool = False, enabled: bool = True) -> None:
- codex_freeze_runner.py:373:_ = trace
- os_observer_export.sh:156:"${SQLITE_BIN}" -cmd '.timeout 10000' "${telemetry_copy}" "VACUUM; PRAGMA optimize;" >/dev/null 2>&1 // true
- os_observer_export.sh:157:"${SQLITE_BIN}" -cmd '.timeout 10000' "${knowledge_copy}" "VACUUM; PRAGMA optimize;" >/dev/null 2>&1 // true
- os_observer_export.sh:160:"${SQLITE_BIN}" -cmd '.timeout 5000' "${DB_PATH}" "PRAGMA wal_checkpoint(FULL);" >/dev/null 2>&1 // true
- os_observer_export.sh:165:"${SQLITE_BIN}" -cmd '.timeout 10000' "${DB_PATH}" ".backup '${pkg_dir}/telemetry.sqlite'"

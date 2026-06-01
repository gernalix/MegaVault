# os-observer Features

Questa pagina deriva dal codice attivo auditato con `#604927`.

## Mappa funzionale dal codice
- `os_observer_export.sh`: choose_db_path, compact_export_sqlite
- `codex_freeze_runner.py`: LimitedResult, JobCommandResult, SnapshotPolicyState, Pressure, AdmissionResult, ContainmentPlan, AdaptiveThrottle, now_ts
- `kuma_auto_healer.py`: print_json, command_status, readable_status, systemctl_json, command_run_once, systemctl_user, command_bootstrap, command_doctor
- `os_observer_ai_diagnostics.py`: now_ts, norm_text, sha256_text, compact_line, pattern_counts, significant_lines, top_offenders, capsule_path
- `os_observer_autofix_agent.py`: Settings, AgentLog, SQLiteBackupPolicy, SQLiteTarget, Event, KumaMonitor, AutofixAgent, now_ts
- `tests/test_autofix_agent.py`: AutofixAgentTests, init_telemetry, init_knowledge, make_agent
- `tests/test_codex_freeze_runner.py`: CodexFreezeRunnerTests, sh
- `os_observer.sh`: choose_db_path, now_local, now_utc, sqlq, sqln, sha256_text, normalize_event_text, truncate_text
- `os_observer_autofix_dashboard.sh`: sql, systemctl_value, line
- `os_observer_cleanup.sh`: usage
- `os_observer_dashboard.sh`: choose_db_path, kq, render_once
- `os_observer_memory.sh`: choose_db_path, choose_telemetry_db_path, now_local, sqlq, sqln, db, db_stdin, tdb

## Confini operativi
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

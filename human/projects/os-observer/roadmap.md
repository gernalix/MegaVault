# os-observer Roadmap

## Segnali dal codice
- codex_freeze_runner.py:8:from __future__ import annotations
- codex_freeze_runner.py:48:DEFAULT_RUN_NEXT_TIMEOUT_SECONDS = 2 * 3600
- codex_freeze_runner.py:49:RUN_NEXT_HEARTBEAT_SECONDS = 15
- codex_freeze_runner.py:57:ADMISSION_DEFER = "DEFER"
- codex_freeze_runner.py:67:PHASE_DEFERRED = "deferred"
- codex_freeze_runner.py:819:heartbeat_seconds: int = RUN_NEXT_HEARTBEAT_SECONDS,
- docs/prompt_482_knowledge_patch.sql:104:'{"guardian_expected_classification":"WARNING/IO_PRESSURE_OBSERVE","os_observer_next_action":"false_positive_candidate_observe_dedup_notify_
- docs/prompt_731_knowledge_patch.sql:49:'Do read-only lsusb -t, lsblk identity, udevadm serial/path, targeted journalctl. Do not start rsync or fsck. Test physical isolation only as
- docs/prompt_731_knowledge_patch.sql:111:'After a clean shutdown/unmount, os-observer may emit repeated disappeared alerts because the previous external mount is absent in every lat
- docs/prompt_731_knowledge_patch.sql:112:'For each mountpoint, emit one disappeared incident per transition present->absent; later samples should be already_absent/info unless the d
- kuma_auto_healer.py:2:from __future__ import annotations
- kuma_auto_healer.py:35:payload["timer"] = systemctl_json(["systemctl", "--user", "show", "os-observer-autofix-agent.timer", "--property=ActiveState,NextElapseUSecRealtime,Result"])

## Debito/rischi da considerare
- os_observer_export.sh:3:set -euo pipefail
- os_observer_export.sh:120:except sqlite3.DatabaseError:
- os_observer_export.sh:132:"UPDATE codex_sessions SET transcript_excerpt=substr(coalesce(transcript_excerpt,''),1,2000), recent_errors=substr(coalesce(recent_errors,''),1,2000), tou
- os_observer_export.sh:137:except sqlite3.DatabaseError:
- os_observer_export.sh:149:timeout 90 nice -n 19 ionice -c3 python3 "${PROJECT_DIR}/os_observer_ai_diagnostics.py" \
- os_observer_export.sh:156:"${SQLITE_BIN}" -cmd '.timeout 10000' "${telemetry_copy}" "VACUUM; PRAGMA optimize;" >/dev/null 2>&1 // true
- os_observer_export.sh:157:"${SQLITE_BIN}" -cmd '.timeout 10000' "${knowledge_copy}" "VACUUM; PRAGMA optimize;" >/dev/null 2>&1 // true
- os_observer_export.sh:160:"${SQLITE_BIN}" -cmd '.timeout 5000' "${DB_PATH}" "PRAGMA wal_checkpoint(FULL);" >/dev/null 2>&1 // true
- os_observer_export.sh:48:trap 'rm -rf "${tmp}"' EXIT
- os_observer_export.sh:98:conn.execute("PRAGMA journal_mode=DELETE")
- os_observer_export.sh:202:"${SQLITE_BIN}" -readonly -cmd '.timeout 5000' "${DB_PATH}" "SELECT ts // ' table=' // table_name // ' deleted=' // deleted_rows // ' cutoff=' // cutoff_t
- systemd/user/home-backup-kuma-push.service:12:PrivateTmp=true
- systemd/user/home-backup-retention-kuma-push.service:13:PrivateTmp=true
- codex_freeze_runner.py:84:last_block_reason TEXT NOT NULL DEFAULT '',

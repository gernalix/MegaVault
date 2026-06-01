META:
name=os-observer
slug=os-observer
path=/home/daniele/codex-workspace/os-observer
remote=none
branch=codex/prompt-914582
verified_commit=b1ed3b0
verified_at=2026-06-01T13:39:31+02:00
PURPOSE:
- Linux Mint black-box recorder: user-systemd timer records read-only telemetry into SQLite, maintains diagnostic knowledge, exports boun...
STACK:
lang=Python,Shell;fw=UNKNOWN;db=Room/SQLite,SQLite;platform=UNKNOWN;tools=ADB,Chrome,Uptime Kuma,restic,systemd
MAP:
entry=UNKNOWN
core=codex_freeze_runner.py
core=config/codex-resource-presets.json
core=dev/project.metadata.json
core=docs/prompt_482_knowledge_patch.sql
core=docs/prompt_683_knowledge_patch.sql
core=docs/prompt_731_knowledge_patch.sql
core=docs/prompt_734_knowledge_patch.sql
core=docs/prompt_735_knowledge_patch.sql
ui=UNKNOWN
db=os_observer_export.sh
db=systemd/user/home-backup-kuma-push.service
db=systemd/user/home-backup-kuma-push.timer
db=systemd/user/home-backup-retention-kuma-push.service
db=systemd/user/home-backup-retention-kuma-push.timer
tests=tests/test_autofix_agent.py,tests/test_codex_freeze_runner.py
scripts=os_observer.sh,os_observer_autofix_dashboard.sh,os_observer_cleanup.sh,os_observer_dashboard.sh,os_observer_memory.sh
build=UNKNOWN
ci=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
- os_observer_export.sh=>choose_db_path,compact_export_sqlite
- codex_freeze_runner.py=>LimitedResult,JobCommandResult,SnapshotPolicyState,Pressure,AdmissionResult,ContainmentPlan,
- kuma_auto_healer.py=>print_json,command_status,readable_status,systemctl_json,command_run_once,systemctl_user,comman
- os_observer_ai_diagnostics.py=>now_ts,norm_text,sha256_text,compact_line,pattern_counts,significant_lines,top_offend
- os_observer_autofix_agent.py=>Settings,AgentLog,SQLiteBackupPolicy,SQLiteTarget,Event,KumaMonitor,AutofixAgent
- os_observer_export.sh:12:EXPORT_DIR="/home/daniele/os_observer_exports"
- os_observer_export.sh:20:EXPORT_TARGET_MB=25
- os_observer_export.sh:21:EXPORT_MAX_MB=50
- os_observer_export.sh:22:EXPORT_CAPSULE_ROOT_NAME="ai-diagnostics/capsules"
- os_observer_export.sh:23:EXPORT_RAW_ROOT_NAME="ai-diagnostics/raw"
- os_observer_export.sh:45:mkdir -p "${EXPORT_DIR}"
FLOW:
- os_observer_export.sh:12:EXPORT_DIR="/home/daniele/os_observer_exports"
- os_observer_export.sh:20:EXPORT_TARGET_MB=25
- os_observer_export.sh:21:EXPORT_MAX_MB=50
- os_observer_export.sh:22:EXPORT_CAPSULE_ROOT_NAME="ai-diagnostics/capsules"
- os_observer_export.sh:23:EXPORT_RAW_ROOT_NAME="ai-diagnostics/raw"
- os_observer_export.sh:45:mkdir -p "${EXPORT_DIR}"
- os_observer_export.sh:49:pkg_dir="${tmp}/os_observer_export_${stamp}"
- os_observer_export.sh:52:compact_export_sqlite() {
- systemd/user/home-backup-kuma-push.service:2:Description=Home backup Kuma push heartbeat v16
- systemd/user/home-backup-kuma-push.service:4:ConditionPathExists=/home/daniele/home_backup_kuma_push.sh
- systemd/user/home-backup-kuma-push.service:8:ExecStart=/home/daniele/home_backup_kuma_push.sh HEARTBEAT systemd_time
- systemd/user/home-backup-kuma-push.timer:2:Description=Home backup Kuma push heartbeat timer v16
INV:
arch=os_observer_export.sh:55:if [[ -r "${PROJECT_DIR}/dev/ai-diagnostics/SCHEMA.md" ]]; then
arch=os_observer_export.sh:57:cp "${PROJECT_DIR}/dev/ai-diagnostics/SCHEMA.md" "${pkg_dir}/ai-diagnostics/SCHEMA.md"
arch=os_observer_export.sh:149:timeout 90 nice -n 19 ionice -c3 python3 "${PROJECT_DIR}/os_observer_ai_diagnostics.py
arch=os_observer_export.sh:156:"${SQLITE_BIN}" -cmd '.timeout 10000' "${telemetry_copy}" "VACUUM; PRAGMA optimize;" >
arch=os_observer_export.sh:157:"${SQLITE_BIN}" -cmd '.timeout 10000' "${knowledge_copy}" "VACUUM; PRAGMA optimize;" >
arch=os_observer_export.sh:160:"${SQLITE_BIN}" -cmd '.timeout 5000' "${DB_PATH}" "PRAGMA wal_checkpoint(FULL);" >/dev
data=os_observer_export.sh:10:DEFAULT_TELEMETRY_DB_PATH="${FALLBACK_DB_DIR}/telemetry.sqlite"
data=os_observer_export.sh:11:DEFAULT_KNOWLEDGE_DB_PATH="${FALLBACK_DB_DIR}/knowledge.sqlite"
data=os_observer_export.sh:12:EXPORT_DIR="/home/daniele/os_observer_exports"
data=os_observer_export.sh:19:SQLITE_BIN="${SQLITE_BIN:-sqlite3}"
data=os_observer_export.sh:20:EXPORT_TARGET_MB=25
data=os_observer_export.sh:21:EXPORT_MAX_MB=50
safety=os_observer_export.sh:48:trap 'rm -rf "${tmp}"' EXIT
safety=os_observer_export.sh:98:conn.execute("PRAGMA journal_mode=DELETE")
safety=os_observer_export.sh:202:"${SQLITE_BIN}" -readonly -cmd '.timeout 5000' "${DB_PATH}" "SELECT ts // ' table=' //
safety=systemd/user/home-backup-kuma-push.service:12:PrivateTmp=true
safety=systemd/user/home-backup-retention-kuma-push.service:13:PrivateTmp=true
safety=codex_freeze_runner.py:84:last_block_reason TEXT NOT NULL DEFAULT '',
safety=codex_freeze_runner.py:372:def emit_progress(message: str, *, trace: bool = False, enabled: bool = True) -> None
ux=docs/prompt_482_knowledge_patch.sql:13:'Classify equivalent freeze guardian PRE_EMERGENCY reports with healthy h
ux=docs/prompt_731_knowledge_patch.sql:48:'Real block/USB path failure below filesystem layer; correlate /dev/sdX t
ux=docs/prompt_735_knowledge_patch.sql:9:'2026-05-19 prompt #735: /dev/sdb2 BitLocker, seriale WFF0FEX8, GUID 3bc48
version=systemd/user/home-backup-kuma-push.service:2:Description=Home backup Kuma push heartbeat v16
version=systemd/user/home-backup-kuma-push.service:4:ConditionPathExists=/home/daniele/home_backup_kuma_push.sh
version=systemd/user/home-backup-kuma-push.service:8:ExecStart=/home/daniele/home_backup_kuma_push.sh HEARTBEAT systemd_
version=systemd/user/home-backup-kuma-push.timer:2:Description=Home backup Kuma push heartbeat timer v16
i18n=strings/resources present; verify no hardcoded UI
BUILD:
- UNKNOWN
TEST:
- tests/test_autofix_agent.py:11:import unittest
- tests/test_autofix_agent.py:13:from unittest import mock
- tests/test_autofix_agent.py:19:assert SPEC.loader is not None
- tests/test_autofix_agent.py:25:assert AI_SPEC.loader is not None
- tests/test_autofix_agent.py:38:CREATE TABLE disk_events(id INTEGER PRIMARY KEY, ts TEXT NOT NULL, event_type TEXT, d
- tests/test_autofix_agent.py:124:class AutofixAgentTests(unittest.TestCase):
- tests/test_autofix_agent.py:129:def test_telemetry_fresh_no_intervention(self) -> None:
- tests/test_autofix_agent.py:134:self.assertEqual(result["telemetry_health"]["status"], "healthy")
- tests/test_autofix_agent.py:136:self.assertEqual(conn.execute("SELECT COUNT(*) FROM tuning_decisions").fetchone()[0]
- tests/test_autofix_agent.py:138:def test_telemetry_stale_plans_writer_restart(self) -> None:
- tests/test_codex_freeze_runner.py:8:import unittest
- tests/test_codex_freeze_runner.py:15:assert SPEC.loader is not None
DATA:
db=os_observer_export.sh:10:DEFAULT_TELEMETRY_DB_PATH="${FALLBACK_DB_DIR}/telemetry.sqlite"
db=os_observer_export.sh:11:DEFAULT_KNOWLEDGE_DB_PATH="${FALLBACK_DB_DIR}/knowledge.sqlite"
db=os_observer_export.sh:12:EXPORT_DIR="/home/daniele/os_observer_exports"
db=os_observer_export.sh:19:SQLITE_BIN="${SQLITE_BIN:-sqlite3}"
db=os_observer_export.sh:20:EXPORT_TARGET_MB=25
db=os_observer_export.sh:21:EXPORT_MAX_MB=50
backup=systemd/user/home-backup-kuma-push.service:2:Description=Home backup Kuma push heartbeat v16
backup=systemd/user/home-backup-kuma-push.service:4:ConditionPathExists=/home/daniele/home_backup_kuma_push.sh
backup=systemd/user/home-backup-kuma-push.service:8:ExecStart=/home/daniele/home_backup_kuma_push.sh HEARTBEAT systemd_
backup=systemd/user/home-backup-kuma-push.timer:2:Description=Home backup Kuma push heartbeat timer v16
import=codex_freeze_runner.py:8:from __future__ import annotations
import=codex_freeze_runner.py:10:import argparse
import=codex_freeze_runner.py:11:import dataclasses
export=os_observer_export.sh:10:DEFAULT_TELEMETRY_DB_PATH="${FALLBACK_DB_DIR}/telemetry.sqlite"
export=os_observer_export.sh:11:DEFAULT_KNOWLEDGE_DB_PATH="${FALLBACK_DB_DIR}/knowledge.sqlite"
export=os_observer_export.sh:12:EXPORT_DIR="/home/daniele/os_observer_exports"
migration=UNKNOWN
retention=systemd/user/home-backup-retention-kuma-push.service:2:Description=Home backup retention Kuma push heartbeat v16
retention=systemd/user/home-backup-retention-kuma-push.service:4:ConditionPathExists=/home/daniele/home_backup_kuma_push.s
retention=systemd/user/home-backup-retention-kuma-push.service:8:Environment=HOME_BACKUP_KUMA_ENV=/home/daniele/.config/ho
DNB:
- os_observer_export.sh:48:trap 'rm -rf "${tmp}"' EXIT
- os_observer_export.sh:98:conn.execute("PRAGMA journal_mode=DELETE")
- os_observer_export.sh:202:"${SQLITE_BIN}" -readonly -cmd '.timeout 5000' "${DB_PATH}" "SELECT ts // ' table=' // tab
- systemd/user/home-backup-kuma-push.service:12:PrivateTmp=true
- systemd/user/home-backup-retention-kuma-push.service:13:PrivateTmp=true
- codex_freeze_runner.py:84:last_block_reason TEXT NOT NULL DEFAULT '',
- codex_freeze_runner.py:372:def emit_progress(message: str, *, trace: bool = False, enabled: bool = True) -> None:
- codex_freeze_runner.py:373:_ = trace
- os_observer_export.sh:156:"${SQLITE_BIN}" -cmd '.timeout 10000' "${telemetry_copy}" "VACUUM; PRAGMA optimize;" >/dev
- os_observer_export.sh:157:"${SQLITE_BIN}" -cmd '.timeout 10000' "${knowledge_copy}" "VACUUM; PRAGMA optimize;" >/dev
BUG:
- os_observer_export.sh:3:set -euo pipefail
- os_observer_export.sh:120:except sqlite3.DatabaseError:
- os_observer_export.sh:132:"UPDATE codex_sessions SET transcript_excerpt=substr(coalesce(transcript_excerpt,''),1,200
- os_observer_export.sh:137:except sqlite3.DatabaseError:
- os_observer_export.sh:149:timeout 90 nice -n 19 ionice -c3 python3 "${PROJECT_DIR}/os_observer_ai_diagnostics.py" \
- os_observer_export.sh:156:"${SQLITE_BIN}" -cmd '.timeout 10000' "${telemetry_copy}" "VACUUM; PRAGMA optimize;" >/dev
- os_observer_export.sh:157:"${SQLITE_BIN}" -cmd '.timeout 10000' "${knowledge_copy}" "VACUUM; PRAGMA optimize;" >/dev
- os_observer_export.sh:160:"${SQLITE_BIN}" -cmd '.timeout 5000' "${DB_PATH}" "PRAGMA wal_checkpoint(FULL);" >/dev/nul
- codex_freeze_runner.py:48:DEFAULT_RUN_NEXT_TIMEOUT_SECONDS = 2 * 3600
- codex_freeze_runner.py:51:QUEUE_BUSY_TIMEOUT_MS = 1000
RISK:
- os_observer_export.sh:48:trap 'rm -rf "${tmp}"' EXIT
- os_observer_export.sh:98:conn.execute("PRAGMA journal_mode=DELETE")
- os_observer_export.sh:202:"${SQLITE_BIN}" -readonly -cmd '.timeout 5000' "${DB_PATH}" "SELECT ts // ' table=' // tab
- systemd/user/home-backup-kuma-push.service:12:PrivateTmp=true
- systemd/user/home-backup-retention-kuma-push.service:13:PrivateTmp=true
- codex_freeze_runner.py:84:last_block_reason TEXT NOT NULL DEFAULT '',
- codex_freeze_runner.py:372:def emit_progress(message: str, *, trace: bool = False, enabled: bool = True) -> None:
- codex_freeze_runner.py:373:_ = trace
- codex_freeze_runner.py:674:os.kill(int(pid), 0)
- codex_freeze_runner.py:747:os.set_blocking(proc.stdout.fileno(), False)
ROAD:
now=codex_freeze_runner.py:8:from __future__ import annotations
next=codex_freeze_runner.py:48:DEFAULT_RUN_NEXT_TIMEOUT_SECONDS = 2 * 3600
later=codex_freeze_runner.py:49:RUN_NEXT_HEARTBEAT_SECONDS = 15
LINK:
meta=../../../os-observer/dev/project.metadata.json
human=../../human/projects/os-observer/overview.md
legacy=../../../os-observer/dev/legacy
repo=../../../os-observer
OPEN:
- none

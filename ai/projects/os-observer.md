META:
name=os-observer
slug=os-observer
path=/home/daniele/codex-workspace/os-observer
remote=none
branch=codex/prompt-914582
verified_commit=b1ed3b0
verified_at=2026-06-01T13:59:53+02:00
protocol=MEGAVAULT_PROTOCOL.md:v2
PURPOSE:
purpose=Linux Mint black-box recorder: user-systemd timer records read-only telemetry into SQLite, maintains diagnostic knowledge, exports bounded context for ChatGPT/Codex, and has guarded autofix/heartbe
STACK:
lang=Python,Shell
fw=UNKNOWN
db=Room/SQLite,SQLite
platform=UNKNOWN
tools=ADB,Chrome,Uptime Kuma,restic,systemd
MAP:
entry=UNKNOWN
ui=UNKNOWN
core=codex_freeze_runner.py,config/codex-resource-presets.json,dev/project.metadata.json,docs/prompt_482_knowledge_patch.sql,docs/prompt_683_knowledge_patch.sql
db=os_observer_export.sh,systemd/user/home-backup-kuma-push.service,systemd/user/home-backup-kuma-push.timer,systemd/user/home-backup-retention-kuma-push.service,systemd/user/home-backup-retention-kuma-push.timer
tests=tests/test_autofix_agent.py,tests/test_codex_freeze_runner.py
scripts=os_observer.sh,os_observer_autofix_dashboard.sh,os_observer_cleanup.sh,os_observer_dashboard.sh,os_observer_memory.sh
build=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated
ARCH:
data=os_observer_export.sh:choose_db_path,compact_export_sqlite
core=codex_freeze_runner.py:LimitedResult,JobCommandResult,SnapshotPolicyState,Pressure,AdmissionResult,ContainmentPlan
core=kuma_auto_healer.py:print_json,command_status,readable_status,systemctl_json,command_run_once,systemctl_user
core=os_observer_ai_diagnostics.py:now_ts,norm_text,sha256_text,compact_line,pattern_counts,significant_lines
core=os_observer_autofix_agent.py:Settings,AgentLog,SQLiteBackupPolicy,SQLiteTarget,Event,KumaMonitor
test=tests/test_autofix_agent.py:AutofixAgentTests,init_telemetry,init_knowledge,make_agent
test=tests/test_codex_freeze_runner.py:CodexFreezeRunnerTests,sh
script=os_observer.sh:choose_db_path,now_local,now_utc,sqlq,sqln,sha256_text
FLOW:
flow=script->os_observer.sh=>os_observer_export.sh
flow=data->os_observer_export.sh
flow=os_observer_export.sh:12:EXPORT_DIR="/home/daniele/os_observer_exports"
flow=os_observer_export.sh:20:EXPORT_TARGET_MB=25
flow=os_observer_export.sh:21:EXPORT_MAX_MB=50
INV:
arch=os_observer_export.sh:choose_db_path,compact_export_sqlite; codex_freeze_runner.py:LimitedResult,JobCommandResult,SnapshotPolicyState,Pressure,AdmissionResult; kuma_auto_healer.py:print_json,command_status,readable_status,systemctl_json,...
data=os_observer_export.sh:55:if [[ -r "${PROJECT_DIR}/dev/ai-diagnostics/SCHEMA.md" ]]; then; os_observer_export.sh:57:cp "${PROJECT_DIR}/dev/ai-diagnostics/SCHEMA.md" "${pkg_dir}/ai-diagnostics/SCHEMA.md"
ux=docs/prompt_482_knowledge_patch.sql:13:'Classify equivalent freeze guardian PRE_EMERGENCY reports with healthy headroom and no mitigation as false_positive_candidate/observe; deduplicate by fingerprint; notify once; n...; docs/prompt_731...
backup=os_observer_export.sh:165:"${SQLITE_BIN}" -cmd '.timeout 10000' "${DB_PATH}" ".backup '${pkg_dir}/telemetry.sqlite'"; os_observer_export.sh:168:"${SQLITE_BIN}" -cmd '.timeout 10000' "${KNOWLEDGE_DB_PATH}" ".backup '${pkg_dir}/knowledge.s...
migration=os_observer_export.sh:55:if [[ -r "${PROJECT_DIR}/dev/ai-diagnostics/SCHEMA.md" ]]; then; os_observer_export.sh:57:cp "${PROJECT_DIR}/dev/ai-diagnostics/SCHEMA.md" "${pkg_dir}/ai-diagnostics/SCHEMA.md"
version=codex_freeze_runner.py:32:VERSION = "v19"; dev/project.metadata.json:9:"metadata_version": 1,
i18n=UNKNOWN
security=codex_freeze_runner.py:35:PROTECTED_PROCESS_RE = re.compile(r"(rsync|restic|backup|borg|rclone|sshd|systemd-journald|journalctl --follow)", re.I); docs/prompt_735_knowledge_patch.sql:7:'Il SOURCE Seagate 4TB era presente a livello kernel...
perf=os_observer_export.sh:149:timeout 90 nice -n 19 ionice -c3 python3 "${PROJECT_DIR}/os_observer_ai_diagnostics.py" \; os_observer_export.sh:156:"${SQLITE_BIN}" -cmd '.timeout 10000' "${telemetry_copy}" "VACUUM; PRAGMA optimize;" >/dev/nul...
BUILD:
files=UNKNOWN
cmd=UNKNOWN
TEST:
files=tests/test_autofix_agent.py,tests/test_codex_freeze_runner.py
cmd=UNKNOWN
DATA:
db=os_observer_export.sh:10:DEFAULT_TELEMETRY_DB_PATH="${FALLBACK_DB_DIR}/telemetry.sqlite"; os_observer_export.sh:11:DEFAULT_KNOWLEDGE_DB_PATH="${FALLBACK_DB_DIR}/knowledge.sqlite"
paths=os_observer_export.sh:10:DEFAULT_TELEMETRY_DB_PATH="${FALLBACK_DB_DIR}/telemetry.sqlite"; os_observer_export.sh:11:DEFAULT_KNOWLEDGE_DB_PATH="${FALLBACK_DB_DIR}/knowledge.sqlite"
backup=systemd/user/home-backup-kuma-push.service:2:Description=Home backup Kuma push heartbeat v16; systemd/user/home-backup-kuma-push.service:4:ConditionPathExists=/home/daniele/home_backup_kuma_push.sh
restore=os_observer_export.sh:10:DEFAULT_TELEMETRY_DB_PATH="${FALLBACK_DB_DIR}/telemetry.sqlite"; os_observer_export.sh:11:DEFAULT_KNOWLEDGE_DB_PATH="${FALLBACK_DB_DIR}/knowledge.sqlite"
import=docs/prompt_482_knowledge_patch.sql:43:INSERT INTO diagnostic_notes(ts, category, signature, note, provenance, importance_score); docs/prompt_482_knowledge_patch.sql:66:INSERT INTO telemetry.incidents(first_seen_ts,last_seen_ts,status,se...
export=os_observer_export.sh:10:DEFAULT_TELEMETRY_DB_PATH="${FALLBACK_DB_DIR}/telemetry.sqlite"; os_observer_export.sh:11:DEFAULT_KNOWLEDGE_DB_PATH="${FALLBACK_DB_DIR}/knowledge.sqlite"
migration=docs/prompt_735_knowledge_patch.sql:189:'Schema extended additively; v1-v6 export compatibility preserved; repeated disappeared alert suppressed without deleting history',; os_observer_export.sh:55:if [[ -r "${PROJECT_DIR}/dev/ai-diagnos...
retention=systemd/user/home-backup-retention-kuma-push.service:2:Description=Home backup retention Kuma push heartbeat v16; systemd/user/home-backup-retention-kuma-push.service:4:ConditionPathExists=/home/daniele/home_backup_kuma_push.sh
DNB:
dnb=os_observer_export.sh:98:conn.execute("PRAGMA journal_mode=DELETE")
dnb=os_observer_export.sh:202:"${SQLITE_BIN}" -readonly -cmd '.timeout 5000' "${DB_PATH}" "SELECT ts || ' table=' || table_name || ' deleted=' || deleted_rows || ' cutoff=' || cutoff_ts FROM retention_log ORDER BY id DESC...
dnb=codex_freeze_runner.py:84:last_block_reason TEXT NOT NULL DEFAULT '',
dnb=codex_freeze_runner.py:372:def emit_progress(message: str, *, trace: bool = False, enabled: bool = True) -> None:
dnb=codex_freeze_runner.py:373:_ = trace
dnb=codex_freeze_runner.py:674:os.kill(int(pid), 0)
dnb=preserve=dev/project.metadata.json,dev/legacy,AI/Human links; docs-only tasks must not touch app code/DB
BUG:
issue=docs/prompt_683_knowledge_patch.sql:7:'The transfer rsync process can remain alive or stopped while progress/log output is stale after a real DEST USB/storage transport error.',
issue=docs/prompt_683_knowledge_patch.sql:26:'Use exact transfer rsync cmdline validation plus log/progress age. Correlate DEST by UUID/serial/path to sdc/usb 2-1.3. If PID is alive but stale and DEST has recent DID_ERROR o...
issue=docs/prompt_735_knowledge_patch.sql:48:'Separate device_missing_kernel, mapper_missing, mount_missing_only and transport_error before calling a Seagate mount disappeared event a disconnect.',
RISK:
risk=os_observer_export.sh:98:conn.execute("PRAGMA journal_mode=DELETE")
risk=os_observer_export.sh:202:"${SQLITE_BIN}" -readonly -cmd '.timeout 5000' "${DB_PATH}" "SELECT ts || ' table=' || table_name || ' deleted=' || deleted_rows || ' cutoff=' || cutoff_ts FROM retention_log ORDER BY id DESC...
risk=codex_freeze_runner.py:84:last_block_reason TEXT NOT NULL DEFAULT '',
risk=codex_freeze_runner.py:372:def emit_progress(message: str, *, trace: bool = False, enabled: bool = True) -> None:
risk=codex_freeze_runner.py:373:_ = trace
risk=codex_freeze_runner.py:674:os.kill(int(pid), 0)
ROAD:
now=UNKNOWN
next=UNKNOWN
later=UNKNOWN
LINK:
meta=../../../os-observer/dev/project.metadata.json
human=../../human/projects/os-observer/overview.md
legacy=../../../os-observer/dev/legacy
repo=../../../os-observer
OPEN:
open=none

VERSION=1
STATUS=MANDATORY_STANDARD
MODE=codex_first
FORMAT=ultracompact
AUTHORITY=global_incident_registry

META:
scope=all MegaVault projects
ai_doc=dev/ai/INCIDENT_REGISTRY.md
human_doc=dev/human/INCIDENT_REGISTRY.md
sqlite_default=/home/ubuntu/sync_root/db/incident_registry.sqlite
override=INCIDENT_REGISTRY_DB

PURPOSE:
purpose=single structured timeline for operational incidents, symptoms, root causes, attempts, final state.
goal=avoid repeated alert amnesia; group recurring symptoms under stable root-cause incidents.

REQUIRED_FIELDS:
field=Incident ID
field=Titolo
field=Data prima comparsa UTC/Z
field=Data ultima comparsa UTC/Z
field=Numero occorrenze
field=Gravita massima
field=Stato OPEN/MITIGATED/RESOLVED/ACCEPTED
field=Root cause
field=Sistemi coinvolti
field=Alert coinvolti
field=Tentativi effettuati
field=Soluzione finale
field=Commit correlati
field=Prompt correlati
field=Tempo totale di impatto
field=Note

SQLITE:
table=incidents
columns=incident_id,first_seen_utc,last_seen_utc,occurrence_count,severity,status,root_cause,resolution_summary
extra_columns=title,systems,alerts,prompt_ids,commit_refs allowed
table=incident_events
purpose=append-only event history with timestamp,severity,status,source,alert_code,symptom,detail,payload_json
write_rule=automatic_upsert_only;no manual sqlite edits except emergency repair documented in incident_events
time=UTC Z only

ID_RULES:
id=stable root-cause slug, uppercase snake case.
example=OCI_STORAGE_LIMIT_EXCEEDED groups BACKUP_BLOCKED_FALLBACK_QUOTA and REMOTE_DEGRADED when StorageLimitExceeded is root cause.
forbid=new incident per repeated symptom when root cause unchanged.
allow=separate incident for distinct root cause, e.g. OCI_REMOTE_REPOSITORY_CORRUPT distinct from OCI_STORAGE_LIMIT_EXCEEDED.

STATUS_RULES:
OPEN=root cause still active.
MITIGATED=symptom controlled but root cause not eliminated.
RESOLVED=root cause eliminated and verification proves normal path works.
ACCEPTED=known unresolved risk intentionally accepted with documented owner/constraint.

INTEGRATION:
healthcheck=must upsert known incident, increment occurrence_count, update last_seen_utc, append incident_events.
monitor=must classify symptom vs root cause before selecting incident_id.
fix=must update incident status/resolution_summary automatically or via project tool.
bootstrap=new project initializes AI doc, human doc, SQLite path/config, and updater hook.

ORACLE_BACKUP_REFERENCE:
db=/home/ubuntu/sync_root/db/incident_registry.sqlite
tool=/opt/oracle_backup/incident_registry.py
incidents=OCI_STORAGE_LIMIT_EXCEEDED,OCI_REMOTE_REPOSITORY_CORRUPT,ORACLE_ROOT_DISK_PRESSURE

INCIDENT:
Incident_ID=CODEX_SQLITE_WAL_T7_ROOT_GROWTH
Titolo=Codex SQLite WAL growth filled 157GiB on T7 root
Data_prima_comparsa_UTC=2026-06-13T15:56:16Z
Data_ultima_comparsa_UTC=2026-06-13T19:13:08Z
Numero_occorrenze=1
Gravita_massima=HIGH
Stato=MITIGATED
Root_cause=Codex logs_2.sqlite uses WAL mode with default wal_autocheckpoint=1000; long-lived Codex sessions hold DB/WAL/SHM handles, so high-volume TRACE/INFO writes can leave a very large WAL allocation until a SQLite checkpoint TRUNCATE succeeds.
Sistemi_coinvolti=Linux Mint T7 root /dev/sda2; Codex CLI; /home/daniele/.codex/logs_2.sqlite; Disk Usage Monitor
Alert_coinvolti=disk_usage_monitor delta canonical:t7 +156.97GiB/24h; codex_sqlite_wal_critical optional Telegram guardrail at 20GiB
Tentativi_effettuati=du/find/lsof/sqlite quick_check/integrity_check/wal_checkpoint; stale Codex processes terminated by previous session; after-codex watcher recovered 163682495352 bytes; prompt_938274 PRAGMA/lsof/log aggregation confirmed WAL mode, autocheckpoint default 1000, current Codex holder, and no single runaway error loop.
Soluzione_finale=/home/daniele/.local/bin/codex-sqlite-wal-maintenance plus codex-sqlite-wal-maintenance.timer every 30min; script logs UTC/Z, checks quick_check, classifies soft/hard/critical thresholds, attempts SQLite-safe wal_checkpoint(TRUNCATE) at hard threshold, reports before/after bytes, detects holders, and never rm's open WAL.
Commit_correlati=none
Prompt_correlati=482917,731584,938274
Tempo_totale_di_impatto=about 2026-06-13T15:56Z onward until WAL truncation after Codex closes
Note=Postmortem values: journal_mode=wal; wal_autocheckpoint=1000; synchronous=2; page_size=4096; page_count=82970; freelist_count=12001; quick_check=ok. Incident cleanup recovered 152.44GiB because WAL frames were checkpointable and TRUNCATE released the sidecar file allocation, not because Codex sessions/config/transcripts were deleted. Forbidden: rm open WAL/SHM, pkill/killall codex generic, deleting .codex sessions/config/credentials.

INCIDENT:
Incident_ID=MTT_AUTOEXPORT_THROTTLE_SKIPPED_PENDING_MUTATION
Titolo=MultiTimeTracker autoexport pending mutation could be skipped by legacy throttle
Data_prima_comparsa_UTC=2026-06-15T00:00:00Z
Data_ultima_comparsa_UTC=2026-06-15T00:00:00Z
Numero_occorrenze=1
Gravita_massima=HIGH
Stato=RESOLVED
Root_cause=Autoexport requests were serialized only by call timing; when a persistent mutation arrived during an export, the follow-up request could be suppressed by SqliteVault EXPORT_THROTTLE_MS because the first export success timestamp was newer than the mutation.
Sistemi_coinvolti=MultiTimeTracker Android app; SQLite SAF autoexport; PersistentMutationTracker; SqliteVault
Alert_coinvolti=none
Tentativi_effettuati=Targeted TCL deviceTest for in-flight mutation timed out; code audit found throttle path; autoexport queue now calls SqliteVault export with force=true and loops until last_successful_export_at covers last_database_mutation_at.
Soluzione_finale=PersistentMutationTracker single-flight queue with 1200 ms debounce, pending_export follow-up loop, sync metadata excluded from mutation tracking, and forced queued exports that bypass legacy throttle while keeping manual throttle behavior.
Commit_correlati=b612da3
Prompt_correlati=947381
Tempo_totale_di_impatto=unknown pre-fix; detected during 2026-06-15 validation before release
Note=TCL targeted deviceTest rerun passed 7/7 after fix; this incident is app-local, not a host monitoring alert.

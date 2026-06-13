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

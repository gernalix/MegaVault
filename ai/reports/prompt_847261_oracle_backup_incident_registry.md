# Prompt 847261 Oracle Backup Root Cause + Incident Registry

date_utc=2026-06-13
scope=oracle-backup-service;OCI StorageLimitExceeded;Incident Registry
host=ubuntu@150.230.148.128

ROOT_CAUSE:
primary=OCI Object Storage tenancy/bucket remains write-blocked by StorageLimitExceeded.
bucket=oci:bucket-20260206-0730
usage=7474 objects;22.262 GBytes;23903533548 bytes;assumed_limit=22GiB;critical=21GiB
dominant_prefix=oraclevm 22.223GBytes;oraclevm/data 22.222GBytes
remote_snapshots=837;host=instance-20260201-1126;tags=oracle-vm,autosnap-5min;oldest=2026-05-02T01:33:03Z;newest=2026-05-05T05:27:01Z
remote_repo_health=corrupt_or_unindexed;oraclevm/index objects=0;restic_check_no_lock reports unreferenced packs, missing trees, repository contains errors
why_retention_not_applied=standard restic retention needs lock/index writes; OCI rejects writes; no safe non-destructive prune/rebuild without quota headroom

LOCAL_FIX:
changed=backup.sh preflights remote/fallback before SQLite snapshots
changed=remote unavailable forces SQLite stream-to-restic, no retained disk snapshot
changed=stream auto threshold uses total DB bytes + margin + root floor
changed=LOCAL_FALLBACK_KEEP_LAST 11;LOCAL_FALLBACK_MAX_GB 7;SQLITE_SNAPSHOTS_RETENTION_COUNT 0;SQLITE_SNAPSHOTS_MIN_KEEP 0
changed=sticky last_backup_status fixed so successful fallback remains REMOTE_DEGRADED after quota/retention update
changed=check_backup_health.py and oracle-backup-healthcheck.sh write incident registry events
new=incident_registry.py with SQLite tables incidents and incident_events

CLEANUP:
target=/var/lib/oracle_backup/emergency_repo local only
deleted=local fallback snapshot 40c19232 from 2026-06-13T01:04:22Z;retained complete stream run from 2026-06-12T23:01..23:04Z before new successful run
deleted=retained on-disk sqlite snapshot /var/lib/oracle_backup/sqlite_snapshots/20260613_010030 via prune_local_snapshots.sh after policy set count=0,min_keep=0
remote_deleted=no

VALIDATION:
backup_manual=rc 0;REMOTE_DEGRADED;fallback=/var/lib/oracle_backup/emergency_repo
root_after=/dev/sda1 45G 30G used 16G free 66%
sqlite_snapshots_after=40K
emergency_repo_after=4.8G
local_fallback_quota=OK;repo 4.71GiB < soft 5.60GiB hard 7.00GiB
healthcheck_dry_run=rc 0;WARNING REMOTE_DEGRADED;root/local quota OK
monitor_dry_run=rc 0;WARNING REMOTE_DEGRADED
remote_quota_service=SUCCESS;state CRITICAL 22.262GBytes
systemd=all oracle-backup timers active;all oracle-backup services not failed after reset

INCIDENTS:
db=/home/ubuntu/sync_root/db/incident_registry.sqlite
created=OCI_STORAGE_LIMIT_EXCEEDED OPEN first_seen=2026-06-05T06:07:00Z occurrence_count=20
created=OCI_REMOTE_REPOSITORY_CORRUPT OPEN first_seen=2026-06-13T13:42:59Z occurrence_count=1
created=ORACLE_ROOT_DISK_PRESSURE RESOLVED first_seen=2026-06-12T17:58:57Z occurrence_count=2
events=23 after retrofill

FINAL_REMOTE_STATUS:
storage_limit_resolved=no
reason=OCI still rejects writes and quota monitor still reports CRITICAL; safe technical elimination requires quota/headroom or new object-storage capacity. Destructive alternative is reset/delete corrupt remote prefix and reinitialize, but that destroys existing remote backup objects and was not performed.

RUNTIME_BACKUP:
backup_dir=/opt/oracle_backup/backups/prompt847261-20260613T135434Z
cleanup_log=/home/ubuntu/maintenance-847261/logs/local_cleanup_20260613T135641Z.log
reports=/home/ubuntu/maintenance-847261/reports/

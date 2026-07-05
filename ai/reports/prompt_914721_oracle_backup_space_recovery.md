# Prompt 914721 Oracle Backup Space Recovery

scope=Oracle VM disk pressure;oracle-backup-service;runtime_change=yes;docs_update=yes
host=ubuntu@150.230.148.128
date=2026-06-12

DISCOVERY:
root_before=/dev/sda1 48274628608B used=48257851392B available=0B use=100%
emergency_repo=/var/lib/oracle_backup/emergency_repo size_before=16G disk, data=16G, index=11M, snapshots=376K, locks=4K
sqlite_snapshots=/var/lib/oracle_backup/sqlite_snapshots size_before=5.0G disk;child=/var/lib/oracle_backup/sqlite_snapshots/20260608_180131 size=5292109824B files=10
strano_anello=/home/ubuntu/db/strano_anello.db 5282144256B + WAL/SHM + code 401353954B; live process observed; not touched
remote_oci=CRITICAL;path=oci:bucket-20260206-0730;used=22.262GBytes;error=StorageLimitExceeded
fallback=required;last_successful_repo=/var/lib/oracle_backup/emergency_repo;last_backup_status=REMOTE_DEGRADED

DECISION:
selected=move_verified_retained_sqlite_snapshot_then_delete_source
reason=lowest-risk reversible cleanup; snapshot static and duplicated to Seagate before removal; emergency_repo is active fallback and not safe to remove
not_selected=delete_or_move_emergency_repo because fallback is currently required while remote OCI is degraded
not_selected=migrate_strano_anello because DB is live and smaller recovery than backup area

ACTION:
backup_dest=/media/daniele/Seagate6TB2/oracle-vm-offloads/prompt_914721_20260612T175857Z/sqlite_snapshots/20260608_180131
copy=ssh sudo tar stream to Seagate;no temp file on VM;preserved numeric owner, permissions, timestamps
verify=remote/local manifest entries 11;remote/local sha256 rows 10;sha256 files identical
delete=removed only /var/lib/oracle_backup/sqlite_snapshots/20260608_180131 after verification
rollback=copy verified Seagate directory back to /var/lib/oracle_backup/sqlite_snapshots/20260608_180131 with sudo tar or cp -a, restore owner/mode from manifest if needed

POST:
root_after=/dev/sda1 48274628608B used=39361404928B available=8896446464B use=82%
sqlite_snapshots_after=40K
emergency_repo_after=12G disk after automatic local fallback retention
backup_after=automatic oracle-backup.service ran after space recovery, remote failed with StorageLimitExceeded, local fallback completed REMOTE_DEGRADED
markers_after=last_any_success_epoch=1781290301;last_local_fallback_success_epoch=1781290301;last_backup_status=REMOTE_DEGRADED;last_successful_repo=/var/lib/oracle_backup/emergency_repo
timers_after=oracle-backup.timer,oracle-backup-monitor.timer,oracle-backup-healthcheck.timer,oracle-backup-localprune.timer,oracle-backup-prune.timer,oracle-backup-remote-quota.timer active

RISKS:
risk=OCI remote still full;mitigation=do not delete emergency_repo or run no-lock remote prune without explicit quota/remediation plan
risk=Seagate backup is local to Mint host, not VM;mitigation=path documented and checksums retained outside MegaVault
risk=oracle-backup-service repo local worktree was dirty before task;mitigation=not touched

LINKS:
ai_doc=../projects/oracle-backup-service.md
human_changelog=../../human/projects/oracle-backup-service/changelog.md

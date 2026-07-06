# Strano Anello Decommission Report

Status: PASS
Created: 2026-07-05 16:34 Europe/Copenhagen
Finalized: 2026-07-05 16:52 Europe/Copenhagen
Target: ubuntu@150.230.148.128 / instance-20260201-1126
Protocol: C:\Users\seste\Documents\megavault_content_aware_merge_20260705\ai\MEGAVAULT_PROTOCOL.md
Evidence bundle: C:\Users\seste\Documents\vm oracle\strano_decommission_evidence\
Primary logs:
- pre-delete audit: C:\Users\seste\Documents\vm oracle\strano_decommission_evidence\strano_anello_decommission_audit_20260705_142651\
- removal transcript: C:\Users\seste\Documents\vm oracle\strano_decommission_evidence\strano_remove_remote_20260705_1636.log
- active ref cleanup: C:\Users\seste\Documents\vm oracle\strano_decommission_evidence\strano_active_ref_cleanup_20260705_1644.log
- healthcheck cleanup: C:\Users\seste\Documents\vm oracle\strano_decommission_evidence\strano_healthcheck_cleanup_20260705_1646.log
- final verification/inventory: C:\Users\seste\Documents\vm oracle\strano_decommission_evidence\strano_final_inventory_20260705_1650.log

## Summary
`strano_anello` has been removed from the Oracle VM as an active project. Dedicated code, SQLite DB/WAL/SHM, log directory, dedicated systemd service/timer, timer state, draft unit files, project zip, and dedicated manual DB backup were deleted after pre-delete inventory and dry-run/stat checks.

Shared services were not removed. Datasette was edited and restarted with only the `/home/ubuntu/db/strano_anello.db` argument removed. Oracle backup healthcheck and DB sanity scripts were edited to remove Strano-specific allow/monitoring logic. Post-delete checks found no active Strano references in systemd, cron, Docker, processes/open files, Datasette config, active DB sanity script, active Oracle backup healthcheck script, or active Oracle backup state JSON.

Historical multi-project diagnostics/backups still contain old textual references and were not touched because they are global evidence archives, not active Strano components.

## Host Profile
- Hostname: `instance-20260201-1126`
- OS: Ubuntu 22.04.5 LTS, kernel `6.8.0-1054-oracle`, x86_64 KVM VM
- User/home/shell: `ubuntu`, `/home/ubuntu`, `/bin/bash`
- Sudo: passwordless sudo available for `ubuntu`
- Root filesystem: `/dev/sda1` ext4, final `45G` total, `24G` used, `22G` free, `53%`
- Docker: installed; only container found is `uptime-kuma`
- DB engines: SQLite files present; no active Postgres/MySQL Strano objects found; MySQL client absent; no `postgres` user

## Pre-delete Inventory
| Resource | Type | Size | Owner | Modified | Evidence | Risk |
|---|---:|---:|---|---|---|---|
| `/etc/systemd/system/strano-anello.service` | service | 346 B | root:root | 2026-06-29 15:31 UTC | name, Description, WorkingDirectory, ExecStart | Low |
| `/etc/systemd/system/strano-anello.timer` | timer | 231 B | root:root | 2026-06-29 15:31 UTC | name and Unit target | Low |
| `/var/lib/systemd/timers/stamp-strano-anello.timer` | timer state | 0 B | root:root | 2026-07-05 14:32 UTC | systemd state for dedicated timer | Low |
| `/home/ubuntu/bots/strano_anello` | code+venv+data+logs | 509M | ubuntu:ubuntu | 2026-06-29 14:50 UTC | project root, Git repo, script, tests, tools, logs | Medium, dedicated |
| `/home/ubuntu/db/strano_anello.db` | SQLite DB | 2,400,256 B | ubuntu:ubuntu | 2026-07-05 14:21 UTC | service and Datasette DB path | Medium, dedicated |
| `/home/ubuntu/db/strano_anello.db-wal` | SQLite WAL | 5,022,312 B | ubuntu:ubuntu | 2026-07-05 14:33 UTC | WAL for dedicated DB | Medium, dedicated |
| `/home/ubuntu/db/strano_anello.db-shm` | SQLite SHM | 32,768 B | ubuntu:ubuntu | 2026-07-05 14:33 UTC | SHM for dedicated DB | Medium, dedicated |
| `/home/ubuntu/strano-anello.service.new` | draft unit | 347 B | ubuntu:ubuntu | 2026-04-01 01:09 UTC | name/content dedicated | Low |
| `/home/ubuntu/strano-anello.timer.new` | draft unit | 231 B | ubuntu:ubuntu | 2026-04-01 01:09 UTC | name/content dedicated | Low |
| `/home/ubuntu/strano_anello_oracle_v1.zip` | project archive | 10,703 B | ubuntu:ubuntu | 2026-02-06 12:09 UTC | dedicated name | Low |
| `/var/lib/oracle_backup/manual_db_backups/strano_anello.pre-maintenance-20260629T145430Z.db.zst` | dedicated DB backup | 168,019,218 B | ubuntu:ubuntu | 2026-06-29 14:58 UTC | dedicated backup filename | Medium, dedicated |
| Datasette ExecStart DB arg | shared service reference | n/a | systemd/root | active | Datasette had open handles to Strano DB | Medium, edit-only |
| `/usr/local/bin/db_sanity_check.sh` Strano allow | shared script reference | n/a | root:root | active | allow exception for removed DB | Medium, edit-only |
| `/usr/local/bin/oracle-backup-healthcheck.sh` Strano growth block | shared script reference | n/a | root:root | active | monitored removed DB | Medium, edit-only |

## Actions Taken
1. Read mandatory MegaVault protocol and host profile.
2. Verified SSH access with maintenance key and passwordless sudo.
3. Ran read-only pre-delete audit covering host, systemd, cron, Docker, venvs, DB files, backup candidates, logs, and Strano text/path refs.
4. Created this Markdown report before deletion.
5. Stopped/disabled `strano-anello.timer`; stopped `strano-anello.service`.
6. Removed `/home/ubuntu/db/strano_anello.db` from Datasette base unit and drop-in, reloaded systemd, restarted Datasette.
7. Removed dedicated Strano units/state/files/code/DB/backup/archive.
8. Removed Codex-created remote audit temp files after copying evidence locally.
9. Removed active Strano references from `db_sanity_check.sh`, `oracle-backup-healthcheck.sh`, and active Oracle backup state JSON.
10. Ran final verification and final VM project/script inventory.

## Deleted / Quarantined Items
Deleted:
- `/etc/systemd/system/strano-anello.service`
- `/etc/systemd/system/strano-anello.timer`
- `/etc/systemd/system/timers.target.wants/strano-anello.timer` via `systemctl disable --now`
- `/var/lib/systemd/timers/stamp-strano-anello.timer`
- `/home/ubuntu/bots/strano_anello`
- `/home/ubuntu/db/strano_anello.db`
- `/home/ubuntu/db/strano_anello.db-wal`
- `/home/ubuntu/db/strano_anello.db-shm`
- `/home/ubuntu/strano-anello.service.new`
- `/home/ubuntu/strano-anello.timer.new`
- `/home/ubuntu/strano_anello_oracle_v1.zip`
- `/var/lib/oracle_backup/manual_db_backups/strano_anello.pre-maintenance-20260629T145430Z.db.zst`
- temporary audit/removal scripts and audit tar/directory under `/home/ubuntu` created by this task

Quarantined: none. All removed items were clearly dedicated; ambiguous global artifacts were left untouched.

## Services/Cron/Docker Changes
- Removed: `strano-anello.service`, `strano-anello.timer`.
- Edited: `datasette.service` and `/etc/systemd/system/datasette.service.d/override.conf` to remove only the Strano DB argument.
- Datasette final state: active/running, serving `/home/ubuntu/sync_root/db/*.db` only.
- Cron: no Strano user/root `/etc/cron*` refs found before or after.
- Docker: no Strano containers/images/volumes/networks found. Existing `uptime-kuma` container left untouched.

## Database Changes
- Deleted dedicated SQLite DB trio: `/home/ubuntu/db/strano_anello.db`, `-wal`, `-shm`.
- Removed active Oracle backup healthcheck metrics/alerts for `strano_anello_growth` from state JSON.
- No Postgres/MySQL Strano DB/schema/table/user was found.
- Shared DBs in `/home/ubuntu/sync_root/db` and `/opt/uptime-kuma/data` were not touched.

## Post-delete Verification
Final verification showed `ABSENT` for every deleted target path listed above.

No active matches were returned for:
- systemd service/timer units and unit files matching Strano
- `systemctl cat datasette.service` Strano refs
- active `/usr/local/bin/oracle-backup-healthcheck.sh`
- active `/usr/local/bin/db_sanity_check.sh`
- active `/var/lib/oracle_backup/healthcheck_alert_state.json`
- active `/var/lib/oracle_backup/healthcheck_state.json`
- process list and `lsof`
- user/root cron and `/etc/cron*`
- Docker containers/images/volumes/networks

Health checks:
- `datasette.service`: active
- `oracle-backup-healthcheck.sh` dry-run: OK for root usage/free, SQLite snapshots, local fallback quota, emergency repo, retention; WARNING remains for remote quota degraded/fallback valid (`StorageLimitExceeded`), unrelated to Strano.

## Remaining VM Projects/Scripts Inventory
| Name estimated | Main path | Stack | Entrypoints/scripts | systemd/cron/docker | DB association | Updated | State |
|---|---|---|---|---|---|---|---|
| oracle-backup-service | `/opt/oracle_backup` | Bash/Python/restic | `backup.sh`, `check_backup_health.py`, `check_remote_quota.py`, `oracle-backup-healthcheck.sh`, prune scripts | `oracle-backup*` services/timers active/waiting | `/var/lib/oracle_backup/*`, incident registry SQLite | 2026-07-05 active script edits | active, remote degraded warning |
| oracle-uptime-kuma | `/opt/uptime-kuma` | Docker Compose/Node | `docker-compose.yml`, scripts under `/opt/uptime-kuma/scripts` | Docker container `uptime-kuma`, port `127.0.0.1:3002->3001` | `/opt/uptime-kuma/data/kuma.db` | 2026-07-05 DB active | active |
| Datasette multi-db | `/home/ubuntu/sync_root/bots/telegram_insert_bot-master` | Python/Datasette | Datasette CLI via systemd, `db_sanity_check.sh` | `datasette.service`, `cloudflared-datasette.service` | `/home/ubuntu/sync_root/db/*.db` | 2026-07-05 config edit | active |
| Telegram Insert Bot | `/home/ubuntu/sync_root/bots/telegram_insert_bot-master` | Python | `telegram_insert_bot.py`, `run_bot.sh`, seed/rebuild scripts | `telegram-insert-bot.service` | `telegram_bot_db.db` | 2026-04-13/2026-07 DB | active |
| OwnTracks HTTP Server | `/home/ubuntu/bots/owntracks_http_server` | Python/Flask | `owntracks_http_server.py` | `owntracks-http-server.service` | `owntracks.db` | 2026-07-05 DB | active |
| Software audit / mint-update-tracker | `/opt/software-audit` | Python/systemd | `mint_update_tracker.py` | `software-audit.service`, `software-audit-backfill.timer` | `software_audit.db` | 2026-07-04 DB | active |
| Codex weekly limit monitor | `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor` | Python/systemd | `codex_weekly_limit_watcher.py` | `codex-weekly-limit-monitor.service` | not detected | 2026-07-05 | active |
| Codex usage monitor | `/home/ubuntu/codex-workspace/codex-usage-monitor` | Python/systemd user files | `codex_usage_monitor.py`, `codex_cli_status_watcher.py` | user unit files present | `codex_usage.sqlite3` | 2026-07-05 DB | incerto/user-managed |
| oracle-time-triggers | `/opt/oracle_time_triggers`, `/home/ubuntu/oracle_time_triggers_v1` | Python/systemd | `apply_time_triggers.py` | `oracle-time-triggers.timer` active/waiting | sync_root SQLite DBs | 2026-02-06 | active timer |
| Workflowy import | `/opt/workflowy_import` | Python/systemd | `workflowy_job.py` | `workflowy-import.timer` active/waiting | `workflowy.db` | 2026-06-29 DB | scheduled/inactive service |
| Logseq updates | `/opt/logseq_updates` | Python/systemd | `logseq_updates.py` | `logseq-updates.timer` active/waiting | not detected | 2026-03-28 repo | scheduled/inactive service |
| Telegram media monitor | `/opt/telegram-media-monitor` | Python/Bash/systemd | `telegram_media_monitor_service.py`, `run_monitor.sh` | `telegram-media-monitor.timer` active/waiting | not detected | 2026-04-19 | scheduled/inactive service |
| Amici FB | `/home/ubuntu/bots/amici_fb` | Python/systemd files | `amici_fb.py`, `amici-fb.service`, `amici-fb.timer` | unit files in project; not active in system summary | `amici_fb.sqlite3` | 2026-02-20 DB | incerto/inactive |
| yt-dlp downloader | `/home/ubuntu/bots/yt_dlp_downloader_oracle_ubuntu` | Python/systemd files | `yt_dlp_downloader.py`, watcher, install script | project systemd file present | `/home/ubuntu/db/yt_dlp_oracle_ubuntu.db` and `yt_dlp.db` | 2026-03-11 | incerto |
| Unner importer | `/opt/unner_importer` | Python | `importer.py`, plugins | no active unit found | not detected | 2026-03-28 repo | incerto |
| NVM | `/home/ubuntu/.nvm` | shell/Node tooling | `nvm.sh`, install/test scripts | none found | none | 2026-04-13 | tooling |
| Pornobot | `/home/ubuntu/sync_root/bots/porno_bot` | Python | `porno_downloader.py`, `telegram_porno_bot.py` | no active unit found in final summary | `porno.db` | 2026-07-05 DB | incerto |
| Telegram bot small | `/home/ubuntu/sync_root/bots/telegram_bot` | Python | `bot.py` | no active unit found | venv only; DB not distinct | 2026-02-01 | incerto |
| Oracle maintenance standalone | `/home/ubuntu/*.py`, `/home/ubuntu/*.sh`, `/usr/local/bin/oracle-backup-healthcheck.sh` | Bash/Python | OCI abort/inspect, restic emergency, prune/repair scripts | mostly manual; oracle backup units use some | oracle backup state | 2026-07-05 active script edits | mixed/manual |
| Historical snapshots/diagnostics | `/home/ubuntu/oracle_snapshot_20260206_013958`, `/home/ubuntu/maintenance-*`, `/home/ubuntu/oracle-backup-diagnostics` | mixed archives | copied scripts/reports | not active | archived DB/script copies | historical | inactive/archive |

Raw complete listings are in `strano_final_inventory_20260705_1650.log` sections `project markers`, `standalone scripts`, `python venvs`, `databases`, `service/timer summary`, and `docker summary`.

## Ambiguities / Risks
Not touched because global/historical/multi-project, not active Strano components:
- `/home/ubuntu/maintenance-*` reports/logs containing old Strano references.
- `/home/ubuntu/oracle-backup-diagnostics/*` historical diagnostic bundles containing old Strano references.
- `/opt/oracle_backup/backups/*` backup copies of global backup scripts with old Strano healthcheck code.
- `/usr/local/bin/*.bak*` historical script backups containing old Strano references.
- System journal historical lines were not purged.

Known unrelated warning after completion:
- Oracle backup remote target remains degraded because remote quota is full; local fallback is valid. This predates and is unrelated to Strano removal.

## Follow-up Recommendations
1. If the policy becomes "purge historical references too", review and separately approve deletion or archival of global maintenance/diagnostic bundles; they contain non-Strano evidence and were intentionally left untouched.
2. Refresh MegaVault global registries (`SERVICE_REGISTRY`, `DATA_REGISTRY`, project indexes) if they still list Strano as live.
3. Monitor the next `oracle-backup-healthcheck.timer` and `datasette.service` cycle; the manual dry-run already passed after cleanup.

## Commands Used For Verification
Representative commands:
```bash
systemctl list-units --all --type=service --type=timer --no-pager --plain | grep -Ei 'strano|anello' || true
systemctl list-unit-files --type=service --type=timer --no-pager --plain | grep -Ei 'strano|anello' || true
systemctl cat datasette.service --no-pager | grep -nEi 'strano[_ -]?anello|strano anello|stranoanello' || true
sudo grep -RInEi 'strano[_ -]?anello|strano anello|stranoanello|STRANO' /usr/local/bin/oracle-backup-healthcheck.sh /usr/local/bin/db_sanity_check.sh /var/lib/oracle_backup/healthcheck_alert_state.json /var/lib/oracle_backup/healthcheck_state.json || true
ps -eo pid,user,comm,args | grep -Ei 'strano[_ -]?anello|strano anello|stranoanello' | grep -v grep || true
sudo lsof | grep -Ei 'strano[_ -]?anello|strano anello|stranoanello' || true
crontab -l; sudo crontab -l; sudo grep -RInEi 'strano[_ -]?anello|strano anello|stranoanello' /etc/cron* /var/spool/cron /var/spool/cron/crontabs || true
sudo docker ps -a --no-trunc; sudo docker images --no-trunc; sudo docker volume ls; sudo docker network ls
sudo ORACLE_BACKUP_HEALTHCHECK_DRY_RUN=1 ORACLE_BACKUP_HEALTHCHECK_SAVE_DRY_RUN_STATE=0 /usr/local/bin/oracle-backup-healthcheck.sh
df -hT /
```

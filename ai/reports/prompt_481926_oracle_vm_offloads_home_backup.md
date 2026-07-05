# prompt_481926 oracle-vm-offloads home-backup inclusion

date=2026-06-22
host=daniele-Surface-Pro
scope=home-incremental-backup extra source addition
protocol=../MEGAVAULT_PROTOCOL.md
host_profile=../global/HOST_PROFILE.md

SUMMARY:
objective=permanently include /media/daniele/Seagate6TB2/oracle-vm-offloads in rsync home backups
source=/media/daniele/Seagate6TB2/oracle-vm-offloads
source_size=5.0G;dry_run_total_bytes=5292109458
source_files=22 total;18 regular;4 dirs
critical_files=18 matched .db,.sqlite,.sqlite3,manifest,sha256 patterns
destination_root=/media/daniele/Seagate6TB2/home-backups
snapshot_destination=external/oracle-vm-offloads
space_available=2.7T on /dev/sdc1 ext4 /media/daniele/Seagate6TB2

ARCHITECTURE:
service=home-incremental-backup.service user
timer=home-incremental-backup.timer user;OnCalendar=03:40;RandomizedDelaySec=2h;Persistent=true
runner=/home/daniele/home_incremental_backup.sh
config=/home/daniele/.config/home-backup/home-backup.env
docs=/home/daniele/backup_docs
method=rsync -aAX --numeric-ids --one-file-system --partial --stats --info=progress2 --bwlimit=$HOME_BACKUP_BWLIMIT_KB
normal_source=/home/daniele
extra_sources_config=HOME_BACKUP_EXTRA_SOURCES colon-separated list
extra_source_flow=after normal /home/daniele chunks;copy each source into external/<basename>
extra_link_dest=uses previous snapshot external/<basename> when present

CHANGE:
config_before=no HOME_BACKUP_EXTRA_SOURCES
config_after=HOME_BACKUP_EXTRA_SOURCES="/media/daniele/Seagate6TB2/oracle-vm-offloads"
script_change=added extra_sources_list, preflight validation, run_rsync_extra_source, and extra-source loop after normal chunks
docs_change=backup_docs architecture/config/operations/changelog updated
megavault_docs=DATA_REGISTRY updated;this report added

EXCLUDES:
excluded_critical_extensions=none
verified_no_exclude=.db,.sqlite,.sqlite3,manifest,sha256
existing_noise_excludes=cache,node_modules,trash,browser_cache,build_tmp,sockets,locks,download_images

VALIDATION:
syntax=bash -n live+backup_docs copies PASS
live_doc_copy=cmp live script and backup_docs/bin copy PASS
source_exists=yes
destination_exists=yes
dry_run_full_home=bounded 15m official dry-run started and exercised normal /home chunks;timeout before extra source due full home traversal
dry_run_extra_direct=PASS;rsync --dry-run to snapshots/.dry-run-481926/external/oracle-vm-offloads reported 18 regular files,0 deletes,total size 5292109458 bytes
dry_run_script_targeted=PASS with temporary config;source /tmp/home-backup-empty-481926;extra source real;log showed EXTRA_SOURCE_START,EXTRA_SOURCE_DONE,SUCCESS dry-run;transferred_bytes=5292109458
cleanup=removed only dry-run temporary directories .dry-run-481926 and .incomplete-20260622084208-3993124;targeted script dry-run removed its own temporary snapshot

CURRENT_RUN:
home-incremental-backup_active=no before change
include_current_run=no active home-backup run existed;change applies to next automatic cycle and manual runs
surface_export_rsync=separate prompt #914762 still running to Seagate 4TB;not part of home-backup architecture

RESULT:
status=applied_for_future_runs
future_backup=yes
restore_path_pattern=/media/daniele/Seagate6TB2/home-backups/snapshots/<timestamp>/external/oracle-vm-offloads

VERSION=5
STATUS=MANDATORY_STANDARD
MODE=codex_first
FORMAT=ultracompressed
AUTHORITY=global_incident_registry

META:
scope=all MegaVault projects
ai_doc=ai/global/INCIDENT_REGISTRY.md
human_doc=human/global/INCIDENT_REGISTRY.md
sqlite_default=/home/daniele/sync_root/db/incident_registry.sqlite
override=INCIDENT_REGISTRY_DB
global_rule=keep_global_schema_and_cross_project_index_here
project_incident_ai=docs/ai/INCIDENT_REGISTRY.md
project_incident_human=docs/human/INCIDENT_REGISTRY.md
project_specific_existing_entries=premigration_debt;migrate_to_owner_project_docs_after_repo_verified

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

INCIDENT:
Incident_ID=CODEX_WEEKLY_LIMIT_MONITOR_PROLITE_DECODE
Titolo=Oracle VM Codex weekly limit monitor failed on prolite plan decode and Telegram hardcoded helper
Data_prima_comparsa_UTC=2026-06-11T06:27:26Z
Data_ultima_comparsa_UTC=2026-07-05T14:25:21Z
Numero_occorrenze=recurring_every_poll_until_fix
Gravita_massima=HIGH
Stato=RESOLVED
Root_cause=Runtime service used /opt/codex-native/bin/codex 0.120.0; account/rateLimits/read failed when ChatGPT wham usage returned plan_type=prolite, while the watcher logged the raw error body and treated valid quota data as failure. Telegram delivery also depended on legacy hardcoded values inside /home/ubuntu/telegram_notify.py while config/env only had placeholders.
Sistemi_coinvolti=Oracle VM instance-20260201-1126; codex-weekly-limit-monitor.service; /home/ubuntu/codex/automazione/codex_weekly_limit_monitor; /home/ubuntu/telegram_notify.py; /etc/codex-weekly-limit-monitor.env
Alert_coinvolti=Codex weekly token limit monitor Telegram notifications; local codex weekly usage log/state
Tentativi_effettuati=Identified systemd service, no cron; inspected app logs, journal, process tree, config placeholders, Codex binaries, network/DNS/TLS reachability, helper imports, dry-run config, and Telegram delivery path without printing secrets.
Soluzione_finale=Switched config to /usr/bin/codex 0.137.0; added normal rateLimits parser plus wham/usage snake_case fallback; sanitized log/state errors; replaced /home/ubuntu/telegram_notify.py with env-based compatible helper; migrated Telegram token/chat from legacy hardcoded helper into /etc/codex-weekly-limit-monitor.env mode 600; set module_path to the safe helper; redacted monitor logs/state/helper backups; restarted service.
Commit_correlati=894b880
Prompt_correlati=codex_weekly_limit_monitor_vm_fix_20260705
Tempo_totale_di_impatto=At least 2026-06-11T06:27:26Z to 2026-07-05T14:25:21Z based on journal/log evidence
Note=Post-fix live state: service enabled+active, weekly_left=64.0, five_hour_left=94.0, last_error empty, Telegram notification sent. Security scan in monitor perimeter found zero email/user_id/telegram_bot_url/literal_bot_token matches after redaction. Residual out-of-scope risk: other VM Telegram helper copies may still be hardcoded and require separate migration.

INCIDENT:
Incident_ID=CODEX_WEEKLY_LIMIT_MONITOR_WRONG_5H_SOURCE
Titolo=Oracle VM Codex quota monitor used Spark 5h limit instead of main shared 5h limit
Data_prima_comparsa_UTC=2026-07-05T16:02:07Z
Data_ultima_comparsa_UTC=2026-07-05T16:13:00Z
Numero_occorrenze=1_confirmed_runtime_window
Gravita_massima=MEDIUM
Stato=RESOLVED
Root_cause=The 5h parser selected rateLimitsByLimitId.codex_bengalfox.primary, which is the separate GPT-5.3-Codex-Spark limit shown at 100 percent in Codex Analytics, instead of the main shared Codex 5h limit exposed as rateLimits.primary.
Sistemi_coinvolti=Oracle VM instance-20260201-1126; codex-weekly-limit-monitor.service; /home/ubuntu/codex/automazione/codex_weekly_limit_monitor; Codex Analytics; Telegram quota notifications
Alert_coinvolti=Codex weekly left changed Telegram notification with incorrect 5h field; codex_weekly_limit_monitor runtime logs/state
Tentativi_effettuati=Compared user Codex Analytics screenshot against live app-server payload, systemd journal, state JSON, and parser tests; verified weekly at 57 percent and main 5h at 49 percent while codex_bengalfox/Spark stayed at 100 percent.
Soluzione_finale=Mapped main 5h to rateLimits.primary (or normalized wham rate_limit.primary_window), removed codex_bengalfox as source for main 5h, kept telegram_notify.py as sole Telegram helper, ignored previous 5h state when source changes, added anti-Spark parser test, deployed with backups, restarted service.
Commit_correlati=this_MegaVault_report_commit
Prompt_correlati=codex_weekly_limit_monitor_wrong_5h_source_20260705
Tempo_totale_di_impatto=about 11 minutes for the confirmed Spark-source runtime window; earlier user-observed 5h mismatch triggered the investigation and is covered by the same final parser correction.
Note=Post-fix evidence: dry-run and real service run both read five_hour_left=49 percent and weekly_left=57 percent from rateLimits.primary/rateLimits.secondary; user screenshot after fix showed the same values. First post-fix notification marks previous 5h as unavailable because the stored previous source was Spark and must not be compared to the main quota.

INCIDENT:
Incident_ID=EXTERNAL_NTFS_DISCONNECT_DURING_MOUNTED_IO
Titolo=External NTFS volume disappeared during mounted I/O
Data_prima_comparsa_UTC=2026-07-09T17:07:00Z
Data_ultima_comparsa_UTC=2026-07-09T17:07:10Z
Numero_occorrenze=1 incident with repeated I/O symptoms coalesced
Gravita_massima=CRITICAL
Stato=OPEN
Root_cause=UNKNOWN; cable,power path,or device instability requires physical inspection
Sistemi_coinvolti=Fedora host; external mounted NTFS volume; udisks2; ntfs-3g; Fedora System Monitor
Alert_coinvolti=disk_io_error;unsafe_device_removal;Uptime Kuma Fedora Storage monitor ID 40
Tentativi_effettuati=Journal reconstruction,current mount check,non-destructive SMART/NVMe collection,cursor-idempotent backfill,and stable device identity enrichment
Soluzione_finale=No root-cause repair yet; permanent event capture,critical alert,category heartbeat,and reconnect recovery mitigate observability risk
Commit_correlati=fedora-system-monitor activity 593184
Prompt_correlati=593184
Tempo_totale_di_impatto=approximately 10 seconds until observed remount
Note=No physical disconnect or destructive reproduction was attempted; device serial and filesystem UUID are intentionally omitted from documentation; project source=/home/daniele/MegaVault/projects/fedora-system-monitor/docs/ai/INCIDENT_REGISTRY.md

INCIDENT:
Incident_ID=T7_MOUNTPOINT_FELL_THROUGH_TO_INTERNAL_ROOT
Titolo=T7 fstab mountpoint existed on internal root while external device was absent
Data_prima_comparsa_UTC=2026-07-11T23:09:00Z
Data_ultima_comparsa_UTC=2026-07-11T23:09:00Z
Numero_occorrenze=1 confirmed preflight state
Gravita_massima=CRITICAL
Stato=RESOLVED
Root_cause=The nofail fstab entry allowed boot without T7; the persistent /mnt/T7_BACKUP directory then resolved to internal Btrfs and directory existence alone could not prove the external mount.
Sistemi_coinvolti=Fedora host; Samsung T7; /mnt/T7_BACKUP; fedora-t7-backup
Alert_coinvolti=journal nonzero backup job; no external notification configured
Tentativi_effettuati=Live findmnt+lsblk+udev+UUID+label+serial inventory; isolated mount-namespace missing-device simulation; internal entry count before/after.
Soluzione_finale=Every operation requires separate mountpoint, ext4, expected UUID+label, persistent by-id serial/model,parent-disk match,and device number different from root before credential or repository access.
Commit_correlati=fedora-t7-backup activity 583921
Prompt_correlati=583921
Tempo_totale_di_impatto=no backup write occurred; unsafe state detected before implementation
Note=Isolated absent simulation exited 21 and preserved internal entry count 0 to 0; subsequent real T7 backup succeeded; project source=/home/daniele/MegaVault/projects/fedora-t7-backup/docs/ai/INCIDENT_REGISTRY.md

INCIDENT:
Incident_ID=T7_LIFECYCLE_MOUNT_NAMESPACE
Titolo=T7 connect lifecycle could not observe or release its system mount
Data_prima_comparsa_UTC=2026-07-11T23:51:57Z
Data_ultima_comparsa_UTC=2026-07-11T23:54:58Z
Numero_occorrenze=4 failed development trigger attempts before correction
Gravita_massima=HIGH
Stato=RESOLVED
Root_cause=ProtectSystem filesystem namespace hid a mount created after service start; replacing it with RequiresMountsFor then caused stopping the mount to stop the requiring backup service.
Sistemi_coinvolti=Fedora host; t7-restic-backup.service; mnt-T7_BACKUP.mount; Samsung T7
Alert_coinvolti=Four Telegram unmount-cleanup failure notifications during activity 684219 validation
Tentativi_effettuati=Real-device udev replay; libmount and blkid comparison; filesystem namespace inspection; RequiresMountsFor test; journal and systemd job analysis.
Soluzione_finale=The lifecycle manages the global systemd mount without service filesystem namespace options; it retains NoNewPrivileges, restricted capabilities, locking, timeouts and process restrictions. Controlled tests are now explicitly marked TEST in Telegram.
Commit_correlati=fedora-t7-backup 55d310db67eaff1ee2dc15884213311e1269f2f4
Prompt_correlati=684219
Tempo_totale_di_impatto=approximately 3 minutes during controlled installation validation; no retained repository corruption and final jobs succeeded
Note=Real udev replay created f7682be7 and later tests created a989e8fd and 3082eb92; all successful jobs synced and unmounted. Project source=/home/daniele/MegaVault/projects/fedora-t7-backup/docs/ai/INCIDENT_REGISTRY.md

INCIDENT:
Incident_ID=ANDROID_STUDIO_FLATPAK_STALE_DIRECTORYLOCK_SOCKET
Titolo=Android Studio Flatpak blocked by stale DirectoryLock Unix socket
Data_prima_comparsa_UTC=2026-07-09T17:11:52Z
Data_ultima_comparsa_UTC=2026-07-12T11:08:04Z
Numero_occorrenze=1 confirmed persistent stale-socket incident
Gravita_massima=HIGH
Stato=RESOLVED
Root_cause=The Android Studio Flatpak session started on 2026-07-09 did not complete IDE shutdown and left the filesystem Unix socket .port plus PID/lock markers containing namespace PID 3. No process or listener remained, so the next launch saw bind address in use but connect refused.
Sistemi_coinvolti=Fedora 44 host; Flatpak com.google.AndroidStudio 2026.1.1.10; JetBrains DirectoryLock; Android Studio config and system paths
Alert_coinvolti=GNOME launch error dialog; user activity 516803
Tentativi_effettuati=Flatpak/install/launcher inventory;host and namespace process mapping;ss,lsof,fuser,/proc/net/unix ownership checks;artifact stat/content;idea.log and journal reconstruction;three successful launch-close checks.
Soluzione_finale=After proving no valid Studio process or socket owner existed,move only .port,.pid,.lock to a retained timestamped backup. No process signal,cache reset,reinstall,or data deletion. Normal starts now create an owned listening socket and normal shutdown removes .port and .lock.
Commit_correlati=this MegaVault activity commit
Prompt_correlati=516803
Tempo_totale_di_impatto=From the failed launch confirmed at 2026-07-12T11:08:04Z until the first verified fixed launch at 2026-07-12T11:15:49Z; stale artifacts originated 2026-07-09T17:11:52Z.
Note=Process 3 is PID 3 inside the Flatpak namespace,not host PID 3. Failed new launch host PID was 16895; stale creator host PID is UNKNOWN because it had already exited. Backup=/home/daniele/.local/state/android-studio-recovery/activity-516803-20260712T131700+0200. Never automate blind lock deletion.

INCIDENT:
Incident_ID=KUMA_STALE_CATEGORY_ALERTS
Titolo=Fedora System Monitor category alerts could not recover reliably
Data_prima_comparsa_UTC=2026-07-13T07:18:00Z
Data_ultima_comparsa_UTC=2026-07-13T07:35:12Z
Numero_occorrenze=1 multi-root audit incident
Gravita_massima=HIGH
Stato=RESOLVED_WITH_REAL_STORAGE_ALERTS_REMAINING
Root_cause=One-sided sensor recovery;unstable WiFi device key;invalid absolute filesystem floor;synthetic FUSE inodes;historical replay timestamp loss;missing clean-journal I/O recovery;DNF Started race
Sistemi_coinvolti=Fedora host;fedora-system-monitor;SQLite;systemd;udev;NetworkManager;Uptime Kuma
Alert_coinvolti=Fedora Host ID39;Fedora Storage ID40;Fedora Network ID41;Fedora Software ID43
Tentativi_effettuati=Full source+installed+runtime audit;all collector scopes;DB state reconstruction;real category pushes;systemd+udev+selftest;DNF source reconciliation
Soluzione_finale=Fedora System Monitor 1.1.0 adds bidirectional recovery,stable identity,valid thresholds,FUSE filtering,original timestamps,clean-window recovery,terminal DNF retry,exact event dedup,and endpoint reconciliation
Commit_correlati=fedora-system-monitor activity 471852
Prompt_correlati=471852
Tempo_totale_di_impatto=Stale state persisted from first installation until 2026-07-13 audit;exact user-visible duration UNKNOWN
Note=Host,Network,Services,Software healthy after fix;Storage intentionally DOWN for Seagate 3.6754 percent free and unmatched unsafe removal;fresh Kuma admin readback pending because Chrome JWT was rejected;project source=/home/daniele/MegaVault/projects/fedora-system-monitor/docs/ai/INCIDENT_REGISTRY.md

INCIDENT:
Incident_ID=AUTOKEY_FEDORA44_WAYLAND_INPUT_BLOCKED
Titolo=AutoKey unusable on Fedora 44 GNOME Wayland
Data_prima_comparsa_UTC=2026-07-13T07:39:00Z
Data_ultima_comparsa_UTC=2026-07-13T08:21:00Z
Numero_occorrenze=1
Gravita_massima=HIGH
Stato=MITIGATED
Root_cause=Fedora autokey 0.96 is X11-only;AutoKey for Wayland 0.97.4 additionally cloned incomplete EV_ABS tablet axes into one uinput device so GNOME Shell 50/libinput rejected the entire virtual device;its synchronous wl-paste read could also block when no clipboard owner existed.
Sistemi_coinvolti=Fedora 44 host;GNOME Shell 50.3;AutoKey;libinput;uinput;wl-clipboard
Alert_coinvolti=GNOME launcher not apparent;XRecord-only native input failure;libinput missing tablet capabilities;ownerless wl-paste hang
Tentativi_effettuati=Baseline package,desktop,tray,process,journal,coredump,config,window,extension,alternate install and environment inventory;real kernel input into GTK Wayland and Zenity XWayland;official source/release/COPR audit;fork uinput and clipboard trace;Chrome native Wayland isolated QA.
Soluzione_finale=Signed dlk/autokey COPR 0.97.4;GNOME 50 extension;input group and udev access;single user launcher and graphical-session systemd service;user wrapper filters invalid EV_ABS and bounds wl-paste to one second without modifying RPM files.
Commit_correlati=this MegaVault activity commit
Prompt_correlati=638417
Tempo_totale_di_impatto=Unknown before report;technical repair and current-session core validation completed 2026-07-13T08:21:00Z
Note=GTK Wayland,Chrome Wayland,and Zenity XWayland hotkey+clipboard phrase tests PASS;GUI visible and single instance PASS. Real GNOME extension discovery,menu launch,service autostart,and persistence after logout/login remain pending because forcing logout risked user work. SQLite incident updated and backed up at /home/daniele/sync_root/db/backups/incident_registry.activity-638417.pre-update.20260713T082100Z.sqlite.

INCIDENT:
Incident_ID=VLC_FEDORA_FLATPAK_FAKE_OPENH264
Titolo=VLC Fedora Flatpak could not decode H264
Data_prima_comparsa_UTC=2026-07-13T18:55:48Z
Data_ultima_comparsa_UTC=2026-07-13T19:00:00Z
Numero_occorrenze=1 confirmed user incident with controlled reproduction
Gravita_massima=HIGH
Stato=RESOLVED
Root_cause=The only VLC installation was Fedora Flatpak org.videolan.vlc using org.fedoraproject.KDE5Platform f44;its ffmpeg-free disabled the native h264 decoder and delegated to libopenh264,but the sandbox supplied noopenh264 2.6.0,explicitly a fake OpenH264 implementation,so decoder creation failed even though the host had the real openh264 RPM.
Sistemi_coinvolti=Fedora 44 host;Flatpak Fedora remote;org.videolan.vlc;org.fedoraproject.KDE5Platform f44;FFmpeg;OpenH264
Alert_coinvolti=VLC Codec not supported h264 dialog and terminal decoder errors
Tentativi_effettuati=RPM/Flatpak/repository inventory;plugin and linkage audit;host versus sandbox FFmpeg comparison;controlled Baseline H264 MP4 reproduction;full VLC -vvv pre/post logs;ffprobe,ffmpeg,ffplay,DNF and Flatpak integrity checks.
Soluzione_finale=Unfiltered the existing system Flathub remote,removed only Fedora org.videolan.vlc,and installed system Flathub org.videolan.VLC 3.0.23;kept one VLC installation and made no RPM codec changes. Post-fix avcodec received the first H264 picture and real video output exited 0.
Commit_correlati=this MegaVault activity commit
Prompt_correlati=684271
Tempo_totale_di_impatto=UNKNOWN before report;technical repair and validation completed 2026-07-13T19:00:00Z
Note=Original user file path was not supplied,so a controlled MP4/H264 Baseline/yuv420p/AAC LC sample proved the same generic failure and fix. mpv was not installed and was not added only as a test dependency. Host libpostproc is absent but unrelated to H264 and disabled in both VLC builds. Old lowercase Flatpak app data remains preserved at /home/daniele/.var/app/org.videolan.vlc.

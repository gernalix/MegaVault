VERSION=8
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
incidents=OCI_STORAGE_LIMIT_EXCEEDED,OCI_REMOTE_REPOSITORY_CORRUPT,ORACLE_ROOT_DISK_PRESSURE,TELEGRAM_TRANSPORT_SECRET_DISCLOSURE
status_2026_07_26=OCI_STORAGE_LIMIT_EXCEEDED_RESOLVED+OCI_REMOTE_REPOSITORY_CORRUPT_RESOLVED+TELEGRAM_TRANSPORT_SECRET_DISCLOSURE_MITIGATED
owner_docs=/home/daniele/projects/oracle-backup-service/docs/ai/INCIDENT_REGISTRY.md
maintenance_731842=credential_argv_exposure_mitigated+Telegram_and_Cloudflare_rotation_required+telegram_media_environment_fixed+software_audit_boot_watchdog_transient_resolved;owner_docs=/home/daniele/projects/vm_oracle/docs/ai/INCIDENT_REGISTRY.md
activity=731904

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
Incident_ID=CODEX_WEEKLY_LIMIT_MONITOR_QUOTA_SCHEMA_CHANGE
Titolo=Oracle VM Codex quota monitor failed after 5h window removal and primary weekly schema change
Data_prima_comparsa_UTC=2026-07-12T18:28:00Z
Data_ultima_comparsa_UTC=2026-07-14T17:48:27Z
Numero_occorrenze=recurring_every_poll_until_fix
Gravita_massima=HIGH
Stato=RESOLVED
Root_cause=Codex app-server account/rateLimits/read stopped returning the previous 300-minute main 5h window and changed codex primary to a 10080-minute window while secondary became null; the watcher still required secondary as weekly and kept obsolete last_five_hour state.
Sistemi_coinvolti=Oracle VM instance-20260201-1126; codex-weekly-limit-monitor.service; /home/ubuntu/codex/automazione/codex_weekly_limit_monitor; /home/ubuntu/telegram_notify.py; Codex app-server account/rateLimits/read
Alert_coinvolti=Codex quota Telegram notifications; codex_weekly_limit_monitor runtime log/state
Tentativi_effettuati=Read MegaVault protocol and host profile; found active monitor by systemd, process tree, logs, state, config, helper path, and source JSON-RPC; observed live redacted payload; backed up runtime files; deployed generic category parser and state migration; ran deterministic tests, dry-run real source, controlled real service restart, and no-duplicate restart verification.
Soluzione_finale=Monitor now parses dynamic quota categories from actual rateLimits/rateLimitsByLimitId windows, skips null windows, maps codex 10080-minute window to Weekly, emits Telegram only for present categories, removes obsolete last_five_hour state, preserves last valid categories on errors, keeps telegram_notify.py as the only Telegram helper, and documents UTC dd/mm/yy hh:mm timestamps.
Commit_correlati=this_MegaVault_report_commit
Prompt_correlati=738416
Tempo_totale_di_impatto=At least 2026-07-12T18:28:00Z to 2026-07-14T17:48:27Z based on monitor logs/state; previous successful state was 2026-07-12T18:13:53Z and errors repeated until fix.
Note=Post-fix evidence: state version=3, last_error empty, categories weekly left=82 reset=20/07/26 07:18 and GPT-5.3-Codex-Spark left=100; no last_five_hour_* keys; real Telegram notification sent once for Weekly 94% -> 82%; second restart did not resend.

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
Note=No physical disconnect or destructive reproduction was attempted; device serial and filesystem UUID are intentionally omitted from documentation; project source=/home/daniele/projects/fedora-system-monitor/docs/ai/INCIDENT_REGISTRY.md

INCIDENT:
Incident_ID=CODEX_DATA_ANALYTICS_WIDGETS_MISSING_PNG
Titolo=Codex Data Analytics plugin MCP closed initialize response due missing PNG asset
Data_prima_comparsa_UTC=2026-07-14T11:30:01Z
Data_ultima_comparsa_UTC=2026-07-14T12:03:44Z
Numero_occorrenze=1 confirmed current startup failure
Gravita_massima=MEDIUM
Stato=RESOLVED
Root_cause=The plugin-provided MCP server dataAnalyticsWidgets in /home/daniele/.codex/plugins/cache/openai-curated-remote/data-analytics/0.2.8-13ceeea1f599 loaded assets/datascience.png during module initialization, but that asset was absent from the installed cache; Node threw ENOENT before replying to MCP initialize, so Codex reported connection closed: initialize response.
Sistemi_coinvolti=Fedora host; Codex CLI 0.144.4; OpenAI curated Data Analytics plugin 0.2.8-13ceeea1f599; node /usr/bin/node v22.22.2
Alert_coinvolti=Codex startup banner MCP startup incomplete failed dataAnalyticsWidgets
Tentativi_effettuati=Read MEGAVAULT_PROTOCOL and HOST_PROFILE; captured Fedora/Codex versions, codex mcp help/list/get, doctor, plugin config, process cwd/env, journal/systemd state, plugin .mcp.json, server.cjs, package manifests, manual server stdout/stderr/exit/duration before and after fix, official Codex manual MCP section, and two real codex --yolo launches.
Soluzione_finale=Regenerated /home/daniele/.codex/plugins/cache/openai-curated-remote/data-analytics/0.2.8-13ceeea1f599/assets/datascience.png from the bundled datascience.svg using ImageMagick; no MCP disable, model change, timeout change, retry change, package update, or config replacement.
Commit_correlati=none_local_cache_repair
Prompt_correlati=739184
Tempo_totale_di_impatto=active at task start until local cache repair and two clean Codex launches on 2026-07-14T12:03:44Z
Note=Backups: plugin backup activity_739184_20260714T140237+0200 and MegaVault registry backup activity_739184_20260714T140520+0200. Residual warning: remote plugin refresh or reinstall could replace the local cache if upstream still lacks the asset.

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
Note=Host,Network,Services,Software healthy after fix;Storage intentionally DOWN for Seagate 3.6754 percent free and unmatched unsafe removal;fresh Kuma admin readback pending because Chrome JWT was rejected;project source=/home/daniele/projects/fedora-system-monitor/docs/ai/INCIDENT_REGISTRY.md

INCIDENT:
Incident_ID=KUMA_HOST_STORAGE_REAL_STATE_471853
Titolo=Fedora System Monitor Host and Storage red states were real after Seagate cleanup
Data_prima_comparsa_UTC=2026-07-14T12:15:00Z
Data_ultima_comparsa_UTC=2026-07-14T12:23:02Z
Numero_occorrenze=1 audit follow-up
Gravita_massima=HIGH
Stato=RESOLVED_WITH_REAL_ALERTS_REMAINING
Root_cause=Host had real swap.used_percent warning near 39 percent;Storage had Seagate filesystem.free_percent 5.2273 below recovery threshold;unsafe_device_removal was stale because mount point was present again
Sistemi_coinvolti=Fedora host;fedora-system-monitor;SQLite;Uptime Kuma Oracle VM
Alert_coinvolti=Fedora Host ID39;Fedora Storage ID40;swap.used_percent;filesystem.free_percent;unsafe_device_removal
Tentativi_effettuati=Live DB queries;df/findmnt;minute+five_minute+fifteen_minute collectors;remote Kuma SQLite readback;systemd+udev+selftest
Soluzione_finale=Fedora System Monitor 1.1.1 refreshes active metric alerts and reconciles unsafe-removal alerts when findmnt proves the recorded mount point is present
Commit_correlati=fedora-system-monitor activity 471853
Prompt_correlati=471853
Tempo_totale_di_impatto=User-visible red state persisted until real conditions were distinguished and stale unsafe removal recovered;exact UI duration UNKNOWN
Note=Final state Host DOWN truthful for swap warning;Storage DOWN truthful for Seagate free space;Network/Services/Software UP;project source=/home/daniele/projects/fedora-system-monitor/docs/ai/AUDIT_471853.md

INCIDENT:
Incident_ID=AUTOKEY_FEDORA44_WAYLAND_INPUT_BLOCKED
Titolo=AutoKey unusable on Fedora 44 GNOME Wayland
Data_prima_comparsa_UTC=2026-07-13T07:39:00Z
Data_ultima_comparsa_UTC=2026-07-14T20:23:24Z
Numero_occorrenze=2
Gravita_massima=HIGH
Stato=RESOLVED
Root_cause=Fedora autokey 0.96 is X11-only;AutoKey for Wayland 0.97.4 additionally cloned incomplete EV_ABS tablet axes into one uinput device so GNOME Shell 50/libinput rejected the entire virtual device;its synchronous wl-paste read could also block when no clipboard owner existed.
Sistemi_coinvolti=Fedora 44 host;GNOME Shell 50.3;AutoKey;libinput;uinput;wl-clipboard
Alert_coinvolti=GNOME launcher not apparent;XRecord-only native input failure;libinput missing tablet capabilities;ownerless wl-paste hang
Tentativi_effettuati=Baseline package,desktop,tray,process,journal,coredump,config,window,extension,alternate install and environment inventory;real kernel input into GTK Wayland and Zenity XWayland;official source/release/COPR audit;fork uinput and clipboard trace;Chrome native Wayland isolated QA;later fan/power diagnostics found recurring ENODEV uinput loop;activity_582941 removed AutoKey and migrated text expansion to Espanso.
Soluzione_finale=AutoKey packages,service,launcher,wrapper,GNOME extension,config,cache,logs,and dlk/autokey COPR removed;configuration backed up at /home/daniele/backups/autokey/582941-20260714T222324+0200;Espanso Wayland 2.3.0 installed as user service with migrated text expansions.
Commit_correlati=this MegaVault activity commit
Prompt_correlati=638417,582941
Tempo_totale_di_impatto=Unknown before report;runtime risk eliminated by removal on 2026-07-14T20:23:24Z
Note=Activity_582941 verified no AutoKey package/process/user unit/repo remains, espanso.service active+enabled, no listening ports, migrated Espanso matches inject in a GTK temp window, and virtual-keyboard trigger typing expands with the expected word separator.

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

INCIDENT:
Incident_ID=SMART_SERVICE_CAPABILITY_FALSE_POSITIVE
Titolo=Fedora System Monitor registrava falsi smart_check_failed su NVMe interno e Samsung T7
Data_prima_comparsa_UTC=2026-07-10T10:30:53Z
Data_ultima_comparsa_UTC=2026-07-26T12:08:27Z
Numero_occorrenze=156
Gravita_massima=MEDIUM
Stato=RESOLVED
Root_cause=Il collector hourly rimuoveva CAP_SYS_ADMIN necessaria all NVMe nativo e CAP_SYS_RAWIO necessaria al passthrough SCSI del bridge USB NVMe ASMedia del T7
Sistemi_coinvolti=Fedora 44 host;fedora-system-monitor;KIOXIA NVMe interno;Samsung T7 Shield USB NVMe;SQLite;systemd
Alert_coinvolti=smart_check_failed warning events;zero active SMART alerts;zero false Kuma transitions
Tentativi_effettuati=Database reconstruction;lsblk+findmnt+udevadm+smartctl scan-open;capability-isolated transient units;SMART and NVMe health,error,self-test,temperature and kernel journal checks
Soluzione_finale=Fedora System Monitor 1.3.1 scopes CAP_SYS_ADMIN and CAP_SYS_RAWIO only to hourly and daily,records bounded diagnostic output,skips absent or unsupported devices,and avoids the ASMedia error-log page while preserving health and self-test monitoring
Commit_correlati=fedora-system-monitor activity 482731
Prompt_correlati=482731
Tempo_totale_di_impatto=2026-07-10T10:30:53Z to 2026-07-26T12:08:27Z for false warning event generation
Note=Internal KIOXIA health PASS with media errors 0 and T7 health PASS through sntasmedia;two Seagate USB SAT disks remained intentionally asleep. An explicit T7 error-log probe during investigation caused two successful UAS resets and was stopped;it is separate from the historical cause. Project source=/home/daniele/projects/fedora-system-monitor/docs/ai/REPORT_482731.md

INCIDENT:
Incident_ID=ZRAM_OCCUPANCY_MISCLASSIFIED_AS_MEMORY_PRESSURE
Titolo=Fedora Host marked DOWN for normal compressed zram occupancy
Data_prima_comparsa_UTC=2026-07-14T10:15:00Z
Data_ultima_comparsa_UTC=2026-07-18T18:40:34Z
Numero_occorrenze=1 persistent false category state
Gravita_massima=HIGH
Stato=RESOLVED
Root_cause=Fedora System Monitor 1.1.1 alerted directly on swap.used_percent,which measured normal zram occupancy without requiring evidence from MemAvailable,PSI,swap rate,reclaim,or OOM.
Sistemi_coinvolti=Fedora 44 host;zram-generator;fedora-system-monitor;SQLite;Uptime Kuma Fedora Host ID39
Alert_coinvolti=swap.used_percent;Fedora Host ID39
Tentativi_effettuati=Live zram configuration and compression audit;MemAvailable and PSI baseline;vmstat swap/reclaim/OOM sampling;7-day Prometheus history;installed minute and daily collector tests.
Soluzione_finale=Fedora System Monitor 1.2.0 keeps zram use informational and alerts only on composite memory.pressure_level using independent pressure evidence;legacy swap threshold keys migrate safely. Later 1.3.1 retains this behavior.
Commit_correlati=c36f1fcf55fdaa6e06675a588068189198f203d4;project=7f91e2316887
Prompt_correlati=962417
Tempo_totale_di_impatto=User-visible Host false warning persisted from the prior audit until recovery at 2026-07-18T18:40:34Z.
Note=Post-fix memory available 68.752 percent,PSI zero,pressure level zero,zram compression 2.857x,writeback zero,OOM delta zero;Storage alerts remain separate and real. Project evidence=/home/daniele/projects/fedora-system-monitor/docs/ai/AUDIT_962417.md

INCIDENT:
Incident_ID=AUTOKEY_UINPUT_STALE_DEVICE_BUSY_LOOP
Titolo=AutoKey stale input device caused CPU and fan runaway
Data_prima_comparsa_UTC=2026-07-14T18:35:00Z
Data_ultima_comparsa_UTC=2026-07-14T18:49:50Z
Numero_occorrenze=1
Gravita_massima=HIGH
Stato=MITIGATED_HISTORICAL_AUTOKEY_REMOVED
Root_cause=AutoKey for Wayland 0.97.4 retained a disappeared evdev device in its uinput flush set;repeated read calls raised ENODEV and the exception loop had no device removal or backoff,consuming one CPU and writing tracebacks continuously.
Sistemi_coinvolti=Fedora 44 host;AutoKey for Wayland;uinput;evdev;systemd-journald;thermal cooling
Alert_coinvolti=CPU_84_89C;fans_about4480RPM;AutoKey_99pct_CPU+about3MB_s_journal_writes
Tentativi_effettuati=Five-minute no-benchmark CPU/frequency/temperature/fan/GPU/power/interrupt/process baseline;bounded AutoKey journal;controlled three-minute stop/start comparison;post-deploy five-minute measurement.
Soluzione_finale=Controlled autokey.service stop/start rebuilt the device set and restored AutoKey about0.2pct CPU,post-window CPU average62.2C,and fan average2975RPM;AutoKey was subsequently removed and replaced by Espanso in activity 582941.
Commit_correlati=fd1344fdafdf9e0639c03af247652c4adf35c9d9
Prompt_correlati=614283
Tempo_totale_di_impatto=At least 2026-07-14T18:35:00Z to controlled restart at 2026-07-14T18:49:50Z;earlier start UNKNOWN
Note=Historical incident; recurrence through AutoKey is no longer operationally applicable. SQLite upsert integrity=ok;backup=/home/daniele/sync_root/db/backups/incident_registry.activity-614283.pre-update.20260714T194000Z.sqlite;source=/home/daniele/projects/fedora-diagnostics/docs/ai/AUDIT_614283.md.

INCIDENT:
Incident_ID=ESPANSO_WAYLAND_PRECOMPOSITOR_START_RACE
Titolo=Espanso risultava attivo ma non espandeva su GNOME Wayland
Data_prima_comparsa_UTC=2026-07-15T07:55:19Z
Data_ultima_comparsa_UTC=2026-07-26T12:25:25Z
Numero_occorrenze=multiple_boots_exact_count_UNKNOWN
Gravita_massima=MEDIUM
Stato=RESOLVED
Root_cause=La user unit era abilitata sotto default.target mentre linger era attivo;systemd avviava Espanso prima del compositor GNOME Wayland. Il worker falliva con NoCompositor e i retry potevano lasciare un worker parzialmente inizializzato, attivo per systemd ma privo di EVDEVInjector e accesso a /dev/uinput.
Sistemi_coinvolti=Fedora_44;GNOME_Wayland;systemd_user;Espanso_2.3.0;evdev;uinput
Alert_coinvolti=trigger_cdd_non_espanso;worker_NoCompositor_panic;servizio_active_ma_backend_incompleto
Tentativi_effettuati=Inventario installazione e sessione;validazione YAML e regole;ricerca duplicati;processi,fd,device,permessi,gruppi,variabili,log Espanso e journal multi-boot;riavvio controllato a sessione matura;matrice GTK Wayland;test XTerm XWayland separato.
Soluzione_finale=Unit utente spostata da default.target a graphical-session.target con PartOf=graphical-session.target;nessun loop,delay,aggiornamento,reinstallazione o modifica al testo del match. Dopo stop/start il singolo worker inizializza EVDEVSource,EVDEVInjector e WaylandFallbackClipboard.
Commit_correlati=9be9196bb9dee7334a0dc7d63c90e02e4f07a5ea
Prompt_correlati=573814
Tempo_totale_di_impatto=intermittente_dal_primo_log_disponibile_2026-07-15_fino_alla_correzione_2026-07-26
Note=GTK Wayland ha completato 30/30 rilevamenti ed espansioni. XTerm XWayland non ha superato il test di iniezione clipboard; Chrome non e stato rivalidato e un logout/login reale non e stato forzato per non interrompere la sessione. Report=docs/ai/REPORT_573814.md;backup=/home/daniele/backups/espanso/573814-20260726T201952+0200.

INCIDENT:
Incident_ID=GNOME_IDLE_SUSPEND_WIFI_SLEEP
Titolo=GNOME inactivity suspension turned off the display and disconnected WiFi
Data_prima_comparsa_UTC=2026-07-22T20:35:44Z
Data_ultima_comparsa_UTC=2026-07-22T23:39:36Z
Numero_occorrenze=4 confirmed suspend sequences in current boot before fix
Gravita_massima=HIGH
Stato=RESOLVED
Root_cause=GNOME Settings Daemon Power retained Fedora defaults of 900 seconds plus suspend for both AC and battery even though desktop idle-delay was already zero; each idle suspend caused NetworkManager to disconnect wlp2s0 explicitly with reason sleeping. Separately the WiFi profile inherited default powersave and the ath11k driver reported power save on.
Sistemi_coinvolti=Fedora 44 host;GNOME Wayland;gnome-settings-daemon Power;systemd-logind;systemd sleep targets;NetworkManager;wlp2s0;ath11k_pci;QCNFA765
Alert_coinvolti=User-visible display off and WiFi disconnected after inactivity;system journal suspend and NetworkManager sleeping transitions
Tentativi_effettuati=Targeted audit of gsettings,dconf,schema defaults,GNOME idle and power plugin,Mutter DPMS,extensions,PPD/TuneD/TLP,logind,sleep targets,inhibitors,NetworkManager,iw,rfkill,driver,modinfo,modprobe,udev,kernel command line,PCI runtime PM,ASPM relevance and journal causality;real continuous idle test.
Soluzione_finale=Set GNOME AC and battery inactive timeouts to zero and actions to nothing,disabled idle dimming,kept idle-delay zero and every manual sleep target unmasked;added NetworkManager global wifi.powersave=2,then reloaded,reapplied and disabled current ath11k link powersave. No BIOS,kernel,udev,modprobe,logind,tuned or profile edits were needed.
Commit_correlati=d5ab6578e1fa98d68db9323c64a594b863afe25f
Prompt_correlati=641827
Tempo_totale_di_impatto=At least four confirmed suspensions between 2026-07-22T20:35:44Z and 2026-07-22T23:39:36Z; earlier user-visible duration UNKNOWN.
Note=Post-fix continuous idle reached 600594 ms with Mutter PowerSaveMode 0,eDP-1 DPMS On,wlp2s0 associated,power save off,gateway reachable and zero suspend or sleeping-disconnect markers. AC was physically online; battery policy readback is correct but a physical unplugged 10-minute run was not performed. Backups are under /home/daniele/.local/state/activity-641827/backups/20260723T020636+0200.

INCIDENT:
Incident_ID=SECURE_BOOT_DRACUT_LUKS_UNLOCK_NOT_PERSISTED
Titolo=Boot Fedora con Secure Boot raggiunge dracut ma il Btrfs dentro LUKS non compare
Data_prima_comparsa_UTC=2026-07-30T03:01:36Z_to_2026-07-30T03:10:52Z;exact_UNKNOWN
Data_ultima_comparsa_UTC=2026-07-30T03:01:36Z_to_2026-07-30T03:10:52Z;exact_UNKNOWN
Numero_occorrenze=1
Gravita_massima=HIGH
Stato=OPEN
Root_cause=Il riferimento mostrato da dracut non e obsoleto: e il FSID Btrfs corrente passato dalle opzioni BLS e compare solo dopo apertura LUKS. Il guasto a monte del tentativo fallito e delimitato a mancata scoperta NVMe/LUKS oppure richiesta cryptsetup fallita o terminata, ma il boot initramfs non monto la root e non lascio journal o rdsosreport persistenti; la causa dinamica esatta e quindi UNKNOWN.
Sistemi_coinvolti=Fedora 44;UEFI Secure Boot;shim;GRUB;BLS;kernel 7.1.x;dracut;NVMe interno;LUKS2;Btrfs
Alert_coinvolti=/dev/disk/by-uuid/6ff76a46-6614-4ac6-b1fa-a9590f09c709 does not exist;Not all disks have been found;dracut emergency mode
Tentativi_effettuati=32 boot journal verificati;artefatti dracut,rdsosreport,pstore,coredump e kdump cercati;UUID tracciato in fstab,kernel cmdline,BLS,GRUB,generatori,EFI e binari;quattro initramfs estratti in tmpfs con lsinitrd e hash invariati;selezione BLS,grubenv,ordine EFI,fallback,firme e moduli verificati;activity 948315 ha armato collector first-successful-boot e BLS diagnostica separata con output console.
Soluzione_finale=Causa ancora OPEN. Preparata raccolta forense reversibile: archivio automatico root-only dopo il primo boot riuscito e BLS non predefinita sullo stesso kernel/initramfs con soli parametri debug; LUKS,partizioni,Secure Boot,chiavi,kernel,initramfs,BLS originali,GRUB e grubenv invariati.
Commit_correlati=activity_214587_MegaVault_commit;activity_948315_MegaVault_commit
Prompt_correlati=731846;214587;948315
Tempo_totale_di_impatto=Un singolo tentativo nel gap tra arresto pulito 2026-07-30T03:01:36Z e avvio corrente 2026-07-30T03:10:52Z; durata esatta UNKNOWN
Note=Origine FSID provata da /var/log/anaconda/storage.log mkfs.btrfs del 2026-07-07. Secure Boot corrente disabilitato. Nessun reboot activity 948315. Pstore EFI e journal persistente gia operativi ma un timeout dracut normale pre-root resta volatile; foto/video console obbligatori. Sources=ai/reports/activity_214587_secure_boot_dracut_forensics.md;/home/daniele/projects/fedora-diagnostics/docs/ai/AUDIT_948315.md

INCIDENT:
Incident_ID=MEGAVAULT_V16_BASELINE_DIVERGENCE_DIRTY_STATE
Titolo=Baseline canonica ferma a VERSION=13 mentre le sessioni operavano su linee v16 divergenti e spesso dirty
Data_prima_comparsa_UTC=2026-07-09T00:00:00Z
Data_ultima_comparsa_UTC=2026-08-01T00:00:00Z
Numero_occorrenze=multiple_exact_count_UNKNOWN
Gravita_massima=HIGH
Stato=RESOLVED
Root_cause=Le evoluzioni v14-v16 furono pubblicate su branch Codex divergenti senza promozione a master;la timeline veniva aggiornata tramite commit generated-only e il builder usava orologio/mtime,scansioni implicite,delete-on-missing e WAL persistente;cache,private,secrets e sidecar non erano coperti integralmente da .gitignore.
Sistemi_coinvolti=MegaVault;origin/master;branch Codex;protocollo;timeline SQLite+Markdown;Git worktree
Alert_coinvolti=VERSION=13_su_master;task_avviati_da_VERSION=16_non_canonico;git_status_dirty;PR_1_ancestry_obsoleta
Tentativi_effettuati=Audit baseline read-only;classificazione semantica c50fdbc;bundle dei commit locali unici;ricostruzione da origin/master senza merge o cherry-pick monolitico;archiviazione dei sette blob 2917aa9;test determinismo repo+worktree.
Soluzione_finale=PR 2 corretta con import una-volta dei commit semantici primary-repo,esclusione dei soli commit generated-only,delete manifest 7/7 e policy trunk-based globale;merge commit e4b24d1 su master;VERSION=17 ricostruita semanticamente con copertura 214/214 e lint permanente senza cherry-pick della linea storica.
Commit_correlati=4876843;12bf2bd;b949d12;58bd3db;6010550;5622c97;59073f9;38d6aa8;c50fdbc;0774200;76b44d2;287dddb;e4b24d1
Prompt_correlati=816427;816428
Tempo_totale_di_impatto=2026-07-09_to_2026-08-01T16:14:15+02:00
Note=PR 1 resta chiusa e non mergiata. Due commit locali unici preservati nel bundle esterno SHA256 1e0df2bb7545c266f1d3f08fc815eda4c7f768e624cd550b3bc5f4fee08156a7. Owner repository SuperContacts resta UNKNOWN con fallback archivio v33. La policy vieta branch-per-task,branch chaining,riuso estraneo e successo dichiarato prima dell'integrazione canonica o defer esplicito.

INCIDENT:
Incident_ID=PIXEL_WHATSAPP_METERED_BACKGROUND_RESTRICTION
Titolo=Pixel 8a restringeva i dati in background di WhatsApp e ritardava le notifiche
Data_prima_comparsa_UTC=2026-07-02T03:14:07Z
Data_ultima_comparsa_UTC=2026-07-26T18:28:58Z
Numero_occorrenze=2
Gravita_massima=HIGH
Stato=RESOLVED
Root_cause=Android NetworkPolicyManager aveva nuovamente assegnato all UID 10363 di com.whatsapp policy 1 REJECT_METERED_BACKGROUND; il push poteva funzionare in primo piano o su WiFi non misurato ma veniva negato in background sui percorsi misurati.
Sistemi_coinvolti=Google Pixel 8a;Android 17;com.whatsapp;Google Play Services FCM;NetworkPolicyManager
Alert_coinvolti=notifiche WhatsApp assenti o ritardate in background;nessun alert automatico
Tentativi_effettuati=Recuperata diagnosi 2026-07-02 dai commit 856efce e 33f13ae;verificati identita ADB,permesso,canali,appops,batteria,Doze,standby,Data Saver,rete,DND,GMS,servizi e logcat;due test reali esterni.
Soluzione_finale=Rimossa la blacklist per il solo UID WhatsApp e aggiunta allowlist dati misurati persistente;policy finale 4 ALLOW_METERED_BACKGROUND;nessuna modifica a dati,cache,account,chat,backup,DND,Doze o canali.
Commit_correlati=856efce;33f13ae;activity_473821_MegaVault_commit
Prompt_correlati=473821
Tempo_totale_di_impatto=UNKNOWN tra la ricomparsa della policy e il fix 2026-07-26;la prima occorrenza fu risolta il 2026-07-02
Note=Test finale 2026-07-26 20:28:37-20:29:24 CEST: Pixel sempre Dozing, push C2DM alle 20:28:58, GcmFGService avviato, due record Android mIntercept false e mHidden false. Il writer che ha reintrodotto policy 1 non e conservato nei log. Due record WhatsApp distinti furono intercettati il 2026-07-25 da DND manuale, comportamento atteso non modificato. SQLite globale integro ma non aggiornato manualmente perche il registro impone upsert automatici e non offre un updater globale. Source=ai/reports/activity_473821_pixel_whatsapp_notifications.md

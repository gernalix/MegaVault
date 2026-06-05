# Prompt 739482 - initial incident report

Generated: 2026-06-05 06:15 CEST

Scope: os-observer/autofix, Kuma monitor/recovery, rsync-transfer, codex-token-watcher, disk-usage-monitor, mint software audit, telemetry DB, freeze hardening, mint/cloud/oracle backup, Android SDK auto update.

## Runtime state

- os-observer user units were disabled on explicit operator request before remediation: `os-observer.timer`, `os-observer.service`, `os-observer-autofix-agent.timer`, `os-observer-autofix-agent.service`, `os-observer-startup-bootstrap.service` are inactive/disabled.
- `codex-usage-monitor.timer` is active hourly; last DB observations are `error` because the dashboard is behind Cloudflare/challenge and one boot run lacked `$DISPLAY`.
- `mint-update-tracker.service` is active/running. Live DB `/home/ubuntu/sync_root/db/software_audit.db` passed `quick_check`; latest Kuma push state is up/HTTP 200.
- `disk-usage-monitor.timer` is active every 5 minutes and the service exits successfully; its DB records frequent `SPACE_DELTA` alerts and per-alert Kuma pushes.
- `rsync-transfer.service` is not loaded; `rsync-uptime-kuma-push.service` is active and reports `pidfile_stale pid=3481045` every minute. Source BitLocker mount is not present; destination `/media/daniele/Seagate6TB2` is mounted ext4 rw.
- `mint-cloud-backup.service` is active/activating with restic running locally; the reported `/` 85-95% issue belongs to the Oracle side, not the Mint host checked here.
- Current Mint host `/` was 11% used; `/media/daniele/Seagate6TB2` was 44% used. Load was elevated after boot, with memory and swap still available.

## Missing Kuma mappings

- `codex-token-watcher`: no handler in `KUMA_MONITOR_HANDLERS`, causing `NO_MAPPING` notifications instead of a diagnosis of Cloudflare/login or timer state.
- `disk-usage-monitor`: no handler in `KUMA_MONITOR_HANDLERS`, causing `NO_MAPPING` despite a loaded system timer and successful oneshot runs.
- `software audit mint`: no handler in `KUMA_MONITOR_HANDLERS`, causing `NO_MAPPING` even though the live tracker DB and Kuma push state were healthy.

## Recurrent alert causes

- `blocked_by_safety`: os-observer digest flushing is forced every run, so safety blocks are sent repeatedly instead of being grouped and throttled. The event text does not carry enough unit/reason context in the notification.
- Kuma `NO_MAPPING`: unmapped monitor names return immediately before any recovery cooldown, so each dashboard check can generate a new knowledge row and Telegram alert.
- `rsync-transfer`: stale pidfile plus missing source mount correctly blocks resume, but the pusher sends identical down pushes every minute. Previous USB/disk I/O errors make automatic restart unsafe until mounts and filesystem state are manually verified.
- `disk-usage-monitor`: low delta threshold plus per-alert Telegram and per-alert `SPACE_DELTA` Kuma pushes makes normal backup/disk churn noisy.
- `TELEMETRY_STALE main_file_stale_wal_fresh`: main SQLite file mtime is stale while WAL is fresh and small; treating that as a checkpoint-required fault causes a loop even when writer activity exists.
- Freeze risk: pressure actions exist but cooldowns are short for repeated high-load conditions, so alerts repeat without materially changing containment.
- Oracle backup: remote quota is full (`StorageLimitExceeded` in supplied evidence) and fallback local is valid; no destructive retention should run unless existing docs define it.
- Android SDK auto update: the current consolidated updater run is `status=ok`; earlier `sdkmanager update/install failed` appears resolved by current path/env consolidation.

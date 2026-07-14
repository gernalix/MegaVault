# Prompt 738416 - Codex quota monitor schema change

ID_attivita=738416
Data_UTC=2026-07-14
Host=ubuntu@150.230.148.128
Hostname=instance-20260201-1126
Runtime=/home/ubuntu/codex/automazione/codex_weekly_limit_monitor
Service=codex-weekly-limit-monitor.service
Timer=none;watch_loop_internal_poll_interval=900s
Entrypoint=/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/codex_weekly_limit_watcher.py --config /home/ubuntu/codex/automazione/codex_weekly_limit_monitor/config.ini --watch --console
Interpreter=/usr/bin/python3
Codex_binary=/usr/bin/codex
Codex_version=codex-cli_0.137.0
Telegram_helper=/home/ubuntu/telegram_notify.py
Timezone=UTC for Codex reset timestamps and service logs; user-facing format dd/mm/yy hh:mm

## Discovery

- MegaVault protocol read first from `/home/daniele/MegaVault/ai/MEGAVAULT_PROTOCOL.md`; the Windows canonical backup path also exists under `/home/daniele/Downloads/.../megavault_content_aware_merge_20260705/...` but differs by hash and is not the active Linux root.
- Oracle VM access used existing SSH alias `oracle-vm`; host verified as `instance-20260201-1126`.
- Active monitor proven by systemd and process tree: service `codex-weekly-limit-monitor.service`, PID command `/usr/bin/python3 /home/ubuntu/codex/automazione/codex_weekly_limit_monitor/codex_weekly_limit_watcher.py --config ... --watch --console`.
- Runtime directory is not a Git repository; backups were created before edits.

## Root cause

The Codex app-server `account/rateLimits/read` schema changed. Previously the monitor expected `rateLimits.primary` as 300-minute main 5h and `rateLimits.secondary` as 10080-minute weekly. The current real payload exposes `rateLimits.primary` as a 10080-minute `codex` window and `rateLimits.secondary=null`. A separate `rateLimitsByLimitId.codex_bengalfox.primary` 10080-minute category exists with label `GPT-5.3-Codex-Spark`.

Observed redacted live categories:

- `weekly|Weekly|left=82|used=18|reset=20/07/26 07:18|duration=10080|source=rateLimits.primary`
- `codex_bengalfox|GPT-5.3-Codex-Spark|left=100|used=0|reset=21/07/26 17:51|duration=10080|source=rateLimitsByLimitId.codex_bengalfox.primary`

The old parser required `secondary` and failed every poll with `Missing secondary rate limit window`. It also retained obsolete `last_five_hour_*` state after the 5h category disappeared.

## Changes applied

- `codex_weekly_limit_watcher.py`
  - Added generic `QuotaCategory` model based on returned categories.
  - Parser now reads valid `primary`/`secondary` windows from `rateLimits` and `rateLimitsByLimitId`; `null` windows are skipped.
  - `weekly` maps only to a real 10080-minute `codex` category.
  - `five_hour` maps only if a real 300-minute `codex` category exists; current payload does not create it.
  - Partial parse errors are logged without discarding valid categories.
  - If no valid category is extracted, the run fails observably and preserves previous valid category state.
  - Telegram messages are generated only from present categories.
  - Legacy `last_five_hour_*` state is removed during successful migration.
- `test_watcher_local.py`: deterministic tests for current real output, no-5h output, new category, migration, no false notification, category change, reset-only change, fetch failure, unrecognized output, partial parse, state preservation, timestamp format, UTC timezone, dedup, Telegram helper import, dry-run Telegram, and absence of `5h left`.
- `README.md`: dynamic category behavior, legacy CSV columns, JSON `categories`, UTC timestamp basis.
- `config.example.ini` and `config.ini`: `notify_on_category_change=true`; obsolete `notify_on_five_hour_change` removed.

## Telegram format

Dry-run and real notification:

```text
Codex quota monitor
Weekly left: 94% -> 82%
Weekly reset: 20/07/26 07:18
Last check: 14/07/26 17:47
```

No 5h line appeared because no 300-minute category was present.

## Verification

- `python3 -m py_compile codex_weekly_limit_watcher.py test_watcher_local.py /home/ubuntu/telegram_notify.py` -> PASS.
- `python3 test_watcher_local.py` -> `local-tests: ok`.
- Real-source dry-run: categories above, 1 weekly event, no send, no state write.
- Controlled real restart: Telegram sent once for `quota_left_change:weekly:94->82:20/07/26 07:18`.
- Second restart: no duplicate Telegram notification.
- Final state: `version=3`, `last_success_at=2026-07-14T17:51:09+00:00`, `last_error=''`, `pending_notification=None`, no `last_five_hour_*`.
- systemd: service `enabled` and `active`; no dedicated timer; internal watch loop logged `Next poll in 892.4 seconds`.

## Files changed on Oracle VM

- `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/codex_weekly_limit_watcher.py`
- `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/test_watcher_local.py`
- `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/README.md`
- `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/config.example.ini`
- `/home/ubuntu/codex/automazione/codex_weekly_limit_monitor/config.ini`
- Runtime state/history updated by real run: `data/codex_usage_state.json`, `data/codex_usage_history.csv`

Backups created under runtime `backups/` with suffixes `738416-20260714T174640Z` and `738416-docconfig-20260714T175042Z`.

## Limitations

- Runtime monitor remains outside Git; preservation is via backups plus this MegaVault report.
- CSV still carries legacy 5h columns for backward compatibility; authoritative current categories are in JSON `categories`.
- `GPT-5.3-Codex-Spark` reset can drift while percent remains 100; reset-only drift is logged but does not notify.

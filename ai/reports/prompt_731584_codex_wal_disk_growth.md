# Prompt 731584 - Codex WAL T7 Root Growth

## Summary
- Root cause: `/home/daniele/.codex/logs_2.sqlite-wal` grew to 163,682,495,352 bytes / 152.441 GiB and accounts for 99.37% of `/home/daniele/.codex`.
- Detection source: Disk Usage Monitor SQLite, canonical T7 root `/dev/sda2` mounted `/`.
- Impact: latest monitor delta at `2026-06-13T19:08:08Z` was +156.97 GiB over 24h and +157.59 GiB over 48h.
- Cleanup state: resolved safely by SQLite checkpoint; watcher recovered `163,682,495,352` bytes and left `wal_bytes_after=0`.
- Mitigation applied: user timer `codex-sqlite-wal-maintenance.timer` installed every 30 minutes; script now has soft/hard/critical thresholds, dry-run, `quick_check`, holder logging, before/after byte report, critical Telegram guardrail through existing env/helper only, and no manual WAL removal.
- Deep dive update: prompt `938274`, 2026-06-13.

## Disk Usage Monitor Delta
| window_h | current_utc | baseline_utc | device | mountpoint | current_used_gib | baseline_used_gib | delta_gib |
|---:|---|---|---|---|---:|---:|---:|
| 1 | 2026-06-13T19:08:08Z | 2026-06-13T18:07:45Z | /dev/sda2 | / | 256.10 | 242.77 | 13.33 |
| 3 | 2026-06-13T19:08:08Z | 2026-06-13T16:06:21Z | /dev/sda2 | / | 256.10 | 118.66 | 137.45 |
| 6 | 2026-06-13T19:08:08Z | 2026-06-13T13:04:29Z | /dev/sda2 | / | 256.10 | 104.21 | 151.89 |
| 12 | 2026-06-13T19:08:08Z | 2026-06-13T07:05:22Z | /dev/sda2 | / | 256.10 | 102.54 | 153.56 |
| 24 | 2026-06-13T19:08:08Z | 2026-06-12T19:08:07Z | /dev/sda2 | / | 256.10 | 99.14 | 156.97 |
| 48 | 2026-06-13T19:08:08Z | 2026-06-11T19:07:45Z | /dev/sda2 | / | 256.10 | 98.52 | 157.59 |

## `.codex` Size Attribution
| path | size_bytes | size_gib | percent_of_codex | last_update |
|---|---:|---:|---:|---|
| `/home/daniele/.codex/logs_2.sqlite-wal` | 163682495352 | 152.441 | 99.37% | 2026-06-13 21:13:08 +0200 |
| `/home/daniele/.codex/logs_2.sqlite` | 339845120 | 0.317 | 0.21% | 2026-06-13 21:13:06 +0200 |
| `/home/daniele/.codex/sessions` | 274210417 | 0.255 | 0.17% | 2026-05-05 22:23:29 +0200 |
| `/home/daniele/.codex/.tmp` | 59618455 | 0.056 | 0.04% | 2026-06-10 11:27:12 +0200 |
| `/home/daniele/.codex/memories` | 3328775 | 0.003 | 0.00% | 2026-06-13 20:30:01 +0200 |
| `/home/daniele/.codex/cache` | 1961720 | 0.002 | 0.00% | 2026-06-02 06:59:47 +0200 |
| `/home/daniele/.codex/logs_2.sqlite-shm` | 851968 | 0.001 | 0.00% | 2026-06-13 21:13:06 +0200 |

## File Classification
| path | classification | reason | action |
|---|---|---|---|
| `/home/daniele/.codex/logs_2.sqlite-wal` | SAFE_TO_TRUNCATE_SQLITE_CHECKPOINT_ONLY | WAL frames are checkpointable and DB integrity is OK, but file is open by Codex. | Do not `rm`; timer will truncate when no holder exists. |
| `/home/daniele/.codex/logs_2.sqlite` | DO_NOT_DELETE | Operational SQLite DB. | Keep. |
| `/home/daniele/.codex/logs_2.sqlite-shm` | DO_NOT_DELETE_WHILE_OPEN | SQLite shared-memory sidecar. | Keep; SQLite manages it. |
| `/home/daniele/.codex/sessions` | DO_NOT_DELETE | Session transcripts/history. | Keep. |
| `/home/daniele/.codex/cache` | SAFE_BUT_NOT_RELEVANT | Only about 1.9 MiB. | No cleanup needed. |
| `/home/daniele/.codex/.tmp` | SAFE_BUT_NOT_RELEVANT | Only about 79 MiB. | No cleanup needed. |

## Commands/Evidence
- `du -sh /home/daniele/.codex` -> `154G`.
- `du -xh --max-depth=3 /home/daniele/.codex` -> only `.codex` total is huge; largest normal directory is `sessions` at `263M`.
- `find /home/daniele/.codex -xdev -type f -size +1G` -> only `logs_2.sqlite-wal`.
- `lsof logs_2.sqlite*` -> only active Codex PID `1027576` held the DB/WAL/SHM after stale processes were gone.
- `PRAGMA quick_check` -> `ok`; `PRAGMA integrity_check` -> `ok`.
- `PRAGMA wal_checkpoint(PASSIVE)` -> `0|932|932`.
- `PRAGMA wal_checkpoint(TRUNCATE)` -> `1|1147|1147`, busy due active holder.
- `codex-sqlite-wal-maintenance.service` run -> `status=skip reason=db_open holders=1027576`.
- 60-second growth check from `2026-06-13T19:16:16Z` to `2026-06-13T19:17:16Z`: WAL stayed at `163682495352` bytes; `delta_bytes=0`.

## Fix Applied
- Created `/home/daniele/.local/bin/codex-sqlite-wal-maintenance`.
- Created/enabled `/home/daniele/.config/systemd/user/codex-sqlite-wal-maintenance.service`.
- Created/enabled `/home/daniele/.config/systemd/user/codex-sqlite-wal-maintenance.timer`.
- Timer cadence: boot + every 30 minutes.
- Safety behavior after prompt `938274`: inspect/log every run; below `1 GiB` OK, `1 GiB` soft warning, `5 GiB` hard SQLite-safe maintenance, `20 GiB` critical notification if Telegram helper/env already exist. It runs `quick_check`, attempts `PRAGMA wal_checkpoint(TRUNCATE)` only through SQLite, logs holders and before/after bytes, exits `75` if checkpoint reports busy, and never `rm`s WAL/SHM.
- Started transient unit `codex-sqlite-wal-maintenance-after-codex.service` to run the same cleanup as soon as the current Codex holder exits.

## Current State
- After watcher cleanup: `wal_bytes_after=0`, `recovered_bytes=163682495352`.
- Later prompt `938274` verification: `/dev/sda2` about `916G` size, `104G` used, `766G` available, `12%` used; `/home/daniele/.codex` about `1019M`.
- Current PRAGMA: `journal_mode=wal`, `wal_autocheckpoint=1000`, `synchronous=2`, `page_size=4096`, `page_count=82970`, `freelist_count=12001`, `quick_check=ok`.
- Current holders: active Codex process keeps DB/WAL/SHM handles open during the session, which is expected and must not be interrupted generically.
- Current growth sample: WAL around `10,077,552` bytes for multiple 30-second samples; no rapid recurrence observed during the 2-5 minute check.

## Deep Dive Root Cause
- Technical cause: Codex stores operational logs in SQLite WAL mode. `wal_autocheckpoint=1000` is default and not disabled, but autocheckpoint copies frames back to the DB; it does not guarantee truncating the WAL file allocation, especially while long-lived Codex connections keep DB/WAL/SHM handles open.
- Log pattern: aggregated `logs` table shows high normal verbosity (`TRACE log`, `INFO codex_otel.*`, `TRACE codex_api::endpoint::responses_websocket`) and periodic batches near 1000 rows. No single stacktrace/retry loop was found that alone explains 152 GiB of payload.
- Why cleanup recovered 152.44 GiB: SQLite `wal_checkpoint(TRUNCATE)` could checkpoint the frames and truncate the sidecar after the blocking holder disappeared. This releases allocated filesystem space without deleting Codex sessions/config/credentials/transcripts.
- Forbidden commands: `rm ~/.codex/logs_2.sqlite-wal`, `rm ~/.codex/logs_2.sqlite-shm`, generic `pkill codex`, generic `killall codex`, deleting recent `.codex/sessions`, config, credentials, or transcripts.
- Safe commands: `sqlite3 ~/.codex/logs_2.sqlite 'PRAGMA quick_check;'`, `sqlite3 ~/.codex/logs_2.sqlite 'PRAGMA wal_checkpoint(PASSIVE);'`, `/home/daniele/.local/bin/codex-sqlite-wal-maintenance --dry-run`, `systemctl --user status codex-sqlite-wal-maintenance.timer codex-sqlite-wal-maintenance.service --no-pager`.

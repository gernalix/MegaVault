# os-observer Changelog

This is a synthesized changelog from legacy docs and migration evidence. It does not invent missing dates.

## Extracted Milestones
| source | fact |
|---|---|
| `dev/legacy/dev/CHANGELOG.md` | # Changelog |
| `dev/legacy/dev/CHANGELOG.md` | ## v17 prompt #914582 |
| `dev/legacy/dev/CHANGELOG.md` | - Added configurable cgroups v2 containment for Codex/Android/adb/heavy local jobs through `codex_freeze_runner.py` and `config/codex-resource-presets.json`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added CPU reservation via automatic `AllowedCPUs`, preserving at least one logical CPU for UI/system work. |
| `dev/legacy/dev/CHANGELOG.md` | - Added admission control decisions `ALLOW`, `ALLOW_ULTRA_LIGHT`, `DEFER`, `QUEUE`, `SKIP`, `ABORT_EMERGENCY` using RAM, swap, load, PSI, active rsync/backup and active Gradle/Kotlin evidence. |
| `dev/legacy/dev/CHANGELOG.md` | - Added PSI-driven adaptive throttling with smoothing and hysteresis; pressure raises reduce `CPUQuota`/`IOWeight`, increase cooldown and suppress heavy snapshot/diff work. |
| `dev/legacy/dev/CHANGELOG.md` | - Added local SQLite job queue with `enqueue`, `list`, `run-next`, `cancel`, `retry`, `pause`, `resume`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added Android ultra-light wrappers for build, install, adb and instrumentation; wrappers queue by default and apply single-worker/no-daemon/no-parallel Gradle flags. |
| `dev/legacy/dev/CHANGELOG.md` | - Added tests for PSI hysteresis, admission decisions, cpuset selection, cgroup command generation, queue persistence, unsupported feature fallback and no forced Gradle under critical pressure. |
| `dev/legacy/dev/CHANGELOG.md` | ## v16 prompt #276 |
| `dev/legacy/dev/CHANGELOG.md` | - Root cause fixed for Kuma monitor ID 8 `os-observer-autofix`: the daemon heartbeat is now sent by a dedicated thread, independent from the slow recovery/dashboard/freeze-protection cycle. |
| `dev/legacy/dev/CHANGELOG.md` | - Added heartbeat metrics in `/home/daniele/os_observer/state/autofix_heartbeat_state.json`: `LAST_HEARTBEAT_SENT_AT`, `HEARTBEAT_SEND_RESULT`, `HEARTBEAT_LAG_SECONDS`, `WHY_HEARTBEAT_SKIPPED`, and send duration/status. |
| `dev/legacy/dev/CHANGELOG.md` | - Added recovery-loop timing fields `RECOVERY_CYCLE_DURATION` and `MAX_LOOP_DURATION` to `run_complete` logs. |
| `dev/legacy/dev/CHANGELOG.md` | - Changed the ID 8 self-healer policy: when Kuma reports heartbeat timeout but `os-observer-autofix-agent.service` is loaded, active and running, the agent sends a heartbeat refresh and does not restart itself. |
| `dev/legacy/dev/CHANGELOG.md` | - Added `os_observer_autofix_agent.py --doctor` and extended status output with heartbeat age, next expected heartbeat, and independent-heartbeat state. |
| `dev/legacy/dev/CHANGELOG.md` | ## v15 prompt #944 |
| `dev/legacy/dev/CHANGELOG.md` | - Added reboot/login resilience bootstrap: `os-observer-startup-bootstrap.service` runs at user `default.target`, enables the required user timers/services, starts the autofix daemon and both Kuma pushers, and sends initial `BOOTIN |
| `dev/legacy/dev/CHANGELOG.md` | - Added startup state machine fields `BOOTING`, `WARMING_UP`, `HEALTHY`, `RECOVERING` with `OS_OBSERVER_BOOT_GRACE_SECONDS` and `OS_OBSERVER_HEARTBEAT_STARTUP_DELAY_SECONDS`. |
| `dev/legacy/dev/CHANGELOG.md` | - During boot grace, known push-monitor heartbeat gaps are deferred instead of recorded as recovery attempts, avoiding false-positive Kuma alert churn while the local pusher services come up. |
| `dev/legacy/dev/CHANGELOG.md` | - Extended `kuma-auto-healer doctor` with `LAST_BOOT`, `BOOT_GRACE_ACTIVE`, `HEARTBEAT_STARTUP_DELAY`, `USER_LINGER`, and `STARTUP_STATE`. |
| `dev/legacy/dev/CHANGELOG.md` | - Hardened backup, retention and rsync pushers for post-reboot: backup has a dedicated idle heartbeat timer, retention waits before sending persistent mount-down, and rsync sends `OK idle` heartbeats after a fresh boot without star |
| `dev/legacy/dev/CHANGELOG.md` | - Updated user systemd units to v15, faster startup timers, and `Restart=always` for the long-running autofix daemon. |
| `dev/legacy/dev/CHANGELOG.md` | - Added systemd system automount/mount units for the Seagate6TB2 DEST by UUID, preventing `/media/daniele/Seagate6TB2` from resolving to `/` after reboot. |
| `dev/legacy/dev/CHANGELOG.md` | ## v14 prompt #913 |

## MegaVault Documentation Events
- 2026-06-01: `#739482` moved legacy documentation into `dev/legacy` and created metadata/initial MegaVault docs.
- 2026-06-01T13:20:29+02:00: `#842915` enriched AI and Human docs from legacy docs, repo structure, scripts, tests, and build files.

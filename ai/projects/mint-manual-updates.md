# mint-manual-updates AI OPERATIONS

PROJECT
- name: mint-manual-updates
- slug: mint-manual-updates
- purpose: Servizio user systemd v4 per controllare e applicare aggiornamenti prudenti su Linux Mint 22.3 / Ubuntu noble.
- current_status: Working tree has 6 non-clean entries; do not mix unrelated changes. First entries: M dev/README.md, ?? bin/mint-extra-updater, ?? dev/CHANGELOG.md, ?? dev/TEST_PLAN.md, ?? systemd/user/mint-extra-updater.service
- repo_path: `/home/daniele/codex-workspace/mint-manual-updates`
- remote: `none`
- branch: `master`
- last_verified_commit/date: `6bbe32e` / `2026-06-01T13:20:29+02:00`

STACK
- languages: UNKNOWN
- frameworks: UNKNOWN
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: systemd

CODE_MAP
entrypoints:
- UNKNOWN
important_folders:
- `bin`
- `dev`
- `systemd`
important_files:
- `dev/README.md`
- `dev/TEST_PLAN.md`
- `dev/CHANGELOG.md`
tests:
- `dev/TEST_PLAN.md`
scripts:
- `bin/mint-extra-updater`
- `bin/mint-manual-updates`
generated/runtime/avoid_touch_casually:
- `dev/legacy`

ARCH
summary:
- dev/TEST_PLAN.md: systemd-analyze --user verify systemd/user/mint-extra-updater.service systemd/user/mint-extra-updater.timer
- dev/CHANGELOG.md: - Added `bin/mint-extra-updater` for prompt `#{{RANDOM_6_DIGITS}}`.
- dev/legacy/README.md: Servizio user systemd v4 per controllare e applicare aggiornamenti prudenti su Linux Mint 22.3 / Ubuntu noble.
- dev/legacy/dev/INDEX.md: Patch v4 maintenance fixups: #492837.
- dev/legacy/dev/AGENT_RULES.md: - Non aggiornare automaticamente pip globali, AppImage, Docker Compose o VM Oracle.
- dev/legacy/dev/TEST_PLAN.md: bash -n bin/mint-manual-updates
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/TEST_PLAN.md` | # Test Plan |
| `dev/TEST_PLAN.md` | ## Static checks |
| `dev/TEST_PLAN.md` | ## Install verification |
| `dev/TEST_PLAN.md` | ## Safe execution |
| `dev/CHANGELOG.md` | # Changelog |
| `dev/CHANGELOG.md` | ## 2026-06-01 |
| `dev/legacy/README.md` | # mint-manual-updates |
| `dev/legacy/README.md` | ## Uso |
| `dev/legacy/README.md` | ## Guardrail |
| `dev/legacy/README.md` | ## Cosa aggiorna |
| `dev/legacy/README.md` | ## Cosa segnala soltanto |
| `dev/legacy/README.md` | ## Fixup manuali |
| `dev/legacy/README.md` | ## Timer |
| `dev/legacy/dev/INDEX.md` | # dev index |
| `dev/legacy/dev/INDEX.md` | ## Componenti |
| `dev/legacy/dev/INDEX.md` | ## Operazioni rapide |
| `dev/legacy/dev/INDEX.md` | ## Guardrail v3 |
| `dev/legacy/dev/INDEX.md` | ## Maintenance fixups v4 |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/TEST_PLAN.md` | ## Safe execution |
| `dev/TEST_PLAN.md` | - `--run` updates only safe extra surfaces: Flatpak, fwupd non-reboot firmware candidates, user zipapp `yt-dlp`, `pipx upgrade-all`, and `rustup update` when installed. |
| `dev/legacy/README.md` | - swap: non oltre `70%`; |
| `dev/legacy/README.md` | - PSI `some avg10`: CPU/IO/memoria non oltre `25`; |
| `dev/legacy/README.md` | - processi pesanti: backup reali, `rsync` reali, gradle/kotlin/freeze noti; |
| `dev/legacy/README.md` | `--relaxed` è solo manuale: alza solo load a `CPU * 3.00` e PSI CPU a `35`. Non rilassa RAM, swap, processi pesanti, freeze emergency, apt/dpkg o batteria critica. |
| `dev/legacy/README.md` | I monitor di trasferimento che non copiano dati non sono bloccanti: `transfer_usb_io_watchdog.sh`, `transfer_vecchio_disco_adaptive_throttle.sh`, `rsync_uptime_kuma_push.sh` e `tail -F` dei log di trasferimento. Un trasferimento blocca so |
| `dev/legacy/README.md` | `--force` è solo manuale e richiede un TTY con conferma esatta `FORCE_UPDATE`. Non bypassa apt/dpkg attivi, freeze emergency o batteria critica. Il timer non usa mai `--relaxed` o `--force`. |
| `dev/legacy/README.md` | - `apt`: esegue `sudo apt update`, simula `upgrade` e `full-upgrade`, applica solo se non ci sono hold, lock, check falliti, rimozioni o problemi evidenti. |
| `dev/legacy/README.md` | - `fwupd`: esegue refresh e `get-updates`; applica solo update che non dichiarano reboot/interazione manuale e passa comunque dai safety check di `fwupdmgr`. Gli altri sono solo segnalati. |
| `dev/legacy/README.md` | - `Docker`: mostra immagini e container locali; non esegue pull, compose up o update globali. |
| `dev/legacy/README.md` | - diagnosi `fwupd` con `--version`, `get-devices`, `get-updates --verbose` e journal; riavvia `fwupd` e forza refresh solo se il fallimento sembra servizio/cache; |
| `dev/legacy/README.md` | - non sovrascrive `pipx` apt-managed con pip; usa `pipx self-upgrade` solo se disponibile; |
| `dev/legacy/README.md` | Se `sudo -n` non e disponibile, le sezioni apt falliscono pulite e il report mostra il comando manuale necessario. |
| `dev/legacy/dev/INDEX.md` | - Manuale `--force`: richiede TTY e conferma `FORCE_UPDATE`; non bypassa apt/dpkg, freeze emergency o batteria critica. |
| `dev/legacy/dev/INDEX.md` | - I monitor `transfer_usb_io_watchdog.sh`, `transfer_vecchio_disco_adaptive_throttle.sh`, `rsync_uptime_kuma_push.sh` e `tail -F` dei log trasferimento non sono bloccanti. |
| `dev/legacy/dev/INDEX.md` | - `--maintenance-fixups` e solo manuale e non deve essere aggiunto al timer. |
| `dev/legacy/dev/INDEX.md` | - `fwupd`: diagnosi completa; restart/refresh solo per problemi servizio/cache; non installa firmware rischiosi. |
| `dev/legacy/dev/AGENT_RULES.md` | - Non aggiornare automaticamente pip globali, AppImage, Docker Compose o VM Oracle. |
| `dev/legacy/dev/AGENT_RULES.md` | - Non aggiungere segreti Telegram; usare solo `/home/daniele/codex-workspace/scripts/amici_fb/telegram_notify.py` se presente e gia configurato. |
| `dev/legacy/dev/AGENT_RULES.md` | - Non trasformare il servizio user in servizio root. |
| `dev/legacy/dev/AGENT_RULES.md` | - Non aggiungere `--relaxed` o `--force` alle unit systemd/timer automatiche. |
| `dev/legacy/dev/AGENT_RULES.md` | - Non usare `--force` senza richiesta esplicita dell'utente; richiede conferma interattiva `FORCE_UPDATE`. |
| `dev/legacy/dev/AGENT_RULES.md` | - `--relaxed` puo rilassare solo load e PSI CPU; non deve rilassare RAM, swap, apt/dpkg, freeze emergency, batteria critica o processi pesanti. |
| `dev/legacy/dev/AGENT_RULES.md` | - Non trattare i monitor di trasferimento come backup pesanti: bloccare solo processi reali con comando `rsync`, non watchdog/push/tail dei log. |
| `dev/legacy/dev/AGENT_RULES.md` | - Non rimuovere pacchetti apt in automatico: le simulazioni con rimozioni o problemi devono bloccare la sezione. |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
| source | fact |
|---|---|
| `dev/TEST_PLAN.md` | bash -n bin/mint-extra-updater |
| `dev/TEST_PLAN.md` | systemctl --user daemon-reload |
| `dev/TEST_PLAN.md` | systemctl --user status mint-extra-updater.service --no-pager |
| `dev/TEST_PLAN.md` | systemctl --user status mint-extra-updater.timer --no-pager |
| `dev/TEST_PLAN.md` | - npm, gem, cargo, and Android SDK stay report-only. |
| `dev/CHANGELOG.md` | - Kept this updater outside `apt`, `dist-upgrade`, package removals, and automatic npm/gem/cargo/Android SDK changes. |
| `dev/legacy/README.md` | - processi pesanti: backup reali, `rsync` reali, gradle/kotlin/freeze noti; |
| `dev/legacy/README.md` | systemctl --user status mint-manual-updates.timer |
| `dev/legacy/README.md` | systemctl --user list-timers mint-manual-updates.timer |
| `dev/legacy/README.md` | journalctl --user -u mint-manual-updates.service -n 120 --no-pager |
| `dev/legacy/dev/INDEX.md` | systemctl --user status mint-manual-updates.timer |
| `dev/legacy/dev/INDEX.md` | systemctl --user list-timers mint-manual-updates.timer |
| `dev/legacy/dev/AGENT_RULES.md` | - Preservare compatibilita bash e validare con `bash -n`; usare `shellcheck` se disponibile. |
| `dev/legacy/dev/TEST_PLAN.md` | bash -n bin/mint-manual-updates |
| `dev/legacy/dev/TEST_PLAN.md` | yt-dlp --version |
| `dev/legacy/dev/TEST_PLAN.md` | python3 -m pip --version |
| `dev/legacy/dev/TEST_PLAN.md` | fwupdmgr get-updates |
| `dev/legacy/dev/TEST_PLAN.md` | systemctl --user daemon-reload |
| `dev/legacy/dev/TEST_PLAN.md` | systemctl --user enable --now mint-manual-updates.timer |
| `dev/legacy/dev/TEST_PLAN.md` | systemctl --user start mint-manual-updates.service |
| `dev/legacy/dev/TEST_PLAN.md` | systemctl --user status mint-manual-updates.timer --no-pager |
| `dev/legacy/dev/TEST_PLAN.md` | systemctl --user list-timers mint-manual-updates.timer --no-pager |
test_targets:
- `dev/TEST_PLAN.md`
known_test_flakiness_or_requirements:
- dev/TEST_PLAN.md: - `fwupdmgr get-updates` with `No updatable devices` is not treated as a critical error.
- dev/legacy/README.md: - processi pesanti: backup reali, `rsync` reali, gradle/kotlin/freeze noti;
- dev/legacy/README.md: `--explain-guardrails` mostra tutti i valori misurati, soglie, esito `PASS`/`FAIL`, processi responsabili, `rsync` reali, top CPU/RAM e un `Decision summary` finale.
- dev/legacy/dev/TEST_PLAN.md: - `--explain-guardrails` mostri valore, soglia, PASS/FAIL, processi responsabili, `rsync` reali, top CPU/RAM e `Decision summary`;
- dev/legacy/dev/TEST_PLAN.md: - `--relaxed` rilassi solo load e PSI CPU, non RAM/swap/processi pesanti/freeze/apt/batteria;

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/TEST_PLAN.md` | - `--run` updates only safe extra surfaces: Flatpak, fwupd non-reboot firmware candidates, user zipapp `yt-dlp`, `pipx upgrade-all`, and `rustup update` when installed. |
| `dev/legacy/README.md` | I monitor di trasferimento che non copiano dati non sono bloccanti: `transfer_usb_io_watchdog.sh`, `transfer_vecchio_disco_adaptive_throttle.sh`, `rsync_uptime_kuma_push.sh` e `tail -F` dei log di trasferimento. Un trasferimento blocca so |
| `dev/legacy/README.md` | - diagnosi `fwupd` con `--version`, `get-devices`, `get-updates --verbose` e journal; riavvia `fwupd` e forza refresh solo se il fallimento sembra servizio/cache; |
| `dev/legacy/dev/INDEX.md` | - I monitor `transfer_usb_io_watchdog.sh`, `transfer_vecchio_disco_adaptive_throttle.sh`, `rsync_uptime_kuma_push.sh` e `tail -F` dei log trasferimento non sono bloccanti. |
| `dev/legacy/dev/AGENT_RULES.md` | - Non trattare i monitor di trasferimento come backup pesanti: bloccare solo processi reali con comando `rsync`, non watchdog/push/tail dei log. |
| `dev/legacy/dev/TEST_PLAN.md` | - i monitor `transfer_usb_io_watchdog.sh`, `transfer_vecchio_disco_adaptive_throttle.sh`, `rsync_uptime_kuma_push.sh` e `tail -F` log trasferimento non siano bloccanti; |
| `dev/legacy/dev/TEST_PLAN.md` | yt-dlp --version |
| `dev/legacy/dev/TEST_PLAN.md` | pipx --version |
| `dev/legacy/dev/TEST_PLAN.md` | python3 -m pip --version |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/README.md` | - processi pesanti: backup reali, `rsync` reali, gradle/kotlin/freeze noti; |
| `dev/legacy/README.md` | I monitor di trasferimento che non copiano dati non sono bloccanti: `transfer_usb_io_watchdog.sh`, `transfer_vecchio_disco_adaptive_throttle.sh`, `rsync_uptime_kuma_push.sh` e `tail -F` dei log di trasferimento. Un trasferimento blocca so |
| `dev/legacy/dev/INDEX.md` | - I monitor `transfer_usb_io_watchdog.sh`, `transfer_vecchio_disco_adaptive_throttle.sh`, `rsync_uptime_kuma_push.sh` e `tail -F` dei log trasferimento non sono bloccanti. |
| `dev/legacy/dev/AGENT_RULES.md` | - Non trattare i monitor di trasferimento come backup pesanti: bloccare solo processi reali con comando `rsync`, non watchdog/push/tail dei log. |
| `dev/legacy/dev/TEST_PLAN.md` | - i monitor `transfer_usb_io_watchdog.sh`, `transfer_vecchio_disco_adaptive_throttle.sh`, `rsync_uptime_kuma_push.sh` e `tail -F` log trasferimento non siano bloccanti; |
| `dev/CHANGELOG.md` | - Kept this updater outside `apt`, `dist-upgrade`, package removals, and automatic npm/gem/cargo/Android SDK changes. |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `dev/TEST_PLAN.md` | - `fwupdmgr get-updates` with `No updatable devices` is not treated as a critical error. |
| `dev/legacy/README.md` | - processi pesanti: backup reali, `rsync` reali, gradle/kotlin/freeze noti; |
| `dev/legacy/README.md` | `--explain-guardrails` mostra tutti i valori misurati, soglie, esito `PASS`/`FAIL`, processi responsabili, `rsync` reali, top CPU/RAM e un `Decision summary` finale. |
| `dev/legacy/README.md` | `--relaxed` è solo manuale: alza solo load a `CPU * 3.00` e PSI CPU a `35`. Non rilassa RAM, swap, processi pesanti, freeze emergency, apt/dpkg o batteria critica. |
| `dev/legacy/README.md` | `--force` è solo manuale e richiede un TTY con conferma esatta `FORCE_UPDATE`. Non bypassa apt/dpkg attivi, freeze emergency o batteria critica. Il timer non usa mai `--relaxed` o `--force`. |
| `dev/legacy/dev/INDEX.md` | - Manuale `--force`: richiede TTY e conferma `FORCE_UPDATE`; non bypassa apt/dpkg, freeze emergency o batteria critica. |
| `dev/legacy/dev/AGENT_RULES.md` | - Mantenere guardrail anti-freeze prima di ogni run reale. |
| `dev/legacy/dev/AGENT_RULES.md` | - `--relaxed` puo rilassare solo load e PSI CPU; non deve rilassare RAM, swap, apt/dpkg, freeze emergency, batteria critica o processi pesanti. |
| `dev/legacy/dev/TEST_PLAN.md` | - `--explain-guardrails` mostri valore, soglia, PASS/FAIL, processi responsabili, `rsync` reali, top CPU/RAM e `Decision summary`; |
| `dev/legacy/dev/TEST_PLAN.md` | - `--relaxed` rilassi solo load e PSI CPU, non RAM/swap/processi pesanti/freeze/apt/batteria; |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/TEST_PLAN.md: ## Safe execution
- dev/TEST_PLAN.md: - `--run` updates only safe extra surfaces: Flatpak, fwupd non-reboot firmware candidates, user zipapp `yt-dlp`, `pipx upgrade-all`, and `rustup update` when installed.
- dev/legacy/README.md: - processi pesanti: backup reali, `rsync` reali, gradle/kotlin/freeze noti;
- dev/legacy/README.md: - `fwupd`: esegue refresh e `get-updates`; applica solo update che non dichiarano reboot/interazione manuale e passa comunque dai safety check di `fwupdmgr`. Gli altri sono solo segnalati.
- dev/legacy/README.md: - diagnosi `fwupd` con `--version`, `get-devices`, `get-updates --verbose` e journal; riavvia `fwupd` e forza refresh solo se il fallimento sembra servizio/cache;
- dev/legacy/dev/AGENT_RULES.md: - Non trattare i monitor di trasferimento come backup pesanti: bloccare solo processi reali con comando `rsync`, non watchdog/push/tail dei log.
- dev/legacy/dev/AGENT_RULES.md: - Nei fixup manuali non usare `sudo pip` o `--break-system-packages`; preservare pacchetti apt-managed.
- dev/legacy/dev/AGENT_RULES.md: - Firmware su Surface delicato: applicare solo update che non dichiarano reboot/interazione manuale e senza disabilitare i safety check di `fwupdmgr`; altrimenti segnalare soltanto.
- dev/legacy/dev/TEST_PLAN.md: - fwupd applichi solo firmware senza reboot/interazione dichiarata e senza disabilitare i safety check.
- dev/legacy/dev/TEST_PLAN.md: yt-dlp --version
- dev/legacy/dev/TEST_PLAN.md: pipx --version
- dev/legacy/dev/TEST_PLAN.md: python3 -m pip --version

RECENT_DECISIONS
| source | fact |
|---|---|
| `dev/CHANGELOG.md` | # Changelog |
| `dev/CHANGELOG.md` | ## 2026-06-01 |
| `dev/CHANGELOG.md` | - Added `bin/mint-extra-updater` for prompt `#{{RANDOM_6_DIGITS}}`. |
| `dev/CHANGELOG.md` | - Added optional user-level `mint-extra-updater.service` and `mint-extra-updater.timer`. |
| `dev/CHANGELOG.md` | - Kept this updater outside `apt`, `dist-upgrade`, package removals, and automatic npm/gem/cargo/Android SDK changes. |
| `dev/CHANGELOG.md` | - Wrote timestamped logs under `~/.local/state/mint-extra-updater/logs/` and reports under `~/.local/state/mint-extra-updater/reports/`. |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `UNKNOWN` | no verified roadmap found in read sources. |

LEGACY_SUMMARY
- legacy_docs_read_count: 7
- legacy_docs_read:
- `dev/README.md`
- `dev/TEST_PLAN.md`
- `dev/CHANGELOG.md`
- `dev/legacy/README.md`
- `dev/legacy/dev/INDEX.md`
- `dev/legacy/dev/AGENT_RULES.md`
- `dev/legacy/dev/TEST_PLAN.md`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../mint-manual-updates/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/mint-manual-updates/overview.md)
- human_folder: [human folder](../../human/projects/mint-manual-updates)
- legacy_docs: [dev/legacy](../../../mint-manual-updates/dev/legacy)
- repo_path: [repo](../../../mint-manual-updates)

OPEN_QUESTIONS
- none detected in extracted sources

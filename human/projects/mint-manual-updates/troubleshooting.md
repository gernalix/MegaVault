# mint-manual-updates Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
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

## Useful Checks Or Commands
| source | fact |
|---|---|
| `dev/README.md` | - npm global packages |
| `dev/README.md` | systemctl --user status mint-extra-updater.service --no-pager |
| `dev/README.md` | systemctl --user status mint-extra-updater.timer --no-pager |
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

## Safety Checks Before Fixing
- dev/TEST_PLAN.md: ## Safe execution
- dev/TEST_PLAN.md: - `--run` updates only safe extra surfaces: Flatpak, fwupd non-reboot firmware candidates, user zipapp `yt-dlp`, `pipx upgrade-all`, and `rustup update` when installed.
- dev/legacy/README.md: - processi pesanti: backup reali, `rsync` reali, gradle/kotlin/freeze noti;
- dev/legacy/README.md: I monitor di trasferimento che non copiano dati non sono bloccanti: `transfer_usb_io_watchdog.sh`, `transfer_vecchio_disco_adaptive_throttle.sh`, `rsync_uptime_kuma_push.sh` e `tail -F` dei log di trasferimento. Un trasferimento blocca so
- dev/legacy/README.md: - `fwupd`: esegue refresh e `get-updates`; applica solo update che non dichiarano reboot/interazione manuale e passa comunque dai safety check di `fwupdmgr`. Gli altri sono solo segnalati.
- dev/legacy/README.md: - diagnosi `fwupd` con `--version`, `get-devices`, `get-updates --verbose` e journal; riavvia `fwupd` e forza refresh solo se il fallimento sembra servizio/cache;
- dev/legacy/dev/INDEX.md: - I monitor `transfer_usb_io_watchdog.sh`, `transfer_vecchio_disco_adaptive_throttle.sh`, `rsync_uptime_kuma_push.sh` e `tail -F` dei log trasferimento non sono bloccanti.
- dev/legacy/dev/AGENT_RULES.md: - Non trattare i monitor di trasferimento come backup pesanti: bloccare solo processi reali con comando `rsync`, non watchdog/push/tail dei log.
- dev/legacy/dev/AGENT_RULES.md: - Nei fixup manuali non usare `sudo pip` o `--break-system-packages`; preservare pacchetti apt-managed.
- dev/legacy/dev/AGENT_RULES.md: - Firmware su Surface delicato: applicare solo update che non dichiarano reboot/interazione manuale e senza disabilitare i safety check di `fwupdmgr`; altrimenti segnalare soltanto.
- dev/legacy/dev/TEST_PLAN.md: - i monitor `transfer_usb_io_watchdog.sh`, `transfer_vecchio_disco_adaptive_throttle.sh`, `rsync_uptime_kuma_push.sh` e `tail -F` log trasferimento non siano bloccanti;
- dev/legacy/dev/TEST_PLAN.md: - fwupd applichi solo firmware senza reboot/interazione dichiarata e senza disabilitare i safety check.
- dev/legacy/dev/TEST_PLAN.md: yt-dlp --version
- dev/legacy/dev/TEST_PLAN.md: pipx --version

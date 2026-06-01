# mint-manual-updates Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/TEST_PLAN.md: systemd-analyze --user verify systemd/user/mint-extra-updater.service systemd/user/mint-extra-updater.timer

## Useful Limits And Boundaries
- dev/TEST_PLAN.md: ## Safe execution
- dev/TEST_PLAN.md: - `--run` updates only safe extra surfaces: Flatpak, fwupd non-reboot firmware candidates, user zipapp `yt-dlp`, `pipx upgrade-all`, and `rustup update` when installed.
- dev/legacy/README.md: - processi pesanti: backup reali, `rsync` reali, gradle/kotlin/freeze noti;
- dev/legacy/README.md: `--relaxed` è solo manuale: alza solo load a `CPU * 3.00` e PSI CPU a `35`. Non rilassa RAM, swap, processi pesanti, freeze emergency, apt/dpkg o batteria critica.
- dev/legacy/README.md: `--force` è solo manuale e richiede un TTY con conferma esatta `FORCE_UPDATE`. Non bypassa apt/dpkg attivi, freeze emergency o batteria critica. Il timer non usa mai `--relaxed` o `--force`.
- dev/legacy/README.md: - `fwupd`: esegue refresh e `get-updates`; applica solo update che non dichiarano reboot/interazione manuale e passa comunque dai safety check di `fwupdmgr`. Gli altri sono solo segnalati.
- dev/legacy/README.md: Se `sudo -n` non e disponibile, le sezioni apt falliscono pulite e il report mostra il comando manuale necessario.
- dev/legacy/dev/INDEX.md: - Manuale `--force`: richiede TTY e conferma `FORCE_UPDATE`; non bypassa apt/dpkg, freeze emergency o batteria critica.
- dev/legacy/dev/INDEX.md: - `--maintenance-fixups` e solo manuale e non deve essere aggiunto al timer.
- dev/legacy/dev/AGENT_RULES.md: - Non trattare i monitor di trasferimento come backup pesanti: bloccare solo processi reali con comando `rsync`, non watchdog/push/tail dei log.
- dev/legacy/dev/AGENT_RULES.md: - Nei fixup manuali non usare `sudo pip` o `--break-system-packages`; preservare pacchetti apt-managed.
- dev/legacy/dev/AGENT_RULES.md: - Firmware su Surface delicato: applicare solo update che non dichiarano reboot/interazione manuale e senza disabilitare i safety check di `fwupdmgr`; altrimenti segnalare soltanto.

## Where The Feature Code Appears To Live
- `bin/mint-extra-updater`
- `bin/mint-manual-updates`

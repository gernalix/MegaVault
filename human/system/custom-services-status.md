# Custom Services Status

Aggiornamento operativo: 2026-06-07 07:40 CEST.

Prompt: `#847261`.

## Anti-Freeze Legacy Rimossi

Eliminati da systemd/disko e rimossi dal routing MegaVault vivo:

- `freeze-reboot-monitor.service`
- `freeze-zram-swap.service`
- `screen-watchdog.service`
- `system-watchdog.service`
- `/home/daniele/freeze_reboot_monitor`
- `/home/daniele/codex-workspace/mint_freeze_diag`
- `/home/daniele/codex-workspace/system_watchdog`
- `/home/daniele/bin/kuma-auto-healer`
- `/home/daniele/.config/kuma-auto-healer`
- `/etc/sysctl.d/99-codex-mint-freeze.conf`
- `/etc/sysctl.d/99-z-freeze-anti-freeze.conf`

Verifica:

```bash
systemctl list-unit-files --no-pager | rg -i 'freeze-reboot|freeze-zram|screen-watchdog|system-watchdog'
systemctl --user list-unit-files --no-pager | rg -i 'freeze|autofix|os-observer|system-watchdog|screen-watchdog'
```

Risultato 2026-06-07: nessuna unità legacy trovata.

## Nuovi Servizi Osservativi

| Nome | Scope | Stato atteso | Script | Note |
|---|---|---|---|---|
| `mint-freeze-forensics.service` | user | enabled/running | `~/.local/bin/mint-freeze-forensics daemon` | sampler 5s; no remediation |
| `mint-resource-guardian.timer` | user | enabled/running | `mint-resource-guardian.service` | early warning; cooldown; no kill automatico |
| `mint-resource-guardian.service` | user | oneshot | `mint-freeze-forensics guardian --once --non-interactive` | CLI manuale supporta prompt `[K] [I] [W] [D]` |

## Servizi Lasciati Fuori Dalla Rimozione

- `transfer-usb-io-watchdog.service`: non è anti-freeze generico; guardrail dati per transfer rsync.
- `rsync-uptime-kuma-push.service`: pusher Kuma specifico transfer.
- `home-backup-kuma-push*`, `mint-cloud-backup-kuma-push*`, `mint-update-tracker*`: monitor/pusher specifici, non remediation freeze.

## Kuma

- Kuma runtime: Oracle VM `150.230.148.128`, container `uptime-kuma`.
- Nuovo gruppo: `Mint Freeze Analysis`, id `12`.
- Monitor: `Freeze Gaps` id `13`, `PSI Memory` id `14`, `PSI IO` id `15`, `Guardian Alerts` id `16`, `Forensics Alive` id `17`.

## Fonti

- `systemctl list-unit-files`
- `systemctl --user list-unit-files`
- `systemctl --user status mint-freeze-forensics.service`
- `ssh ubuntu@150.230.148.128 sudo sqlite3 /opt/uptime-kuma/data/kuma.db`

---

## Merged Detailed Snapshot From GitHub Branch 20260705

## Prompt #584731 Operative Update

Aggiornamento: 2026-06-05 07:50 CEST.

Anti-freeze/watchdog residui disattivati operativamente:

- `user:codex-freeze-runner@.service` rimosso dal path live e spostato nello snapshot del prompt.

Servizi utili lasciati attivi:

- `transfer-usb-io-watchdog.service`: guardrail safety del transfer rsync, non anti-freeze generico.
- `rsync-uptime-kuma-push.service`: Kuma/pusher del transfer.
- `disk-usage-monitor.timer`: monitor disco.
- `codex-usage-monitor.timer`: monitor uso Codex.
- `mint-update-tracker.service` e `mint-update-tracker.timer`: audit software.
- `mint-cloud-backup*`: backup e pusher/monitor backup.

Snapshot pre-modifica:

`/home/daniele/codex-workspace/MegaVault/ai/reports/prompt_584731_antifreeze_snapshot_20260605T074354+0200`

Scansione locale: 2026-06-05 05:58:49 CEST

Prompt: #739284

Definizione custom applicata: solo servizi/timer creati da te, da automazioni personali, da tuoi progetti o da precedenti prompt Codex. Esclusi servizi di software terzi anche quando il file unit si trova in `~/.config/systemd/user/`.

Vincolo rispettato: scansione read-only; nessuna unit avviata, fermata, abilitata, disabilitata o modificata.

Nota protocollo MegaVault: il report human è la fonte dello snapshot; AI doc aggiornato solo con link, senza duplicare tabella/stato vivo.

## Sintesi

- Servizi custom: 42
- Timer custom: 20
- Path custom: 1
- Socket custom: 0
- Servizi attivi: 18
- Servizi inattivi: 20
- Servizi failed: 1
- Servizi altro/transizione: 3
- Servizi esclusi come software terzi: 1

## Servizi Custom

| Nome | Scope | Progetto associato | Stato | Timer associato | Script principale | Ultimo stato significativo |
|---|---|---|---|---|---|---|
| `disk-usage-monitor.service` | system | dedotta/incerta | inattivo | `disk-usage-monitor.timer` | `/home/daniele/disk_usage_monitor/disk_usage_monitor.sh` | result=success; inactive_enter=Fri 2026-06-05 05:55:47 CEST |
| `freeze-reboot-monitor.service` | system | /home/daniele/freeze_reboot_monitor (dedotta/incerta) | attivo | - | `/home/daniele/freeze_reboot_monitor/freeze_reboot_monitor.sh` | result=success; active_enter=Fri 2026-06-05 05:43:51 CEST |
| `freeze-zram-swap.service` | system | /home/daniele/freeze_reboot_monitor (dedotta/incerta) | attivo | - | `/home/daniele/freeze_reboot_monitor/setup_zram_swap.sh` | result=success; active_enter=Fri 2026-06-05 05:43:49 CEST |
| `mint-cloud-backup-dashboard.service` | system | /home/daniele/codex-projects/mint-cloud-backup | attivo | - | `/usr/local/bin/mint-cloud-backup-dashboard` | result=success; active_enter=Fri 2026-06-05 05:44:01 CEST |
| `mint-cloud-backup-kuma-push.service` | system | /home/daniele/codex-projects/mint-cloud-backup | activating | `mint-cloud-backup-kuma-push.timer` | `/usr/local/bin/mint-cloud-backup-kuma-push` | result=success; inactive_enter=Fri 2026-06-05 05:57:46 CEST |
| `mint-cloud-backup-monitor.service` | system | /home/daniele/codex-projects/mint-cloud-backup | attivo | - | `/usr/local/bin/mint-cloud-backup-monitor` | result=success; active_enter=Fri 2026-06-05 05:44:01 CEST |
| `mint-cloud-backup.service` | system | /home/daniele/codex-projects/mint-cloud-backup | activating | `mint-cloud-backup.timer` | `/usr/local/bin/mint-cloud-backup` | result=success |
| `remote-recovery-tmux.service` | system | /home/daniele/codex-workspace/surface-recovery-hardening (dedotta) | attivo | - | `/home/daniele/remote_recovery_tmux.sh` | result=success; active_enter=Fri 2026-06-05 05:44:01 CEST |
| `screen-watchdog.service` | system | /home/daniele/codex-workspace/surface-recovery-hardening (dedotta) | inattivo | - | `/home/daniele/screen_watchdog.sh` | result=success |
| `surface-no-suspend.service` | system | /home/daniele/codex-workspace/surface-recovery-hardening (dedotta) | attivo | - | `/usr/bin/systemd-inhibit` | result=success; active_enter=Fri 2026-06-05 05:44:01 CEST |
| `system-watchdog.service` | system | /home/daniele/codex-workspace/system_watchdog | attivo | - | `/home/daniele/codex-workspace/system_watchdog/watchdog.py` | result=success; active_enter=Fri 2026-06-05 05:44:01 CEST |
| `transfer-usb-io-watchdog.service` | system | /home/daniele/codex-workspace/surface-recovery-hardening (dedotta) | attivo | - | `/home/daniele/transfer_usb_io_watchdog.sh` | result=success; active_enter=Fri 2026-06-05 05:44:01 CEST |
| `adb-wifi-autoconnect.service` | user | /home/daniele/.local/bin + Android SDK (dedotta/incerta) | attivo | - | `/home/daniele/.local/bin/adb-wifi-autoconnect` | result=success; active_enter=Fri 2026-06-05 05:43:58 CEST |
| `amici_fb.service` | user | /home/daniele/codex-workspace/scripts/amici_fb | inattivo | `amici_fb.timer` | `/home/daniele/codex-workspace/scripts/amici_fb/.venv/bin/python` | result=success |
| `android-sdk-auto-update.service` | user | /home/daniele/codex-workspace/android-sdk-auto-update | inattivo | `android-sdk-auto-update.timer` | `/home/daniele/bin/android_sdk_auto_update.sh` | result=success |
| `chatgpt-chrome-live-logger.service` | user | /home/daniele/codex-workspace/chatgpt-chrome-debug | attivo | - | `/home/daniele/codex-workspace/chatgpt-chrome-debug/scripts/live_chrome_logger.sh` | result=success; active_enter=Fri 2026-06-05 05:43:58 CEST |
| `codex-freeze-runner@.service` | user | /home/daniele/codex-workspace/os-observer | unknown | - | `-` | n/a |
| `codex-html-live.service` | user | dedotta/incerta | attivo | - | `/home/daniele/bin/codex-html-live` | result=success; active_enter=Fri 2026-06-05 05:43:58 CEST |
| `codex-usage-monitor.service` | user | /home/daniele/codex-workspace/codex-token-watcher | inattivo | `codex-usage-monitor.timer` | `/home/daniele/codex-workspace/codex-token-watcher/codex_usage_monitor.py` | result=success; inactive_enter=Fri 2026-06-05 05:54:31 CEST |
| `facebook-video-archiver.service` | user | /home/daniele/codex-workspace/facebook-video-archiver | inattivo | `facebook-video-archiver.timer` | `/home/daniele/codex-workspace/facebook-video-archiver/facebook_video_archiver.sh` | result=success |
| `home-backup-kuma-push.service` | user | /home/daniele/codex-workspace/os-observer | inattivo | `home-backup-kuma-push.timer` | `/home/daniele/home_backup_kuma_push.sh` | result=success; inactive_enter=Fri 2026-06-05 05:54:23 CEST |
| `home-backup-retention-kuma-push.service` | user | /home/daniele/codex-workspace/os-observer | inattivo | `home-backup-retention-kuma-push.timer` | `/home/daniele/home_backup_kuma_push.sh` | result=success; inactive_enter=Fri 2026-06-05 05:58:22 CEST |
| `home-incremental-backup.service` | user | dedotta/incerta | inattivo | `home-incremental-backup.timer` | `/home/daniele/home_incremental_backup.sh` | result=success |
| `logseq-update-checker.service` | user | dedotta/incerta | inattivo | `logseq-update-checker.timer` | `/home/daniele/.local/bin/logseq-update-checker` | result=success |
| `mint-extra-updater.service` | user | /home/daniele/codex-workspace/mint-manual-updates | inattivo | `mint-extra-updater.timer` | `/home/daniele/codex-workspace/mint-manual-updates/bin/mint-extra-updater` | result=success |
| `mint-manual-updates.service` | user | /home/daniele/codex-workspace/mint-manual-updates | inattivo | `mint-manual-updates.timer` | `/home/daniele/codex-workspace/mint-manual-updates/bin/mint-manual-updates` | result=success |
| `mint-update-tracker-backfill.service` | user | /home/daniele/codex-workspace/mint-update-tracker | inattivo | `mint-update-tracker.timer` | `/home/daniele/codex-workspace/mint-update-tracker/mint_update_tracker.py` | result=success; inactive_enter=Fri 2026-06-05 05:54:18 CEST |
| `mint-update-tracker.service` | user | /home/daniele/codex-workspace/mint-update-tracker | attivo | `mint-update-tracker.timer` | `/home/daniele/codex-workspace/mint-update-tracker/mint_update_tracker.py` | result=success; active_enter=Fri 2026-06-05 05:44:20 CEST |
| `mint-xfce-layout-guard.service` | user | dedotta/incerta | inattivo | `mint-xfce-layout-guard.timer` | `/home/daniele/.local/bin/mint-xfce-layout-guard` | result=success; inactive_enter=Fri 2026-06-05 05:58:20 CEST |
| `os-observer-autofix-agent.service` | user | /home/daniele/codex-workspace/os-observer | inattivo | `os-observer-autofix-agent.timer` | `/home/daniele/codex-workspace/os-observer/os_observer_autofix_agent.py` | result=success |
| `os-observer-startup-bootstrap.service` | user | /home/daniele/codex-workspace/os-observer | inattivo | - | `/home/daniele/codex-workspace/os-observer/kuma_auto_healer.py` | result=success |
| `os-observer.service` | user | /home/daniele/codex-workspace/os-observer | inattivo | `os-observer.timer` | `/home/daniele/codex-workspace/os-observer/os_observer.sh` | result=success |
| `owntracks-sqlite-watcher.service` | user | /home/daniele/codex-workspace/owntracks-sqlite-watcher | inattivo | - | `/home/daniele/.local/bin/owntracks-sqlite-watcher` | result=success |
| `parcel-tracker.service` | user | /home/daniele/codex-workspace/parcel-tracker | inattivo | `parcel-tracker.timer` | `/home/daniele/codex-workspace/parcel-tracker/parcel_tracker.sh` | result=success; inactive_enter=Fri 2026-06-05 05:48:41 CEST |
| `rsync-uptime-kuma-push.service` | user | dedotta/incerta | attivo | - | `/home/daniele/rsync_uptime_kuma_push.sh` | result=success; active_enter=Fri 2026-06-05 05:43:58 CEST |
| `system-service-dashboard.service` | user | /home/daniele/codex-workspace/linux-mint-service-dashboard | attivo | - | `/home/daniele/codex-workspace/linux-mint-service-dashboard/app/server.py` | result=success; active_enter=Fri 2026-06-05 05:44:18 CEST |
| `terminal-logger-codex-snapshot.service` | user | /home/daniele/codex-workspace/os-observer (dedotta/incerta) | inattivo | `terminal-logger-codex-snapshot.timer` | `/home/daniele/.local/share/terminal-logger/bin/terminal-logger` | result=success; inactive_enter=Fri 2026-06-05 05:58:39 CEST |
| `terminal-logger-codex.service` | user | /home/daniele/codex-workspace/os-observer (dedotta/incerta) | attivo | - | `/home/daniele/.local/share/terminal-logger/bin/terminal-logger` | result=success; active_enter=Fri 2026-06-05 05:44:18 CEST |
| `terminal-logger-maintenance.service` | user | /home/daniele/codex-workspace/os-observer (dedotta/incerta) | failed | `terminal-logger-maintenance.timer` | `/home/daniele/.local/share/terminal-logger/bin/terminal-logger` | result=exit-code; main=1/2; inactive_enter=Fri 2026-06-05 05:44:56 CEST |
| `transfer-vecchio-disco-adaptive-throttle.service` | user | dedotta/incerta | attivo | - | `/home/daniele/transfer_vecchio_disco_adaptive_throttle.sh` | result=success; active_enter=Fri 2026-06-05 05:44:19 CEST |
| `windowtabnotes.service` | user | /home/daniele/codex-workspace/WindowTabNotes | attivo | - | `/home/daniele/codex-workspace/WindowTabNotes/system/bin/windowtabnotes` | result=success; active_enter=Fri 2026-06-05 05:43:58 CEST |
| `x11vnc-real-display.service` | user | remote desktop local host (dedotta/incerta) | attivo | - | `/home/daniele/.local/bin/x11vnc-real-display` | result=success; active_enter=Fri 2026-06-05 05:44:19 CEST |

## Path Custom

| Nome | Scope | Progetto associato | Stato | Servizio attivato |
| `mint-xfce-layout-guard.path` | user | dedotta/incerta | attivo | `mint-xfce-layout-guard.service` |

## Servizi esclusi perché appartenenti a software terzi

| Nome | Scope | Stato rilevato | Percorso unit | Motivazione esclusione |
| `aw-watcher-media-player.service` | user | activating | `/home/daniele/.config/systemd/user/aw-watcher-media-player.service` | Servizio del software terzo ActivityWatch; unit user-local ma non creato per un progetto/automazione Codex/personale autonoma. |

## Unit Sospette O Da Verificare

- `user:codex-freeze-runner@.service` - template custom non istanziato; nessuno stato runtime puntuale nello snapshot.
- `user:terminal-logger-maintenance.service` - FAILED: ExecStart usa `/bin/bash` su script Python; journal mostra `import: command not found` e syntax error.
- `system:mint-cloud-backup-kuma-push.service` - stato transitorio `activating/start`.
- `system:mint-cloud-backup.service` - In corso durante scansione; backup restic attivo.

## Comandi Rapidi

sed -n "1,220p" /home/daniele/codex-workspace/MegaVault/human/system/custom-services-status.md
systemctl --user status terminal-logger-maintenance.service --no-pager --lines=30
systemctl --user list-units --all --no-pager --plain
systemctl list-units --all --no-pager --plain

## Fonti Lette

- `systemctl --user list-units --all`
- `systemctl list-units --all`
- `find ~/.config/systemd/user /etc/systemd/system`
- `systemctl show/cat sui candidati custom`
- `journalctl/status read-only su unit sospette`

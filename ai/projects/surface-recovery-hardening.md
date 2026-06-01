# surface-recovery-hardening AI OPERATIONS

PROJECT
- name: surface-recovery-hardening
- slug: surface-recovery-hardening
- purpose: Kit locale per rendere un Surface Pro con Linux Mint piu recuperabile durante trasferimenti USB pesanti:
- current_status: Working tree has 10 non-clean entries; do not mix unrelated changes. First entries: ?? .codexmeta, ?? .codexmeta.bak.20260528_191731, ?? .codexmeta.bak.20260528_191758, ?? .codexmeta.bak.20260528_191912, ?? .codexmeta.bak.20260528_193715
- repo_path: `/home/daniele/codex-workspace/surface-recovery-hardening`
- remote: `git@github.com:gernalix/surface-recovery-hardening.git`
- branch: `main`
- last_verified_commit/date: `0868849` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Python, Shell
- frameworks: UNKNOWN
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: systemd

CODE_MAP
entrypoints:
- `scripts/source_cleanup_analyzer.py`
important_folders:
- `configs`
- `dev`
- `reports`
- `screenshots`
- `scripts`
- `systemd`
important_files:
- `dev/README.md`
tests:
- UNKNOWN
scripts:
- `configs/xrdp_startwm.sh`
- `scripts/bundle_freeze_reboot_monitor_logs.sh`
- `scripts/fix_mint_scaling_theme.sh`
- `scripts/freeze_reboot_monitor.sh`
- `scripts/low_memory_mode.sh`
- `scripts/memory_pressure_guardian.sh`
- `scripts/mint-xfce-layout-guard`
- `scripts/recovery_dump.sh`
- `scripts/recovery_status.sh`
- `scripts/remote_recovery_tmux.sh`
- `scripts/restore_mint_scaling_theme_backup.sh`
- `scripts/rsync_uptime_kuma_push.sh`
- `scripts/screen_watchdog.sh`
- `scripts/show_scaling_theme_status.sh`
- `scripts/source-cleanup-analyzer`
- `scripts/source-cleanup-dashboard`
- `scripts/source_cleanup_analyzer.py`
- `scripts/surface_recovery_rollback.sh`
- `scripts/transfer_usb_io_diag.sh`
- `scripts/transfer_usb_io_watchdog.sh`
- `scripts/transfer_vecchio_disco_adaptive_throttle.sh`
- `scripts/transfer_vecchio_disco_dashboard.sh`
- `scripts/transfer_vecchio_disco_phase2_limited.sh`
- `scripts/transfer_vecchio_disco_recovery_commands.sh`
- `scripts/transfer_vecchio_disco_watchdog.sh`
generated/runtime/avoid_touch_casually:
- `dev/legacy`

ARCH
summary:
- dev/legacy/README.md: Kit locale per rendere un Surface Pro con Linux Mint piu recuperabile durante trasferimenti USB pesanti:
- dev/legacy/docs/ARCHITECTURE.md: Observed prompt #684 topology on 2026-05-14:
- dev/legacy/docs/TROUBLESHOOTING.md: ## DID_ERROR / DRIVER_OK On sdc
- dev/legacy/CHANGELOG.md: - Diagnosi prompt #684: confermato `DID_ERROR/DRIVER_OK` su destinazione `sdc` Seagate 6TB `0bc2:331a`, path USB `2-1.3`, driver `usb-storage`, dietro hub Realtek SuperSpeed `0bda:0411`.
- dev/legacy/docs/OPERATIONS.md: /home/daniele/transfer_vecchio_disco_dashboard.sh --once
- dev/legacy/reports/display_theme_scaling_report_v2.txt: timestamp=2026-05-07T11:07:23+01:00
- dev/legacy/reports/REPORT_v1.md: - GRUB: `i915.enable_psr=0`, `i915.enable_dc=0`, `intel_idle.max_cstate=1`, `usbcore.autosuspend=-1`.
- dev/legacy/reports/REPORT_v2_display_theme_scaling.md: # Report v2 - Display, Tema e Scaling XFCE
- dev/legacy/reports/REPORT_v4_usb_io_hardening.md: # Report Versione 4 - USB/I/O hardening transfer_vecchio_disco
- dev/legacy/reports/REPORT_v5_source_cleanup_analyzer.md: # Report Versione 5 - Source cleanup analyzer prompt #274
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # Surface Recovery Hardening |
| `dev/legacy/README.md` | ## Accesso Remoto |
| `dev/legacy/README.md` | ## Script Principali |
| `dev/legacy/README.md` | ## Architettura Transfer USB/I/O |
| `dev/legacy/README.md` | ## Hardening USB/I/O |
| `dev/legacy/README.md` | ## Diagnostica USB |
| `dev/legacy/README.md` | ## Troubleshooting USB |
| `dev/legacy/README.md` | ## Recovery |
| `dev/legacy/README.md` | ## Rollback |
| `dev/legacy/README.md` | ## Mitigazione Seagate 6TB |
| `dev/legacy/README.md` | ## Source Cleanup Analyzer |
| `dev/legacy/docs/ARCHITECTURE.md` | # Architecture |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Transfer Topology |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Data Flow |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Runtime Components |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Failure Model |
| `dev/legacy/docs/TROUBLESHOOTING.md` | # Troubleshooting |
| `dev/legacy/docs/TROUBLESHOOTING.md` | ## DID_ERROR / DRIVER_OK On sdc |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/README.md` | `FERMO_PAUSATO` e non calcola ETA live. |
| `dev/legacy/README.md` | abort journal, read-only filesystem, errori xHCI/UAS, oppure reset USB ripetuti |
| `dev/legacy/README.md` | nella finestra configurata. Un singolo `reset SuperSpeed USB device` viene |
| `dev/legacy/README.md` | `usb 2-1.3: reset SuperSpeed USB device ... using xhci_hcd`: |
| `dev/legacy/README.md` | - device: destinazione `sdc/sdc1`, Seagate 6TB `0bc2:331a`. |
| `dev/legacy/README.md` | - causa piu probabile: instabilita del link hub/cavo/alimentazione sulla singola porta xHCI sotto carico lungo, non autosuspend. |
| `dev/legacy/README.md` | - stato atteso dopo mitigazione: device ancora montato, filesystem r/w, rsync vivo, nessun `Buffer I/O`, `JBD2 abort`, `device offline` o disconnect. |
| `dev/legacy/README.md` | 1. Non riavviare, non smontare e non fare fsck live. |
| `dev/legacy/README.md` | 5. Se appaiono `read-only filesystem`, `Buffer I/O`, `JBD2 abort`, `device offline` o disconnect, fermare solo dopo decisione esplicita e pianificare recovery offline. |
| `dev/legacy/README.md` | - ridurre carico utente non essenziale; |
| `dev/legacy/README.md` | Il rollback ripristina i backup in `/home/daniele/surface_recovery_backups/...`, rimuove i servizi recovery e rigenera GRUB. |
| `dev/legacy/README.md` | Verificare che il 6TB sia stabile e che non ricompaiano errori `Buffer I/O`, |
| `dev/legacy/README.md` | `JBD2`, `device offline`, `reset SuperSpeed USB device` o disconnect USB. |
| `dev/legacy/docs/ARCHITECTURE.md` | - source disk: Seagate Expansion `0bc2:2322`, internal model `ST4000LM024-2AN17V`, serial `WFF0FEX8`, USB path `2-1.2`, driver `usb-storage`, BitLocker mapper mounted read-only at `/media/daniele/Seagate Expansion Drive`. |
| `dev/legacy/docs/ARCHITECTURE.md` | Safety invariants: |
| `dev/legacy/docs/ARCHITECTURE.md` | - source mount is read-only; |
| `dev/legacy/docs/ARCHITECTURE.md` | - `/home/daniele/transfer_vecchio_disco_phase2_limited.sh`: rsync launcher and UUID safety gate. |
| `dev/legacy/docs/ARCHITECTURE.md` | - `/home/daniele/transfer_vecchio_disco_recovery_commands.sh`: explicit recovery command entrypoint. It prepares resume but never runs it unless called with `resume`. |
| `dev/legacy/docs/ARCHITECTURE.md` | - `/home/daniele/rsync_uptime_kuma_push.sh`: Uptime Kuma push monitor; paused rsync is reported as down with `rsync_paused`. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | usb 2-1.3: reset SuperSpeed USB device number 5 using xhci_hcd |
| `dev/legacy/docs/TROUBLESHOOTING.md` | - less likely: filesystem corruption, because ext4 stayed mounted read-write and no `JBD2 abort`, `EXT4-fs error`, read-only remount or disconnect was observed; |
| `dev/legacy/docs/TROUBLESHOOTING.md` | journalctl -k --since '30 minutes ago' --no-pager / grep -Ei 'JBD2/EXT4-fs.*error/aborting journal/read-only/Buffer I/O/device offline/disconnect/DID_ERROR/I/O error/reset SuperSpeed' |
| `dev/legacy/docs/TROUBLESHOOTING.md` | 4. If only USB reset plus read error is present and mounts remain healthy, do not fsck live. Keep stopped or resume only after operator decision. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Do not send `SIGCONT` while the operator instruction says rsync must stay stopped. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | Do not add quirks for other bridges without fresh `lsusb`, `lsusb -t`, `udevadm info`, and kernel evidence. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | - filesystem remounted read-only; |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
| source | fact |
|---|---|
| `dev/legacy/README.md` | - rsync phase2 protetto da UUID destinazione stabile. |
| `dev/legacy/README.md` | nice -n 19 ionice -c2 -n7 rsync --bwlimit=5120 --timeout=900 --partial --append-verify |
| `dev/legacy/README.md` | Se il PID rsync esiste ma e in stato `T`, la dashboard mostra |
| `dev/legacy/README.md` | rsync validati sul trasferimento, senza smontare dischi e senza resume automatico. |
| `dev/legacy/README.md` | Eseguire senza interrompere rsync: |
| `dev/legacy/README.md` | systemctl status transfer-usb-io-watchdog.service |
| `dev/legacy/README.md` | - stato atteso dopo mitigazione: device ancora montato, filesystem r/w, rsync vivo, nessun `Buffer I/O`, `JBD2 abort`, `device offline` o disconnect. |
| `dev/legacy/README.md` | 2. Verificare rsync e mount con i comandi sopra. |
| `dev/legacy/README.md` | 4. Se il filesystem resta r/w e rsync prosegue, continuare monitorando. |
| `dev/legacy/README.md` | Azioni consentite durante rsync attivo: |
| `dev/legacy/README.md` | Azioni vietate durante rsync attivo: |
| `dev/legacy/README.md` | sudo systemctl disable --now transfer-usb-io-watchdog.service |
| `dev/legacy/README.md` | sudo systemctl daemon-reload |
| `dev/legacy/README.md` | file sicuramente inutili e duplicati video veri prima di un nuovo rsync lungo. |
| `dev/legacy/README.md` | Delete mode, da usare solo dopo aver letto i report e con rsync fermo: |
| `dev/legacy/docs/ARCHITECTURE.md` | The transfer is a single logical rsync pipeline: |
| `dev/legacy/docs/ARCHITECTURE.md` | rsync -aHAX --numeric-ids --partial --append-verify --info=progress2,name --human-readable --bwlimit=5120 --timeout=900 --no-inc-recursive |
| `dev/legacy/docs/ARCHITECTURE.md` | - `/home/daniele/transfer_vecchio_disco_phase2_limited.sh`: rsync launcher and UUID safety gate. |
| `dev/legacy/docs/ARCHITECTURE.md` | - `/home/daniele/transfer_vecchio_disco_adaptive_throttle.sh`: LOW/MEDIUM/HIGH sidecar using `nice`/`ionice`; rsync 3.2.7 cannot change `--bwlimit` live. |
| `dev/legacy/docs/ARCHITECTURE.md` | - `/home/daniele/transfer_usb_io_watchdog.sh`: kernel USB/I/O event detector, Telegram notifier, and automatic `SIGSTOP` pause for validated rsync processes. |
| `dev/legacy/docs/ARCHITECTURE.md` | - `/home/daniele/rsync_uptime_kuma_push.sh`: Uptime Kuma push monitor; paused rsync is reported as down with `rsync_paused`. |
| `dev/legacy/docs/ARCHITECTURE.md` | `DID_ERROR/DRIVER_OK` on `sdc` means the SCSI command failed below the filesystem layer. In this topology it is treated as USB link or bridge instability first, not filesystem corruption by default. The watchdog pauses rsync on |
| `dev/legacy/docs/TROUBLESHOOTING.md` | 1. Keep rsync stopped if requested by the operator. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | journalctl -k --since '30 minutes ago' --no-pager / grep -Ei 'JBD2/EXT4-fs.*error/aborting journal/read-only/Buffer I/O/device offline/disconnect/DID_ERROR/I/O error/reset SuperSpeed' |
test_targets:
- UNKNOWN
known_test_flakiness_or_requirements:
- dev/legacy/README.md: nice -n 19 ionice -c2 -n7 rsync --bwlimit=5120 --timeout=900 --partial --append-verify
- dev/legacy/README.md: Notifica Telegram solo eventi critici reali: disconnect, offline, I/O error,
- dev/legacy/docs/ARCHITECTURE.md: rsync -aHAX --numeric-ids --partial --append-verify --info=progress2,name --human-readable --bwlimit=5120 --timeout=900 --no-inc-recursive
- dev/legacy/docs/TROUBLESHOOTING.md: journalctl -k --since '30 minutes ago' --no-pager / grep -Ei 'JBD2/EXT4-fs.*error/aborting journal/read-only/Buffer I/O/device offline/disconnect/DID_ERROR/I/O error/reset SuperSpeed'
- dev/legacy/docs/TROUBLESHOOTING.md: 4. If only USB reset plus read error is present and mounts remain healthy, do not fsck live. Keep stopped or resume only after operator decision.
- dev/legacy/CHANGELOG.md: - Reso il prossimo avvio rsync piu conservativo: default `BW_LIMIT=5120` KiB/s e `--timeout=900`, mantenendo `--partial --append-verify`.
- dev/legacy/CHANGELOG.md: - Fermato il trasferimento rsync/watchdog/dashboard dopo I/O failure grave sul 6TB ext4, senza rilanciare il trasferimento.
- dev/legacy/docs/OPERATIONS.md: journalctl -k --since '2026-05-14 06:30:00' --no-pager / grep -Ei 'DID_ERROR/DRIVER_OK/usb/uas/xhci/reset/I/O error/Buffer I/O/JBD2/EXT4/sdb/sdc'
- dev/legacy/reports/display_theme_scaling_report_v2.txt: org.gnome.desktop.interface cursor-blink-timeout 10
- dev/legacy/reports/display_theme_scaling_report_v2.txt: org.gnome.desktop.interface gtk-timeout-initial 200

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/docs/ARCHITECTURE.md` | - `/home/daniele/rsync_uptime_kuma_push.sh`: Uptime Kuma push monitor; paused rsync is reported as down with `rsync_paused`. |
| `dev/legacy/CHANGELOG.md` | - Aggiunti script `fix_mint_scaling_theme.sh`, `restore_mint_scaling_theme_backup.sh`, `show_scaling_theme_status.sh` e `mint-xfce-layout-guard`. |
| `dev/legacy/docs/OPERATIONS.md` | XDG_RUNTIME_DIR=/run/user/$(id -u) systemctl --user status transfer-vecchio-disco-adaptive-throttle.service rsync-uptime-kuma-push.service --no-pager |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | ===== os release ===== |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | VERSION="22.3 (Zena)" |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | eDP-1 connected primary 2736x1824+0+0 (0x47) normal (normal left inverted right x axis y axis) 260mm x 173mm |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | /plugins/plugin-6/known-legacy-items <<UNSUPPORTED>> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | /plugins/plugin-8/known-legacy-items <<UNSUPPORTED>> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | org.gnome.desktop.interface gtk-enable-primary-paste true |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | org.cinnamon.desktop.interface gtk-enable-primary-paste true |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | org.cinnamon.desktop.interface gtk-theme-backup 'Adwaita' |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | org.cinnamon.desktop.interface icon-theme-backup 'gnome' |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | <?xml version="1.0" encoding="UTF-8"?> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | <channel name="displays" version="1.0"> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | <property name="Primary" type="bool" value="true"/> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | <channel name="keyboard-layout" version="1.0"> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | <channel name="keyboards" version="1.0"> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | <channel name="thunar" version="1.0"> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | <channel name="xfce4-appfinder" version="1.0"> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | <channel name="xfce4-desktop" version="1.0"> |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/README.md` | Il rollback ripristina i backup in `/home/daniele/surface_recovery_backups/...`, rimuove i servizi recovery e rigenera GRUB. |
| `dev/legacy/CHANGELOG.md` | - Aggiornata dashboard transfer: distingue `FERMO_PAUSATO` da trasferimento attivo, evita ETA live su log stale e non ricalcola `du` pesante quando rsync e fermo salvo override esplicito. |
| `dev/legacy/CHANGELOG.md` | - Aggiunti report JSON/CSV/TXT e safety gate: delete mode richiede `--delete-confirmed` e rifiuta rsync attivo su origine/destinazione. |
| `dev/legacy/CHANGELOG.md` | - Aggiunti script `fix_mint_scaling_theme.sh`, `restore_mint_scaling_theme_backup.sh`, `show_scaling_theme_status.sh` e `mint-xfce-layout-guard`. |
| `dev/legacy/CHANGELOG.md` | - Aggiunta persistenza layout con autostart XFCE e `systemd --user` path watcher `mint-xfce-layout-guard.path`. |
| `dev/legacy/CHANGELOG.md` | - Verificato self-test di regressione: layout sabotato in alto con menu classico e riparato automaticamente dal guard e dal watcher. |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | org.cinnamon.desktop.interface gtk-theme-backup 'Adwaita' |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | org.cinnamon.desktop.interface icon-theme-backup 'gnome' |
| `dev/legacy/docs/ARCHITECTURE.md` | The transfer is a single logical rsync pipeline: |
| `dev/legacy/docs/ARCHITECTURE.md` | `DID_ERROR/DRIVER_OK` on `sdc` means the SCSI command failed below the filesystem layer. In this topology it is treated as USB link or bridge instability first, not filesystem corruption by default. The watchdog pauses rsync on |
| `dev/legacy/docs/TROUBLESHOOTING.md` | If `ps` shows rsync state `T` or dashboard says `FERMO_PAUSATO`, rsync is paused and will not advance. This is different from an uninterruptible I/O hang (`D` state). |
| `dev/legacy/CHANGELOG.md` | - Aggiornato watchdog USB/I/O: deduplica eventi kernel, maschera output Telegram, e mette in pausa con `SIGSTOP` solo i processi rsync validati quando vede eventi critici o reset ripetuti. |
| `dev/legacy/CHANGELOG.md` | - Reso il prossimo avvio rsync piu conservativo: default `BW_LIMIT=5120` KiB/s e `--timeout=900`, mantenendo `--partial --append-verify`. |
| `dev/legacy/CHANGELOG.md` | - Aggiunto analyzer dry-run-first `source_cleanup_analyzer.py` per ridurre il sorgente prima di trasferimenti rsync lunghi. |
| `dev/legacy/CHANGELOG.md` | - Aggiunto tuning persistente `99-transfer-usb-io.conf` per ridurre burst di writeback durante rsync multi-TB. |
| `dev/legacy/CHANGELOG.md` | - Verificato che rsync, mount, tmux dashboard e watchdog restino attivi senza reboot, remount o reset controller. |
| `dev/legacy/CHANGELOG.md` | - Fermato il trasferimento rsync/watchdog/dashboard dopo I/O failure grave sul 6TB ext4, senza rilanciare il trasferimento. |
| `dev/legacy/CHANGELOG.md` | - Aggiornati script rsync per usare UUID ext4 6TB stabile invece di `/dev/sdb1`. |
| `dev/legacy/docs/OPERATIONS.md` | journalctl -k --since '2026-05-14 06:30:00' --no-pager / grep -Ei 'DID_ERROR/DRIVER_OK/usb/uas/xhci/reset/I/O error/Buffer I/O/JBD2/EXT4/sdb/sdc' |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | # This file is not read by bash(1), if ~/.bash_profile or ~/.bash_login |
| `dev/legacy/reports/prompt418_recovery_restart_20260510_224929/pre_start_pgrep_af_rsync_required.txt` | 84085 /bin/bash -c set -euo pipefail logdir=$(cat /tmp/prompt418_logdir) kill -TERM 63966 2>/dev/null // true sleep 1 pgrep -af rsync > "$logdir/pre_start_pgre |
| `dev/legacy/reports/prompt684_did_error_20260514_070407/FINAL_REPORT.md` | Current rsync state: |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `dev/legacy/README.md` | - mitigazione reversibile UAS per il 6TB Seagate `0bc2:331a` dopo I/O failure USB. |
| `dev/legacy/README.md` | nice -n 19 ionice -c2 -n7 rsync --bwlimit=5120 --timeout=900 --partial --append-verify |
| `dev/legacy/README.md` | Notifica Telegram solo eventi critici reali: disconnect, offline, I/O error, |
| `dev/legacy/docs/ARCHITECTURE.md` | rsync -aHAX --numeric-ids --partial --append-verify --info=progress2,name --human-readable --bwlimit=5120 --timeout=900 --no-inc-recursive |
| `dev/legacy/docs/ARCHITECTURE.md` | ## Failure Model |
| `dev/legacy/docs/TROUBLESHOOTING.md` | I/O error, dev sdc, sector 6777997832 op READ |
| `dev/legacy/docs/TROUBLESHOOTING.md` | - less likely: filesystem corruption, because ext4 stayed mounted read-write and no `JBD2 abort`, `EXT4-fs error`, read-only remount or disconnect was observed; |
| `dev/legacy/docs/TROUBLESHOOTING.md` | journalctl -k --since '30 minutes ago' --no-pager / grep -Ei 'JBD2/EXT4-fs.*error/aborting journal/read-only/Buffer I/O/device offline/disconnect/DID_ERROR/I/O error/reset SuperSpeed' |
| `dev/legacy/docs/TROUBLESHOOTING.md` | 4. If only USB reset plus read error is present and mounts remain healthy, do not fsck live. Keep stopped or resume only after operator decision. |
| `dev/legacy/docs/TROUBLESHOOTING.md` | - `EXT4-fs (sdc1): error`; |
| `dev/legacy/CHANGELOG.md` | - Reso il prossimo avvio rsync piu conservativo: default `BW_LIMIT=5120` KiB/s e `--timeout=900`, mantenendo `--partial --append-verify`. |
| `dev/legacy/CHANGELOG.md` | - Fermato il trasferimento rsync/watchdog/dashboard dopo I/O failure grave sul 6TB ext4, senza rilanciare il trasferimento. |
| `dev/legacy/docs/OPERATIONS.md` | journalctl -k --since '2026-05-14 06:30:00' --no-pager / grep -Ei 'DID_ERROR/DRIVER_OK/usb/uas/xhci/reset/I/O error/Buffer I/O/JBD2/EXT4/sdb/sdc' |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | /panels/panel-1/position-locked true |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | /panels/panel-2/position-locked true |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | /plugins/plugin-6/known-items <<UNSUPPORTED>> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | /plugins/plugin-6/known-legacy-items <<UNSUPPORTED>> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | /plugins/plugin-8/known-items <<UNSUPPORTED>> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | /plugins/plugin-8/known-legacy-items <<UNSUPPORTED>> |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | org.gnome.desktop.interface cursor-blink-timeout 10 |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | org.gnome.desktop.interface gtk-timeout-initial 200 |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | org.gnome.desktop.interface gtk-timeout-repeat 20 |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | org.cinnamon.desktop.interface cursor-blink-timeout 10 |
| `dev/legacy/reports/display_theme_scaling_report_v2.txt` | org.cinnamon.desktop.interface gtk-timeout-initial 200 |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/legacy/README.md: Il rollback ripristina i backup in `/home/daniele/surface_recovery_backups/...`, rimuove i servizi recovery e rigenera GRUB.
- dev/legacy/docs/ARCHITECTURE.md: Safety invariants:
- dev/legacy/docs/ARCHITECTURE.md: - `/home/daniele/transfer_vecchio_disco_phase2_limited.sh`: rsync launcher and UUID safety gate.
- dev/legacy/docs/ARCHITECTURE.md: - `/home/daniele/transfer_vecchio_disco_recovery_commands.sh`: explicit recovery command entrypoint. It prepares resume but never runs it unless called with `resume`.
- dev/legacy/docs/TROUBLESHOOTING.md: 4. If only USB reset plus read error is present and mounts remain healthy, do not fsck live. Keep stopped or resume only after operator decision.
- dev/legacy/docs/TROUBLESHOOTING.md: Do not send `SIGCONT` while the operator instruction says rsync must stay stopped.
- dev/legacy/docs/TROUBLESHOOTING.md: Do not add quirks for other bridges without fresh `lsusb`, `lsusb -t`, `udevadm info`, and kernel evidence.
- dev/legacy/docs/TROUBLESHOOTING.md: Offline checks must happen only after safe stop, `sync`, unmount, and with destructive repair disabled unless there is explicit operator approval.
- dev/legacy/CHANGELOG.md: - Aggiunti report JSON/CSV/TXT e safety gate: delete mode richiede `--delete-confirmed` e rifiuta rsync attivo su origine/destinazione.
- dev/legacy/CHANGELOG.md: - Aggiunti script `fix_mint_scaling_theme.sh`, `restore_mint_scaling_theme_backup.sh`, `show_scaling_theme_status.sh` e `mint-xfce-layout-guard`.
- dev/legacy/CHANGELOG.md: - Aggiunta persistenza layout con autostart XFCE e `systemd --user` path watcher `mint-xfce-layout-guard.path`.
- dev/legacy/CHANGELOG.md: - Verificato self-test di regressione: layout sabotato in alto con menu classico e riparato automaticamente dal guard e dal watcher.
- dev/legacy/docs/OPERATIONS.md: For prompt #684 the operator instruction is: rsync must remain stopped. Do not send `SIGCONT` and do not run `resume`.
- dev/legacy/docs/OPERATIONS.md: ## Safe Recovery Sequence
- dev/legacy/docs/OPERATIONS.md: /home/daniele/transfer_vecchio_disco_recovery_commands.sh safe-stop
- dev/legacy/docs/OPERATIONS.md: Resume is explicit and must not be used while the operator wants rsync stopped:

RECENT_DECISIONS
| source | fact |
|---|---|
| `dev/legacy/CHANGELOG.md` | # Changelog |
| `dev/legacy/CHANGELOG.md` | ## Versione 6 - 2026-05-14 |
| `dev/legacy/CHANGELOG.md` | - Diagnosi prompt #684: confermato `DID_ERROR/DRIVER_OK` su destinazione `sdc` Seagate 6TB `0bc2:331a`, path USB `2-1.3`, driver `usb-storage`, dietro hub Realtek SuperSpeed `0bda:0411`. |
| `dev/legacy/CHANGELOG.md` | - Aggiornata dashboard transfer: distingue `FERMO_PAUSATO` da trasferimento attivo, evita ETA live su log stale e non ricalcola `du` pesante quando rsync e fermo salvo override esplicito. |
| `dev/legacy/CHANGELOG.md` | - Aggiornato watchdog USB/I/O: deduplica eventi kernel, maschera output Telegram, e mette in pausa con `SIGSTOP` solo i processi rsync validati quando vede eventi critici o reset ripetuti. |
| `dev/legacy/CHANGELOG.md` | - Reso il prossimo avvio rsync piu conservativo: default `BW_LIMIT=5120` KiB/s e `--timeout=900`, mantenendo `--partial --append-verify`. |
| `dev/legacy/CHANGELOG.md` | - Aggiunto `transfer_vecchio_disco_recovery_commands.sh` per status, pausa, verifica mapping, stop, unmount, power-off e resume esplicito; nessun resume automatico. |
| `dev/legacy/CHANGELOG.md` | - Aggiornato monitor Uptime Kuma per segnalare `rsync_paused` invece di `OK` quando il PID esiste ma e in stato `T`. |
| `dev/legacy/CHANGELOG.md` | - Aggiunta documentazione Codex-friendly in `docs/ARCHITECTURE.md`, `docs/OPERATIONS.md` e `docs/TROUBLESHOOTING.md`. |
| `dev/legacy/CHANGELOG.md` | ## Versione 5 - 2026-05-10 |
| `dev/legacy/CHANGELOG.md` | - Aggiunto analyzer dry-run-first `source_cleanup_analyzer.py` per ridurre il sorgente prima di trasferimenti rsync lunghi. |
| `dev/legacy/CHANGELOG.md` | - Aggiunti wrapper `source-cleanup-analyzer` con `nice`/`ionice` e mini-dashboard `source-cleanup-dashboard`. |
| `dev/legacy/CHANGELOG.md` | - Implementata cache/stato SQLite in `/home/daniele/source_cleanup_state/`, con resume degli hash video gia calcolati. |
| `dev/legacy/CHANGELOG.md` | - Implementate regole conservative: duplicati video solo per stessa dimensione e hash completo SHA-256; estensioni inutili solo `.exe`, `.msi`, `.iso`. |
| `dev/legacy/CHANGELOG.md` | - Aggiunti report JSON/CSV/TXT e safety gate: delete mode richiede `--delete-confirmed` e rifiuta rsync attivo su origine/destinazione. |
| `dev/legacy/CHANGELOG.md` | - Testato su directory temporanea con path spazi/newline, duplicati video reali, file inutili e file non-video >1GB simulato. |
| `dev/legacy/CHANGELOG.md` | ## Versione 4 - 2026-05-10 |
| `dev/legacy/CHANGELOG.md` | - Analizzata la topologia USB live del trasferimento: T7 root, sorgente Seagate `0bc2:2322` e destinazione Seagate 6TB `0bc2:331a` sono sullo stesso root xHCI via hub Realtek SuperSpeed. |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `dev/legacy/reports/prompt684_did_error_20260514_070407/FINAL_REPORT.md` | - `transfer_vecchio_disco_phase2_limited.sh`: next safe start defaults to `BW_LIMIT=5120` and adds `--timeout=900`. |
| `dev/legacy/reports/prompt684_did_error_20260514_070407/user_services_status.txt` | ● transfer-vecchio-disco-adaptive-throttle.service - Adaptive conservative throttle for transfer_vecchio_disco phase 2 |
| `scripts/memory_pressure_guardian.sh` | local row priority rss_mb pid comm cmd total_rss_mb=0 |
| `scripts/memory_pressure_guardian.sh` | while IFS=$'\t' read -r priority rss_mb pid comm cmd; do |
| `scripts/memory_pressure_guardian.sh` | [[ "$lcomm" =~ ^(node/python/python3/npm/pnpm/vite/webpack/next/tsserver)$ // "$lcmd" == *"node "* // "$lcmd" == *"python"* ]] // return 1 |
| `scripts/memory_pressure_guardian.sh` | function print_candidate(priority, rss_mb, pid, comm, cmd) { |
| `scripts/memory_pressure_guardian.sh` | printf "%s\t%s\t%s\t%s\t%s\n", priority, rss_mb, pid, comm, cmd |
| `scripts/memory_pressure_guardian.sh` | if (pid !~ /^[0-9]+$/ // rss !~ /^[0-9]+$/) next |
| `scripts/memory_pressure_guardian.sh` | if (protected_process(pid, lcomm, lcmd)) next |
| `scripts/memory_pressure_guardian.sh` | } else if (rss_mb >= codex_min && lcmd ~ /codex/ && (lcomm ~ /^(node/python/python3/npm/pnpm/vite/webpack/next/tsserver)$/ // lcmd ~ /node /python/)) { |
| `scripts/memory_pressure_guardian.sh` | local row priority rss_mb pid comm cmd count=0 |
| `scripts/memory_pressure_guardian.sh` | local kill_severity="${1:-PRE_EMERGENCY}" max_kills="${2:-$MAX_CRITICAL_GRADLE_KILLS}" row priority rss_mb pid comm cmd killed=0 |
| `scripts/transfer_vecchio_disco_phase2_limited.sh` | next |

LEGACY_SUMMARY
- legacy_docs_read_count: 43
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/README.md`
- `dev/legacy/docs/ARCHITECTURE.md`
- `dev/legacy/docs/TROUBLESHOOTING.md`
- `dev/legacy/CHANGELOG.md`
- `dev/legacy/docs/OPERATIONS.md`
- `dev/legacy/reports/display_theme_scaling_report_v2.txt`
- `dev/legacy/reports/REPORT_v1.md`
- `dev/legacy/reports/REPORT_v2_display_theme_scaling.md`
- `dev/legacy/reports/REPORT_v4_usb_io_hardening.md`
- `dev/legacy/reports/REPORT_v5_source_cleanup_analyzer.md`
- `dev/legacy/reports/xfce_layout_guard_systemd_path_selftest_v2.txt`
- `dev/legacy/reports/prompt418_recovery_restart_20260510_224929/pre_start_pgrep_af_rsync_required.txt`
- `dev/legacy/reports/prompt418_recovery_restart_20260510_224929/source_cryptsetup_status_after_open.txt`
- `dev/legacy/reports/prompt418_recovery_restart_20260510_224929/source_cryptsetup_status_after_open_sudo.txt`
- `dev/legacy/reports/prompt418_recovery_restart_20260510_224929/source_mapper_lsblk_after_open.txt`
- `dev/legacy/reports/prompt684_did_error_20260514_070407/FINAL_REPORT.md`
- `dev/legacy/reports/prompt684_did_error_20260514_070407/user_services_status.txt`
- `dev/legacy/reports/prompt734_post_crash_20260510_222255/dmesg_filtered_usb_io_before_quirk.txt`
- `dev/legacy/reports/prompt734_post_crash_20260510_222255/pre_second_reboot_pgrep.txt`
- `dev/legacy/reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt`
- `configs/xrdp_startwm.sh`
- `scripts/bundle_freeze_reboot_monitor_logs.sh`
- `scripts/fix_mint_scaling_theme.sh`
- `scripts/freeze_reboot_monitor.sh`
- `scripts/low_memory_mode.sh`
- `scripts/memory_pressure_guardian.sh`
- `scripts/recovery_dump.sh`
- `scripts/recovery_status.sh`
- `scripts/remote_recovery_tmux.sh`
- `scripts/restore_mint_scaling_theme_backup.sh`
- `scripts/rsync_uptime_kuma_push.sh`
- `scripts/screen_watchdog.sh`
- `scripts/show_scaling_theme_status.sh`
- `scripts/source_cleanup_analyzer.py`
- `scripts/surface_recovery_rollback.sh`
- `scripts/transfer_usb_io_diag.sh`
- `scripts/transfer_usb_io_watchdog.sh`
- `scripts/transfer_vecchio_disco_adaptive_throttle.sh`
- `scripts/transfer_vecchio_disco_dashboard.sh`
- `scripts/transfer_vecchio_disco_phase2_limited.sh`
- `scripts/transfer_vecchio_disco_recovery_commands.sh`
- `scripts/transfer_vecchio_disco_watchdog.sh`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../surface-recovery-hardening/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/surface-recovery-hardening/overview.md)
- human_folder: [human folder](../../human/projects/surface-recovery-hardening)
- legacy_docs: [dev/legacy](../../../surface-recovery-hardening/dev/legacy)
- repo_path: [repo](../../../surface-recovery-hardening)

OPEN_QUESTIONS
- scripts/fix_mint_scaling_theme.sh: log "error missing default panel XML: $DEFAULT_PANEL"
- scripts/screen_watchdog.sh: notify "rsync-stale" "transfer_vecchio_disco possibile freeze" "Processo rsync rilevato, ma log fermo oltre soglia." 900

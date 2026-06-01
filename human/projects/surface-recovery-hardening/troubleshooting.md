# surface-recovery-hardening Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
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

## Useful Checks Or Commands
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

## Safety Checks Before Fixing
- dev/legacy/README.md: abort journal, read-only filesystem, errori xHCI/UAS, oppure reset USB ripetuti
- dev/legacy/README.md: nella finestra configurata. Un singolo `reset SuperSpeed USB device` viene
- dev/legacy/README.md: `usb 2-1.3: reset SuperSpeed USB device ... using xhci_hcd`:
- dev/legacy/README.md: - device: destinazione `sdc/sdc1`, Seagate 6TB `0bc2:331a`.
- dev/legacy/README.md: - stato atteso dopo mitigazione: device ancora montato, filesystem r/w, rsync vivo, nessun `Buffer I/O`, `JBD2 abort`, `device offline` o disconnect.
- dev/legacy/README.md: 5. Se appaiono `read-only filesystem`, `Buffer I/O`, `JBD2 abort`, `device offline` o disconnect, fermare solo dopo decisione esplicita e pianificare recovery offline.
- dev/legacy/README.md: Il rollback ripristina i backup in `/home/daniele/surface_recovery_backups/...`, rimuove i servizi recovery e rigenera GRUB.
- dev/legacy/README.md: `JBD2`, `device offline`, `reset SuperSpeed USB device` o disconnect USB.
- dev/legacy/docs/ARCHITECTURE.md: - source disk: Seagate Expansion `0bc2:2322`, internal model `ST4000LM024-2AN17V`, serial `WFF0FEX8`, USB path `2-1.2`, driver `usb-storage`, BitLocker mapper mounted read-only at `/media/daniele/Seagate Expansion Drive`.
- dev/legacy/docs/ARCHITECTURE.md: Safety invariants:
- dev/legacy/docs/ARCHITECTURE.md: - source mount is read-only;
- dev/legacy/docs/ARCHITECTURE.md: - `/home/daniele/transfer_vecchio_disco_phase2_limited.sh`: rsync launcher and UUID safety gate.
- dev/legacy/docs/ARCHITECTURE.md: - `/home/daniele/transfer_vecchio_disco_recovery_commands.sh`: explicit recovery command entrypoint. It prepares resume but never runs it unless called with `resume`.
- dev/legacy/docs/ARCHITECTURE.md: - `/home/daniele/rsync_uptime_kuma_push.sh`: Uptime Kuma push monitor; paused rsync is reported as down with `rsync_paused`.

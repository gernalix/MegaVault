# surface-recovery-hardening Changelog

This is a synthesized changelog from legacy docs and migration evidence. It does not invent missing dates.

## Extracted Milestones
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
| `dev/legacy/CHANGELOG.md` | - Confermato che il reset `usb 2-1.3` corrisponde alla destinazione `sdc/sdc1` Seagate 6TB, ora gia vincolata a `usb-storage` tramite quirk UAS persistente. |
| `dev/legacy/CHANGELOG.md` | - Aggiunta regola udev mirata `91-transfer-usb-io-power.rules` per mantenere hub, T7, sorgente e destinazione con `power/control=on`. |
| `dev/legacy/CHANGELOG.md` | - Aggiunto tuning persistente `99-transfer-usb-io.conf` per ridurre burst di writeback durante rsync multi-TB. |
| `dev/legacy/CHANGELOG.md` | - Aggiunti `transfer_usb_io_diag.sh`, `transfer_usb_io_watchdog.sh` e servizio `transfer-usb-io-watchdog.service` con log dedicato `/home/daniele/transfer_usb_io_watchdog.log`. |
| `dev/legacy/CHANGELOG.md` | - Verificato che rsync, mount, tmux dashboard e watchdog restino attivi senza reboot, remount o reset controller. |
| `dev/legacy/CHANGELOG.md` | ## Versione 3 - 2026-05-08 |

## MegaVault Documentation Events
- 2026-06-01: `#739482` moved legacy documentation into `dev/legacy` and created metadata/initial MegaVault docs.
- 2026-06-01T13:20:29+02:00: `#842915` enriched AI and Human docs from legacy docs, repo structure, scripts, tests, and build files.

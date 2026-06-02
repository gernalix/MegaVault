# surface-recovery-hardening Features

## rsync-transfer
- Avvio operativo: `systemd-run --user --unit=rsync-transfer /usr/bin/env BW_LIMIT=5120 RSYNC_IO_TIMEOUT=900 /home/daniele/transfer_vecchio_disco_phase2_limited.sh`
- Modalita: `rsync -aHAX --numeric-ids --partial --append-verify --info=progress2,name --human-readable --bwlimit=5120 --timeout=900 --no-inc-recursive`
- Sorgente: `/media/daniele/Seagate Expansion Drive/`
- Destinazione: `/media/daniele/Seagate6TB2/vecchio disco/`
- Secondo avvio: esce `0` con lock attivo e non crea altri processi rsync.
- Ripresa pausa: dopo mapping OK, ext4 clean e nessun errore storage recente, usare `SIGCONT` sugli stessi PID rsync target.

## Safety
- Source BitLocker aperta read-only con `cryptsetup --type bitlk --readonly`.
- Destinazione accettata solo se UUID ext4 atteso.
- `findmnt -T` non basta se risolve a `/` o mostra righe automount; usare riga reale `/dev/mapper/*` per source e `/dev/sdc1` per dest.
- Monitor USB/I/O mette in pausa solo processi rsync che includono source, dest e `--append-verify`.
- Watchdog: eventi non-storage come `usb 1-5` Marvell WLAN non devono mettere in pausa il transfer.

## Osservabilita
- Stato unit: `systemctl --user status rsync-transfer.service`
- Stato mapping: `/home/daniele/transfer_vecchio_disco_recovery_commands.sh verify-mapping`
- Log transfer: `/home/daniele/transfer_vecchio_disco_phase2.log`
- Warning/errori: `/home/daniele/transfer_vecchio_disco_phase2_warnings_errors.log`
- Watchdog USB/I/O: `/home/daniele/transfer_usb_io_watchdog.log`
- Stato compatto: `/home/daniele/transfer_vecchio_disco_phase2_status.env`
- Health locale Kuma senza push reale: `DRY_RUN=1 RUN_ONCE=1 LOCK_FILE=/tmp/rsync_uptime_kuma_push_check.lock /home/daniele/rsync_uptime_kuma_push.sh`

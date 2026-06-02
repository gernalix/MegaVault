# surface-recovery-hardening Troubleshooting

## Preflight rsync-transfer
- Verificare che non esista gia un rsync target: `pgrep -x rsync` piu controllo cmdline source/dest.
- Verificare source: `findmnt -T "/media/daniele/Seagate Expansion Drive"` deve mostrare `/dev/mapper/source_bitlocker` e opzioni `ro`.
- Verificare dest: `findmnt -T "/media/daniele/Seagate6TB2/vecchio disco"` deve includere `/dev/sdc1`, ext4, UUID `75e5363d-6736-4a7e-84be-5242f4735a27`, rw.
- Verificare kernel recente: nessun `I/O error`, `Buffer I/O`, `JBD2`, `EXT4`, reset/disconnect USB recenti.

## Problemi trovati in #847392
- Source BitLocker non era montata; `findmnt -T "/media/daniele/Seagate Expansion Drive"` risolveva a `/`.
- `verify-mapping` falliva sulla destinazione con automount per output multilinea `systemd-1` + `/dev/sdc1`.
- `unmount_safe` chiudeva solo il vecchio mapper `bitlk-...`, non `source_bitlocker`.
- `rsync-uptime-kuma-push` tornava `down log_stale` mentre rsync era vivo e leggeva dati in fase di scansione/lista.
- `rsync-uptime-kuma-push` usciva con status curl (`7`/`28`) invece di restare vivo e loggare il push fallito.
- 2026-06-03: `transfer-usb-io-watchdog` ha messo in pausa rsync per `usb 1-5` Marvell Bluetooth/WLAN, evento non-storage.

## Fix applicati
- Aperta source con mapper read-only `source_bitlocker`.
- Montata source read-only su `/media/daniele/Seagate Expansion Drive`.
- Fix script `transfer_vecchio_disco_recovery_commands.sh`: seleziona la riga reale di `findmnt`, richiede source mapper e chiude entrambi i nomi mapper noti.
- Backup live creato: `/home/daniele/transfer_vecchio_disco_recovery_commands.sh.bak-20260601-141559`.
- Fix script `rsync_uptime_kuma_push.sh`: se il log e stale ma il pid rsync target consuma CPU e i mount sono safe, lo stato resta `up`.
- Fix script `rsync_uptime_kuma_push.sh`: errori curl sono non fatali e non fanno cadere il servizio.
- Backup live creato: `/home/daniele/rsync_uptime_kuma_push.sh.bak-20260601-142223`.
- Fix script `transfer_usb_io_watchdog.sh`: `usb disconnect` e reset pausano rsync solo con contesto storage del transfer (`sdb`, `sdc`, `dm-0`, `source_bitlocker`, `Seagate`, `uas`, `ext4`, `jbd2`, `usb 2-1.[123]`).
- Fix script `transfer_usb_io_watchdog.sh`: notifica Telegram non fatale sotto `set -e`.
- Backup live creato: `/home/daniele/transfer_usb_io_watchdog.sh.bak-20260603-013451`.
- Ripresa 2026-06-03: `SIGCONT` su PID `3481045 3481050 3504182`; `write_bytes` cresciuto da `273024778240` a `273098440704` in 15s; Kuma `up msg=running pid=3481045`.

## Quando fermarsi
- Non rilanciare automaticamente se il watchdog segnala USB/I/O critico.
- Non usare `rsync --delete`.
- Non smontare o spegnere USB se esiste rsync attivo non pausato.
- Non stampare chiave BitLocker o URL Kuma.

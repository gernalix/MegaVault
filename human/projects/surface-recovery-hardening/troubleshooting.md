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

## Fix applicati
- Aperta source con mapper read-only `source_bitlocker`.
- Montata source read-only su `/media/daniele/Seagate Expansion Drive`.
- Fix script `transfer_vecchio_disco_recovery_commands.sh`: seleziona la riga reale di `findmnt`, richiede source mapper e chiude entrambi i nomi mapper noti.
- Backup live creato: `/home/daniele/transfer_vecchio_disco_recovery_commands.sh.bak-20260601-141559`.
- Fix script `rsync_uptime_kuma_push.sh`: se il log e stale ma il pid rsync target consuma CPU e i mount sono safe, lo stato resta `up`.
- Backup live creato: `/home/daniele/rsync_uptime_kuma_push.sh.bak-20260601-142223`.

## Quando fermarsi
- Non rilanciare automaticamente se il watchdog segnala USB/I/O critico.
- Non usare `rsync --delete`.
- Non smontare o spegnere USB se esiste rsync attivo non pausato.
- Non stampare chiave BitLocker o URL Kuma.

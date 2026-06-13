# External Disk I/O Diagnosis #483920

Diagnosi eseguita il 2026-06-13 senza fermare processi, servizi, mount o backup.

## Causa piu probabile

I dischi erano attivi per il backup locale `/home`, avviato dal timer `home-incremental-backup.timer`.

Il servizio era in esecuzione da `2026-06-13 05:25:53 CEST` e stava copiando verso:

`/media/daniele/Seagate6TB2/home-backups/snapshots/.incomplete-20260613052609-3671550/`

Il comando effettivo era un `rsync` con `--bwlimit=512`, `nice=19` e `ionice=idle`, quindi configurato come basso impatto ma comunque sufficiente a tenere attivo il disco Seagate6TB2.

## Prove principali

- `systemctl --user status home-incremental-backup.service` mostrava il servizio `activating (start)` con `MainPID=3671550`.
- `iotop` mostrava i processi `rsync` del backup con scritture intorno a `460-716 KiB/s` e letture a burst.
- `/proc/*/io` su 10 secondi confermava I/O sui PID `3676819` e `3676881`.
- `lsof` e `fuser` su `/media/daniele/Seagate6TB2` mostravano file aperti nello snapshot incompleto e nel log `rsync-20260613052609.log`.
- Lo stato del backup indicava `status=RUNNING`, `phase=rsync`, `snapshot=20260613052609`, `bwlimit_kb=512`.

## Cosa non sembra essere la causa principale

- Il transfer storico BitLocker -> Seagate6TB2 era ancora presente come unit `transfer-vecchio-disco-adaptive-throttle.service`, ma i suoi `rsync` dati erano in stato fermo/stale e il campione su `/dev/sdb2` / `dm-0` era `0 KiB/s`.
- `gvfs`, `udisks`, `tumblerd` e altri processi desktop erano presenti, ma non risultavano responsabili dell'I/O intensivo osservato.
- `mint-cloud-backup.service`, `restic`, `rclone` e `borg` non risultavano come data mover attivi nel campione.

## Comando rapido

Per vedere in tempo reale chi sta usando i dischi:

```bash
sudo iotop -oP -d 1
```

## Azione sicura consigliata

Nessun fix e stato applicato. La scelta piu sicura e lasciare finire il backup: durante la diagnosi il log `rsync` mostrava avanzamento vicino alla fine e velocita coerente con il limite di `512 KiB/s`.

Se serve fermare subito l'attivita disco, farlo solo consapevolmente con:

```bash
systemctl --user stop home-incremental-backup.service
```

Questo interrompe il backup e lascia uno snapshot incompleto da rivedere nei log/stato prima di considerarlo pulito.


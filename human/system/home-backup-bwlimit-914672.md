# Home Backup Bwlimit Check #914672

Diagnosi eseguita il 2026-06-13 senza fermare backup, processi o timer.

## Esito

Il backup `home-incremental-backup.service` e' ancora attivo. Il processo `rsync` del run corrente usa ancora `--bwlimit=512`, perche' il valore configurato a `1024 KiB/s` vale solo dal prossimo avvio del servizio.

Non ho alzato `HOME_BACKUP_BWLIMIT_KB` oltre `1024`.

## Perche'

Il sistema non era abbastanza tranquillo per passare a `2048-5120 KiB/s`:

- Linux Mint e `/home` sono sul T7 USB (`/dev/sda2` montato su `/`).
- Seagate6TB2 e' `/dev/sdc1` su `/media/daniele/Seagate6TB2`.
- T7, Seagate 4TB e Seagate6TB2 condividono lo stesso hub SABRENT e lo stesso percorso USB del Surface.
- La PSI I/O era ancora alta: circa `avg60=14.20`, con `full avg60=4.75`.
- La CPU PSI era alta: circa `avg60=23.24`.
- La zram era molto usata: circa `2.1-2.4 GiB`.
- Codex stava scrivendo molto sul T7/root, circa `10.6 MiB/s` nel campione `pidstat`.
- Il backup scriveva su Seagate6TB2 circa `510 KiB/s`, coerente con il `--bwlimit=512` del run corrente.

Non sono emersi errori storage USB/ext4/JBD2 recenti nel `dmesg` filtrato, ma il carico e la topologia USB restano il rischio principale.

## Stato configurazione

File config:

```bash
/home/daniele/.config/home-backup/home-backup.env
```

Valore attuale:

```bash
HOME_BACKUP_BWLIMIT_KB="1024"
```

Backup reversibile precedente:

```bash
/home/daniele/.config/home-backup/home-backup.env.bak-20260613-073520
```

## Monitoraggio

Comandi consigliati:

```bash
iostat -xz 1
pidstat -d 1
fuser -vm /media/daniele/Seagate6TB2
```

# Home Backup Baseline #628451

Diagnosi eseguita il 2026-06-13 dopo la fine forzata del run `home-incremental-backup.service`.

## Esito

Il backup non e' piu' attivo: il servizio e' finito in `failed` per timeout systemd alle `12:25:54 CEST`, dopo circa 7 ore. Non risultavano piu' processi `rsync` del backup home.

Lo snapshot non e' stato finalizzato: resta la cartella incompleta:

```bash
/media/daniele/Seagate6TB2/home-backups/snapshots/.incomplete-20260613052609-3671550
```

Dimensione misurata: circa `13G`. Non e' stata cancellata.

## Baseline senza backup

La macchina non era tranquilla nemmeno senza il backup home:

- PSI I/O a meta' misura: `some avg60=91.74`, `full avg60=82.01`.
- PSI memoria a meta' misura: `some avg60=91.51`, `full avg60=83.82`.
- A fine misura la PSI I/O era ancora alta: `some avg60=67.18`, `full avg60=28.75`.
- ZRAM e' arrivata a `4G` usati a meta' misura.
- Swapfile su disco cresciuta fino a circa `578.6M`.
- `/dev/sda` T7/root ha avuto media `44.7 MiB/s` read, `7.3 MiB/s` write, `60.6%` util, con picchi di await oltre `475-519 ms`.
- `/dev/sdc` Seagate6TB2 aveva throughput medio basso, ma picchi di latenza write/flush fino a circa `891/876 ms`.

## Carico residuo

Processi principali nel campione `pidstat`:

- Codex: circa `4.3 MiB/s` read e `3.7 MiB/s` write aggregati, su file `.codex` nel T7/root.
- Script `transfer_vecchio_disco_adaptive_throttle.sh`: read alto nel campione, ma non era il backup home.
- Firefox: profilo/cache su T7/root con read/write regolari.
- Servizi locali Python: `mint-freeze-forensics`, `mint-update-tracker`, `terminal-logger`, `codex-html-live`.
- `mintUpdate`: I/O basso-moderato.

Il collo di bottiglia non e' solo il backup: e' la combinazione di root su T7 USB, hub USB condiviso, RAM/zram sotto pressione e processi utente che scrivono sul filesystem root.

## Decisione bwlimit

Non ho modificato la configurazione. Il valore resta:

```bash
HOME_BACKUP_BWLIMIT_KB="1024"
```

Tabella rischio:

| bwlimit KiB/s | rischio freeze | rischio rallentamenti | giudizio |
| --- | --- | --- | --- |
| 1024 | medio-alto | alto | BORDERLINE |
| 2048 | alto | alto | NOT_RECOMMENDED |
| 3072 | alto | alto | NOT_RECOMMENDED |
| 4096 | molto alto | molto alto | NOT_RECOMMENDED |
| 5120 | molto alto | molto alto | NOT_RECOMMENDED |

Raccomandazione: tenere `1024 KiB/s` come massimo candidato tra quelli richiesti, ma non considerarlo "safe" in assoluto con questa baseline. Non ci sono dati per salire a `2048-5120 KiB/s`.

## Monitoraggio

Comando pratico:

```bash
iostat -xz 1; pidstat -d 1; vmstat 1; cat /proc/pressure/io
```

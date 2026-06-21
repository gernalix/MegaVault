# Storage Topology

Topologia storage leggibile derivata da [STORAGE_TOPOLOGY AI](../../ai/global/STORAGE_TOPOLOGY.md). La fonte operativa e' il file AI; questo documento non va usato come sorgente per Codex.

## Host corrente Windows

Il ThinkPad P14s Gen 5 AMD e' l'host principale corrente. Il dato verificato dal prompt e' SSD interno da 1 TB. Restano `UNKNOWN` lettera del drive di sistema, layout volumi, stato BitLocker, path workspace GitHub, path backup Windows, dischi esterni correnti e topologia USB corrente.

Non applicare la topologia del Surface al ThinkPad senza verifica live.

## Dischi legacy Surface

- Root Linux: `/dev/sda2` su Samsung PSSD T7 Shield USB, seriale `S6YGNS0Y903440H`.
- EFI: `/dev/sda1`.
- Disco interno NVMe: `/dev/nvme0n1`, Toshiba `KBG30ZPZ256G`, usato per partizioni Windows/BitLocker, non root Linux.
- Sorgente storica transfer: `/dev/sdb2`, Seagate 4 TB BitLocker.
- Destinazione backup/transfer: `/dev/sdc1`, Seagate 6 TB ext4, mount `/media/daniele/Seagate6TB2`.

## Hub USB legacy

Root, sorgente storica e destinazione backup passano dal SABRENT HB-BUP7 alimentato. Questo rende il singolo hub un punto critico per freeze, backup e transfer I/O.

Vista sintetica:

- Surface: host locale, root su T7 USB.
- T7 root: critico, qualsiasi stall USB puo' impattare tutto il sistema.
- 4TB BitLocker source: sorgente storica transfer, da trattare read-only.
- 6TB backup destination: destinazione backup e transfer, critica.
- SABRENT hub: punto condiviso e critico per root, sorgente e destinazione.

## Percorsi critici legacy

- Backup home: `/media/daniele/Seagate6TB2/home-backups`.
- Transfer vecchio disco: `/media/daniele/Seagate6TB2/vecchio disco`.
- Stato backup cloud: `/var/lib/mint-cloud-backup`.
- Stato freeze forensics: `~/.local/state/mint-freeze-forensics`.

## Vincoli

Per il Surface legacy, non assumere indipendenza tra root, sorgente e destinazione quando ci sono workload USB pesanti. Non usare `rsync --delete` sul transfer e non riprendere automaticamente dopo errori storage. Per il ThinkPad, verificare prima drive, mount e backup path reali.

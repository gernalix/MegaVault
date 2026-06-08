# Storage Topology

Topologia storage del Surface verificata con `lsblk` e `HOST_PROFILE`. Il file AI autorevole e' [STORAGE_TOPOLOGY.md](../../ai/global/STORAGE_TOPOLOGY.md).

## Dischi

- Root Linux: `/dev/sda2` su Samsung PSSD T7 Shield USB, seriale `S6YGNS0Y903440H`.
- EFI: `/dev/sda1`.
- Disco interno NVMe: `/dev/nvme0n1`, Toshiba `KBG30ZPZ256G`, usato per partizioni Windows/BitLocker, non root Linux.
- Sorgente storica transfer: `/dev/sdb2`, Seagate 4 TB BitLocker.
- Destinazione backup/transfer: `/dev/sdc1`, Seagate 6 TB ext4, mount `/media/daniele/Seagate6TB2`.

## Hub USB

Root, sorgente storica e destinazione backup passano dal SABRENT HB-BUP7 alimentato. Questo rende il singolo hub un punto critico per freeze, backup e transfer I/O.

## Percorsi critici

- Backup home: `/media/daniele/Seagate6TB2/home-backups`.
- Transfer vecchio disco: `/media/daniele/Seagate6TB2/vecchio disco`.
- Stato backup cloud: `/var/lib/mint-cloud-backup`.
- Stato freeze forensics: `~/.local/state/mint-freeze-forensics`.

## Vincoli

Non assumere indipendenza tra root, sorgente e destinazione quando ci sono workload USB pesanti. Non usare `rsync --delete` sul transfer e non riprendere automaticamente dopo errori storage.

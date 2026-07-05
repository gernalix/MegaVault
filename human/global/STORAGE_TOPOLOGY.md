# Topologia storage globale

Aggiornato: 2026-07-05. Autorita' operativa: [STORAGE_TOPOLOGY AI](../../ai/global/STORAGE_TOPOLOGY.md).

## Stato Windows corrente

- Host: `DANIELE_PC`, Lenovo ThinkPad P14s Gen 5 AMD.
- Root/documenti: `C:\Users\seste\Documents`.
- Repo corrente: `C:\Users\seste\Documents\megavault_content_aware_merge_20260705`.
- `C:` NTFS, disco Kioxia NVMe, sistema Windows.
- `D:` Seagate Expansion Drive USB NTFS, poco spazio libero al controllo.
- `E:` NTFS, ruolo non verificato.
- T7: non connesso nel controllo; verificare mount/lettera prima di usarlo.

## Regole

- Non usare path Linux `/home`, `/mnt`, `/media` come path host corrente.
- Non assumere che una lettera disco Veeam/T7 sia stabile.
- Non cancellare, formattare, fare prune o unlock senza intenzione esplicita e prova del target.

## Storico

La topologia Surface/Linux Mint con root ext4 su Samsung T7 e backup `/media/daniele/Seagate6TB2` resta storica o project-specific.

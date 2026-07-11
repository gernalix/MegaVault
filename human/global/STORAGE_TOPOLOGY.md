# Topologia storage globale

Aggiornato: 2026-07-12. Autorita' operativa: [STORAGE_TOPOLOGY AI](../../ai/global/STORAGE_TOPOLOGY.md).

## Stato Fedora corrente

- Host `fedora`, Lenovo ThinkPad P14s Gen 5 AMD.
- Root e `/home`: Btrfs cifrato LUKS su Kioxia NVMe da circa 951 GiB; circa 844 GiB disponibili al controllo.
- Home corrente: `/home/daniele`; repo: `/home/daniele/MegaVault`.
- Seagate 3.5 TiB: `/run/media/daniele/Seagate Expansion Drive`; volume NTFS 155.9 GiB: `/run/media/daniele/09FA16D309FA16D3`.
- Samsung chiamato `T7`: `/mnt/T7_BACKUP`, ext4 `T7_BACKUP`, circa 761 GiB liberi; il vfat recovery con label `VEEAMRE` e' distinto e scollegato.
- Repository Restic cifrato: `/mnt/T7_BACKUP/restic-fedora`; backup giornaliero, check settimanale 5%, check completo/prune mensile, retention 7 giornalieri/5 settimanali/12 mensili/3 annuali.
- Fedora System Monitor conserva il database sotto `/var/lib/fedora-system-monitor` e backup online nella sottodirectory `backups`; identifica i rimovibili con UUID o hash seriale stabile, mai con `/dev/sdX`.
- Il 9 luglio 2026 un volume NTFS esterno e' scomparso durante I/O e si e' rimontato circa dieci secondi dopo. La causa e' ancora aperta; vedere il registro incidenti globale.

## Regole

- Verificare `findmnt`, `lsblk` e `df` prima di backup, cleanup o I/O pesante.
- I mount rimovibili e i nomi device possono cambiare.
- Non cancellare, formattare, fare prune o unlock senza intenzione esplicita e prova del target.

Backup reale, check completo, restore e comportamento fail-closed sono PASS nell'attivita' 583921. Resta da salvare manualmente la password nel password manager.

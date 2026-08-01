# Topologia storage globale

Aggiornato: 2026-07-26. Autorita' operativa: [STORAGE_TOPOLOGY AI](../../ai/global/STORAGE_TOPOLOGY.md).

## Stato Fedora corrente

- Host `fedora`, Lenovo ThinkPad P14s Gen 5 AMD.
- Root e `/home`: Btrfs cifrato LUKS su Kioxia NVMe da circa 951 GiB; root e home sono subvolumi separati e `nodiscard` è esplicito.
- Snapper protegge soltanto root con snapshot periodici e pre-transazione DNF5, retention e cleanup. Lo scrub read-only è mensile; il collaudo su 41,18 GiB e i device stats sono senza errori.
- Home corrente: `/home/daniele`; repo: `/home/daniele/MegaVault`.
- Seagate 3.5 TiB: `/run/media/daniele/Seagate Expansion Drive`; volume NTFS 155.9 GiB: `/run/media/daniele/09FA16D309FA16D3`.
- Samsung chiamato `T7`: normalmente scollegato oppure presente USB ma smontato;
  durante il job usa `/mnt/T7_BACKUP`, ext4 `T7_BACKUP`, circa 761 GiB liberi.
  Il vfat recovery con label `VEEAMRE` e' distinto e scollegato.
- Repository Restic cifrato: `/mnt/T7_BACKUP/restic-fedora`; backup a ogni
  collegamento, check leggero/prune al massimo settimanali, check completo al
  massimo mensile, retention 7 giornalieri/5 settimanali/12 mensili/3 annuali.
- Fedora System Monitor conserva il database sotto `/var/lib/fedora-system-monitor` e backup online nella sottodirectory `backups`; identifica i rimovibili con UUID o hash seriale stabile, mai con `/dev/sdX`. Ogni cinque minuti confronta lo spazio libero dei filesystem reali con l'ultima baseline Telegram consegnata; i delta inferiori a 1 GiB si accumulano e gli smontaggi non cancellano lo stato.
- Prometheus conserva la TSDB in `/var/lib/prometheus/metrics2` fino al primo limite tra 30 giorni e 5 GB. La crescita misurata iniziale e' circa 96,9 KiB/minuto, proiezione grezza circa 4,2 GiB/30 giorni. I volumi esterni reali sotto `/run/media` sono inclusi tramite ACL di solo attraversamento per l'exporter; filesystem virtuali e temporanei sono filtrati.
- Il 9 luglio 2026 un volume NTFS esterno e' scomparso durante I/O e si e' rimontato circa dieci secondi dopo. La causa e' ancora aperta; vedere il registro incidenti globale.

## Regole

- Verificare `findmnt`, `lsblk` e `df` prima di backup, cleanup o I/O pesante.
- I mount rimovibili e i nomi device possono cambiare.
- Non cancellare, formattare, fare prune o unlock senza intenzione esplicita e prova del target.

Backup reale, trigger udev, job singolo, check leggero/prune, smontaggio,
notifiche e comportamento fail-closed sono verificati nell'attivita' 684219;
check completo e restore restano verificati dall'attivita' 583921. Resta da
salvare manualmente la password nel password manager.

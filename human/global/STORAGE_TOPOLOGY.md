# Topologia storage globale

Aggiornato: 2026-07-09. Autorita' operativa: [STORAGE_TOPOLOGY AI](../../ai/global/STORAGE_TOPOLOGY.md).

## Stato Fedora corrente

- Host `fedora`, Lenovo ThinkPad P14s Gen 5 AMD.
- Root e `/home`: Btrfs cifrato LUKS su Kioxia NVMe da circa 951 GiB; circa 936 GiB disponibili al controllo.
- Home corrente: `/home/daniele`; repo: `/home/daniele/MegaVault`.
- Seagate 3.5 TiB: `/run/media/daniele/Seagate Expansion Drive`; volume NTFS 155.9 GiB: `/run/media/daniele/09FA16D309FA16D3`.
- Samsung T7: `/run/media/daniele/Ventoy`; supporto recovery: `/run/media/daniele/VEEAMRE`.

## Regole

- Verificare `findmnt`, `lsblk` e `df` prima di backup, cleanup o I/O pesante.
- I mount rimovibili e i nomi device possono cambiare.
- Non cancellare, formattare, fare prune o unlock senza intenzione esplicita e prova del target.

Policy, repository e retention backup Fedora restano da verificare.

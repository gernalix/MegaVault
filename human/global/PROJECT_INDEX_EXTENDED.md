# Project Index Extended

Aggiornato: 2026-07-12. Autorita' operativa: [PROJECT_INDEX_EXTENDED AI](../../ai/global/PROJECT_INDEX_EXTENDED.md).

## Relazione verificata su Fedora

MegaVault risiede in `/home/daniele/MegaVault`; usa `codex_global_timeline.sqlite` come DB canonico e `build_codex_global_timeline.py` come builder. Non ha servizi o timer host registrati.

Fedora System Monitor risiede in `/home/daniele/MegaVault/projects/fedora-system-monitor`. Il runtime è installato in `/usr/local/libexec/fedora-system-monitor`, usa configurazione sotto `/etc/fedora-system-monitor`, dati sotto `/var/lib/fedora-system-monitor`, un daemon eventi, unita' lifecycle/collector, quattro timer e una path unit. Installazione e prove live sono state verificate nell'attivita' 593184.

Fedora T7 Backup risiede in `/home/daniele/MegaVault/projects/fedora-t7-backup`;
runtime lifecycle `/usr/local/libexec/t7-restic-lifecycle`, repository cifrato
`/mnt/T7_BACKUP/restic-fedora`, trigger udev, service backup e reminder one-shot.
Trigger, singola istanza, backup, manutenzione, smontaggio, notifiche e
fail-closed sono verificati nell'attivita' 684219; HEAD progetto
`1495f135a81e9457e1efcb12a5db6689983b3c79`.

## Stato migrazione

Servizi, timer, database, dashboard, monitor e alert degli altri progetti indicizzati non sono ancora stati riverificati sul Fedora corrente. Le relazioni vanno ricostruite in modo incrementale quando ciascun progetto viene migrato o toccato, usando evidenza live e i metadata locali.

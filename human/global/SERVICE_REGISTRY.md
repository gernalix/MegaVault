# Service Registry

Aggiornato: 2026-07-26. Autorita' operativa: [SERVICE_REGISTRY AI](../../ai/global/SERVICE_REGISTRY.md).

## Fedora corrente

Il system manager e lo user manager systemd risultano `running`. Tra i servizi rilevanti verificati sono attivi NetworkManager, firewalld, DNF daemon, fwupd, smartd, systemd-oomd, udisks2 e GDM; nella sessione utente sono attivi GNOME, Flatpak portal, PipeWire, WirePlumber e XDG portal.

Timer di sistema rilevanti: `dnf-makecache`, `fstrim`, `logrotate`, `systemd-tmpfiles-clean`, `snapper-timeline`, `snapper-cleanup`, `btrfs-scrub` e `fwupd-refresh`; `raid-check` resta disabilitato perché non esistono array MD.

Fedora System Monitor 1.3.1 è verificato e attivo: conserva la pressione memoria composta introdotta dalla 1.2.0, aggiunge SMART corretto e mantiene daemon, lifecycle, collector, quattro timer, path software e template udev. Il collector filesystem usa `telegram_notify.py` per delta cumulativi di almeno 1 GiB; exporter read-only su `127.0.0.1:9109`. I 110 test e 18 self-check passano.

Prometheus 3.13.0 (`prometheus.service`) e Node Exporter 1.11.1 (`prometheus-node-exporter.service`) sono abilitati e attivi, con restart su errore e listener esclusivamente `127.0.0.1:9090` e `127.0.0.1:9100`. Prometheus conserva al massimo 30 giorni o 5 GB. `fedora-diagnostics` 1.2.0 resta un comando manuale; un timer di supporto ogni 30 secondi esegue un oneshot senza rete che aggiorna atomicamente metriche fan/power/processi nel textfile di Node Exporter. L'unita' separata `fedora-secureboot-forensics-capture.service` e' abilitata ma inattiva: al primo boot riuscito crea un solo archivio forense root-only se la directory non ne contiene gia' uno; non e' un timer o monitor periodico.

Fedora T7 Backup e' installato e testato: il collegamento del seriale T7 corretto
attiva via udev `t7-restic-backup.service`, che monta, verifica, esegue backup e
manutenzioni dovute, sincronizza, smonta e notifica. I vecchi timer periodici
sono rimossi; `t7-restic-reminder.timer` e' un one-shot a 30 minuti dopo un
successo. Il doppio evento e' bloccato da lock in `/run`; log in journal.

Il servizio utente `adb-device-keeper.service` e' abilitato e attivo per mantenere disponibili via ADB Wi-Fi il Pixel 8a e il TCL 6102H. Il linger di `daniele` e' attivo per eseguirlo anche senza sessione grafica. Dettagli e comandi: [ADB Device Keeper](ADB_DEVICE_KEEPER.md).

`autokey.service` e' stato rimosso nell'attivita' `582941` insieme ai pacchetti AutoKey, al launcher, al wrapper e all'estensione GNOME. Non riabilitare AutoKey salvo rollback esplicito.

`espanso.service` e' l'autostart per l'espansione testo: unita' utente legata a `graphical-session.target` con `PartOf=graphical-session.target`, restart `on-failure` e nessun autostart XDG duplicato. Questa configurazione evita il worker parziale avviato prima del compositor.

`rustdesk.service` e' l'unico meccanismo di avvio RustDesk: servizio di sistema abilitato e attivo, con server e tray utente quando la sessione grafica esiste. Non aggiungere autostart XDG o unita' utente duplicate. Su Wayland il servizio persiste dopo logout/boot, ma la schermata GDM pre-login non e' controllabile; l'accesso torna utilizzabile soltanto dopo un login grafico compatibile. L'`ExecStop` ufficiale usa un match `pkill` ampio: eseguire restart/stop in un comando separato da altri comandi RustDesk con opzioni.

## Stato progetti

Fedora System Monitor e Fedora T7 Backup sono servizi di progetto MegaVault verificati sul Fedora corrente. Per gli altri progetti usare `systemctl` o `systemctl --user` e verificare unit, stato, enablement e path `ExecStart` prima di documentarli come attivi.

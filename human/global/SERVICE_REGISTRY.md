# Service Registry

Aggiornato: 2026-07-26. Autorita' operativa: [SERVICE_REGISTRY AI](../../ai/global/SERVICE_REGISTRY.md).

## Fedora corrente

Il system manager e lo user manager systemd risultano `running`. Tra i servizi rilevanti verificati sono attivi NetworkManager, firewalld, DNF daemon, fwupd, smartd, systemd-oomd, udisks2 e GDM; nella sessione utente sono attivi GNOME, Flatpak portal, PipeWire, WirePlumber e XDG portal.

Timer di sistema rilevanti: `dnf-makecache`, `fstrim`, `logrotate` e `systemd-tmpfiles-clean`.

Fedora System Monitor 1.3.0 è verificato e attivo: daemon journal, lifecycle, collector, quattro timer, path software e template udev sono operativi. Le esecuzioni più recenti di `minute`, `five_minute`, `fifteen_minute`, `hourly`, `daily`, `weekly` e `software_event` sono tutte `ok`; una prova prima/dopo ha confermato una nuova scrittura nel DB SQLite canonico. Il collector filesystem esistente controlla ogni cinque minuti i filesystem reali e usa `telegram_notify.py` per variazioni cumulative di almeno 1 GiB, senza nuovi servizi o timer. Dashboard, timeline, trend e storico servizi leggono il DB esistente. Il suo exporter read-only su `127.0.0.1:9109` e' ora avviato come dipendenza di Prometheus, senza modificare collector o Kuma. I 107 test e 18 self-check passano; soltanto il collector giornaliero conserva `CAP_SYS_ADMIN` per NVMe.

Prometheus 3.13.0 (`prometheus.service`) e Node Exporter 1.11.1 (`prometheus-node-exporter.service`) sono abilitati e attivi, con restart su errore e listener esclusivamente `127.0.0.1:9090` e `127.0.0.1:9100`. Prometheus conserva al massimo 30 giorni o 5 GB. `fedora-diagnostics` e' un comando manuale, senza servizio o timer periodico.

Fedora T7 Backup e' installato e testato: il collegamento del seriale T7 corretto
attiva via udev `t7-restic-backup.service`, che monta, verifica, esegue backup e
manutenzioni dovute, sincronizza, smonta e notifica. I vecchi timer periodici
sono rimossi; `t7-restic-reminder.timer` e' un one-shot a 30 minuti dopo un
successo. Il doppio evento e' bloccato da lock in `/run`; log in journal.

Il servizio utente `adb-device-keeper.service` e' abilitato e attivo per mantenere disponibili via ADB Wi-Fi il Pixel 8a e il TCL 6102H. Il linger di `daniele` e' attivo per eseguirlo anche senza sessione grafica. Dettagli e comandi: [ADB Device Keeper](ADB_DEVICE_KEEPER.md).

`autokey.service` e' l'unico autostart AutoKey: unita' utente abilitata su `graphical-session.target`, con restart solo su errore e wrapper `~/.local/libexec/autokey-wayland-fedora44`. Non creare anche un autostart XDG e non avviare direttamente `/usr/bin/autokey-gtk`. Nella sessione corrente resta intenzionalmente inattivo: il gruppo `input` e l'estensione GNOME appena installata saranno acquisiti al prossimo login; il collaudo post-login dell'attivita' `638417` e' ancora pendente.

`rustdesk.service` e' l'unico meccanismo di avvio RustDesk: servizio di sistema abilitato e attivo, con server e tray utente quando la sessione grafica esiste. Non aggiungere autostart XDG o unita' utente duplicate. Su Wayland il servizio persiste dopo logout/boot, ma la schermata GDM pre-login non e' controllabile; l'accesso torna utilizzabile soltanto dopo un login grafico compatibile. L'`ExecStop` ufficiale usa un match `pkill` ampio: eseguire restart/stop in un comando separato da altri comandi RustDesk con opzioni.

## Stato progetti

Fedora System Monitor e Fedora T7 Backup sono servizi di progetto MegaVault verificati sul Fedora corrente. Per gli altri progetti usare `systemctl` o `systemctl --user` e verificare unit, stato, enablement e path `ExecStart` prima di documentarli come attivi.

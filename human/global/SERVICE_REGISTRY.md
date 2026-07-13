# Service Registry

Aggiornato: 2026-07-13. Autorita' operativa: [SERVICE_REGISTRY AI](../../ai/global/SERVICE_REGISTRY.md).

## Fedora corrente

Il system manager e lo user manager systemd risultano `running`. Tra i servizi rilevanti verificati sono attivi NetworkManager, firewalld, DNF daemon, fwupd, smartd, systemd-oomd, udisks2 e GDM; nella sessione utente sono attivi GNOME, Flatpak portal, PipeWire, WirePlumber e XDG portal.

Timer di sistema rilevanti: `dnf-makecache`, `fstrim`, `logrotate` e `systemd-tmpfiles-clean`.

Fedora System Monitor 1.1.0 è verificato e attivo: daemon journal, lifecycle, collector, quattro timer, path software e template udev sono operativi. Dashboard, timeline, trend e storico servizi leggono il DB esistente. L’unità Prometheus locale è installata, verificata e disabilitata per default. I 92 test e 17 self-check passano; soltanto il collector giornaliero conserva `CAP_SYS_ADMIN` per NVMe.

Fedora T7 Backup e' installato e testato: il collegamento del seriale T7 corretto
attiva via udev `t7-restic-backup.service`, che monta, verifica, esegue backup e
manutenzioni dovute, sincronizza, smonta e notifica. I vecchi timer periodici
sono rimossi; `t7-restic-reminder.timer` e' un one-shot a 30 minuti dopo un
successo. Il doppio evento e' bloccato da lock in `/run`; log in journal.

Il servizio utente `adb-device-keeper.service` e' abilitato e attivo per mantenere disponibili via ADB Wi-Fi il Pixel 8a e il TCL 6102H. Il linger di `daniele` e' attivo per eseguirlo anche senza sessione grafica. Dettagli e comandi: [ADB Device Keeper](ADB_DEVICE_KEEPER.md).

`rustdesk.service` e' l'unico meccanismo di avvio RustDesk: servizio di sistema abilitato e attivo, con server e tray utente quando la sessione grafica esiste. Non aggiungere autostart XDG o unita' utente duplicate. Su Wayland il servizio persiste dopo logout/boot, ma la schermata GDM pre-login non e' controllabile; l'accesso torna utilizzabile soltanto dopo un login grafico compatibile. L'`ExecStop` ufficiale usa un match `pkill` ampio: eseguire restart/stop in un comando separato da altri comandi RustDesk con opzioni.

## Stato progetti

Fedora System Monitor e Fedora T7 Backup sono servizi di progetto MegaVault verificati sul Fedora corrente. Per gli altri progetti usare `systemctl` o `systemctl --user` e verificare unit, stato, enablement e path `ExecStart` prima di documentarli come attivi.

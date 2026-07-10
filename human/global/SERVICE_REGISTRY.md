# Service Registry

Aggiornato: 2026-07-10. Autorita' operativa: [SERVICE_REGISTRY AI](../../ai/global/SERVICE_REGISTRY.md).

## Fedora corrente

Il system manager e lo user manager systemd risultano `running`. Tra i servizi rilevanti verificati sono attivi NetworkManager, firewalld, DNF daemon, fwupd, smartd, systemd-oomd, udisks2 e GDM; nella sessione utente sono attivi GNOME, Flatpak portal, PipeWire, WirePlumber e XDG portal.

Timer di sistema rilevanti: `dnf-makecache`, `fstrim`, `logrotate` e `systemd-tmpfiles-clean`.

Fedora System Monitor è verificato e attivo: `fedora-system-monitor-events.service` segue il journal, `fedora-system-monitor-lifecycle.service` registra boot e shutdown, mentre il template collector è attivato dai timer ogni minuto, ogni ora, ogni giorno e ogni settimana. La path unit software e i template udev sono attivi. Tutte le unità passano `systemd-analyze verify`.

Il servizio utente `adb-device-keeper.service` e' abilitato e attivo per mantenere disponibili via ADB Wi-Fi il Pixel 8a e il TCL 6102H. Il linger di `daniele` e' attivo per eseguirlo anche senza sessione grafica. Dettagli e comandi: [ADB Device Keeper](ADB_DEVICE_KEEPER.md).

`rustdesk.service` e' l'unico meccanismo di avvio RustDesk: servizio di sistema abilitato e attivo, con server e tray utente quando la sessione grafica esiste. Non aggiungere autostart XDG o unita' utente duplicate. Su Wayland il servizio persiste dopo logout/boot, ma la schermata GDM pre-login non e' controllabile; l'accesso torna utilizzabile soltanto dopo un login grafico compatibile. L'`ExecStop` ufficiale usa un match `pkill` ampio: eseguire restart/stop in un comando separato da altri comandi RustDesk con opzioni.

## Stato progetti

Fedora System Monitor e' il primo servizio di progetto MegaVault verificato sul Fedora corrente. Per gli altri progetti usare `systemctl` o `systemctl --user` e verificare unit, stato, enablement e path `ExecStart` prima di documentarli come attivi.

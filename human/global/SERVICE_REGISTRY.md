# Service Registry

Aggiornato: 2026-07-10. Autorita' operativa: [SERVICE_REGISTRY AI](../../ai/global/SERVICE_REGISTRY.md).

## Fedora corrente

Il system manager e lo user manager systemd risultano `running`. Tra i servizi rilevanti verificati sono attivi NetworkManager, firewalld, DNF daemon, fwupd, smartd, systemd-oomd, udisks2 e GDM; nella sessione utente sono attivi GNOME, Flatpak portal, PipeWire, WirePlumber e XDG portal.

Timer di sistema rilevanti: `dnf-makecache`, `fstrim`, `logrotate` e `systemd-tmpfiles-clean`.

Il servizio utente `adb-device-keeper.service` e' abilitato e attivo per mantenere disponibili via ADB Wi-Fi il Pixel 8a e il TCL 6102H. Il linger di `daniele` e' attivo per eseguirlo anche senza sessione grafica. Dettagli e comandi: [ADB Device Keeper](ADB_DEVICE_KEEPER.md).

`rustdesk.service` e' l'unico meccanismo di avvio RustDesk: servizio di sistema abilitato e attivo, con server e tray utente quando la sessione grafica esiste. Non aggiungere autostart XDG o unita' utente duplicate. Su Wayland il servizio persiste dopo logout/boot, ma la schermata GDM pre-login non e' controllabile; l'accesso torna utilizzabile soltanto dopo un login grafico compatibile. L'`ExecStop` ufficiale usa un match `pkill` ampio: eseguire restart/stop in un comando separato da altri comandi RustDesk con opzioni.

## Stato progetti

Nessun servizio o timer specifico di progetto MegaVault e' stato verificato come migrato sul Fedora corrente. Prima di documentarlo come attivo usare `systemctl` o `systemctl --user` e verificare unit, stato, enablement e path `ExecStart`.

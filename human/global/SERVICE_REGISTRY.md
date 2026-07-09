# Service Registry

Aggiornato: 2026-07-09. Autorita' operativa: [SERVICE_REGISTRY AI](../../ai/global/SERVICE_REGISTRY.md).

## Fedora corrente

Il system manager e lo user manager systemd risultano `running`. Tra i servizi rilevanti verificati sono attivi NetworkManager, firewalld, DNF daemon, fwupd, smartd, systemd-oomd, udisks2 e GDM; nella sessione utente sono attivi GNOME, Flatpak portal, PipeWire, WirePlumber e XDG portal.

Timer di sistema rilevanti: `dnf-makecache`, `fstrim`, `logrotate` e `systemd-tmpfiles-clean`.

## Stato progetti

Nessun servizio o timer specifico di progetto MegaVault e' stato verificato come migrato sul Fedora corrente. Prima di documentarlo come attivo usare `systemctl` o `systemctl --user` e verificare unit, stato, enablement e path `ExecStart`.

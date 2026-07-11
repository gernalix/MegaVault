# Inventario software globale

Aggiornato: 2026-07-12. Autorita' operativa: [SOFTWARE_INVENTORY AI](../../ai/global/SOFTWARE_INVENTORY.md).

## Tool Fedora verificati

- Bash 5.3.9, DNF 5.4.2.1, systemd 259 e Git 2.55.0 dai path di sistema.
- GitHub CLI 2.94.0 in `/usr/bin/gh`; Codex CLI 0.144.1 si avvia direttamente da `/usr/local/bin/codex` nel PTY nativo di Ptyxis, senza wrapper o cattura automatica.
- Python 3.14.6, pip 26.0.1, pipx 1.15.0 e uv 0.11.26.
- OpenJDK 25.0.3 con `JAVA_HOME=/usr/lib/jvm/java-25-openjdk`.
- OpenSSH 10.2p1 in `/usr/bin/ssh`; il path standard `~/.ssh` (`/home/daniele/.ssh`) non e' ancora presente.
- Docker non e' installato e non ha una unit systemd; Podman 5.8.4 e' disponibile come runtime opzionale.
- Fedora System Monitor 1.0.1 e' installato in `/usr/local/libexec/fedora-system-monitor` con CLI `/usr/local/bin/fedora-system-monitor`; audit udev, hardening, concorrenza, retention e crescita database sono verificati con test live e sintetici.
- Restic 0.19.0 e' installato in `/usr/bin/restic`; repository cifrato T7, automazione, check completo e restore sono verificati nell'attivita' 583921.
- Smartmontools 7.5, nvme-cli 2.16, lm_sensors 3.6 e SQLite 3.51 erano gia' disponibili. L'attivita' 593184 ha aggiunto i pacchetti Fedora Python Socket.IO e compressione necessari soltanto al provisioning amministrativo Kuma; i collector ordinari restano standard-library.
- Android Studio Flatpak `com.google.AndroidStudio` 2026.1.1.10; avvio con `flatpak run com.google.AndroidStudio`.
- Android SDK: `/home/daniele/Android/Sdk`; ADB `1.0.41 / 37.0.0-14910828`; `sdkmanager` sotto `cmdline-tools/latest/bin`.
- Per Gradle usare il wrapper del progetto.
- Obsidian 1.12.7 e' installato per il solo utente come AppImage in `~/.local/opt/obsidian/Obsidian.AppImage`, con voce GNOME e icona locali; l'avvio e la presenza nel menu Applicazioni sono verificati. La compatibilita' AppImage richiede `fuse-libs.x86_64` 2.9.9-25.fc44.
- RustDesk 1.4.9 e' installato dal RPM x86_64 della release GitHub ufficiale tramite DNF in `/usr/bin/rustdesk`. Il digest GitHub coincide con lo SHA-256 locale; l'RPM non ha firma OpenPGP. Esiste una sola voce GNOME visibile e il secondo desktop file e' il link handler nascosto. Il servizio e' abilitato e attivo; l'ID persiste al riavvio del servizio e il rendezvous ufficiale e' raggiungibile. La password permanente va scelta e inserita manualmente in RustDesk, senza riportarla nei documenti. Per aggiornare ripetere selezione e verifica dell'RPM stabile ufficiale, poi `sudo dnf install ./rustdesk-<version>.rpm`; per rimuovere usare `sudo dnf remove rustdesk` senza cancellare configurazioni se non richiesto.

Per il Fedora corrente usare Bash, `dnf`, `systemctl`, `findmnt`, `lsblk` e `df`. Tool e path remoti non descrivono il runtime locale.

## TODO

La password Restic deve ancora essere salvata manualmente nel password manager. La directory SSH andra' creata solo quando necessaria, con permessi appropriati.

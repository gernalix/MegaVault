# Inventario software globale

Aggiornato: 2026-07-10. Autorita' operativa: [SOFTWARE_INVENTORY AI](../../ai/global/SOFTWARE_INVENTORY.md).

## Tool Fedora verificati

- Bash 5.3.9, DNF 5.4.2.1, systemd 259 e Git 2.55.0 dai path di sistema.
- GitHub CLI 2.94.0 in `/usr/bin/gh`; Codex CLI 0.144.0 in `/usr/local/bin/codex`.
- Python 3.14.6, pip 26.0.1, pipx 1.15.0 e uv 0.11.26.
- OpenJDK 25.0.3 con `JAVA_HOME=/usr/lib/jvm/java-25-openjdk`.
- OpenSSH 10.2p1 in `/usr/bin/ssh`; il path standard `~/.ssh` (`/home/daniele/.ssh`) non e' ancora presente.
- Docker non e' installato e non ha una unit systemd; Podman 5.8.4 e' disponibile come runtime opzionale.
- Android Studio Flatpak `com.google.AndroidStudio` 2026.1.1.10; avvio con `flatpak run com.google.AndroidStudio`.
- Android SDK: `/home/daniele/Android/Sdk`; ADB `1.0.41 / 37.0.0-14910828`; `sdkmanager` sotto `cmdline-tools/latest/bin`.
- Per Gradle usare il wrapper del progetto.
- Obsidian 1.12.7 e' installato per il solo utente come AppImage in `~/.local/opt/obsidian/Obsidian.AppImage`, con voce GNOME e icona locali; l'avvio e la presenza nel menu Applicazioni sono verificati. La compatibilita' AppImage richiede `fuse-libs.x86_64` 2.9.9-25.fc44.

Per il Fedora corrente usare Bash, `dnf`, `systemctl`, `findmnt`, `lsblk` e `df`. Tool e path remoti non descrivono il runtime locale.

## TODO

La policy backup Fedora, il client backup corrente e lo stato locale di restic non sono stati verificati in questa migrazione documentale. La directory SSH andra' creata solo quando necessaria, con permessi appropriati.

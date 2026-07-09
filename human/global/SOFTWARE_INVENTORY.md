# Inventario software globale

Aggiornato: 2026-07-09. Autorita' operativa: [SOFTWARE_INVENTORY AI](../../ai/global/SOFTWARE_INVENTORY.md).

## Tool Fedora verificati

- Bash 5.3.9, DNF, Git 2.55.0 e Python 3.14.6 dai path di sistema.
- OpenJDK 25.0.3 con `JAVA_HOME=/usr/lib/jvm/java-25-openjdk`.
- Android Studio Flatpak `com.google.AndroidStudio` 2026.1.1.10; avvio con `flatpak run com.google.AndroidStudio`.
- Android SDK: `/home/daniele/Android/Sdk`; ADB `1.0.41 / 37.0.0-14910828`; `sdkmanager` sotto `cmdline-tools/latest/bin`.
- Per Gradle usare il wrapper del progetto.

Per il Fedora corrente usare Bash, `dnf`, `systemctl`, `findmnt`, `lsblk` e `df`. Tool e path remoti non descrivono il runtime locale.

## TODO

La policy backup Fedora, il client backup corrente e lo stato locale di restic non sono stati verificati in questa migrazione documentale.

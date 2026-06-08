# Software Inventory

Inventario software operativo verificato il 2026-06-08. Il file AI autorevole e' [SOFTWARE_INVENTORY.md](../../ai/global/SOFTWARE_INVENTORY.md).

## Strumenti core

- Codex CLI `0.137.0`.
- Git `2.43.0`.
- GitHub CLI `2.45.0`.
- Python `3.12.3`.
- Node `24.16.0`, npm `11.16.0`.
- Java `17.0.19`.
- `sqlite3` nel PATH viene dall'Android SDK (`3.50.6`); il pacchetto apt installato e' `3.45.1`.

## Android

- ADB: `/home/daniele/Android/Sdk/platform-tools/adb`, versione `1.0.41`.
- sdkmanager: `/home/daniele/Android/Sdk/cmdline-tools/latest/bin/sdkmanager`, versione `20.0`.
- Android Studio ha stato locale sotto `~/.config/Google/AndroidStudio2026.1.1`; la versione product-info non e' stata ri-verificata in questo prompt.

## Backup, storage e rete

- Restic `0.16.4`.
- cryptsetup `2.7.0`.
- VeraCrypt `1.26.24`.
- Tailscale `1.98.4`.
- x11vnc `0.9.16`.

## Browser e desktop rilevanti

- Firefox `151.0.1+linuxmint1+zena`.
- Google Chrome stable `149.0.7827.53-1`.
- Telegram Desktop Flatpak `org.telegram.desktop`.
- Insync `3.9.10.60041-noble`.

## UNKNOWN

Docker non risulta installato localmente; e' documentato come runtime remoto della VM Kuma. Le versioni Gradle dei progetti Android non sono state aggiornate in questa discovery.

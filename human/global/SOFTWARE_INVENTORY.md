# Software Inventory

Inventario software leggibile derivato da [SOFTWARE_INVENTORY AI](../../ai/global/SOFTWARE_INVENTORY.md). La fonte operativa e' il file AI; questo documento non va usato come sorgente per Codex.

## Host corrente Windows

Il ThinkPad P14s Gen 5 AMD con Windows 11 Pro e' l'host principale corrente, ma in questo prompt non e' stata fatta una scansione software live. Restano quindi `UNKNOWN` le versioni e i path Windows di Codex Desktop, Git, GitHub CLI, Python, Node, Java, Android Studio, Android SDK, ADB, `rg`, WSL e Docker.

PowerShell e' la shell operativa attesa; i path Linux documentati sotto sono legacy e non vanno applicati al ThinkPad senza verifica.

## Snapshot legacy Linux Mint

Le sezioni seguenti descrivono il vecchio Surface/Linux Mint verificato nel 2026-06-08.

### Strumenti core legacy

- Codex CLI `0.137.0`.
- Git `2.43.0`.
- GitHub CLI `2.45.0`.
- Python `3.12.3`.
- Node `24.16.0`, npm `11.16.0`.
- Java `17.0.19`.
- `sqlite3` nel PATH viene dall'Android SDK (`3.50.6`); il pacchetto apt installato e' `3.45.1`.

### Android legacy

- ADB: `/home/daniele/Android/Sdk/platform-tools/adb`, versione `1.0.41`.
- sdkmanager: `/home/daniele/Android/Sdk/cmdline-tools/latest/bin/sdkmanager`, versione `20.0`.
- Android Studio ha stato locale sotto `~/.config/Google/AndroidStudio2026.1.1`; la versione product-info non e' stata ri-verificata in questo prompt.

### Backup, storage e rete legacy

- Restic `0.16.4`.
- cryptsetup `2.7.0`.
- VeraCrypt `1.26.24`.
- Tailscale `1.98.4`.
- x11vnc `0.9.16`.

### Browser e desktop legacy

- Firefox `151.0.1+linuxmint1+zena`.
- Google Chrome stable `149.0.7827.53-1`.
- Telegram Desktop Flatpak `org.telegram.desktop`.
- Insync `3.9.10.60041-noble`.

## UNKNOWN

Per Windows non sono ancora verificati toolchain, SDK Android, WSL, Docker e path reali. Nel vecchio snapshot Mint Docker non risultava installato localmente; era documentato come runtime remoto della VM Kuma. Le versioni Gradle dei progetti Android non sono state aggiornate in questa discovery.

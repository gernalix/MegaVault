# Profilo host globale

Aggiornato: 2026-07-09. Autorita' operativa: [HOST_PROFILE AI](../../ai/global/HOST_PROFILE.md).

## Host corrente

- Macchina primaria: Lenovo ThinkPad P14s Gen 5 AMD, host `fedora`.
- Sistema: Fedora Linux 44 Workstation, kernel `7.1.3-200.fc44.x86_64`, architettura x86-64.
- Utente/home: `daniele`, `/home/daniele`; MegaVault: `/home/daniele/MegaVault`.
- Shell: Bash 5.3.9; package manager: `dnf`.
- Git: `/usr/bin/git` 2.55.0; GitHub CLI: `/usr/bin/gh` 2.94.0; Codex CLI: `/usr/local/bin/codex` 0.144.0.
- Python: `/usr/bin/python3` 3.14.6; pip 26.0.1; pipx 1.15.0; uv 0.11.26.
- Servizi: systemd 259 tramite `systemctl` e `systemctl --user`.
- SSH: `/usr/bin/ssh` OpenSSH 10.2p1; directory standard `~/.ssh` (`/home/daniele/.ssh`) non ancora presente.
- Container: Docker non installato e unit assente; Podman 5.8.4 disponibile come runtime opzionale.

Per operazioni locali Codex deve usare path Fedora `/home/daniele/...`, comandi Bash e pacchetti DNF. Path di progetto o remoti non descrivono il filesystem locale.

## Hardware e storage

- CPU AMD Ryzen 7 PRO 8840HS con Radeon 780M, 8 core / 16 thread; RAM circa 27.7 GiB; BIOS `R2LET40W (1.21)`.
- Root e home: Btrfs su volume LUKS Kioxia NVMe da circa 951 GiB, circa 936 GiB disponibili al controllo.
- Seagate 3.5 TiB montato in `/run/media/daniele/Seagate Expansion Drive`; volume NTFS 155.9 GiB montato in `/run/media/daniele/09FA16D309FA16D3`.
- Samsung T7 collegato in `/run/media/daniele/Ventoy`; supporto recovery in `/run/media/daniele/VEEAMRE`.

Prima di backup o I/O pesante verificare `findmnt`, `lsblk` e `df`; i mount rimovibili possono cambiare.

## Android e Java

- Android Studio: Flatpak `com.google.AndroidStudio` 2026.1.1.10, avvio con `flatpak run com.google.AndroidStudio`.
- Android SDK, `ANDROID_HOME` e `ANDROID_SDK_ROOT`: `/home/daniele/Android/Sdk`.
- ADB: `/home/daniele/Android/Sdk/platform-tools/adb`, versione `1.0.41 / 37.0.0-14910828`.
- `JAVA_HOME`: `/usr/lib/jvm/java-25-openjdk`; OpenJDK 25.0.3.
- Non dichiarare un device connesso senza `adb devices -l`.

## Stato da verificare

Policy e target backup Fedora non sono stati verificati. Servizi e path specifici di progetto richiedono una verifica live prima dell'uso sul nuovo host.

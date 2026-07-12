# Profilo host globale

Aggiornato: 2026-07-12. Autorita' operativa: [HOST_PROFILE AI](../../ai/global/HOST_PROFILE.md).

## Host corrente

- Macchina primaria: Lenovo ThinkPad P14s Gen 5 AMD, host `fedora`.
- Sistema: Fedora Linux 44 Workstation, kernel `7.1.3-200.fc44.x86_64`, architettura x86-64.
- Utente/home: `daniele`, `/home/daniele`; MegaVault: `/home/daniele/MegaVault`.
- Shell: Bash 5.3.9; package manager: `dnf`.
- Git: `/usr/bin/git` 2.55.0; GitHub CLI: `/usr/bin/gh` 2.94.0; Codex CLI: `/usr/local/bin/codex` 0.144.0.
- Python: `/usr/bin/python3` 3.14.6; pip 26.0.1; pipx 1.15.0; uv 0.11.26.
- Servizi: systemd 259 tramite `systemctl` e `systemctl --user`.
- Monitor host: Fedora System Monitor 1.0.0 installato, abilitato e verificato con database SQLite locale e cinque Push Monitor Kuma.
- SSH: `/usr/bin/ssh` OpenSSH 10.2p1; directory standard `~/.ssh` (`/home/daniele/.ssh`) non ancora presente.
- Container: Docker non installato e unit assente; Podman 5.8.4 disponibile come runtime opzionale.
- Accesso remoto: RustDesk 1.4.9 RPM ufficiale in `/usr/bin/rustdesk`; servizio di sistema abilitato e attivo. Su GNOME Wayland il controllo e' sperimentale e la schermata GDM pre-login non e' raggiungibile; password permanente e test fisico Android restano manuali.

Per operazioni locali Codex deve usare path Fedora `/home/daniele/...`, comandi Bash e pacchetti DNF. Path di progetto o remoti non descrivono il filesystem locale.

## Hardware e storage

- CPU AMD Ryzen 7 PRO 8840HS con Radeon 780M, 8 core / 16 thread; RAM circa 27.7 GiB; BIOS `R2LET40W (1.21)`.
- Root e home: Btrfs su volume LUKS Kioxia NVMe da circa 951 GiB, circa 844 GiB disponibili al controllo.
- Seagate 3.5 TiB montato in `/run/media/daniele/Seagate Expansion Drive`; volume NTFS 155.9 GiB montato in `/run/media/daniele/09FA16D309FA16D3`.
- Il Samsung chiamato `T7` e' normalmente scollegato o smontato. Quando viene
  collegato, udev avvia il backup: il job monta l'ext4 label `T7_BACKUP` in
  `/mnt/T7_BACKUP`, usa il repository Restic cifrato e lo smonta prima della
  notifica di scollegamento sicuro. Il supporto recovery vfat `VEEAMRE` e' un
  dispositivo storico distinto.

Prima di backup o I/O pesante verificare `findmnt`, `lsblk` e `df`; i mount rimovibili possono cambiare.

## Android e Java

- Android Studio: Flatpak `com.google.AndroidStudio` 2026.1.1.10, avvio con `flatpak run com.google.AndroidStudio`.
- Android SDK, `ANDROID_HOME` e `ANDROID_SDK_ROOT`: `/home/daniele/Android/Sdk`.
- ADB: `/home/daniele/Android/Sdk/platform-tools/adb`, versione `1.0.41 / 37.0.0-14910828`.
- `JAVA_HOME`: `/usr/lib/jvm/java-25-openjdk`; OpenJDK 25.0.3.
- Non dichiarare un device connesso senza `adb devices -l`.

## Stato da verificare

Il backup Fedora sul T7 e' verificato; resta manuale l'escrow della password nel password manager. Altri servizi e path specifici di progetto richiedono verifica live.

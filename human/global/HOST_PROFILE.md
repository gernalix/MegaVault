# Profilo host globale

Aggiornato: 2026-07-05. Autorita' operativa: [HOST_PROFILE AI](../../ai/global/HOST_PROFILE.md).

## Host corrente

- Macchina primaria: Lenovo ThinkPad P14s Gen 5 AMD, host `DANIELE_PC`.
- Sistema: Microsoft Windows 11 Pro, build `26200`, 64 bit.
- Utente/path base: `seste`, `C:\Users\seste\Documents`.
- Shell: PowerShell/pwsh; `pwsh.exe` verificato in `C:\Program Files\PowerShell\7\pwsh.exe`, versione `7.6.3`.
- Git: `C:\Program Files\Git\cmd\git.exe`, versione `2.55.0.windows.2`; nella shell corrente non era nel PATH, quindi usare path completo se serve.

## Hardware

- CPU: AMD Ryzen 7 PRO 8840HS con Radeon 780M, 8 core / 16 thread.
- RAM: circa 27.7 GiB.
- BIOS: `R2LET40W (1.21)`.

## Storage verificato

- `C:` Windows NTFS su Kioxia NVMe da circa 953.9 GB; volume `Windows`, circa 804 GB liberi al controllo.
- `D:` Seagate Expansion Drive USB NTFS, circa 3.57 TB, circa 32 GB liberi al controllo.
- `E:` NTFS, circa 155.9 GB, ruolo non verificato.
- Samsung T7: non connesso nel controllo del 2026-07-05.

Regola: prima di backup o I/O pesante verificare sempre `Get-Disk` e `Get-Volume`; le lettere disco possono cambiare.

## Android

- Android Studio: `C:\Program Files\Android\Android Studio\bin\studio64.exe`.
- Android SDK: `C:\Users\seste\AppData\Local\Android\Sdk`.
- ADB: `C:\Users\seste\AppData\Local\Android\Sdk\platform-tools\adb.exe`, versione `1.0.41 / 37.0.0-14910828`.
- Non dichiarare un device connesso senza `adb devices -l`.

## Backup

- Veeam Agent: servizio `VeeamEndpointBackupSvc` verificato running/automatic.
- Target Veeam corrente: non verificato in questo passaggio; controllare DB/log Veeam e lettere disco prima di agire.
- Backblaze Windows: client non rilevato nei path default del controllo; riferimenti Backblaze B2 possono essere legacy o remoti finche' non riverificati.

## Storico Surface/Linux Mint

Il vecchio profilo Surface/Linux Mint e' storico, non host primario: `daniele-Surface-Pro`, Linux Mint 22.3, root ext4 su Samsung T7 via hub SABRENT, servizi systemd Mint, restic/Backblaze B2. Usarlo solo per contesto storico, progetti Mint, o runtime remoti Linux esplicitamente marcati.

# Inventario software globale

Aggiornato: 2026-07-05. Autorita' operativa: [SOFTWARE_INVENTORY AI](../../ai/global/SOFTWARE_INVENTORY.md).

## Tool Windows verificati

- PowerShell 7: `C:\Program Files\PowerShell\7\pwsh.exe`, versione `7.6.3`.
- Git: `C:\Program Files\Git\cmd\git.exe`, versione `2.55.0.windows.2`.
- Android Studio: `C:\Program Files\Android\Android Studio\bin\studio64.exe`.
- Android SDK/ADB: `C:\Users\seste\AppData\Local\Android\Sdk\platform-tools\adb.exe`, ADB `1.0.41 / 37.0.0-14910828`.
- Veeam Agent: servizio Windows `VeeamEndpointBackupSvc` running/automatic.

## Unknown/TODO

- Java e Gradle globali non riverificati; preferire wrapper Gradle dei progetti.
- GitHub Desktop non verificato; fallback Git CLI disponibile.
- Backblaze Windows client non rilevato nel controllo default.

## Storico

Tool Linux come `systemctl`, `/usr/bin/git`, `/home/daniele/Android/Sdk`, `restic` locale Mint e path `/home/...` sono legacy, remoti o project-specific.

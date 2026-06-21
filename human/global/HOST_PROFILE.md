# Profilo host globale

Aggiornato: 2026-06-21, prompt `#483920`.

Questo documento e' una versione leggibile derivata. La fonte operativa per Codex e' [HOST_PROFILE AI](../../ai/global/HOST_PROFILE.md); in caso di conflitto vince sempre il file AI, letto subito dopo [MEGAVAULT_PROTOCOL](../../ai/MEGAVAULT_PROTOCOL.md).

## Host corrente

- Host principale corrente: Lenovo ThinkPad P14s Gen 5 AMD.
- Modello/listing noto: `21ME003SXX`.
- Sistema operativo out-of-box/documentato: Windows 11 Pro.
- CPU: AMD Ryzen 7 PRO 8840HS.
- RAM: 32 GB.
- SSD interno: 1 TB.
- Display: 14" WUXGA 1920x1200 IPS, 400 nits, Low Power, 100% sRGB.
- Ruolo previsto: workstation principale per Codex Desktop Windows, sviluppo e test Android, repository GitHub, documentazione MegaVault e possibile uso del plugin Android di Codex Desktop.

## Regole operative Windows

Sul ThinkPad si deve ragionare come host Windows: PowerShell, path in stile `C:\...`, workspace GitHub sotto Windows e verifica live degli strumenti. Non vanno riusati automaticamente path Linux come `/home/daniele/...`, servizi `systemd`, stato ADB Linux, IP storici dei telefoni o topologia USB del Surface.

Per Android bisogna verificare il device o il plugin live prima di dichiarare build/test validi. Il path Windows dell'SDK Android, ADB, stato pairing, device connessi e IP attuali sono tutti sconosciuti finche' non vengono verificati.

## UNKNOWN da non inventare

Restano `UNKNOWN`: hostname Windows reale, username Windows, build Windows, firmware, seriale SSD, stato BitLocker, path workspace GitHub, path SDK Android Windows, path ADB Windows, IP attuali dei telefoni, stato device ADB, stato plugin Android Codex Desktop, servizi Windows attivi, WSL, Docker, backup path Windows e raggiungibilita' corrente della VM Oracle.

## Host legacy

Il vecchio `daniele-Surface-Pro` resta contesto storico, non host principale corrente. Era la workstation Linux Mint per Codex, Android, backup, monitoraggio e automazioni, con Linux Mint 22.3, XFCE/X11, Intel Core i5-7300U, circa 7.7 GiB RAM e vincoli forti di performance.

La topologia legacy importante era:

- root Linux su Samsung PSSD T7 Shield USB;
- sorgente storica Seagate 4 TB BitLocker;
- destinazione backup/transfer Seagate 6 TB;
- tutti collegati tramite hub USB alimentato SABRENT HB-BUP7 su una singola porta del Surface.

Questa topologia spiega vecchi progetti, servizi, freeze, backup e transfer, ma non va applicata al ThinkPad senza verifica live.

## Servizi e backup legacy

I servizi Mint come `adb-wifi-autoconnect`, `mint-freeze-forensics`, `mint-update-tracker`, `system-service-dashboard`, `transfer-vecchio-disco-adaptive-throttle`, `windowtabnotes` e i timer di backup/restic/Kuma sono snapshot legacy. Non sono servizi Windows e non vanno tradotti o riattivati senza inventario esplicito.

La VM Oracle/Kuma rimane documentata come nodo remoto storico: prima di operazioni runtime servono verifica SSH, backup DB per modifiche SQLite e attenzione a token o quota.

## Regola pratica

Per nuovo lavoro usare il ThinkPad Windows come `CURRENT_HOST`. Usare il Surface solo come `LEGACY_HOST` quando si interpretano vecchi percorsi, servizi, backup o incidenti.

# Profilo host globale

Aggiornato: 2026-06-07, prompt `#418572`.

Questo documento e' la versione umana del profilo host obbligatorio. La versione operativa per Codex e' [HOST_PROFILE AI](../../ai/global/HOST_PROFILE.md). Il protocollo che ne impone la lettura e' [MEGAVAULT_PROTOCOL](../../ai/MEGAVAULT_PROTOCOL.md).

## Host

- Host: `daniele-Surface-Pro`, workstation principale Linux Mint per Codex, Android, backup, monitoraggio e automazioni.
- Sistema: Linux Mint 22.3 Zena, base Ubuntu noble.
- Kernel: `6.19.8-surface-3`.
- Desktop: XFCE su X11.
- Hardware: Microsoft Surface Pro, firmware `239.871.768`.
- Batteria rilevata: `BAT1 M1009169`, 48%, non in carica al rilevamento.

## Hardware

- CPU: Intel Core i5-7300U, 2 core / 4 thread, fino a 3.5 GHz.
- RAM: circa 7.7 GiB.
- Swap: `/swapfile` da 8 GiB; al rilevamento usati circa 2.9 GiB.
- GPU: Intel HD Graphics 620 con driver `i915`.

Vincoli pratici: macchina laptop con pochi core, RAM limitata, firmware vecchio, root filesystem su SSD USB e workload storage pesanti. Il root Linux e i dischi esterni principali passano dallo stesso hub USB alimentato, quindi i lavori di performance, Android, backup, freeze e storage devono partire da questi limiti.

## Storage

- Root: `/dev/sda2`, ext4, montata su `/`, circa 915 GiB, su Samsung PSSD T7 Shield USB seriale `S6YGNS0Y903440H`.
- EFI: `/dev/sda1`, vfat, montata su `/boot/efi`.
- Disco interno: `/dev/nvme0n1`, Toshiba KBG30ZPZ256G, circa 238 GiB, partizioni Windows/BitLocker; non e' il root Linux.
- Disco esterno sorgente storico: `/dev/sdb`, Seagate ST4000LM024, partizione BitLocker usata come sorgente read-only nei transfer.
- Disco esterno backup/destinazione: `/dev/sdc1`, ext4 label `Seagate6TB`, montato su `/media/daniele/Seagate6TB2`.
- Backup home: `/media/daniele/Seagate6TB2/home-backups`.
- Destinazione transfer storico: `/media/daniele/Seagate6TB2/vecchio disco`.

## Hub USB e topologia storage

- Hub fisico: SABRENT HB-BUP7, "SABRENT USB Hub Active 3.2 x1".
- Porte: 7.
- Alimentazione: 36W, hub alimentato, con switch individuali.
- Collegamento host: una singola porta USB del Surface Pro.
- Vista kernel: hub Realtek su bus USB 3.0; i tre storage principali risultano sotto lo stesso ramo USB a 5000M.
- Topologia: `Surface Pro USB port -> SABRENT HB-BUP7 powered hub -> T7 root Linux + Seagate 4TB source + Seagate 6TB backup/destination`.

In pratica il Samsung T7 Shield, il Seagate 4TB BitLocker e il Seagate 6TB passano tutti dallo stesso hub alimentato. L'intero sistema Linux gira dal T7 collegato tramite quell'hub. Quindi un rallentamento, freeze, reset USB, saturazione I/O o problema sul controller/hub puo' impattare contemporaneamente root, sorgente e destinazione backup/transfer.

Vincoli storage: verificare sempre mount reali e non solo wrapper autofs; sorgenti BitLocker devono restare read-only; evitare `rsync --delete`; non riprendere automaticamente dopo errori USB/I/O; non assumere percorsi storage indipendenti.

## Android e telefoni

- SDK Android: `/home/daniele/Android/Sdk`.
- ADB: `/home/daniele/Android/Sdk/platform-tools/adb`, versione 37.0.0.
- Servizio ADB Wi-Fi: `adb-wifi-autoconnect.service`, user systemd, enabled e active.
- Telefoni configurati: Pixel 8a (`192.168.1.37`) e TCL 6102H (`192.168.1.200`).
- Verifica corrente del 2026-06-07: `adb devices -l` vuoto; i device possono essere storici o fuori rete.

Vincoli Android: pairing manuale di default, UI automatica disabilitata, mDNS/Avahi puo' essere stale, non usare `adb kill-server` senza approvazione esplicita, e non dichiarare device connesso senza `adb devices -l`.

## Oracle VM e Kuma

- VM Oracle: `ubuntu@150.230.148.128`, istanza `instance-20260201-1126`.
- Chiave SSH documentata: `/home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key`.
- Kuma: `http://150.230.148.128:3001`, container `uptime-kuma`, immagine `louislam/uptime-kuma:2.3.2`.
- DB Kuma: `/opt/uptime-kuma/data/kuma.db`.
- Ruolo Kuma: storico, alerting e visualizzazione; non remediation.

Vincoli Oracle: prima di modifiche SQLite su Kuma serve backup DB; non committare token; il backup remoto OCI e' documentato come quota critica, con limite assunto 22 GiB.

## Servizi e monitor

Servizi user attivi rilevanti: `adb-wifi-autoconnect`, `mint-freeze-forensics`, `mint-update-tracker`, `system-service-dashboard`, `transfer-vecchio-disco-adaptive-throttle`, `windowtabnotes`, `aw-server`, `aw-watcher-afk`, `aw-watcher-window`, `aw-watcher-media-player`.

Timer user rilevanti: `amici_fb`, `android-sdk-auto-update`, `home-backup-kuma-push`, `home-backup-retention-kuma-push`, `home-incremental-backup`, `mint-manual-updates`, `mint-resource-guardian`, `mint-update-tracker`, `mint-xfce-layout-guard`, `parcel-tracker`.

Servizi system rilevanti: `mint-cloud-backup-monitor`, `mint-cloud-backup-dashboard`, `transfer-usb-io-watchdog`, `disk-usage-monitor`.

Kuma monitora push da backup cloud, backup home, amici_fb, disk usage, parcel tracker, software audit e freeze analysis. Alcuni monitor obsoleti sono disabilitati: `mint heartbeat`, `rsync-transfer`, `codex-token-watcher`.

## Freeze, performance e I/O

La diagnostica freeze attiva e' `mint-freeze-forensics.service`, con sampler ogni 5 secondi e senza remediation automatica. Il guardian e' `mint-resource-guardian.timer`, con alert non interattivo sotto systemd.

Artefatti legacy anti-freeze rimossi: `freeze-reboot-monitor`, `freeze-zram-swap`, `screen-watchdog`, `system-watchdog`, `os-observer-autofix` e vecchi script correlati.

Storico I/O importante: il caso `rsync_exit=137` del 2026-06-06 era un abort controllato da load guard (`ABORTED_SAFE`, load_x100 sopra 600), non OOM, non disco pieno e non errore kernel I/O. `ABORTED_SAFE` non equivale a backup completato.

Per freeze, rallentamenti USB o problemi I/O bisogna considerare prima la topologia dell'hub: browser, processi o servizi non vanno accusati senza verificare che root T7, sorgente 4TB e destinazione 6TB condividono la stessa porta USB fisica, lo stesso hub e la stessa banda/controller.

## Backup

- Backup locale home: `home-incremental-backup.timer`, destinazione Seagate6TB2, con push Kuma separati per backup e retention.
- Backup cloud root: `mint-cloud-backup`, restic verso Backblaze B2, stato in `/var/lib/mint-cloud-backup`, dashboard locale `127.0.0.1:8765`.
- Backup Oracle: restic e snapshot SQLite sulla VM; quota remota OCI critica e fallback locale da preservare.

Regola pratica: non eseguire prune, unlock, forget, check pesanti o cancellazioni backup senza motivo verificato e approvazione esplicita quando distruttivo o quota-sensitive.

## Vincoli economici

Il budget mensile diretto non e' documentato. Il vincolo economico documentato e' la quota remota OCI per il backup Oracle: uso circa 22.262 GB con limite assunto 22 GiB. Evitare azioni che richiedono aumento quota, spesa, o prune distruttivo senza approvazione esplicita.

## Regola operativa

`HOST_PROFILE.md` deve essere letto subito dopo `MEGAVAULT_PROTOCOL.md` per lavoro di performance, monitoraggio, automazione, servizi, tuning sistema, Android tooling, backup, storage, Linux Mint e indagini freeze. Ignorarlo in questi ambiti e' un bug di processo.

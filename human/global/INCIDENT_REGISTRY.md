# Incident Registry

Ogni progetto deve avere un registro incidenti locale in `docs/ai/INCIDENT_REGISTRY.md` e `docs/human/INCIDENT_REGISTRY.md`, piu' un archivio SQLite aggiornato automaticamente da monitor, healthcheck o tool operativi.

Questo file resta in MegaVault solo come schema/indice globale. Le voci project-specific gia' presenti sono debito premigrazione e vanno migrate nei repo proprietari dopo verifica di metadata e git clean.

## Formato obbligatorio
- Incident ID
- Titolo
- Data prima comparsa UTC/Z
- Data ultima comparsa UTC/Z
- Numero occorrenze
- Gravita' massima
- Stato: `OPEN`, `MITIGATED`, `RESOLVED`, `ACCEPTED`
- Root cause
- Sistemi coinvolti
- Alert coinvolti
- Tentativi effettuati
- Soluzione finale
- Commit correlati
- Prompt correlati
- Tempo totale di impatto
- Note

## Regola pratica
Non creare un incidente nuovo per ogni alert ripetuto. Se `BACKUP_BLOCKED_FALLBACK_QUOTA` e `REMOTE_DEGRADED` derivano ancora da `OCI_STORAGE_LIMIT_EXCEEDED`, il registro deve aggiornare lo stesso incidente.

## SQLite
La tabella minima `incidents` contiene:

`incident_id`, `first_seen_utc`, `last_seen_utc`, `occurrence_count`, `severity`, `status`, `root_cause`, `resolution_summary`.

La tabella `incident_events` mantiene la cronologia completa degli eventi. Gli inserimenti devono essere automatici; niente aggiornamenti manuali ordinari.

## Stati
- `OPEN`: causa radice ancora attiva.
- `MITIGATED`: impatto controllato, causa non eliminata.
- `RESOLVED`: causa eliminata e verificata.
- `ACCEPTED`: rischio noto accettato per vincolo documentato.

## PIXEL_WHATSAPP_METERED_BACKGROUND_RESTRICTION

- Prima occorrenza: `2026-07-02`; ricomparsa e nuova risoluzione:
  `2026-07-26`; stato `RESOLVED`, gravita' `HIGH`, 2 occorrenze.
- Sintomo: molte notifiche WhatsApp arrivavano in ritardo o solo aprendo
  l'app, soprattutto quando il Pixel usava una rete mobile/misurata.
- Root cause: l'UID corrente di WhatsApp era tornato nella blacklist Android
  dei dati in background (`REJECT_METERED_BACKGROUND`).
- Fix: rimossa la blacklist e abilitati i dati mobili senza restrizioni solo
  per WhatsApp. Nessun dato, cache, account, chat o backup e' stato toccato.
- Verifica: dopo force-stop e riapertura, un messaggio reale e' arrivato mentre
  il Pixel restava in `Dozing`; FCM ha avviato WhatsApp e Android ha pubblicato
  due record non intercettati e non nascosti.
- Riconoscimento rapido: ricavare l'UID con `adb shell cmd package list
  packages -U com.whatsapp`, poi controllare `adb shell cmd netpolicy list
  restrict-background-blacklist`. L'UID WhatsApp non deve comparire.
- Nota DND: due notifiche del 25 luglio furono bloccate mentre Non disturbare
  era stato attivato manualmente. Le regole DND non sono state cambiate.
- Report: `ai/reports/activity_473821_pixel_whatsapp_notifications.md`.

## SMART_SERVICE_CAPABILITY_FALSE_POSITIVE

- Timestamp UTC: `2026-07-10T10:30:53Z`–`2026-07-26T12:08:27Z`.
- Stato: `RESOLVED`, gravita' `MEDIUM`, 156 occorrenze.
- Sintomo: `smart_check_failed` ripetuto per NVMe KIOXIA interno e Samsung T7,
  senza alert SMART attivo o transizione Kuma falsa.
- Root cause: al collector orario mancavano `CAP_SYS_ADMIN` per NVMe nativo e
  `CAP_SYS_RAWIO` per il bridge USB-NVMe ASMedia.
- Fix: Fedora System Monitor 1.3.1 limita entrambe le capability a
  `hourly`/`daily`, registra diagnostica strutturata, salta assenti/non
  compatibili e non interroga l'error log che blocca il bridge T7.
- Verifica: KIOXIA e T7 SMART `PASS`, zero nuovi falsi eventi, SQLite/systemd/
  udev/self-check verdi; due Seagate addormentati restano non risvegliati.
- Sorgente: `/home/daniele/MegaVault/projects/fedora-system-monitor/docs/ai/REPORT_482731.md`.

## CODEX_SQLITE_WAL_T7_ROOT_GROWTH
- Timestamp UTC: 2026-06-13T19:13:08Z
- Detection source: Disk Usage Monitor su `/dev/sda2` montato `/`.
- Sintomo: crescita T7/root di circa +157 GiB in 24h.
- Root cause: `/home/daniele/.codex/logs_2.sqlite` e' in WAL mode; Codex tiene DB/WAL/SHM aperti per tutta la sessione e scrive molti log TRACE/INFO. L'autocheckpoint e' default (`1000` pagine), non disabilitato, ma non garantisce il rilascio dello spazio allocato dal WAL; serve `wal_checkpoint(TRUNCATE)`.
- Cleanup: il watcher sicuro ha recuperato `163,682,495,352` byte (`152.44 GiB`) perche' il DB era integro e i frame WAL erano checkpointabili. Non sono stati cancellati sessioni, config, credential o transcript.
- Fix: timer utente `codex-sqlite-wal-maintenance.timer` ogni 30 minuti; script con soglie soft `1 GiB`, hard `5 GiB`, critical `20 GiB`, `quick_check`, holder detection, dry-run, report before/after e notifica Telegram critica solo se il helper/env gia' esistono.
- Verifica prompt `938274`: `journal_mode=wal`, `wal_autocheckpoint=1000`, `synchronous=2`, `page_size=4096`, `page_count=82970`, `freelist_count=12001`, `quick_check=ok`; WAL circa 10 MiB e stabile per il campione 2-5 minuti.
- Non fare: `rm ~/.codex/logs_2.sqlite-wal` o `.sqlite-shm` mentre Codex e' aperto; `pkill/killall codex` generico; cancellare `.codex/sessions`, config o credential.

## MTT_AUTOEXPORT_THROTTLE_SKIPPED_PENDING_MUTATION
- Timestamp UTC: 2026-06-15T00:00:00Z.
- Sintomo: nel test anti-storm, una modifica persistente arrivata durante un export richiedeva un export successivo ma il run andava in timeout.
- Root cause: il throttle legacy di `SqliteVault` poteva sopprimere il follow-up autoexport perche' il primo export riuscito aggiornava `last_export_ms` dopo la mutazione avvenuta durante la copia.
- Fix: `PersistentMutationTracker` ora e' single-flight, debounce 1200 ms, tiene `pending_export`, forza gli export accodati senza throttle e continua finche' `last_successful_export_at` copre `last_database_mutation_at`.
- Anti-loop: gli aggiornamenti sync (`last_export_attempt_at`, `last_successful_export_at`, `last_export_status`, errore/file/integrity) non marcano mutazioni DB.
- Commit app: `b612da3`.
- Verifica: TCL deviceTest mirato PASS 7/7 su TCL 6102H.

## CODEX_WEEKLY_LIMIT_MONITOR_PROLITE_DECODE
- Timestamp UTC: 2026-07-05T14:25:21Z.
- Sintomo: il monitor Oracle VM delle quote Codex restava attivo ma falliva ogni poll e non ripristinava notifiche Telegram affidabili.
- Root cause: il servizio usava `/opt/codex-native/bin/codex` `0.120.0`, che non deserializzava piu' `plan_type=prolite` dalla risposta `wham/usage`; il body conteneva quote valide ma veniva trattato come errore. Telegram dipendeva da una vecchia copia hardcoded di `/home/ubuntu/telegram_notify.py`, mentre config/env avevano placeholder.
- Fix: `config.ini` punta a `/usr/bin/codex` `0.137.0`; il watcher ora gestisce sia `rateLimits` normale sia fallback `wham/usage`, redige log/stato, e carica esplicitamente `/home/ubuntu/telegram_notify.py`. Il helper Telegram e' stato sostituito con versione env-based senza segreti hardcoded; token/chat migrati in `/etc/codex-weekly-limit-monitor.env` con permessi `600`.
- Verifica: dry-run senza Telegram PASS con weekly_left `64.0` e five_hour_left `95.0`; notifica reale Telegram OK; service `enabled` e `active`; run reale registra weekly_left `64.0`, five_hour_left `94.0`, `last_error` vuoto e notifica `weekly_left_change` inviata.
- Sicurezza: log/stato/helper del perimetro monitor redatti; scan finale `email_matches=0`, `user_id_matches=0`, `telegram_bot_url_matches=0`, `literal_bot_token_matches=0`.
- Report: `ai/reports/codex_weekly_limit_monitor_vm_fix_20260705.md`.
- Note: altre copie legacy VM di `telegram_notify.py` fuori scope possono ancora contenere hardcoding e vanno migrate in prompt dedicato.

## CODEX_WEEKLY_LIMIT_MONITOR_WRONG_5H_SOURCE
- Timestamp UTC: 2026-07-05T16:13:00Z.
- Sintomo: la notifica Telegram del monitor Codex mostrava una quota 5h diversa dalla UI Codex Analytics.
- Root cause: il parser usava `rateLimitsByLimitId.codex_bengalfox.primary`, cioe' la quota separata `GPT-5.3-Codex-Spark` mostrata al 100%, invece della quota 5h principale esposta da `rateLimits.primary`.
- Fix: la 5h principale viene letta da `rateLimits.primary`; `codex_bengalfox` non viene piu' usato come fallback per la quota principale. Se il campo manca, la notifica mostra `5h left: unavailable`.
- Verifica: dry-run e run reale systemd hanno letto `weekly_left=57%`, `five_hour_left=49%`, `five_hour_source=rateLimits.primary (codex)`, allineati allo screenshot utente.
- Telegram: resta usato solo `/home/ubuntu/telegram_notify.py`; nessun token o chat id stampato.
- Report: `ai/reports/codex_weekly_limit_real_5h_source_fix_20260705.md`.

## CODEX_WEEKLY_LIMIT_MONITOR_QUOTA_SCHEMA_CHANGE
- Timestamp UTC: 2026-07-14T17:48:27Z.
- Sintomo: dal 2026-07-12 il monitor Oracle VM falliva ogni poll con `Missing secondary rate limit window` e non aggiornava piu' correttamente le notifiche quote.
- Root cause: `account/rateLimits/read` non espone piu' la vecchia finestra main 5h da 300 minuti; `rateLimits.primary` ora e' una finestra da 10080 minuti, `secondary` e' `null`, e `codex_bengalfox` e' una categoria separata `GPT-5.3-Codex-Spark`.
- Fix: parser generico per categorie reali, rimozione/migrazione stato `last_five_hour_*`, Telegram costruito solo da categorie presenti, timestamp UTC in formato `dd/mm/yy hh:mm`.
- Verifica: test locali PASS, dry-run reale senza send PASS, notifica reale singola `Weekly 94% -> 82%`, service enabled+active, nessun timer dedicato perche' il watch loop interno programma il prossimo poll.
- Report: `ai/reports/prompt_738416_codex_quota_monitor_schema_change.md`.

## EXTERNAL_NTFS_DISCONNECT_DURING_MOUNTED_IO
- Timestamp UTC: `2026-07-09T17:07:00Z`.
- Sintomo: un volume NTFS esterno montato e' scomparso durante I/O; `ntfs-3g` ha registrato errori di sync e chiusura.
- Impatto: operazioni filesystem fallite fino alla ricomparsa e al remount circa dieci secondi dopo.
- Stato: `OPEN`, gravita' `CRITICAL`; causa fisica non ancora determinata.
- Mitigazione: Fedora System Monitor usa identita' stabile, registra l'evento, mantiene un alert critico e aggiorna il monitor Kuma `Fedora Storage` ID 40.
- Prossimo controllo: verificare cavo, alimentazione e diagnostica del disco prima di scritture lunghe.
- Sicurezza test: nessun dispositivo e' stato scollegato fisicamente e non e' stata tentata una riproduzione distruttiva.
- Sorgente: `/home/daniele/MegaVault/projects/fedora-system-monitor/docs/ai/INCIDENT_REGISTRY.md`.

## CODEX_DATA_ANALYTICS_WIDGETS_MISSING_PNG

- Timestamp UTC: `2026-07-14T12:03:44Z`; stato `RESOLVED`, gravita' `MEDIUM`.
- Sintomo: `codex --yolo` mostrava `MCP startup incomplete (failed: dataAnalyticsWidgets)` e `connection closed: initialize response`.
- Root cause: il plugin Data Analytics installato in `~/.codex/plugins/cache/openai-curated-remote/data-analytics/0.2.8-13ceeea1f599` avviava `node ./mcp/server.cjs --stdio`; il server caricava `assets/datascience.png` prima dell'handshake MCP, ma il PNG mancava e Node usciva con `ENOENT`.
- Fix: rigenerato solo `assets/datascience.png` dal `datascience.svg` gia' incluso nel plugin. Nessun server disabilitato, nessun cambio modello/YOLO/timeout/retry e nessun update pacchetti.
- Verifica: handshake manuale PASS con 5 tool e 3 risorse; `codex doctor` PASS `17 ok`, `0 warn`, `0 fail`; due avvii reali `codex --yolo` da `/home` senza l'errore MCP.
- Backup: plugin `activity_739184_20260714T140237+0200`; MegaVault registry `activity_739184_20260714T140520+0200`.
- Warning: un refresh/reinstall del plugin potrebbe sovrascrivere la cache locale se il pacchetto remoto resta privo dello stesso asset.

## T7_MOUNTPOINT_FELL_THROUGH_TO_INTERNAL_ROOT

- Timestamp UTC: `2026-07-11T23:09:00Z`; stato `RESOLVED`, gravita' `CRITICAL`.
- Sintomo: `/mnt/T7_BACKUP` esisteva sul Btrfs interno mentre il T7 non era montato.
- Root cause: `nofail` consente il boot senza disco; la directory non prova il mount esterno.
- Fix: ogni job richiede mount separato, ext4, UUID+label attesi, by-id seriale/modello e parent disk corretto prima di credenziale/repository.
- Test: namespace isolato senza T7, exit 21, entry interne `0→0`; backup reale successivo PASS.
- Sorgente: `/home/daniele/MegaVault/projects/fedora-t7-backup/docs/ai/INCIDENT_REGISTRY.md`.

## T7_LIFECYCLE_MOUNT_NAMESPACE

- Timestamp UTC: `2026-07-11T23:51:57Z`; stato `RESOLVED`, gravita' `HIGH`.
- Sintomo: quattro collaudi iniziali hanno notificato `unmount-cleanup` mentre
  il job non riusciva a vedere o rilasciare coerentemente il mount T7.
- Root cause: il namespace filesystem del servizio nascondeva il mount creato
  dopo lo start; `RequiresMountsFor` faceva invece arrestare il servizio quando
  il lifecycle smontava il disco.
- Fix: mount globale gestito dal lifecycle, mantenendo capability limitate,
  lock, timeout e hardening non incompatibile. I futuri fault test Telegram sono
  marcati `TEST CONTROLLATO`.
- Verifica: udev reale riprodotto, backup, check/prune, sync e smontaggio PASS;
  snapshot finali `f7682be7`, `a989e8fd`, `3082eb92`.
- Commit progetto: `55d310db67eaff1ee2dc15884213311e1269f2f4`;
  attività `684219`.

## ANDROID_STUDIO_FLATPAK_STALE_DIRECTORYLOCK_SOCKET

- Timestamp: artefatti dal `2026-07-09T17:11:52Z`; avvio fallito confermato il `2026-07-12T11:08:04Z`; stato `RESOLVED`, gravita' `HIGH`.
- Sintomo: Android Studio non partiva con `CannotActivateException`, `Address already in use` e `Connection refused`.
- Root cause: una chiusura Flatpak incompleta aveva lasciato il socket Unix `.port` e i marker `.pid`/`.lock`, ma nessun processo o listener era ancora vivo.
- PID: `(3)` era il PID interno del namespace Flatpak, non PID 3 dell'host. Il tentativo fallito aveva PID host `16895`; il PID host della vecchia istanza era gia' scomparso e non e' ricostruibile.
- Fix: dopo verifica con `flatpak ps`, processi, namespace, `ss`, `lsof` e `fuser`, sono stati spostati solo i tre artefatti in `/home/daniele/.local/state/android-studio-recovery/activity-516803-20260712T131700+0200`.
- Verifica: tre avvii riusciti, finestre XWayland realmente visibili/responsive, shutdown normali, socket e lock rilasciati; SDK, plugin, due AVD, ADB e keeper preservati.
- Recupero sicuro: non uccidere mai PID host 3 e non cancellare lock automaticamente. Prima provare che nessuna istanza valida possieda il socket, poi spostare `.port`/`.lock` in un backup timestampato.
- Report: `ai/reports/prompt_516803_android_studio_directory_lock.md`.

## KUMA_STALE_CATEGORY_ALERTS

- Timestamp: `2026-07-13`; stato `RESOLVED_WITH_REAL_STORAGE_ALERTS_REMAINING`, gravità `HIGH`.
- Sintomo: Host, Network e Storage restavano rossi anche dopo il rientro di alcune condizioni; DNF poteva generare un falso Software rosso.
- Root cause: recovery sensore monodirezionale, chiave Wi-Fi instabile, soglie filesystem incoerenti, inode FUSE sintetici, timestamp persi nel replay, recovery I/O incompleta e race DNF `Started`.
- Fix: Fedora System Monitor 1.1.0 con recovery bidirezionale, identità stabili, journal pulito, retry DNF terminale e deduplicazione esatta.
- Stato finale: Host, Network, Services e Software sani; Storage resta correttamente rosso per Seagate al 3,6754% libero e unsafe removal senza riconnessione.
- Sorgente: `/home/daniele/MegaVault/projects/fedora-system-monitor/docs/ai/AUDIT_471852.md`.

## KUMA_HOST_STORAGE_REAL_STATE_471853

- Timestamp: `2026-07-14`; stato `RESOLVED_WITH_REAL_ALERTS_REMAINING`, gravita' `HIGH`.
- Sintomo: Fedora Host alternava DOWN e Fedora Storage restava DOWN dopo il cleanup del Seagate.
- Causa reale: Host aveva swap warning reale circa 39%; Storage aveva Seagate al 5,2273% libero, ancora sotto recovery. Un alert `unsafe_device_removal` era stale perché il mount point era di nuovo presente.
- Fix: Fedora System Monitor 1.1.1 aggiorna gli alert metrici attivi e chiude unsafe-removal quando `findmnt` prova il ritorno del mount point.
- Stato finale: Host DOWN corretto per swap; Storage DOWN corretto per spazio Seagate; Network, Services e Software UP.
- Sorgente: `/home/daniele/MegaVault/projects/fedora-system-monitor/docs/ai/AUDIT_471853.md`.

## ZRAM_OCCUPANCY_MISCLASSIFIED_AS_MEMORY_PRESSURE

- Timestamp: dal `2026-07-14T10:15:00Z` al recovery `2026-07-18T18:40:34Z`; stato `RESOLVED`, gravita' `HIGH`.
- Sintomo: Fedora Host risultava DOWN per la sola percentuale di zram occupata.
- Root cause: `swap.used_percent` equiparava memoria compressa utile a pressione memoria senza verificare MemAvailable, PSI, velocita' swap, reclaim o OOM.
- Fix: Fedora System Monitor mantiene zram informativa e genera alert soltanto da `memory.pressure_level` composto; il comportamento resta valido nella 1.3.1.
- Verifica: MemAvailable 68,752%, PSI zero, pressione zero, rapporto compressione 2,857x, writeback e OOM delta zero.
- Commit MegaVault `c36f1fcf`; commit progetto `7f91e2316887`; attività `962417`.

## AUTOKEY_UINPUT_STALE_DEVICE_BUSY_LOOP

- Timestamp: `2026-07-14T18:35:00Z`–`18:49:50Z`; stato storico `MITIGATED`, gravita' `HIGH`.
- Sintomo: AutoKey usava circa il 99% di un core e scriveva traceback continui; CPU 84–89 C e ventole circa 4.480 RPM.
- Root cause: un device evdev era scomparso, ma il flush loop uinput continuava a leggerlo e generava `ENODEV` senza rimuoverlo o applicare backoff.
- Mitigazione allora applicata: stop/start controllato del solo servizio. AutoKey e' stato successivamente rimosso e sostituito da Espanso, quindi il rischio non e' piu' operativo.
- Sorgente: `/home/daniele/projects/fedora-diagnostics/docs/ai/AUDIT_614283.md`; commit `fd1344f`.

## AUTOKEY_FEDORA44_WAYLAND_INPUT_BLOCKED

- Timestamp: `2026-07-13` - `2026-07-14`; stato `RESOLVED`, gravita' massima `HIGH`.
- Sintomo visivo: il launcher RPM esisteva, ma AutoKey restava senza finestra evidente e dipendeva da una tray icon non mostrata da GNOME.
- Causa funzionale: Fedora AutoKey 0.96 usa XRecord ed e' limitato a X11/XWayland. Il fork Wayland 0.97.4 catturava l'input, ma GNOME 50 scartava il dispositivo virtuale per assi `EV_ABS` tablet incompleti; inoltre `wl-paste` poteva attendere senza limite con clipboard vuota.
- Esito finale: nell'attivita' `582941` AutoKey e' stato rimosso completamente e sostituito con Espanso Wayland. Sono stati eliminati pacchetti, COPR, servizio utente, launcher, wrapper, estensione GNOME, config, cache e log AutoKey; backup in `/home/daniele/backups/autokey/582941-20260714T222324+0200`.
- Verifica: nessun processo o pacchetto AutoKey residuo; `espanso.service` attivo e abilitato; 3 match migrati verificati con iniezione Espanso in finestra GTK temporanea; trigger digitati da tastiera virtuale verificati per `aktest638417x` e `adr`, con separatore finale conservato.
- Report: `ai/reports/prompt_638417_autokey_wayland.md` e `ai/reports/activity_582941_autokey_to_espanso.md`.

## VLC_FEDORA_FLATPAK_FAKE_OPENH264

- Timestamp: `2026-07-13T18:55:48Z`; stato `RESOLVED`, gravita' `HIGH`.
- Sintomo: VLC mostrava `Codec not supported` e non decodificava H.264, pur con OpenH264 installato sull'host Fedora.
- Root cause: l'unico VLC era il Flatpak Fedora `org.videolan.vlc`; il suo runtime Fedora 44 usava `ffmpeg-free` senza decoder H.264 nativo e il pacchetto `noopenh264`, una libreria OpenH264 fittizia. Il sandbox non poteva usare l'OpenH264 reale dell'host.
- Fix: rimosso soltanto il ref Fedora e installato il ref Flathub `org.videolan.VLC` 3.0.23 a livello di sistema. Resta una sola installazione VLC; nessun RPM codec e' stato cambiato e i dati della vecchia app sono stati preservati.
- Verifica: lo stesso campione MP4 H.264 Baseline falliva prima con `Unable to create decoder`; dopo il fix VLC `avcodec` ha ricevuto il primo frame, il rendering video e' terminato con codice 0, `ffmpeg` e `ffplay` sono PASS, `dnf check` e `flatpak repair --dry-run` sono PASS.
- Limiti: file originale non fornito; `mpv` non installato; `libpostproc` host assente ma non necessario per H.264.
- Report: `ai/reports/prompt_684271_vlc_h264_fedora.md`.

## GNOME_IDLE_SUSPEND_WIFI_SLEEP

- Timestamp UTC confermati: dal `2026-07-22T20:35:44Z` al `2026-07-22T23:39:36Z`; stato `RESOLVED`, gravita' `HIGH`; warning: test runtime fisico a batteria non eseguito.
- Sintomo: dopo inattivita' il display si spegneva e il Wi-Fi si disconnetteva.
- Root cause: `idle-delay=0` disabilitava il blanking desktop, ma GNOME Power conservava un secondo criterio indipendente: dopo 900 secondi eseguiva `suspend` sia con alimentatore sia a batteria. Il journal prova che NetworkManager disconnetteva `wlp2s0` con motivo `sleeping` subito dopo la richiesta di sospensione. Inoltre il powersave Wi-Fi era realmente attivo.
- Fix: timeout AC e batteria a `0`, azione inattiva `nothing`, idle dim disabilitato; drop-in globale NetworkManager `wifi.powersave=2` e powersave ath11k corrente disattivato. Sospensione, ibernazione e blocco manuali restano disponibili.
- Verifica: 600,594 secondi continui di inattivita' reale con pannello `DPMS=On`, Wi-Fi associato, powersave `off`, gateway raggiungibile e nessun nuovo evento suspend/disconnect. Prova fisica su AC; configurazione batteria verificata ma alimentatore non scollegato.
- Backup: `/home/daniele/.local/state/activity-641827/backups/20260723T020636+0200`.
- Report: `ai/reports/activity_641827_display_wifi_idle.md`.

## SECURE_BOOT_DRACUT_LUKS_UNLOCK_NOT_PERSISTED

- Finestra UTC: tra `2026-07-30T03:01:36Z` e `03:10:52Z`; stato `OPEN`, gravita' `HIGH`.
- Sintomo: con Secure Boot attivo dracut ha atteso `/dev/disk/by-uuid/6ff76a46-6614-4ac6-b1fa-a9590f09c709` ed e' entrato in emergency mode.
- Identita' provata: l'UUID non e' obsoleto. E' il FSID Btrfs corrente creato da Anaconda dentro `/dev/nvme0n1p3`, cifrato LUKS2 con UUID `0c261c5f-02dd-484f-b266-13ff4ee02abb`.
- Meccanismo: la entry BLS passa `root=UUID=6ff...`; dracut lo converte nel link `by-uuid`. Il link compare soltanto dopo che NVMe e' disponibile e cryptsetup apre LUKS.
- Limite probatorio: il boot fallito non ha montato la root e non ha lasciato boot ID, journal initramfs, `rdsosreport`, pstore o dump persistenti. Non si puo' distinguere offline tra mancata scoperta NVMe/LUKS e richiesta cryptsetup fallita o terminata.
- Verifiche: tutti i quattro initramfs, BLS, cmdline, grubenv, ordine EFI, fallback, firme shim/GRUB/kernel e moduli storage sono coerenti; l'UUID Btrfs non e' incorporato negli initramfs.
- Preparazione activity 948315: collector automatico root-only al primo boot riuscito e entry BLS diagnostica separata sullo stesso kernel/initramfs, senza `rhgb quiet`.
- Stato protetto: Secure Boot resta disabilitato; nessun reboot. LUKS, partizioni, chiavi, kernel, initramfs, BLS originali, GRUB e `grubenv` sono invariati.
- Limite residuo: un timeout dracut normale prima della root non entra nel journal interno o in pstore; occorre fotografare o filmare la console diagnostica.
- Report: `ai/reports/activity_214587_secure_boot_dracut_forensics.md`; preparazione: `/home/daniele/projects/fedora-diagnostics/docs/ai/AUDIT_948315.md`.

## MEGAVAULT_V16_BASELINE_DIVERGENCE_DIRTY_STATE

- Periodo: `2026-07-09`–`2026-08-01` e fino al merge della PR v16; stato `MITIGATED_PENDING_DRAFT_PR`, gravita' `HIGH`.
- Root cause: master era rimasto a VERSION=13 mentre le revisioni v14-v16 erano finite su branch Codex divergenti; gli output timeline dipendevano da orologio/mtime e WAL, e cache/private/secrets/sidecar non erano ignorati completamente.
- Fix: ricostruzione semantica da `origin/master=e5f128b`, protocollo VERSION=16, sette blob rimossi archiviati, bundle dei commit locali unici, generatore append-only deterministico e test permanenti repo/worktree.
- Limite: v16 diventa canonica su master soltanto dopo review e merge umano della draft PR; v17 e' esplicitamente esclusa.
- Manifest: `ai/V16_RECONCILIATION_MANIFEST.json`; delete manifest: `ai/archive/2917AA9_DELETE_MANIFEST.json`.

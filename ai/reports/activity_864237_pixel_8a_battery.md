# Attivita 864237 - Diagnosi batteria Google Pixel 8a

## Esito sintetico

- **Esito:** `PASS CON WARNING`
- **Dispositivo:** Google Pixel 8a (`akita`), Android 17, build `CP2A.260705.006`, patch 2026-07-05.
- **Conclusione:** la scarica storica elevata e reale. A schermo acceso e spiegata da carico applicativo/CPU reale, soprattutto WordPulse foreground nella finestra controllata, con Time Clocker come contributore background/foreground-service. A schermo spento la finestra naturale di 45 minuti dimostra un problema distinto: X/Twitter (`com.twitter.android`) ha mantenuto un partial wakelock `AudioMix` quasi continuo, impedendo quasi del tutto il suspend/deep sleep.
- **Sicurezza:** nessun dato app cancellato, nessuna app disinstallata/disabilitata, nessun permesso o setting permanente modificato, nessun root, nessun `force-idle`, nessun firmware/kernel/bootloader modificato.

## Ambito e metodo

La diagnosi usa tre finestre distinte:

1. **Snapshot storico pre-reset:** conserva la sessione quotidiana iniziata alle 16:05:32, prima di qualunque reset diagnostico.
2. **Scenario A controllato:** uso normale con schermo acceso, 25 minuti, campioni ogni 60 secondi.
3. **Scenario B controllato:** telefono immobile e schermo spento, 45 minuti naturali, senza polling ADB durante la finestra.

Il reset eseguito alle 20:33:20 e esclusivamente `dumpsys batterystats --reset`: azzera i contatori BatteryStats, non dati utente. E stato eseguito soltanto dopo snapshot, manifest dei comandi, hash e verifica integrita del bugreport.

Le grandezze hanno livelli di attendibilita differenti:

- charge counter e tempi realtime/uptime: misure dirette esposte dal fuel gauge/framework;
- consumo per componente/UID: modello Android BatteryStats, utile per attribuzione ma non misura hardware diretta;
- corrente istantanea: rumorosa e non adatta da sola ad attribuire una causa;
- deep sleep: inferito da differenza realtime-uptime e storia `running`, con limiti del buffer BatteryStats;
- capacita: stima fuel gauge, non prova di degrado elettrochimico.

## Precheck e inventario

| Voce | Risultato |
|---|---|
| Host | Fedora Linux 44 Workstation |
| ADB | 1.0.41, platform-tools 37.0.0 (`/home/daniele/Android/Sdk/platform-tools/adb`) |
| Target | Google Pixel 8a, product/device `akita` |
| Android | 17, SDK 37 |
| Build | `google/akita/akita:17/CP2A.260705.006/15641320:user/release-keys` |
| Security patch | 2026-07-05 |
| ADB | autorizzato, connessione wireless dedicata al target |
| Alimentazione | USB/DC offline; stato `Discharging`, quindi nessuna ricarica USB interferente |
| Battery saver | disattivato |
| Clock | host e telefono coerenti, timezone Europe/Copenhagen |
| Stato iniziale | 27%, circa 38,7 C, charge counter circa 1.134 Ah |
| Altro device ADB | escluso esplicitamente mediante seriale target; non analizzato |

Il seriale/IP, SSID, identificativi di account/notifiche e contenuti personali non sono riportati negli artefatti curati.

## Snapshot storico

Intervallo BatteryStats: 16:05:32-20:19 circa, 4 h 13 min 53 s.

| Metrica | Valore |
|---|---:|
| Scarica BatteryStats | 2.218 mAh |
| Corrente media derivata | 524,2 mA |
| Scarica percentuale derivata | 12,53-12,76 %/h |
| Schermo acceso | 4 h 03 min 24 s (95,9%) |
| Corrente media screen-on | 536,4 mA; circa 13,08 %/h su 4.100 mAh |
| Schermo spento | 10 min 29,6 s |
| Corrente media screen-off | 240,2 mA; circa 5,86 %/h su 4.100 mAh |
| Screen-off awake | 9 min 34,9 s (91,31%) |
| Screen-off suspend | 54,7 s (8,69%) |
| Partial wakelock union | 10 min 29,6 s |
| Light idle | 24,1 s |
| Deep idle osservato | 0 s nella storia disponibile |

La misura conferma che il circa 13 %/h visto da AccuBattery era reale nella finestra storica. Non dimostra pero un drain a riposo: il 95,9% della sessione era a schermo acceso. La stima screen-on di 536 mA e coerente con l'autonomia AccuBattery dichiarata, mentre i soli 10,5 minuti screen-off sono troppo pochi per caratterizzare stabilmente l'idle.

I 2.218 mAh BatteryStats differiscono di circa il 2,9% dai 2.155 mAh AccuBattery forniti: le due fonti indipendenti concordano sulla grandezza della scarica pur usando modelli e boundary non identici.

Anche le correnti concordano: 536,4 mA screen-on da BatteryStats contro circa 539 mA AccuBattery; per lo screen-off 240,2 contro circa 263 mA, ma su soli 10,5 minuti e quindi con maggiore incertezza.

### Potenza per componente

Modello BatteryStats storico:

| Componente | mAh modellati | Lettura |
|---|---:|---|
| CPU | 720 | dominante |
| Display | 312 | importante, ma luminosita quasi sempre dark/dim |
| Mobile radio | 114 | secondario |
| Wi-Fi | 87,2 | secondario |
| Camera | 32,9 | coerente con uso foreground |
| Audio | 24,5 | secondario |
| GPU | 16,8 | basso rispetto a CPU/display |
| Wakelock | 4,57 | basso come energia modellata; rilevante per suspend |
| Video | 7,53 | basso |
| GNSS | 0,637 | trascurabile |
| Sensori | 0,0148 | trascurabile nel modello |

Display attivo a 1080x2400@60 Hz, `peak_refresh_rate=60`; il 120 Hz compare soltanto per 6,6 secondi storici. La luminosita era quasi tutta `dark`/`dim`, con circa 1 min 49 s in fascia bright. Non emerge un refresh rate o una luminosita anomala.

La radio cellulare era LTE per il 100% del tempo, con RSRP `great` per circa il 91% e `good` per circa l'8%; 5G e segnale debole non spiegano la scarica. GNSS e location hanno energia modellata minima. La temperatura era intorno a 39 C con stato termico virtual-skin leggero, senza evidenza di throttling severo.

### Attribuzione storica per UID

| UID | Pacchetto | Processo/ruolo | mAh modellati | Componenti principali | Interpretazione |
|---:|---|---|---:|---|---|
| 10500 | `com.wordpulse.app` | WordPulse | 369 | CPU 219; screen 148 | carico foreground/cached elevato |
| 1000 | UID Android condiviso | Android System/system_server e servizi HAL | 135 | CPU 130 | aggregato di sistema, non singola app |
| 10295 | `com.openai.chatgpt` | ChatGPT | 124 | screen 66,5; CPU 25,1; camera 17; radio 11,9 | uso foreground legittimo osservato storicamente |
| 10190 | `com.google.android.youtube` | YouTube | 103 | radio 43,7; audio 23,2; CPU 13,9; screen 13,2 | riproduzione/uso foreground |
| 10425 | `com.burockgames.timeclocker` | Time Clocker | 78,8 | CPU 78,1 | background/FGS sospetto |
| 10228 | `com.android.systemui` | System UI | 34,5 | CPU 31,7 | sistema/UI |
| 10571 | `com.example.multitimetracker` | MultiTimeTracker | 30,7 | screen 19,5; CPU 11,0 | soprattutto uso foreground storico |
| 10175 | `com.google.android.gms` | Google Play Services | 25,0 | CPU 12,8; radio 11,8 | contributo secondario |
| 10276 | `com.teslacoilsw.launcher` | Nova Launcher | 23,4 | screen 20,5 | uso launcher |
| 10331 | `org.telegram.messenger` | Telegram | 23,1 | screen 14,8; CPU 5,44 | uso prevalentemente foreground |
| 10167 | `com.google.android.GoogleCamera` | Camera | 18,4 | camera 15,3 | uso camera coerente |
| 10237 | `com.google.android.apps.nexuslauncher` | Pixel Launcher | 11,3 | CPU 6,37; screen 4,27 | secondario |
| 10563 | `com.gernalix.sostanze` | Sostanze | 6,36 | screen 3,35; CPU 2,94 | basso |
| 10566 | `com.gernalix.luoghi` | Luoghi | 4,55 | screen 2,82; CPU 1,71 | basso |
| 10458 | `com.workflowy.android` | Workflowy | 3,32 | screen 1,8; CPU 0,91 | basso |

I numeri AccuBattery e BatteryStats non sono intercambiabili: usano finestre e modelli differenti. L'ordine AccuBattery non basta a dimostrare causalita.

### Wakelock storico

Nella breve parte screen-off storica, X/Twitter (`com.twitter.android`, UID 10393) mostra `AudioMix` per 532,579 s, pari a circa l'84,6% dei 629,591 s screen-off. E una **correlazione forte ma non una causa persistente dimostrata**: nello snapshot audio/media successivo non risultava un player Twitter attivo e il processo non era presente. Va riprodotto separatamente prima di intervenire.

Le principali sorgenti kernel storiche visibili tramite BatteryStats erano `SuspendControl.TotalSuspendDelay` 447,597 s, `PowerManagerService.WakeLocks` 170,559 s, Bluetooth 98,842/53,509 s e wake Wi-Fi RX/TX 75,096/58,602 s. `/proc/wakelocks` e debugfs wakeup sources non erano leggibili senza root; queste sorgenti sono aggregate e non bastano da sole ad attribuire un'app.

## Scenario A - schermo acceso

Finestra controllata: 25 min 32,5 s tra boundary, con 24 min 59,1 s screen-on e 33,2 s screen-off accidentali/non significativi.

| Metrica | Valore |
|---|---:|
| Batteria | 23% -> 20% |
| Charge counter | 1.008 -> 0.846 Ah; delta 162 mAh |
| Media da charge counter | 380,6 mA |
| Media BatteryStats | 371,2 mA |
| Screen-on BatteryStats | 374,6 mA |
| Equivalente su 4.100 mAh | circa 9,1-9,3 %/h |
| Temperatura | min 37,9; media 39,34; max 40,0 C |
| Corrente istantanea campionata | media 394,5 mA; min 193,8; max 730,6 mA |
| Correlazione temperatura/corrente | Pearson r=0,351; debole-moderata, non causalita |
| Overhead logger | 75,778 s di comandi / 1.500 s = 5,05% duty cycle |

Il valore percentuale intero 3%/25,5 min produce 7,05%/h ma soffre quantizzazione. Charge counter e BatteryStats concordano molto meglio: differenza circa 2,5%, elemento contrario a un fuel gauge palesemente inattendibile.

La media screen-on controllata (374,6 mA) e circa il 30% inferiore ai 536,4 mA storici: il picco storico e quindi reale ma non e un assorbimento fisso del dispositivo. Cambia con le app e il carico effettivo.

Il valore AccuBattery di circa -771 mA e compatibile con un picco: il logger ha osservato fino a 730,6 mA, ma una media molto inferiore. Una corrente istantanea non puo essere usata come media della sessione.

Il traffico UID 2000/`com.android.shell` (circa 20 MB) e prodotto principalmente dalla raccolta ADB su Wi-Fi. E conservato nel CSV ma escluso dai grafici applicativi e dalle conclusioni sulle app; i boundary possono analogamente aggiungere pochi secondi di overhead fuori dalla finestra silenziosa.

WordPulse era realmente foreground e domina due fonti indipendenti:

- BatteryStats: 698,709 s CPU, pari al 45,60% di un core medio; 1.162,432 s foreground; 34,645 mAh modellati (21,093 CPU, 13,358 screen).
- runtime cumulativo da `top`: 686,74 CPU-s su 1.200,16 s rappresentati, 57,22% di un core medio.

Queste misure dimostrano il costo durante l'uso, non dimostrano da sole un bug: WordPulse era l'app realmente in primo piano. Nessun repository WordPulse e stato trovato nei percorsi locali ispezionati, quindi non e stata formulata un'attribuzione a una specifica funzione di codice.

Time Clocker ha consumato 342,407 CPU-s (22,35% di un core), e rimasto foreground service per l'intera finestra e vale 4,671 mAh modellati, quasi interamente CPU. Questo e un contributo background dimostrato nello Scenario A, non il carico dominante complessivo.

MultiTimeTracker ha usato 22,539 CPU-s (1,47% di un core), zero partial wakelock, zero job e zero traffico nella finestra; Luoghi ha avuto zero CPU/wakelock/job/rete. Sostanze ha usato 1,748 CPU-s (0,11%). Queste app non spiegano il drain controllato.

Nel repository MultiTimeTracker esiste un ticker UI permanente a 250 ms (`TimeEngine.kt`, righe 72-76), raccolto incondizionatamente da `viewModelScope` (`MainViewModel.kt`, righe 938-944). E una possibile ottimizzazione, ma l'evidenza misurata esclude che sia la causa principale in questa finestra. Nessun codice e stato modificato.

## Scenario B - schermo spento naturale

Precondizioni: Doze light/deep abilitati, `mForceIdle=false`, motion sensor attivo, rete connessa, telefono non in carica. I timeout esposti erano light idle dopo 4 minuti e deep-idle state machine con inattivita/sensing/location da 15 secondi; `wait_for_unlock=true`. Non e stato usato `deviceidle force-idle`.

Finestra controllata: boundary pre alle 21:01:14, finestra silenziosa naturale 21:04:28-21:49:28, boundary post completato alle 21:49:41. Non c'e stato polling ADB durante i 45 minuti.

| Metrica | Valore |
|---|---:|
| Batteria | 19% -> 16% |
| Charge counter | 0.834 -> 0.710 Ah; delta 124 mAh |
| Media da charge counter | 154,2 mA; circa 3,76 %/h |
| Media BatteryStats totale | 141,7 mA; circa 3,46 %/h |
| Screen-on nel boundary completo | 193,6 s |
| Screen-off nel boundary completo | 2.702,2 s |
| Screen-off BatteryStats | 90 mAh; 119,9 mA; circa 2,92 %/h |
| Temperatura | 37,3 -> 32,5 C |
| Screen-off awake | 2.686,1 s |
| Screen-off suspend | 16,1 s |
| Percentuale screen-off in suspend | 0,596% |
| Percentuale screen-off awake | 99,404% |
| Partial wakelock union | 2.702,2 s |
| Light Doze/history | 1.477,5 s |
| Deep Doze/history | 0 s |
| Wake reason principali | Wi-Fi 56, `aoc_mailbox` 1, alarm 1, cellular 1 |

Il consumo screen-off controllato e inferiore al dato AccuBattery screen-off medio/di sessione, ma resta alto per un telefono che dovrebbe sospendere: il punto critico non e la corrente assoluta da sola, e che BatteryStats mostra quasi tutto il tempo screen-off come awake.

La causa principale nella finestra screen-off e dimostrata da fonti indipendenti:

- `batterystats_full`: `Wake lock u0a393 AudioMix: 39m 41s 384ms`, `actual=2736639`, `running for 2736639ms`, UID 10393 `com.twitter.android`.
- `controlled_uid_summary.csv`: UID 10393 ha 2.704,586 s di partial wakelock, 756,337 CPU-s e 26,12% di un core medio nel boundary B.
- `activity_processes.txt` post-boundary: processo `com.twitter.android` presente in stato cached/empty, con provider e servizio Firebase registrati; non foreground.
- `idle_history_metadata.csv`: 2.682,2 s screen-off coperti, 2.683,4 s awake/running, solo 16,6 s suspend, 0 s deep Doze.
- `modeled_uid_power_deltas.csv`: X/Twitter e il primo UID modellato nello Scenario B, con 19,52 mAh, quasi tutti da wakelock.

Questo spiega il "deep sleep praticamente nullo" nella sessione screen-off osservata. Non e un problema di schermo, luminosita o 5G: in B lo schermo era spento, la temperatura scendeva, la rete mobile non mostra segnale debole, e l'energia di GNSS/sensori e trascurabile.

Altri eventi idle esistono ma sono secondari: Google Play Services ha 56 s di partial wakelock e 27 wakeup alarm; Telegram/WhatsApp/Photos/Turbo hanno job o wakelock brevi; DriveSync e altri generano traffico/job. Nessuno si avvicina alla durata di X/Twitter `AudioMix`.

### Robustezza dei dati

- Scenario A: 25/25 campioni attesi, nessun errore nei comandi state/top.
- Charge counter e BatteryStats nello Scenario A differiscono di circa il 2,5%.
- BatteryStats storico e AccuBattery differiscono di circa il 2,9% sui mAh totali.
- Clock host/device e timestamp monotoni sono coerenti; timezone Europe/Copenhagen.
- Scenario B: nessun campionamento periodico, quindi overhead ADB nullo durante la finestra silenziosa; soltanto boundary esterni.
- Bugreport ZIP: verifica integrita superata e SHA-256 registrato.
- Limite: le stime mAh per componente/UID restano un modello Android e non devono chiudere necessariamente il bilancio del fuel gauge.

## Cause ordinate per confidenza

| Causa | Classificazione | Confidenza | Sintesi |
|---|---|---:|---|
| Foreground app + CPU | DIMOSTRATA | 95% | Storico 95,9% screen-on; Scenario A dimostra WordPulse CPU/foreground e consumo screen-on coerente. |
| WordPulse foreground | DIMOSTRATA | 95% | 698,709 CPU-s, 45,60% di un core, 1.162,432 s foreground; nessun wakelock/job anomalo. |
| X/Twitter `AudioMix` screen-off | DIMOSTRATA | 94% | 39m41s partial wakelock, 2.704,6 s nel summary UID, awake quasi continuo in B. |
| Time Clocker CPU/FGS | ALTAMENTE PROBABILE | 88% | 342,407 CPU-s in A e FGS continuo; contributore, non principale in idle. |
| Display duration | DIMOSTRATA | 90% | La sessione storica era quasi tutta screen-on; non emerge anomalia di luminosita/refresh. |
| Deep sleep impedito da wakelock | DIMOSTRATA | 94% | Light Doze entra ma suspend e solo 0,596% dello screen-off; wakelock X/Twitter copre quasi tutta la finestra. |
| Alarm/job troppo frequenti | POSSIBILE | 45% | Presenti, ma durate inferiori al wakelock X/Twitter. |
| Kernel wakelock | POSSIBILE | 55% | Aggregati kernel visibili, attribuzione precisa bloccata da non-root. |
| Wi-Fi wakeup | POSSIBILE | 40% | 56 wake reasons Wi-Fi, ma non domina il consumo rispetto al wakelock userspace. |
| Modem/5G/segnale debole | ESCLUSA NELLA FINESTRA OSSERVATA | 90% | LTE, segnale great/good, nessuna evidenza 5G o segnale scarso come causa. |
| GPS/location | IMPROBABILE | 85% | GNSS/location modellati trascurabili. |
| Sensori | IMPROBABILE | 80% | Energia sensori trascurabile; nessuna correlazione principale. |
| Google Play Services | POSSIBILE | 45% | Attivita idle presente ma secondaria rispetto a X/Twitter. |
| Thermal throttling | IMPROBABILE | 80% | Temperatura in B scende da 37,3 a 32,5 C; nessun thermal severe. |
| Doze/device idle guasto | POSSIBILE | 60% | Light Doze entra; deep Doze no per wakelock/awake quasi continuo. |
| MultiTimeTracker | ESCLUSA NELLA FINESTRA OSSERVATA | 92% | 0 CPU/wakelock/job/rete in B; 1,47% core in A. |
| Luoghi | ESCLUSA NELLA FINESTRA OSSERVATA | 95% | 0 CPU/wakelock/job/rete nelle finestre controllate. |
| Sostanze | ESCLUSA NELLA FINESTRA OSSERVATA | 90% | Attivita minima; non spiega il drain. |
| Batteria degradata | POSSIBILE | 35% | `charge_full/design` 91,4%, ma non prova fisica e non spiega la dinamica. |
| Fuel gauge inattendibile | IMPROBABILE | 80% | AccuBattery, BatteryStats e charge counter sono coerenti entro pochi punti percentuali. |

La tabella completa con evidenza a favore, contraria e dati mancanti e salvata in `derived/cause_assessment.csv`.

Le percentuali esprimono confidenza diagnostica nella classificazione, non quota di batteria.

## Perche AccuBattery puo mostrare 0 min deep sleep

Nel campione storico la spiegazione e multipla e misurata: 95,9% della finestra era screen-on; lo screen-off durava solo 10,5 minuti; in quel tratto la CPU era awake per il 91,31%; BatteryStats registra solo 24,1 secondi di light idle e nessun deep idle nel buffer disponibile. Inoltre Android 17 limita l'accesso non-root alle sorgenti kernel e app di terze parti possono avere una lettura incompleta. Lo Scenario B distingue una condizione persistente da un artefatto della sessione quasi tutta screen-on.

## Batteria fisica e fuel gauge

| Metrica esposta | Valore |
|---|---:|
| Design capacity | 4.486 mAh |
| Learned/full charge capacity | 4.100 mAh |
| Rapporto full/design | 91,40% |
| Stima BatteryStats | 4.082 mAh |
| Cycle count | 485 |
| Health | `Good` |

Il rapporto suggerisce una possibile riduzione stimata dell'8,6%, ma non dimostra degrado elettrochimico. ADB non espone una misura di laboratorio della capacita; temperatura, calibrazione e algoritmo fuel gauge introducono incertezza. L'accordo charge-counter/BatteryStats nello Scenario A rende improbabile un errore di gauge abbastanza grande da spiegare da solo il drain.

Come controllo di coerenza indipendente, i dati AccuBattery forniti (2.155 mAh per 53%) implicano circa 4.066 mAh (`2155 / 0,53`), molto vicini ai 4.082-4.100 mAh esposti da Android. Questo sostiene la coerenza dei contatori, non certifica la salute fisica della cella.

## Azioni correttive proposte

Nessuna azione e stata applicata al telefono.

| Azione proposta | Beneficio atteso | Rischio | Reversibilita | Impatto funzioni | Forza prove |
|---|---|---|---|---|---|
| Ripetere Scenario B dopo aver chiuso ogni riproduzione/media in X/Twitter, senza cambiare permessi o dati | Conferma se `AudioMix` e persistente o legato a una sessione audio rimasta appesa | Basso | Totale | Nessuno se si chiude solo l'app/sessione | Alta |
| Se il repeat conferma X/Twitter, provare correzione manuale non distruttiva: chiusura app, stop media, riavvio app; eventuale reboot solo se autorizzato | Potenziale recupero deep sleep | Basso-medio | Alta | Possibile perdita dello stato volatile dell'app | Alta ma da confermare |
| Valutare limitazione notifiche/background di X/Twitter solo previa autorizzazione | Riduzione wakelock e CPU idle | Medio | Reversibile | Può ritardare notifiche | Alta per questa finestra, invasiva |
| Analizzare Time Clocker o ridurne FGS solo previa autorizzazione | Riduzione CPU mentre usi altre app | Medio | Reversibile | Può alterare funzionalita dell'app | Media-alta |
| Profilare WordPulse a livello codice o con simpleperf in uso reale | Ottimizzazione del consumo screen-on | Basso su clone/test | Reversibile | Nessuno se solo profiling | Alta per carico, non per bug |
| Ottimizzare MultiTimeTracker ticker a 250 ms in un task separato | Potenziale riduzione micro-carico UI | Basso | Alta | Da testare su app | Bassa per questa diagnosi |
| Nessuna azione su modem, 5G, refresh rate, luminosita o batteria fisica ora | Evita interventi non supportati | Basso | Totale | Nessuno | Evidenza contraria forte |

## Riproducibilita

Workspace diagnostico raw/derivato, permessi 0700:

`/home/daniele/diagnostics/activity-864237-pixel-8a-battery-20260714T201731+0200`

Comando unico per ripetere una raccolta nuova, senza modifiche permanenti:

```bash
cd /home/daniele/diagnostics/activity-864237-pixel-8a-battery-20260714T201731+0200 && ./scripts/run_diagnosis.sh idle scenario-b-repeat 2700 15
```

Il comando richiede il Pixel 8a autorizzato e usa il seriale configurato localmente; acquisisce boundary pre/post, lascia 15 secondi per spegnere manualmente lo schermo, non esegue polling ADB nei 45 minuti e rigenera CSV/grafici. Non resetta BatteryStats ne esegue test invasivi.

Cleanup dei soli eventuali file temporanei creati da questa diagnosi sul telefono:

```bash
cd /home/daniele/diagnostics/activity-864237-pixel-8a-battery-20260714T201731+0200 && ./scripts/cleanup_device.sh
```

Nella sessione corrente non sono stati creati file persistenti sul telefono, quindi il cleanup e idempotente.

Artefatti principali:

| Artefatto | Percorso assoluto |
|---|---|
| Snapshot/raw | `/home/daniele/diagnostics/activity-864237-pixel-8a-battery-20260714T201731+0200/raw/` |
| Bugreport completo | `/home/daniele/diagnostics/activity-864237-pixel-8a-battery-20260714T201731+0200/raw/bugreport/bugreport-akita-CP2A.260705.006-2026-07-14-20-20-01.zip` |
| CSV derivati | `/home/daniele/diagnostics/activity-864237-pixel-8a-battery-20260714T201731+0200/derived/` |
| Grafici | `/home/daniele/diagnostics/activity-864237-pixel-8a-battery-20260714T201731+0200/derived/charts/` |
| Script | `/home/daniele/diagnostics/activity-864237-pixel-8a-battery-20260714T201731+0200/scripts/` |
| Hash | `/home/daniele/diagnostics/activity-864237-pixel-8a-battery-20260714T201731+0200/hashes/` |
| Log comandi | `/home/daniele/diagnostics/activity-864237-pixel-8a-battery-20260714T201731+0200/logs/` |

Il bugreport ZIP e stato verificato integralmente; SHA-256 iniziale: `f31b9fa884592adbef57f2d6004f3655a1905b2f5a2c7b6c72a3243f36736920`.

## Disponibilita delle sorgenti

Lo snapshot registra comando, exit code, disponibilita e orario in `raw/snapshot/command-status.tsv`. Risultato finale: 40 sorgenti disponibili, 3 disponibili ma vuote, 3 non disponibili senza root (`/proc/wakelocks`, `/d/wakeup_sources`, `/sys/kernel/debug/wakeup_sources`). Le alternative usate sono BatteryStats, PowerStats, suspend stats e storia `running`. La copia curata e redatta e `derived/source_availability.csv`.

Output potenzialmente sensibili, come Wi-Fi, netstats, notifiche o account, restano nel workspace locale protetto e non sono copiati in MegaVault. CSV, grafici e report curati usano package/UID e dati power, non contenuti personali.

## Timeline diagnostica

| Ora locale | Evento |
|---|---|
| 20:17 | precheck host/ADB/target e stato batteria |
| 20:19 | snapshot storico completo |
| 20:20-20:22 | bugreport Android e verifica ZIP |
| 20:33:20 | reset solo BatteryStats dopo gate di integrita |
| 20:33:47-20:58:47 | Scenario A, 25 campioni a 60 s |
| 20:59 | boundary finale Scenario A |
| 21:01 | boundary iniziale Scenario B |
| 21:04:28-21:49:28 | Scenario B senza polling ADB |
| dopo 21:49 | analisi, report, hash, timeline MegaVault e commit locale |

## Limiti e dati necessari per maggiore certezza

- ADB non-root non espone tutte le wakeup sources kernel ne una misura hardware di potenza per rail.
- Il modello mAh per UID di BatteryStats non chiude necessariamente il bilancio del fuel gauge.
- UID 1000 e un aggregato di sistema; non consente attribuzione univoca ad Android System.
- Una sola finestra idle non dimostra ripetibilita su reti, segnale e notifiche differenti.
- Per dimostrare degrado fisico serve un ciclo di scarica/carica controllato o strumentazione esterna, non il solo `charge_full`.
- Per attribuire X/Twitter `AudioMix` serve una riproduzione screen-off con e senza sessione audio.
- Per separare completamente overhead ADB servirebbe misura esterna; qui il logger e stato disattivato durante Scenario B e il duty cycle e documentato nello Scenario A.

## Git e modifiche

- MegaVault iniziale: branch `codex/826417-fedora-diagnostics`, pulito alla partenza (`0b1fc4b`).
- Durante la diagnosi sono comparse modifiche concorrenti non appartenenti all'attivita; non sono state alterate, aggiunte allo staging o incluse.
- Worktree isolato dell'attivita: `/home/daniele/MegaVault-worktrees/activity-864237`, branch `codex/864237-pixel-battery-diagnosis`.
- Modifiche telefono: reset dei soli contatori BatteryStats; nessuna modifica permanente o dati utente.
- Modifiche repository app: nessuna.
- Push: **non eseguito**, come richiesto.

- Report e timeline MegaVault aggiornati nel worktree isolato.
- Commit locale: il report e la timeline sono inclusi nel commit indicato nell'output finale; il valore non e scritto nel report per evitare un riferimento circolare al contenuto del commit.
- Push: **non eseguito**.

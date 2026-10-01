# MegaVault specialist references
VERSION=61
STATUS=TASK_SPECIFIC_ONLY

Cross-project operations and all meta-infrastructure authority/procedures live only in
[META_INFRASTRUCTURE.md](META_INFRASTRUCTURE.md). Read the sections below only when
the requested task needs these specialized implementation policies. Historical
incident/prompt records in MegaVault are archival, not observed or lifecycle authority.

## Proiezione Obsidian cross-project

Obsidian e' una **proiezione derivata esterna**, non una responsabilita' delle app o dei database sorgente.

Fonte e ownership:
- ogni progetto mantiene la propria fonte canonica e il proprio eventuale formato Git/data export;
- il servizio Fedora condiviso `sqlite-to-obsidian` consuma sorgenti registrate e produce una sola vault navigabile cross-project;
- per PersonalHub la sorgente e' il repository privato `PersonalHub-data`, non il repository sorgente `PersonalHub` e non il file Android live `personalhub.db`;
- PersonalHub non deve contenere renderer Markdown, configurazione vault, code Obsidian, WorkManager Obsidian o dipendenze runtime da Obsidian;
- la vault non e' mai source of truth e non viene importata automaticamente nelle sorgenti.

Contratto del projector:
- adapter separati per sorgente; il core di rendering non deve contenere logica specifica di PersonalHub;
- identita' stabili e namespace globali per permettere wikilink espliciti anche tra progetti diversi;
- generare note solo per entita'/eventi semanticamente utili; cache, queue, ack, contatori tecnici, audit interni e altri dettagli di runtime restano fuori salvo valore umano concreto;
- relazioni solo se supportate da chiavi/relazioni canoniche o mapping espliciti; mai dedurre una relazione dalla sola uguaglianza di etichette;
- stato incrementale proprio del servizio con `source_revision`, versione adapter/renderer e manifest dei file posseduti;
- usare i change-set della sorgente come hint di efficienza, ma rendere sempre possibile un rebuild corretto dal manifest/stato completo;
- cancellare solo file marcati come generati e presenti nel manifest di ownership; preservare note manuali;
- failure del projector non deve mai bloccare o modificare il writer/source upstream.

Runtime Fedora:
- implementare come servizio/timer resiliente secondo lo standard systemd MegaVault;
- preferire trigger periodico leggero o evento Git osservabile; evitare daemon always-on se il polling a timer soddisfa la freschezza richiesta;
- ogni run deve fare fetch/pull, verificare il nuovo revision, applicare il delta, validare la vault e aggiornare lo stato soltanto dopo successo;
- nessun retry identico senza nuova evidenza; su schema incompatibile o stato incrementale mancante eseguire un rebuild bounded e sicuro;
- integrare il runtime nel control plane Uptime Kuma come timer/oneshot: monitorare esito + freschezza dell'ultima run, non `ActiveState=active`.

Il contratto specifico PersonalHub e' documentato in `PersonalHub/docs/OBSIDIAN_ARCHIVE.md`. La documentazione del servizio condiviso vive nel repository `sqlite-to-obsidian` quando creato; MegaVault conserva solo le regole trasversali.

### Database inventory

`database_inventory` e' l'unico inventario autorevole dei database. La riconciliazione scopre i repository dal filesystem, deduplica worktree e clone per origin normalizzato o common Git dir, e riconosce SQLite dalla firma binaria, indipendentemente dall'estensione. Conserva inoltre i database runtime dichiarati fuori repository e sui mount pertinenti, marcandoli `missing` o `remote_declared` quando non osservabili localmente.

`data_assets`, `project_components` e documenti non devono duplicare questa funzione. Le classificazioni ammesse sono `canonical`, `derived`, `cache`, `browser`, `test`, `fixture`, `backup`, `historical`, `demo`.

```bash
PYTHONDONTWRITEBYTECODE=1 python3 megavault.py database-inventory-reconcile
```

### Telegram

`telegram_notification_project_index` e' l'indice una-riga-per-progetto dei progetti per cui esiste evidenza di capacita' Telegram. L'evidenza deriva da `telegram_project_capabilities`, `integrations`, `services`, `project_components` e `project_operations`.

`telegram_shared_infrastructure_index` contiene helper/integrazioni Telegram globali senza `project_id`. Un helper condiviso non deve essere forzato artificialmente su un progetto. La presenza dell'infrastruttura condivisa, da sola, non significa che tutti i progetti possano inviare notifiche.

CLI:

```bash
python3 /home/daniele/MegaVault/megavault.py telegram-index
python3 /home/daniele/MegaVault/megavault.py telegram-index --project-id PROJECT_ID
```

## Segreti, credenziali e Bitwarden

Regola generale: il codice applicativo non deve inventare storage ad hoc per token/password. Ogni progetto usa il provider sicuro nativo del proprio contesto e accede ai segreti attraverso un boundary/adapter dedicato. I valori non vanno mai in source code, SQLite applicativi, URL, export JSON, log, report, Git o MegaVault.

Provider canonici per contesto:

- Fedora desktop / processi interattivi nella sessione utente: Secret Service (libsecret). Python deve usare un adapter dedicato (per esempio `secret-tool`/Secret Service o una libreria equivalente), non file letti a mano.
- Servizi systemd system/user: preferire `LoadCredential=` / `LoadCredentialEncrypted=` e leggere esclusivamente da `$CREDENTIALS_DIRECTORY`; i file `0600` esistenti sono fallback di migrazione, non il target finale.
- GitHub Actions: GitHub Actions Secrets / token forniti dal runner; mai copiare questi valori in file del repository.
- Android / PersonalHub: Android Keystore (o API Android che lo usa); vietato salvare token in Room/SQLite, SharedPreferences in chiaro, export o backup applicativi.
- Credenziali già possedute da un provider/tool (es. `gh auth`, browser profile, Tailscale): riusare il provider e non duplicare il segreto in un secondo store.
- VM/headless senza sessione Secret Service: systemd credentials, secret manager del provider o file dedicato `0600` solo quando il provider nativo non è disponibile; niente dipendenza da keyring grafico.

Ordine di risoluzione raccomandato per tool Linux che devono girare in più contesti:
1. systemd credential esplicita in `$CREDENTIALS_DIRECTORY`;
2. Secret Service/libsecret quando esiste una sessione utente appropriata;
3. variabile d'ambiente solo come input effimero esplicito (CI/test/manuale), mai persistita dal programma;
4. file legacy `0600` solo durante migrazione o per host headless dove è la soluzione prevista.

Regole di implementazione/migrazione:
- ogni repo che usa credenziali deve avere un solo adapter/boundary per ottenerle; il resto del codice riceve valori già risolti e non conosce path/provider;
- nessun fallback silenzioso da un provider configurato ma rotto verso uno meno sicuro: provider presente ma invalido => fail closed;
- i test usano provider finti/in-memory o env test-only, mai valori reali;
- migrare i file legacy al provider corretto senza stampare il valore; verificare il nuovo percorso, poi rimuovere il vecchio solo dopo PASS e solo se non serve più ad altri consumer;
- non introdurre una dipendenza libsecret in daemon/headless se il processo non dispone di session bus/keyring sbloccato;
- `/home/daniele/.config/codex/secrets` resta una root legacy/compatibilità e un luogo ammesso per file temporaneamente ancora necessari; non è più il default architetturale universale.
- MegaVault conserva solo riferimenti/provider metadata in `secret_refs`, mai valori.
- Accesso ai segreti solo quando richiesto dal task; lettura minima; nessun echo in prompt, argv quando evitabile, log, report o Git.
- Rotazione solo su richiesta manuale esplicita.
- Per Bitwarden usare `bw`; se bloccato, fermarsi e chiedere sblocco locale. Non acquisire master password, session token o valori segreti in chat.
- Sincronizzare `bw` prima e dopo scritture; verificare nomi campo e presenza allegati, non valori.

## Regole Daniele Conservate Qui

Usare questa sezione solo quando il task tocca davvero il dominio indicato.

### Python

Usare l'ambiente globale. `venv`, `virtualenv`, `pipenv`, `poetry` e `uv` sono vietati salvo richiesta esplicita dell'utente. Riusa pacchetti globali prima di installare altro.

### Servizi systemd e Host

La tabella canonica per i servizi personalizzati e' `services`. Non creare registri paralleli di servizi. Prima di aggiungere o modificare un servizio, risolvere `project_id`, `host_id`, scope, unit e runtime path da MegaVault quando disponibili; verificare live path, mount, unita' systemd e host runtime prima di documentare lo stato corrente.

`services` descrive l'inventario desiderato. L'evidenza osservata appartiene a Fedora System Monitor; eventuali viste periodiche MegaVault sono proiezioni non autorevoli. Non introdurre un secondo collector/controller.

Classificare sempre l'unita' prima di scegliere la policy:

- **daemon long-running / always-on**: il processo e' previsto attivo per tutta la vita del relativo target/sessione. Usare `Type=simple` o `Type=notify` quando supportato, `Restart=always`, un `RestartSec=` bounded (normalmente 5-30 s), e un target `[Install]` appropriato. `enabled` garantisce l'avvio al target; `Restart=` garantisce la resilienza del processo. Sono requisiti distinti.
- **oneshot schedulato**: non usare `Restart=always`. La riesecuzione appartiene al relativo `.timer`; usare `Persistent=true` quando una run persa a macchina spenta deve essere recuperata al ritorno. Un retry su failure puo' essere previsto solo se idempotente e bounded.
- **oneshot event-driven**: non trasformarlo in daemon. Deve essere riattivato dall'evento proprietario (udev/path/socket/timer/altro trigger) e avere timeout/idempotenza coerenti.
- **lifecycle unit con `RemainAfterExit=yes`**: lo stato active/exited e' intenzionale; non applicare `Restart=always`.
- **user service**: usare `systemctl --user`. Abilitare linger solo quando il servizio deve vivere anche senza login; un servizio legato a GNOME/Wayland/browser deve invece restare legato alla sessione grafica.
- **system service**: usare `systemctl`; non introdurre contemporaneamente un secondo autostart cron/desktop/user per lo stesso runtime.

Per un daemon dichiarato always-on, una uscita pulita del processo e' comunque anomala: per questo la baseline e' `Restart=always`, non `on-failure`. Lo stop amministrativo tramite systemd resta uno stop intenzionale e non viene contrastato da `Restart=always`. Configurare `StartLimitIntervalSec=`/`StartLimitBurst=` per impedire loop di crash incontrollati, senza usarli come sostituto della diagnosi.

Segreti nei servizi: seguire la sezione SECRETS; preferire `LoadCredential=`/`LoadCredentialEncrypted=` e `$CREDENTIALS_DIRECTORY`. Vietati token negli URL/unit file, nel repository, in MegaVault o nei log.

Monitoring policy/authority: META_INFRASTRUCTURE.md. Provisioning/readback: Fedora System Monitor, un monitor per failure domain azionabile, non uno per ogni unit.

Gate minimo per un nuovo daemon always-on:

1. `systemd-analyze verify` sulla unit;
2. installazione + `daemon-reload` + enablement sul target corretto;
3. stato `active` verificato;
4. terminazione del processo figlio controllata e prova che systemd lo riavvii (`NRestarts` aumenta); non usare `systemctl stop` come crash test;
5. prova post-reboot/post-login coerente con lo scope;
6. segnale di salute previsto verificato tramite Fedora; transizione controllata solo quando sicura e richiesta;
7. nessun autostart duplicato.

Template canonico per i daemon long-running: `ai/systemd-service-standard.service.example`. Per timer/oneshot applicare invece la classificazione sopra, senza copiare `Restart=always` meccanicamente.

### Infrastruttura STRICT e cutover

Quando un task `STRICT` modifica rete, listener, reverse proxy, tunnel, firewall,
TLS/DNS, autostart, Docker networking o un runtime critico:

1. prima di qualsiasi mutazione eseguire un singolo preflight read-only della
   catena end-to-end; se il repository proprietario offre un helper di audit,
   usarlo invece di ricostruire lo stesso inventario con molti comandi separati;
2. il preflight deve coprire almeno host/runtime canonico, listener e processi
   proprietari, firewall/esposizione pubblica, DNS, proxy, backend locale,
   unita' system e user rilevanti, tunnel/connettori e relativi autostart,
   configurazioni/identita' del tunnel e stato del worktree;
3. risolvere prima duplicazioni o ambiguita' di ownership/autostart. Non assumere
   che piu' processi simili siano un errore: verificare se appartengono davvero
   allo stesso tunnel/configurazione;
4. prima del cutover creare backup consistente e verificabile e rollback
   idempotente. Il rollback deve fissare le identita' che cambiano col contesto
   (per esempio project name Compose) e usare readiness bounded, non sleep
   arbitrari;
5. un HTTP `2xx`, una UI raggiungibile o uno stato precedente non bastano a
   dichiarare PASS. Per push, heartbeat o pipeline asincrone usare un
   nonce/correlation marker univoco e verificarne il readback nel DB/log/stato
   autorevole del destinatario;
6. quando scheduling o heartbeat fanno parte del task, verificare almeno due
   cicli reali prima del PASS;
7. mantenere il percorso legacy finche' il nuovo percorso non supera il gate
   end-to-end dal producer al destinatario;
8. dopo un fallimento non ripetere lo stesso comando/probe senza nuova evidenza
   o una modifica che cambi l'ipotesi. Classificare prima il livello responsabile
   e fare il successivo controllo minimo discriminante;
9. dopo il PASS fermarsi: niente audit aggiuntivi, esplorazione generale o
   cleanup fuori scope.

### Database

Ispezionare schema/path live prima di query o migrazioni. Per SQLite live/concorrenziale preferire `.backup`; preservare WAL/SHM quando rilevanti.

### Android

- Project docs nel repo proprietario; MegaVault conserva solo regole trasversali.
- `version.txt` e' sorgente unica per versioni Android Daniele quando presente.
- Storage timestamp: UTC `Z`; UI locale dispositivo; test di conversione richiesti quando il task tocca date/ore.
- i18n `en` + `it`; niente testo visibile hardcoded.
- Usare Gradle wrapper del progetto.
- Scoprire emulatori/dispositivi live con `adb devices`; non hardcodare seriali.
- Un endpoint ADB Wi-Fi `IP:porta`, l'ordine di `adb devices`, il model hint di `adb devices -l`, o un seriale ricordato da una sessione precedente **non provano l'identita' del device**.
- Prima di qualsiasi test o conclusione specifica su un device fisico usare il gate fail-closed `python3 /home/daniele/MegaVault/tools/adb_device_gate.py --target pixel|tcl`. Il gate seleziona solo device fisici live e verifica almeno `ro.product.manufacturer` + `ro.product.model` via `getprop`; se viene passato `--serial`, quel seriale viene comunque verificato e non fidato.
- Per target fisici diversi usare `--expect-manufacturer ... --expect-model ...`; con piu' match o nessun match il gate deve fermare il task come `BLOCKED`, senza inferire nulla dal device sbagliato.
- Se il task presume che un package sia installato, passarlo con `--require-package PACKAGE`: il gate controlla il package solo **dopo** l'identita' e attraversa gli Android user/profile rilevati. Una risposta package negativa ottenuta prima dell'identity gate non e' evidenza valida di "app non installata".
- Per verificare un'assenza attesa, eseguire prima il gate d'identita', poi la query package esclusivamente sul seriale restituito e sugli user/profile pertinenti. Evidenza sorprendente o contraddittoria (es. UI mostra l'app ma ADB dice assente) obbliga a rivalidare device + user/profile prima di concludere.
- Dopo PASS del gate, tutte le operazioni successive del task devono usare `adb -s <seriale_verificato>`; se il seriale cambia o si riconnette un altro target, rieseguire il gate.
- Per emulatori, usare solo seriale live `emulator-*` in stato `device`; avviare emulator solo se il test dispositivo e' richiesto e non ce n'e' uno attivo.
- I gate che esercitano `AndroidKeyStore`, `KeyStore.getInstance("AndroidKeyStore")`, chiavi AES/EC non esportabili, firma/attestazione o codice che dipende dal provider Android **devono essere eseguiti su emulator/AVD o device Android reale**. Robolectric/JVM host non fornisce un AndroidKeyStore equivalente e un failure `KeyStoreException`/`NoSuchAlgorithmException` su `AndroidKeyStore` in Robolectric non prova un bug applicativo. Per questi casi: usa unit test host solo per logica pura e verifica il percorso Keystore sul canonical AVD `Pixel_8a` come leaf gate minimo prima di escalare a TCL/Pixel.
- Non sostituire un Pixel fisico con emulator se il task richiede Pixel fisico.
- Non dichiarare device test PASS senza evidenza live sul dispositivo richiesto.

### Physical Pixel

Per test su Pixel fisico:

1. inviare Telegram esatto `smetti di usare il telefono`;
2. attendere 5 secondi dopo invio confermato;
3. eseguire la fase di test;
4. inviare Telegram esatto `testing finito` quando la fase termina.

Per install finale PersonalHub riuscito su Pixel fisico, inviare subito Telegram esatto `PH installato`. Se la notifica pre-test fallisce, non toccare il Pixel e riportare blocker.

### Telegram Task Notifications

Quando le notifiche task sono abilitate e non sovrascritte da regola progetto, inviare una sola notifica terminale per prompt/goal:

- formato: `<titolo chat> - <stato>`;
- stati: `successo`, `pausa`, `fail`;
- usare il titolo reale Codex Desktop se disponibile, altrimenti titolo prompt/goal senza inventare.

# MEGAVAULT_PROTOCOL
VERSION=38
STATUS=AUTHORITATIVE_SPECIALIST_PROTOCOL
MODE=codex_conditional

## Scopo

MegaVault e' necessario solo quando il task richiede project context persistente, `project_id`, fatti canonici su progetti/host/servizi/repository/integrazioni/segreti/incidenti, regole conservate qui, infrastruttura, o aggiornamenti a MegaVault.

Per task locali banali o gia' localizzati, non consultare MegaVault: usa `/home/daniele/.codex/AGENTS.md` e i file direttamente pertinenti.

## Modalita'

- `FAST`: default per lavoro localizzato, basso rischio, con contesto gia' sufficiente. Usa solo fatti/file MegaVault pertinenti.
- `STANDARD`: per lavoro multi-file, cross-component, o quando servono piu' fonti MegaVault correlate.
- `STRICT`: per migrazioni dati, azioni distruttive, sicurezza/segreti, infrastruttura critica, grandi refactor, o richiesta esplicita dell'utente.

Usa sempre la modalita' piu' bassa che soddisfa in sicurezza lo scope. Promuovi solo con evidenza concreta; declassa se il rischio non si materializza.

## Fonti e Precedenza

Fonti autorevoli:

1. Git history per stato storico dei repository;
2. `/home/daniele/MegaVault/megavault.sqlite` per fatti strutturati correnti;
3. Markdown in `ai/` solo come bootstrap/protocollo;
4. comportamento reale del codice o del sistema verificato live.

Precedenza:

- `megavault.sqlite` batte markdown cancellato o duplicato per fatti correnti strutturati.
- I project docs vivono nel repository proprietario; MegaVault conserva solo conoscenza globale, trasversale o di routing.
- Non inventare fatti mancanti: verifica live o registra `UNKNOWN`.
- I valori dei segreti non vanno mai in MegaVault, Git, log o report; solo riferimenti.

## Project Identity

Se `project_id=N` e' fornito, risolverlo solo da `megavault.sqlite`; non inferirlo da nomi, path, memoria o somiglianze.

Tabelle/view principali:

- `projects`, `project_aliases`, `repositories`;
- `hosts`, `services`, `integrations`, `secret_refs`;
- `incidents`, `incident_events`, `tags`, `tag_aliases`, `incident_tags`;
- `events`, `knowledge_notes`, `data_assets`;
- `codex_project_index`, `codex_work_queue`, `codex_remote_projects`, `codex_missing_projects`, `codex_archived_projects`;
- `kuma_monitor_index` per routing Uptime Kuma con spiegazione e `project_id`;
- `telegram_notification_capability_index` come evidenza granulare e `telegram_notification_project_index` come indice una-riga-per-progetto.

Gli indici Kuma/Telegram sono view derivate: non sono registri duplicati. Correggere sempre `services`, `integrations`, `project_components` o `project_operations` alla fonte, poi rigenerare le view. Non correggere manualmente le view.

CLI utile:

```bash
python3 /home/daniele/MegaVault/megavault.py project-list
python3 /home/daniele/MegaVault/megavault.py project-work-queue
python3 /home/daniele/MegaVault/megavault.py project-show PROJECT_ID
python3 /home/daniele/MegaVault/megavault.py project-path PROJECT_ID
python3 /home/daniele/MegaVault/megavault.py project-path --status PROJECT_ID
python3 /home/daniele/MegaVault/megavault.py kuma-index
python3 /home/daniele/MegaVault/megavault.py kuma-index --project-id PROJECT_ID
python3 /home/daniele/MegaVault/megavault.py telegram-index
python3 /home/daniele/MegaVault/megavault.py telegram-index --project-id PROJECT_ID
python3 /home/daniele/MegaVault/megavault.py operational-index-migrate
python3 /home/daniele/MegaVault/megavault.py operational-index-validate
python3 /home/daniele/MegaVault/megavault.py validate
```

`project-path` stampa solo il worktree canonico e fallisce se assente o ambiguo. `project-path --status` stampa un solo token: `LOCAL`, `REMOTE_ONLY`, `MISSING`, `ARCHIVED` o `ABSENT`.

`kuma-index` espone ogni evidenza Kuma con progetto, host, stato e spiegazione. `telegram-index` restituisce una riga per progetto con stato della capacita' ed evidenze aggregate. `operational-index-validate` fallisce se trova entry Kuma/Telegram senza `project_id` o entry Kuma senza spiegazione documentata.

## Lettura Operativa

Per task MegaVault:

1. leggere questo file;
2. leggere solo la parte pertinente di `ai/GLOBAL_INDEX.md` se serve routing compatto;
3. interrogare `megavault.sqlite` per i fatti richiesti;
4. per Uptime Kuma o notifiche Telegram usare prima le view/CLI dedicate e aprire repo specifici solo se l'indice non basta;
5. aprire repository, docs o codice target solo quando il fatto MegaVault non basta o il task lo richiede;
6. validare con `megavault.py validate` dopo modifiche a schema, dati o viste; se toccano Kuma/Telegram, eseguire anche `operational-index-migrate` e `operational-index-validate`.

Non rileggere file o query gia' verificati nella sessione se lo stato non e' cambiato.

## Aggiornamenti MegaVault

- Non cancellare progetti: archiviarli.
- Non riusare mai un `project_id` o un permanent id.
- Abilitare e rispettare foreign keys.
- Nuovi repository gernalix in scope e non rappresentati vanno registrati prima del PASS, con metadati minimi verificati e senza duplicati.
- `events` e' obbligatorio per lavoro completato su progetti/sistemi Daniele quando serve traccia persistente.
- Markdown consentito in MegaVault: `ai/MEGAVAULT_PROTOCOL.md`, `ai/GLOBAL_INDEX.md`, `legacy/README.md`.
- `legacy/` e' non autorevole e si consulta solo per richiesta storica esplicita.
- Cambi a fatti Kuma/Telegram vanno fatti nelle tabelle canoniche; dopo la modifica rigenerare e validare gli indici operativi.

## Segreti e Bitwarden

- Root canonica segreti: `/home/daniele/.config/codex/secrets`.
- MegaVault conserva solo riferimenti in `secret_refs`, mai valori.
- Accesso ai segreti solo quando richiesto dal task; lettura minima; nessun echo in prompt, comandi, log, report o Git.
- Rotazione solo su richiesta manuale esplicita.
- Per Bitwarden usare `bw`; se bloccato, fermarsi e chiedere sblocco locale. Non acquisire master password, session token o valori segreti in chat.
- Sincronizzare `bw` prima e dopo scritture; verificare nomi campo e presenza allegati, non valori.

## Incidenti e Tag

- Ogni incidente e' una occorrenza osservata, con ID SQLite autoincrementale mai riusato.
- Stesso sintomo/stessa causa in un nuovo momento e' un nuovo incidente.
- `cause` puo' essere `UNKNOWN`; non blocca l'identita'.
- Merge vietato.
- Collegare incidenti solo a tag canonici esistenti o alias; niente free-text.
- Creare un nuovo tag solo se non esiste canonical/alias adatto.

## Regole Daniele Conservate Qui

Usare questa sezione solo quando il task tocca davvero il dominio indicato.

### Python

Usare l'ambiente globale. `venv`, `virtualenv`, `pipenv`, `poetry` e `uv` sono vietati salvo richiesta esplicita dell'utente. Riusa pacchetti globali prima di installare altro.

### Servizi e Host

Verificare live path, mount, unita' systemd e host runtime prima di documentare stato corrente. Usare `systemctl` per unita' di sistema e `systemctl --user` per unita' utente. Evitare autostart duplicati.

### Database

Ispezionare schema/path live prima di query o migrazioni. Per SQLite live/concorrenziale preferire `.backup`; preservare WAL/SHM quando rilevanti.

### Android

- Project docs nel repo proprietario; MegaVault conserva solo regole trasversali.
- `version.txt` e' sorgente unica per versioni Android Daniele quando presente.
- Storage timestamp: UTC `Z`; UI locale dispositivo; test di conversione richiesti quando il task tocca date/ore.
- i18n `en` + `it`; niente testo visibile hardcoded.
- Usare Gradle wrapper del progetto.
- Scoprire emulatori/dispositivi live con `adb devices`; non hardcodare seriali.
- Per emulatori, usare solo seriale live `emulator-*` in stato `device`; avviare emulator solo se il test dispositivo e' richiesto e non ce n'e' uno attivo.
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

## Git Per MegaVault

Per modifiche al repository MegaVault:

- lavorare sul branch canonico corrente salvo richiesta diversa;
- non creare branch per task ordinari;
- se il worktree e' sporco prima delle modifiche, preservare le modifiche non correlate;
- dopo acceptance e validazione richiesta, fare un commit finale e un push finale, salvo divieto esplicito dell'utente.

Per altri repository, seguire l'entrypoint generale e le regole del repository target; usare MegaVault solo per identita'/routing/fatti necessari.

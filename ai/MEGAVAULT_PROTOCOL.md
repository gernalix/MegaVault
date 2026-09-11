# MEGAVAULT_PROTOCOL
VERSION=41
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
- `kuma_monitors`, `kuma_monitor_projects`, `operational_inventory_meta`, `kuma_monitor_index`;
- `telegram_project_capabilities`, `telegram_notification_capability_index`, `telegram_notification_project_index`, `telegram_shared_infrastructure_index`.

Gli indici operativi sono strutturati in SQLite. Le view sono derivate: correggere i dati sorgente, non le view.

### Uptime Kuma

`kuma_monitor_index` rappresenta monitor reali, non la sola istanza/server Kuma. Lo stato di completezza e' in `operational_inventory_meta` con `inventory_key='kuma_monitors'`.

Regole:

- non dichiarare l'indice completo se lo stato non e' `COMPLETE`;
- lo stato corrente dei monitor deve provenire dal DB live/backup recente di Uptime Kuma, non da `events`, vecchi report o Git history;
- `kuma-sync-sqlite` importa solo campi necessari e salva target sanitizzati; token push, query segrete e URL sensibili non vanno salvati;
- ogni monitor corrente deve avere almeno un `project_id` in `kuma_monitor_projects` e una spiegazione non `UNKNOWN` prima di `kuma-finalize`;
- un monitor puo' dipendere da piu' progetti;
- monitor non piu' presenti restano storicizzati con `seen_in_last_sync=0`.

CLI:

```bash
python3 /home/daniele/MegaVault/megavault.py kuma-index
python3 /home/daniele/MegaVault/megavault.py kuma-sync-sqlite --source-db PATH [--integration-id INT0002] [--host-id HOST_ID]
python3 /home/daniele/MegaVault/megavault.py kuma-map --monitor-key KEY --project-id PROJECT_ID
python3 /home/daniele/MegaVault/megavault.py kuma-describe --monitor-key KEY --purpose "..."
python3 /home/daniele/MegaVault/megavault.py kuma-finalize
```

### Telegram

`telegram_notification_project_index` e' l'indice una-riga-per-progetto dei progetti per cui esiste evidenza di capacita' Telegram. L'evidenza deriva da `telegram_project_capabilities`, `integrations`, `services`, `project_components` e `project_operations`.

`telegram_shared_infrastructure_index` contiene helper/integrazioni Telegram globali senza `project_id`. Un helper condiviso non deve essere forzato artificialmente su un progetto. La presenza dell'infrastruttura condivisa, da sola, non significa che tutti i progetti possano inviare notifiche.

CLI:

```bash
python3 /home/daniele/MegaVault/megavault.py telegram-index
python3 /home/daniele/MegaVault/megavault.py telegram-index --project-id PROJECT_ID
```

## CLI Generale

```bash
python3 /home/daniele/MegaVault/megavault.py project-list
python3 /home/daniele/MegaVault/megavault.py project-work-queue
python3 /home/daniele/MegaVault/megavault.py project-show PROJECT_ID
python3 /home/daniele/MegaVault/megavault.py project-path PROJECT_ID
python3 /home/daniele/MegaVault/megavault.py project-path --status PROJECT_ID
python3 /home/daniele/MegaVault/megavault.py operational-index-migrate
python3 /home/daniele/MegaVault/megavault.py operational-index-validate
python3 /home/daniele/MegaVault/megavault.py validate
```

`project-path` stampa solo il worktree canonico e fallisce se assente o ambiguo. `project-path --status` stampa un solo token: `LOCAL`, `REMOTE_ONLY`, `MISSING`, `ARCHIVED` o `ABSENT`.

## Lettura Operativa

Per task MegaVault:

1. leggere questo file;
2. leggere solo la parte pertinente di `ai/GLOBAL_INDEX.md` se serve routing compatto;
3. interrogare `megavault.sqlite` per i fatti richiesti;
4. per Kuma o Telegram usare prima gli indici/CLI dedicati;
5. aprire repository, docs o codice target solo quando il fatto MegaVault non basta o il task lo richiede;
6. validare con `megavault.py validate` dopo modifiche a schema/dati; per Kuma/Telegram eseguire anche `operational-index-migrate` e `operational-index-validate`.

Non rileggere file o query gia' verificati nella sessione se lo stato non e' cambiato.

## Aggiornamenti MegaVault

- Non cancellare progetti: archiviarli.
- Non riusare mai un `project_id` o un permanent id.
- Abilitare e rispettare foreign keys.
- Nuovi repository gernalix in scope e non rappresentati vanno registrati prima del PASS, con metadati minimi verificati e senza duplicati.
- `events` e' obbligatorio per lavoro completato su progetti/sistemi Daniele quando serve traccia persistente.
- Markdown consentito in MegaVault: `ai/MEGAVAULT_PROTOCOL.md`, `ai/GLOBAL_INDEX.md`, `ai/personalhubdoc.md`, `legacy/README.md`.
- `legacy/` e' non autorevole e si consulta solo per richiesta storica esplicita.

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

## Machine semantic contract

Questi marker sono il contratto machine-readable verificato da `megavault.py validate`; non sostituiscono le spiegazioni sopra.

```text
CAPSULIZATION=mandatory_all_projects
CAPSULE_TARGET=progressive
NEW_CODE=capsule_only
SHARED_LOGIC=capsule_only
UI_DIRECT_DEPENDENCY=forbidden
CROSS_MODULE_ACCESS=through_capsules_only
LEGACY_REFACTOR=reduce_when_benefit_exceeds_cost_risk
LEGACY_RESIDUALS=document_and_verify
FINAL_GATE=verify_capsule_first_boundaries_and_documented_residuals_before_final
PYTHON:
env=global
isolation=forbidden
tools=venv|virtualenv|pipenv|poetry|uv
override=user_explicit_request
packages=reuse_global>install_global
venv_without_override=protocol_violation
model=trunk_based_single_developer;operative_branches=1
direct_canonical_work=default
per_task_branch=forbidden
branch_chaining=forbidden
commit_push_before_final=required_unless_user_explicitly_forbids
final_branch_fields=repository,canonical_branch,current_branch,temp_branch_reason,integration_status,cleanup_status
secret_values=never_store;reference_paths_only
SECRETS:
values=never_store_in_MegaVault_or_Git
secrets=follow_SECRETS_section
secret_handling=read_only_when_task_requires;canonical_root_first;canonical_paths_from_database;reprompt_for_known_path_forbidden;rotation_manual_explicit_only
project_id_source=megavault.sqlite:projects+project_aliases_only;INTEGER_PRIMARY_KEY
project_lifecycle=never_delete_project;archive_only;never_reuse_project_id;ids_unique_permanent_not_dense
duplicate_truth=forbidden
forbidden=reports_done,human_mirror,project_docs_in_MegaVault,generated_timeline_markdown,duplicate_registries
project_docs=owner_repo_docs_code_tests;MegaVault_only_global_transversal_knowledge
identity=one_observed_occurrence
id=SQLite_AUTOINCREMENT;immediate;unique;never_reused
same_symptom_same_cause_new_time=new_incident
cause=nullable;UNKNOWN_allowed;does_not_affect_id
merge=forbidden
linking=canonical_tags_only
source=megavault.sqlite:tags+tag_aliases
reuse_existing=mandatory
free_text=forbidden
new_tag=only_if_no_canonical_or_alias_match
format=lowercase_atomic
aliases=search_only;canonical_link_only
incident_search=tag_intersection+text
final_fields=files_changed,tests,test_result,docs_or_MegaVault_updates,repo_status,commit,push,sync_state,branch_fields,execution_insights,blockers,optimization_opportunities,remaining_unresolved
blockers=root_cause,impact,workaround,resolution,status;silent_workaround_retry_skip=forbidden
optimization=root_cause,impact,estimated_future_savings,one_time_fix,priority,confidence,status;section=mandatory
success_forbid=silent_failure,false_success,unverified_PASS
required_for=android_projects,android_builds,android_releases,android_tooling
version=version.txt_integer_monotonic;derive_versionCode_versionName_apk_name;home_v_visible;skip_reuse_forbidden
saf_sqlite=autoexport_all_app_data_on_db_change;atomic;validate_after_write;failure_visible;preserve_last_good;test_required
i18n=en+it;no_hardcoded_user_visible_text;missing_translation_blocker
```

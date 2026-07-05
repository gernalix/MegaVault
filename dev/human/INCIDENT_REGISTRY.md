# Incident Registry

Ogni progetto MegaVault deve avere un registro incidenti leggibile da AI e persone, piu' un archivio SQLite aggiornato automaticamente da monitor, healthcheck o tool operativi.

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

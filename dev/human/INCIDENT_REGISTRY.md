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

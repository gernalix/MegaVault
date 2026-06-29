# Intervention Report 2026-06-29

Root cause: crescita non bounded di `watcher_comment_diagnostics`.

Misure principali:
- DB prima `6576418816` byte; WAL `10683192`.
- `watcher_comment_diagnostics` `6573776896` byte.
- Righe diagnostiche `14693332`.
- DB dopo `2351104` byte; WAL `0`; diagnostiche `102`.

Azioni:
- Fermato timer durante intervento.
- Creato backup SQLite, compresso con zstd e testato.
- Implementato filtro diagnostico utile-only.
- Implementato upsert per `candidate_hash`.
- Implementato tool manutenzione.
- Eseguita compaction filtrata e `integrity_check`.
- Eseguito run reale post-fix: 1358 candidati, 102 diagnostiche upsertate, conteggio finale stabile a 102.
- Riattivato timer e riavviato Datasette.

Rischi residui:
- Backup manuale da 161 MiB da mantenere o rimuovere secondo policy futura.
- Nessuna CI remota ancora configurata.

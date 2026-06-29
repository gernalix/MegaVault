# Bug History

## 2026-06-29 DB 6.2 GiB

Sintomo: `/home/ubuntu/db/strano_anello.db` era `6576418816` byte.

Causa: `watcher_comment_diagnostics` inseriva ogni candidato commento a ogni run. Il timer reale girava ogni 10 minuti; ogni run produceva 1358 candidati, quasi tutti ripetuti.

Prova: `dbstat` ha misurato `watcher_comment_diagnostics=6573776896` byte; `sqlite_sequence=14693332`; campione ultimi run con 1358 hash ripetuti.

Fix: persistenza diagnostica solo per segnali utili, upsert per `candidate_hash`, retention, compact filtrato.

# Architecture

`strano_anello.py` e' un watcher oneshot avviato da `strano-anello.timer` ogni 10 minuti.

Flusso: WordPress API produce post normalizzati; HTML dei post produce candidati commento; `apply_snapshots` confronta lo stato esistente e aggiorna `watcher_posts`, `watcher_comments`, `watcher_events`.

La diagnostica commenti e' separata dai dati utente: salva solo candidati scartati, warning o bassa confidenza, con upsert su `candidate_hash`.

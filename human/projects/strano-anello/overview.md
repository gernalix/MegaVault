# Strano Anello

Watcher Python per `lostranoanello.wordpress.com`: legge post e commenti, mantiene uno stato SQLite corrente e invia notifiche Telegram quando rileva inserimenti, modifiche o cancellazioni.

Link operativi: [AI doc](../../../ai/projects/strano-anello.md), [metadata](https://github.com/gernalix/strano-anello/blob/main/dev/project.metadata.json), [repo](https://github.com/gernalix/strano-anello), legacy: non presente.

Stato 2026-06-29: DB ridotto da `6576418816` byte a `2351104` byte. Root cause corretta nel codice: la diagnostica commenti non viene piu' salvata per ogni candidato pulito a ogni run.

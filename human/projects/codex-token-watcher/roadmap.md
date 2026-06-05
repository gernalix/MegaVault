# codex-token-watcher Roadmap

## Segnali dal codice
- Runtime locale contiene lo script reale; VM Oracle e' solo endpoint Kuma.
- Parser v3 copre il layout Analytics nuovo indicato dallo screenshot.
- SQLite/CSV/state/diagnostica sono fuori repo.

## Debito/rischi da considerare
- Risolvere/verificare login o challenge Cloudflare nel profilo Chrome locale dedicato.
- Salvare fixture raw di una lettura live riuscita dopo login.
- Valutare riduzione timeout se Cloudflare continua a causare cicli lunghi.

# mint-manual-updates Roadmap

## Segnali dal codice
- no tests detected by static scan
- data/storage rules absent from active code
- prompt #482917 aggiunge modalità venv; mantenere test smoke per report-only e discovery

## Debito/rischi da considerare
- systemd/user/mint-extra-updater.service:12:TimeoutStartSec=7200
- systemd/user/mint-manual-updates.service:12:TimeoutStartSec=7200
- upgrade venv può rompere dipendenze progetto-specifiche; default resta report-only

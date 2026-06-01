# mint-manual-updates Roadmap

## Segnali dal codice
- no tests detected by static scan
- data/storage rules absent from active code

## Debito/rischi da considerare
- systemd/user/mint-extra-updater.service:12:TimeoutStartSec=7200
- systemd/user/mint-manual-updates.service:12:TimeoutStartSec=7200

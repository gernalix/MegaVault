# mint-manual-updates Roadmap

## Stato attuale

- `#618472`: consolidamento completato.
- Comando ufficiale unico: `bin/mint-manual-updates --run`.
- Nessun secondo script/service/timer updater nel repo.

## Debito/rischi da considerare

- `systemd/user/mint-manual-updates.service:12:TimeoutStartSec=7200`
- Upgrade venv può rompere dipendenze progetto-specifiche; mantenere log per venv e continuazione su fallimento.
- Android SDK/Studio possono essere lenti e pesanti; mantenere timeout, storico e backup.
- Android Studio archive e grande; mantenere precheck metadata e skip sicuro prima di ogni download.
- `rsync`, load alto e PSI CPU alta sono consentiti durante il run; se emergono freeze reali, regolare i blocker critici memoria/swap/PSI memoria/PSI I/O invece di rimettere `rsync` tra i blocker.

## Prossimo vincolo

- Ogni nuova funzione deve entrare nel comando unico o essere rifiutata; non creare nuovi updater paralleli.

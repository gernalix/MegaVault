# mint-manual-updates Features

## Comando unico

- `bin/mint-manual-updates --run`: unico comando ufficiale supportato.
- `bin/mint-manual-updates --dry-run`: validazione report-only, non comando operativo alternativo.

## Funzioni consolidate

- Sistema: apt update, apt upgrade sicuro, apt full-upgrade sicuro, fwupd, flatpak, snap se disponibile.
- Python globale: solo `pip3 list --outdated`; niente `sudo pip`, pip globale o pip3 globale per update di sistema.
- Venv: discovery sotto `/home/daniele/codex-workspace`, report outdated, upgrade `pip setuptools wheel`, upgrade pacchetti outdated, log per venv, continuazione su fallimento.
- Tool sviluppo: `yt-dlp`, `pipx upgrade-all`, `rustup update`, `npm update -g`.
- Report-only: Ruby gems e Cargo installed crates.
- Android: Android Studio da archivio Linux ufficiale con SHA-256; Android SDK via `sdkmanager --list`, licenze, `sdkmanager --update`, storico CSV/SQLite.

## Confini operativi

- Script rimosso: `removed duplicate script`.
- Service rimosso: `removed duplicate service`.
- Timer rimosso: `removed duplicate timer`.
- Service attivo: `systemd/user/mint-manual-updates.service`.
- Timer attivo: `systemd/user/mint-manual-updates.timer`.
- Stato unico: `~/.local/state/mint-manual-updates/`.

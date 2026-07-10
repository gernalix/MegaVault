# Log live delle sessioni Codex

Il comando quotidiano resta `codex`. Nelle shell Bash interattive viene avviato in tmux e tutto l’output è salvato in tempo reale sotto `~/.local/state/codex-session-logger/sessions/`, senza interrompere Codex.

Comandi principali:

```bash
codex
codex-last
codex-tail
codex-open
codex-obsidian
codex-code                 # richiede VS Code installato
codex-log latest
codex-export
```

`screen.txt` è la vista più leggibile, `transcript.log` è adatto a `tail -F`, `terminal.raw` conserva il flusso terminale completo. `Ctrl-b d` stacca tmux lasciando Codex attivo; `tmux attach` rientra. Per diagnosi e limiti vedere [la guida AI](../../ai/global/CODEX_SESSION_LOGGING.md).

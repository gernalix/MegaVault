# mint-freeze-forensics

Prompt `#847261`.

Soluzione nuova: forensics, early warning e telemetria storica. Non riavvia, non restarta servizi, non killa processi e non modifica tuning del sistema operativo.

Percorsi:

- repo: `/home/daniele/codex-workspace/mint-freeze-forensics`
- stato: `~/.local/state/mint-freeze-forensics/`
- config: `~/.config/mint-freeze-forensics/`
- CLI: `~/.local/bin/mint-freeze-forensics`
- AI doc: `MegaVault/ai/projects/mint-freeze-forensics.md`

Servizi:

- `mint-freeze-forensics.service`: sampler ogni 5 secondi.
- `mint-resource-guardian.timer`: early warning non distruttivo.
- `mint-resource-guardian.service`: check non interattivo per systemd; il prompt `[K] [I] [W] [D]` resta disponibile via CLI manuale.

Comandi:

```bash
mint-freeze-forensics status
mint-freeze-forensics human-report
mint-freeze-forensics guardian --once
systemctl --user status mint-freeze-forensics.service --no-pager
```

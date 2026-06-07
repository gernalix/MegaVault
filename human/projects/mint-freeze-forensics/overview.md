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
mint-freeze-forensics recent
mint-freeze-forensics weekly-report
mint-freeze-forensics dashboard-json
mint-freeze-forensics historical-validation
mint-freeze-forensics guardian --once
systemctl --user status mint-freeze-forensics.service --no-pager
```

Novità operative:

- `recent`: timeline ordinata con freeze gap, interruzioni boot, PSI/memoria/I/O critici e guardian alert.
- `weekly-report`: aggregato 7 giorni con durata media, freeze più lungo, processo/pattern ricorrente e medie PSI.
- `dashboard-json`: sorgente stabile letta dalla Linux Mint Service Dashboard, senza duplicare logica.
- `UNEXPECTED_INTERRUPTION`: registrato quando il boot cambia e l’ultimo heartbeat è oltre soglia.
- simulazioni `simulate-gap` e `simulate-interruption`: marcate `simulation=true`, visibili in timeline ma escluse dai conteggi reali.

Kuma:

- Status page: `http://150.230.148.128:3001/status/mint-freeze-analysis`
- Monitor: `Freeze Gaps`, `PSI Memory`, `PSI IO`, `Guardian Alerts`, `Forensics Alive`.
- Messaggi push includono `freeze_count_24h`, `freeze_count_7d`, `guardian_alert_count_24h`, `guardian_alert_count_7d`.
- Solo telemetria/alerting; nessuna remediation.

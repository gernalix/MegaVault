# mint-freeze-forensics

Prompt `#847261`; ultimo intervento `#746182`.

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
mint-freeze-forensics io-report
mint-freeze-forensics freeze-root-cause
mint-freeze-forensics historical-validation
mint-freeze-forensics guardian --once
systemctl --user status mint-freeze-forensics.service --no-pager
```

Novità operative:

- `recent`: timeline ordinata con freeze gap, interruzioni boot, PSI/memoria/I/O critici e guardian alert.
- `weekly-report`: aggregato 7 giorni con durata media, freeze più lungo, processo/pattern ricorrente e medie PSI.
- `dashboard-json`: sorgente stabile letta dalla Linux Mint Service Dashboard, senza duplicare logica.
- `io-report`: report specifico per freeze con PSI I/O alta, swap/root su Samsung T7 e processi che leggono/scrivono troppo.
- `freeze-root-cause`: report forense sui freeze recenti con timeline, PSI/RAM/swap pre-freeze, processi coinvolti e classificazione automatica.
- `UNEXPECTED_INTERRUPTION`: registrato quando il boot cambia e l’ultimo heartbeat è oltre soglia.
- simulazioni `simulate-gap` e `simulate-interruption`: marcate `simulation=true`, visibili in timeline ma escluse dai conteggi reali.

Kuma:

- Status page: non piu pubblica dal prompt `#458217`; usare il tunnel admin Kuma e poi `http://127.0.0.1:3001/status/mint-freeze-analysis`.
- Monitor: `Freeze Gaps`, `PSI Memory`, `PSI IO`, `Guardian Alerts`, `Forensics Alive`.
- Messaggi push includono `freeze_count_24h`, `freeze_count_7d`, `guardian_alert_count_24h`, `guardian_alert_count_7d`.
- Dalla versione 1.4.0 `Freeze Gaps` e `Guardian Alerts` restano verdi se l'heartbeat arriva: i conteggi non-zero sono telemetria, non stato down.
- Il falso rosso del prompt `#746182` era causato dall'invio di `status=down` quando esistevano freeze/guardian alert, più un intervallo locale 60s uguale all'intervallo Kuma.
- Il push locale predefinito è ora 30s.
- Solo telemetria/alerting; nessuna remediation.

Storage/I/O:

- Dalla versione 1.2.0 i sample registrano root device, swap backing device, filesystem, info `/sys/block` e `lsblk` compatto.
- Se root o swap sembrano stare su Samsung Portable T7 USB, il report lo indica esplicitamente.
- I futuri freeze avranno delta read/write per processo e major page faults; i freeze precedenti restano leggibili ma spesso solo con I/O cumulativo.

Adaptive capture:

- Dalla versione 1.3.0 il servizio resta leggero in modalità normale.
- Se PSI memory o PSI I/O arriva a 90, oppure se viene rilevato un freeze gap, apre una finestra di cattura di massimo 120 secondi.
- In quella finestra campiona più spesso e forza delta read/write, major faults, stato T7 e keyword kernel storage/USB.
- Finita la finestra torna automaticamente alla modalità normale.

Telemetria freeze avanzata:

- Dalla versione 1.4.0 i sample registrano campi memoria estesi, PSI memory/I/O/CPU, delta swap/page fault/reclaim da `/proc/vmstat` e dettagli mirati su Firefox/Codex.
- Quando i segnali pre-freeze superano soglia, salva snapshot JSON sotto `~/.local/state/mint-freeze-forensics/pre-freeze-capture/`.

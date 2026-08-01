# linux-mint-service-dashboard Overview

Dashboard locale read-only per i servizi operativi importanti di questo host Linux Mint/XFCE.

## Stato e codice
- Repository: `/home/daniele/codex-workspace/linux-mint-service-dashboard`
- Branch/commit verificati: `prompt-816-local-dashboard` / `487ca7e`
- File codice/config/test/script analizzati: 11 su 11
- Stack rilevato: JS/TS, Python, Playwright, UNKNOWN

## Orientamento rapido
- Entrypoint: `app/server.py`
- Core/data: `app/__init__.py,app/collectors.py,dev/project.metadata.json`
- Test: `tests/playwright-smoke.js,tests/test_dashboard.py`
- Script/build: `UNKNOWN`

## Freeze / Rallentamenti
- Tab aggiunta: `Freeze / Rallentamenti`.
- Fonte dati: `mint-freeze-forensics dashboard-json`.
- Mostra: stato umano, ultimo freeze, riepilogo 24h, riepilogo 7d, spiegazione, azioni consigliate e comandi diagnostici copiabili.
- Sicurezza: nessun kill, restart o remediation dalla dashboard.
- Polling UI: 30s, senza refresh concorrenti.
- Test: `python3 -m unittest tests/test_dashboard.py`; `DASHBOARD_URL=http://127.0.0.1:8881/ node tests/playwright-smoke.js`.

## Link
- AI doc: AI doc (`../../../ai/projects/linux-mint-service-dashboard.md`; status=UNKNOWN)
- Metadata: dev/project.metadata.json (`../../../../linux-mint-service-dashboard/dev/project.metadata.json`; status=UNKNOWN)
- Legacy docs: dev/legacy (`../../../../linux-mint-service-dashboard/dev/legacy`; status=UNKNOWN)
- Repository: repo path (`../../../../linux-mint-service-dashboard`; status=UNKNOWN)

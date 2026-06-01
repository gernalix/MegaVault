# linux-mint-service-dashboard Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/legacy/README.md: # Linux Mint Service Dashboard
- dev/legacy/README.md: Dashboard locale read-only per i servizi operativi importanti di questo host Linux Mint/XFCE.
- dev/legacy/dev/neodocs/INDEX.neodoc: project=linux-mint-service-dashboard
- dev/legacy/dev/neodocs/METRICS.neodoc: common=service_state,timer_state,next_run,last_trigger,last_result,pid,log_tail,path_log,last_success,last_error,data_age,recent_events
- dev/legacy/dev/neodocs/PROJECT.neodoc: name=linux-mint-service-dashboard
- dev/legacy/dev/neodocs/SERVICES.neodoc: required=amici_fb,cloud-backup,disk-usage-monitor,mint-heartbeat,mint-home-backup,mint-home-backup-retention,os-observer-autofix,parcel-tracker,rsync-transfer
- dev/legacy/dev/neodocs/SYSTEMD.neodoc: user_service=system-service-dashboard.service
- dev/legacy/dev/neodocs/TESTS.neodoc: commands=python3 -m unittest discover -s tests/python3 -m py_compile app/server.py app/collectors.py/node tests/playwright-smoke.js/./scripts/dashboardctl status/./scripts/dashboardctl healthcheck
- dev/legacy/docs/ARCHITECTURE_HUMAN.md: La dashboard espone un server HTTP locale Python su `127.0.0.1:8788`.
- app/__init__.py: """Linux Mint service dashboard package."""
- app/collectors.py: from __future__ import annotations
- app/server.py: from __future__ import annotations
- tests/test_dashboard.py: from __future__ import annotations
- tests/playwright-smoke.js: const { chromium } = require("playwright");

## Useful Limits And Boundaries
- dev/legacy/README.md: Dashboard locale read-only per i servizi operativi importanti di questo host Linux Mint/XFCE.
- dev/legacy/README.md: - `mint-home-backup`: stato snapshot, fase, retention, seed-critical, guardrail, spazio libero, eventi systemd.
- dev/legacy/README.md: - `cloud backup`: stato restic dal dashboard locale esistente, snapshot, lock, throughput, ETA e timer.
- dev/legacy/README.md: - job/timer: `amici_fb`, `parcel-tracker`, `disk-usage-monitor`, `mint-heartbeat`, `mint-home-backup-retention`.
- dev/legacy/README.md: - `mint-home-backup` non mostra ETA quando il sorgente non lo espone in modo affidabile.
- dev/legacy/README.md: - `cloud backup` non legge direttamente file root-only: usa l'endpoint locale sanificato e spiega i campi non esposti.
- dev/legacy/README.md: - Il cloud backup viene letto tramite `http://127.0.0.1:8765/api/status`; se quel servizio è down, la tab degrada ai soli dati systemd.
- dev/legacy/README.md: - La dashboard non usa privilegi root e non legge direttamente file root-only quando esiste un endpoint locale già sanificato.
- dev/legacy/dev/neodocs/SERVICES.neodoc: required=amici_fb,cloud-backup,disk-usage-monitor,mint-heartbeat,mint-home-backup,mint-home-backup-retention,os-observer-autofix,parcel-tracker,rsync-transfer
- dev/legacy/dev/neodocs/SERVICES.neodoc: user_units=amici_fb.service,amici_fb.timer,home-incremental-backup.service,home-incremental-backup.timer,home-backup-retention-kuma-push.service,home-backup-retention-kuma-push.timer,os-observer-autofix-agent.service,os-
- dev/legacy/dev/neodocs/SERVICES.neodoc: system_units=mint-cloud-backup.service,mint-cloud-backup.timer,mint-cloud-backup-monitor.service,mint-cloud-backup-dashboard.service,mint-cloud-backup-kuma-push.service,mint-cloud-backup-kuma-push.timer,disk-usage-monito
- dev/legacy/dev/neodocs/SERVICES.neodoc: implemented_tabs=overview,dashboard,rsync-transfer,mint-home-backup,cloud-backup,os-observer-autofix,amici_fb,parcel-tracker,disk-usage-monitor,mint-heartbeat,mint-home-backup-retention

## Where The Feature Code Appears To Live
- `app/server.py`
- `app/__init__.py`
- `app/collectors.py`
- `scripts/dashboard-healthcheck`
- `scripts/dashboardctl`
- `scripts/open-dashboard`
- `tests/test_dashboard.py`

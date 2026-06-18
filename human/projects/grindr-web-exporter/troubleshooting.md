# Troubleshooting

## Sessione Grindr assente

Esegui:

```bash
cd /home/daniele/codex-workspace/grindr-web-exporter
. .venv/bin/activate
grindr-export --profile-mode persistent-copy --pause-for-login setup-check
```

Fai login nella finestra browser Playwright, poi premi Invio nel terminale. Non digitare credenziali nel terminale.

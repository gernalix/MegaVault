# chatgpt-chrome-debug Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/legacy/README.md: # ChatGPT Chrome Redirect Debug Toolkit
- dev/legacy/QUICK_FIXES.md: # Quick Fixes
- dev/legacy/ROOT_CAUSE_ANALYSIS.md: Stato: toolkit preparato, snapshot raccolto e logger passivo abilitato come servizio utente. La root cause definitiva richiede un redirect osservato mentre il monitor tab e' attivo su una conversazione `/c/...`.

## Useful Limits And Boundaries
- dev/legacy/README.md: - ogni script e' restart-safe e puo' appendere a log esistenti.
- dev/legacy/QUICK_FIXES.md: - Fare backup del profilo.
- dev/legacy/ROOT_CAUSE_ANALYSIS.md: - Fix temporaneo: usare profilo Chrome isolato pulito o rimuovere solo dati sito OpenAI/ChatGPT dopo backup.
- package.json: "version": "0.1.0",

## Where The Feature Code Appears To Live
- `package.json`
- `START_DEBUGGING.sh`
- `scripts/common.sh`
- `scripts/dashboard.sh`
- `scripts/install_user_services.sh`
- `scripts/live_chrome_logger.sh`
- `scripts/run_differential_tests.sh`
- `scripts/snapshot_environment.sh`
- `scripts/stress_memory.py`

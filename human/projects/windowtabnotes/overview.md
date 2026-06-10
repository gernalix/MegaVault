# WindowTabNotes Overview

Root repository: `WindowTabNotes/`.

## Stato e codice
- Repository: `/home/daniele/codex-workspace/WindowTabNotes`
- Branch/commit verificati: `codex/prompt-581472` / `19979db`
- Branch MegaVault operativo: `codex/prompt-731845-kuma-operational-runbook`
- Versione corrente: `v23`
- Servizio utente: `windowtabnotes.service`, installato in `~/.config/systemd/user/windowtabnotes.service`
- Stato servizio verificato `2026-06-07T09:02:18+02:00`: `enabled`, `active`, `Linger=yes`, `Restart=always`, `RestartSec=5`
- ExecStart verificato: `/home/daniele/codex-workspace/WindowTabNotes/system/bin/windowtabnotes daemon`
- WorkingDirectory verificata: `/home/daniele/codex-workspace/WindowTabNotes`
- DB note: `~/.local/share/windowtabnotes/windowtabnotes.sqlite3`, schema `5`
- Stack rilevato: Python, JavaScript MV3, Shell, SQLite, systemd user, GTK/X11, Chrome Native Messaging, Firefox Native Messaging

## Orientamento rapido
- Entrypoint: `system/bin/windowtabnotes`, `browser-extension/manifest.json`, `browser-extension-firefox/manifest.json`
- Stato/diagnostica: `system/bin/windowtabnotes-status --json`
- Status systemd: `systemctl --user status windowtabnotes.service --no-pager`
- Log systemd: `journalctl --user -u windowtabnotes.service -n 80 --no-pager`
- Restart: `systemctl --user restart windowtabnotes.service`
- Probe UI non distruttivi: `system/bin/windowtabnotes dashboard-debug`, `system/bin/windowtabnotes search-debug WindowTabNotes`, `system/bin/windowtabnotes overlay-debug`
- Core/data: `system/windowtabnotes/db.py`, `system/windowtabnotes/active_watch.py`, `system/windowtabnotes/api.py`
- Browser bridge: `browser-extension/service_worker.js`, `system/bin/windowtabnotes-native-host`
- Test: `PYTHONPATH=system python3 -m unittest tests/test_context_persistence.py`
- Script/install Chrome: `system/scripts/install.sh --extension-id <chrome_extension_id>`
- Script/install Firefox: `system/scripts/install-firefox.sh` poi caricare `browser-extension-firefox/manifest.json` da `about:debugging#/runtime/this-firefox`
- Firefox Developer Edition persistente: `/home/daniele/.local/bin/firefox-developer-edition-windowtabnotes` con profilo reale `/home/daniele/.config/mozilla/firefox/98228g06.dev-edition-default`
- Install/verifica Developer Edition: `system/scripts/install-firefox-developer-edition.sh`
- Proof Developer Edition: `WTN_FIREFOX_BINARY=/home/daniele/.local/bin/firefox-developer-edition-windowtabnotes WTN_FIREFOX_PROFILE=/home/daniele/.config/mozilla/firefox/98228g06.dev-edition-default system/bin/windowtabnotes firefox-proof --json`
- Test E2E persistente: `WTN_FIREFOX_BINARY=/home/daniele/.local/opt/firefox-developer-edition/firefox WTN_FIREFOX_PROFILE=/home/daniele/.config/mozilla/firefox/98228g06.dev-edition-default WTN_FIREFOX_ADDON_TEMPORARY=0 WTN_FIREFOX_TEST_SECONDS=120 system/scripts/test-firefox-extension.sh`

## Chrome vs Firefox
- Chrome/Chromium: manifest in `browser-extension/`, background MV3 `service_worker`, native host con `allowed_origins` e ID unpacked Chrome.
- Firefox: manifest in `browser-extension-firefox/`, codice comune linkato da `browser-extension/`, background `scripts`, ID Gecko `windowtabnotes@local`, native host in `~/.mozilla/native-messaging-hosts/com.windowtabnotes.host.json` con `allowed_extensions`.
- Firefox Developer Edition: l'estensione `windowtabnotes@local` e installata permanentemente nel profilo reale `98228g06.dev-edition-default` come `app-profile`, con `xpinstall.signatures.required=false`; Firefox standard resta separato.
- Prova visuale: `/tmp/windowtabnotes-firefox-addons-proof.png` mostra `WindowTabNotes` visibile e abilitata in `about:addons` del Firefox Developer Edition reale. Il warning unsigned e atteso in questa configurazione Developer Edition.
- Verifica Chrome: `system/bin/windowtabnotes native-debug --extension-id <chrome_extension_id> --json`
- Verifica Firefox: `system/bin/windowtabnotes native-debug --browser firefox --firefox-extension-id windowtabnotes@local --json`

## Link
- AI doc: [AI doc](../../../ai/projects/windowtabnotes.md)
- Metadata: [dev/project.metadata.json](../../../../WindowTabNotes/dev/project.metadata.json)
- Legacy docs: [dev/legacy](../../../../WindowTabNotes/dev/legacy)
- Repository: [repo path](../../../../WindowTabNotes)

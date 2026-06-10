# WindowTabNotes Troubleshooting

## Browser bridge Chrome/Firefox
- Installazione Chrome: `system/scripts/install.sh --extension-id <chrome_extension_id>`, poi ricaricare `browser-extension/` in `chrome://extensions`.
- Installazione Firefox: `system/scripts/install-firefox.sh`, poi aprire `about:debugging#/runtime/this-firefox` e caricare `browser-extension-firefox/manifest.json`.
- Verifica Chrome: `system/bin/windowtabnotes native-debug --extension-id <chrome_extension_id> --json`.
- Verifica Firefox: `system/bin/windowtabnotes native-debug --browser firefox --firefox-extension-id windowtabnotes@local --json`.
- Stato Firefox reale: `system/bin/windowtabnotes firefox-status --json`.
- Smoke Firefox reale: `system/scripts/test-firefox-extension.sh`.
- Lo smoke Firefox usa Selenium/WebDriver con add-on temporaneo: installa `windowtabnotes@local`, apre tre tab reali, passa tra le tab e controlla native metrics, DB e overlay. Il test non richiede install permanente nel profilo Firefox release.
- Se `pipx` e disponibile, lo smoke usa `pipx run --spec selenium` e puo scaricare Selenium/driver alla prima esecuzione; altrimenti serve un Python con Selenium funzionante.
- Stato globale: `system/bin/windowtabnotes-status --json` oppure `system/bin/windowtabnotes check --json`.

## Servizio systemd --user
- Unit file: `~/.config/systemd/user/windowtabnotes.service`.
- ExecStart: `/home/daniele/codex-workspace/WindowTabNotes/system/bin/windowtabnotes daemon`.
- WorkingDirectory: `/home/daniele/codex-workspace/WindowTabNotes`.
- Stato: `systemctl --user status windowtabnotes.service --no-pager`.
- Log: `journalctl --user -u windowtabnotes.service -n 80 --no-pager`.
- Riavvio: `systemctl --user restart windowtabnotes.service`.
- Persistenza: `systemctl --user is-enabled windowtabnotes.service` deve essere `enabled`; `loginctl show-user daniele -p Linger` deve essere `Linger=yes`.
- Crash test #739284: SIGTERM su `MainPID` ha prodotto nuovo `MainPID` e `NRestarts=1` con stato `active`.
- Nota: `system/bin/windowtabnotes check --json` puo riportare `window_sync: skipped: database is locked` durante attivita del daemon; se `database: ok` e `windowtabnotes-status --json` e ok, il DB non va resettato.

## Se le note browser non compaiono
- Controllare che `system/bin/windowtabnotes status --json` riporti DB ok, servizio attivo e `chrome_bridge`/`firefox_bridge` configurato secondo il browser usato.
- Chrome: il manifest native deve esistere sotto `~/.config/google-chrome/NativeMessagingHosts/` o `~/.config/chromium/NativeMessagingHosts/` e contenere `allowed_origins`.
- Firefox: il manifest native deve esistere in `~/.mozilla/native-messaging-hosts/com.windowtabnotes.host.json` e contenere `allowed_extensions: ["windowtabnotes@local"]`.
- Firefox attuale su Mint usa profili sotto `~/.config/mozilla/firefox/`; `firefox-status --json` deve mostrare il profilo attivo e se `windowtabnotes@local` e caricato in `extensions.json`.
- Se `firefox-status` mostra `extension_uuid_exists_but_addon_not_loaded` o `temporary_addon_path_seen_but_not_loaded`, il profilo conserva stato di un temporaneo precedente ma l'add-on non e caricato: ricaricare il manifest temporaneo da `browser-extension-firefox/manifest.json`.
- Durante i test automatici e normale vedere `location: webdriver-temporary-runtime` o `web-ext-temporary-runtime`: indica che l'add-on unsigned e stato caricato temporaneamente per verifica reale.
- Le tab Firefox usano `profileKey` `firefox:default` e id interni negativi nei report DB. E intenzionale: evita collisioni con Chrome e con vecchie righe che usavano id tab positivi piccoli.
- `browser-extension-firefox/` deve essere self-contained. I symlink verso `browser-extension/` fanno fallire `web-ext lint`/packaging con file background/content/icon mancanti.
- Se il popup dice host non pronto, rieseguire il comando `native-debug ... --fix`, ricaricare l'estensione nel browser e riprovare su una pagina `http`, `https` o `file`.
- Firefox Snap/Flatpak puo non vedere il manifest o il binario host del filesystem host; usare Firefox non confinato o verificare i permessi del portale native messaging.
- Firefox standard non installa permanentemente estensioni locali non firmate; per permanenza serve pacchetto firmato oppure Developer/Nightly/ESR con policy/firma gestita.

## Problemi e sintomi rilevati nel codice
- system/windowtabnotes/cli.py:9:from .active_watch import active_note_for_current_context, active_window_watch_debug, sync_open_windows
- system/windowtabnotes/cli.py:12:from .gtk_ui import dashboard_debug, open_dashboard, open_note_window, overlay_debug
- system/windowtabnotes/cli.py:14:from .native_debug import run_native_debug
- system/windowtabnotes/cli.py:16:from .rofi import install_search_launcher, run_global_search, run_search_launcher, search_debug
- system/windowtabnotes/cli.py:35:overlay_debug_parser = sub.add_parser("overlay-debug")
- system/windowtabnotes/cli.py:36:overlay_debug_parser.add_argument("--fix", action="store_true")
- system/windowtabnotes/cli.py:37:overlay_debug_parser.add_argument("--fix-geometry", action="store_true")
- system/windowtabnotes/cli.py:39:sub.add_parser("active-window-watch-debug")
- browser-extension/dashboard.js:6:const response = await chrome.runtime.sendMessage({ type: "OPEN_DASHBOARD", focusSearch }).catch((error) => ({
- browser-extension/dashboard.js:8:error: String(error),
- browser-extension/dashboard.js:14:statusEl.textContent = response?.error // "Native Messaging host unavailable.";
- browser-extension/popup.js:18:const response = await chrome.runtime.sendMessage({ type: "GET_ACTIVE_TAB_RECORD" }).catch((error) => ({
- browser-extension/popup.js:20:error: String(error),
- browser-extension/popup.js:24:tabInfoEl.textContent = response?.error // "Native Messaging non configurato";
- browser-extension/service_worker.js:10:const NATIVE_FAILURE_BACKOFF_MS = 5000;
- browser-extension/service_worker.js:64:return { ok: false, skipped: true, error: { code: "native_backoff", message: "Native host backoff active." } };
- browser-extension/service_worker.js:68:const code = response?.error?.code // "";
- browser-extension/service_worker.js:70:nativeBackoffUntil = Date.now() + NATIVE_FAILURE_BACKOFF_MS;

## Comandi/verifiche utili trovati
- system/scripts/install.sh:1:#!/usr/bin/env bash
- system/scripts/install.sh:47:sudo apt-get install -y python3 python3-gi gir1.2-gtk-3.0 sqlite3 rofi wmctrl xdotool x11-utils jq
- system/scripts/install.sh:54:python3 - "$CONFIG_DIR/settings.json" "$EXTENSION_ID" <<'PY'
- system/scripts/install.sh:78:systemctl --user daemon-reload // true
- system/scripts/install.sh:79:systemctl --user enable --now windowtabnotes.service // true
- system/scripts/uninstall.sh:1:#!/usr/bin/env bash
- system/scripts/uninstall.sh:5:systemctl --user disable --now windowtabnotes.service 2>/dev/null // true
- system/scripts/uninstall.sh:9:systemctl --user daemon-reload 2>/dev/null // true

## Safety prima di correggere
- browser-extension/content_script.js:13:element.remove();
- browser-extension/focus.js:9:return chrome.tabs.remove(tab.id);
- browser-extension/service_worker.js:135:async function removeOpenTab(tabId) {
- browser-extension/service_worker.js:138:delete snapshot[String(tabId)];
- browser-extension/service_worker.js:259:pendingTabSyncs.delete(key);
- browser-extension/service_worker.js:312:await chrome.tabs.remove(numericTabId);
- browser-extension/service_worker.js:410:chrome.tabs.onRemoved.addListener((tabId) => {
- browser-extension/service_worker.js:411:removeOpenTab(tabId).catch(() => {});
- browser-extension/manifest.json:2:"manifest_version": 3,
- browser-extension/manifest.json:4:"version": "20.0.0",
- browser-extension/manifest.json:5:"version_name": "v20",
- system/windowtabnotes/cli.py:18:from .version import version_label

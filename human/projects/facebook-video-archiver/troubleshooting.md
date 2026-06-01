# facebook-video-archiver Troubleshooting

## Problemi e sintomi rilevati nel codice
- facebook_archive_dashboard.py:38:except OSError:
- facebook_archive_dashboard.py:47:for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
- facebook_archive_dashboard.py:62:lines = path.read_text(encoding="utf-8", errors="ignore").splitlines()
- facebook_archive_dashboard.py:69:except subprocess.CalledProcessError:
- facebook_archive_dashboard.py:89:except OSError:
- facebook_archive_dashboard.py:96:except OSError:
- facebook_archive_dashboard.py:124:if any(token in line.lower() for token in ("warning", "error", "failed", "unsupported", "unable")):
- facebook_archive_dashboard.py:162:"ultimi warning/errori:",
- facebook_session_browser.py:71:for line in path.read_text(encoding="utf-8", errors="ignore").splitlines():
- facebook_session_browser.py:93:except Exception:
- facebook_session_browser.py:100:except Exception as exc:
- facebook_session_browser.py:101:safe_print(f"ERROR: Playwright is not available in this environment: {exc}")
- facebook_session_browser.py:123:await page.goto(args.page_url, wait_until="domcontentloaded", timeout=60000)
- facebook_session_browser.py:147:await page.goto(args.page_url, wait_until="domcontentloaded", timeout=60000)
- facebook_session_browser.py:185:await page.goto(args.page_url, wait_until="domcontentloaded", timeout=60000)
- facebook_session_browser.py:190:await page.wait_for_timeout(int(args.scroll_sleep * 1000))
- facebook_video_archiver.sh:3:set -Eeuo pipefail
- facebook_video_archiver.sh:64:log "ERROR: $*" >&2

## Comandi/verifiche utili trovati
- facebook_video_archiver.sh:2:#!/usr/bin/env bash
- facebook_video_archiver.sh:40:./facebook_video_archiver.sh --version
- facebook_video_archiver.sh:41:./facebook_video_archiver.sh --setup
- facebook_video_archiver.sh:42:./facebook_video_archiver.sh --check
- facebook_video_archiver.sh:43:./facebook_video_archiver.sh --login-browser
- facebook_video_archiver.sh:44:./facebook_video_archiver.sh --check-session
- facebook_video_archiver.sh:45:./facebook_video_archiver.sh --discover-browser
- facebook_video_archiver.sh:46:./facebook_video_archiver.sh --discover-deep

## Safety prima di correggere
- facebook_archive_dashboard.py:124:if any(token in line.lower() for token in ("warning", "error", "failed", "unsupported", "unable")):
- facebook_session_browser.py:5:import http.cookiejar
- facebook_session_browser.py:17:DEFAULT_COOKIE_EXPORT = "~/.config/facebook-video-archiver/facebook-cookies.txt"
- facebook_session_browser.py:133:cookies = await context.cookies("https://www.facebook.com")
- facebook_session_browser.py:134:cookie_names = {cookie.get("name", "") for cookie in cookies}
- facebook_session_browser.py:135:if "c_user" in cookie_names or "xs" in cookie_names:
- facebook_session_browser.py:205:safe_print("Nessun URL trovato. Possibili limiti: cookie/sessione scaduti, checkpoint, rendering Facebook non estraibile, contenuto privato/non auto
- facebook_session_browser.py:339:def cookie_expires(cookie: dict) -> int:
- dev/project.metadata.json:9:"metadata_version": 1,
- facebook_session_browser.py:43:def safe_print(message: str) -> None:
- facebook_session_browser.py:101:safe_print(f"ERROR: Playwright is not available in this environment: {exc}")
- facebook_session_browser.py:102:safe_print("Run: ./facebook_video_archiver.sh --setup")

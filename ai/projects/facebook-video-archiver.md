# facebook-video-archiver AI OPERATIONS

PROJECT
- name: facebook-video-archiver
- slug: facebook-video-archiver
- purpose: Start here for Codex/operator work on `facebook-video-archiver`.
- current_status: Working tree has 14 non-clean entries; do not mix unrelated changes. First entries: M .env.example, M .gitignore, M facebook_video_archiver.sh, M state/discovered_urls.txt, M state/downloaded.txt
- repo_path: `/home/daniele/codex-workspace/facebook-video-archiver`
- remote: `none`
- branch: `work/v4-deep-discovery`
- last_verified_commit/date: `ab0e526` / `2026-06-01T13:20:29+02:00`

STACK
- languages: Python, Shell
- frameworks: UNKNOWN
- DB: UNKNOWN
- platform: UNKNOWN
- external_tools/services: systemd

CODE_MAP
entrypoints:
- `facebook_archive_dashboard.py`
- `facebook_session_browser.py`
important_folders:
- `dev`
- `downloads`
- `logs`
- `state`
- `systemd`
important_files:
- `dev/README.md`
tests:
- UNKNOWN
scripts:
- `facebook_archive_dashboard.py`
- `facebook_session_browser.py`
- `facebook_video_archiver.sh`
generated/runtime/avoid_touch_casually:
- `dev/legacy`
- `state`
- `logs`

ARCH
summary:
- dev/legacy/README.md: Conservative local archiver for Facebook videos/posts that you own or are explicitly authorized to download. The default page is:
- dev/legacy/dev/INDEX.md: Start here for Codex/operator work on `facebook-video-archiver`.
- dev/legacy/dev/ARCHITECTURE.md: `facebook_video_archiver.sh` is the operator entrypoint. It wraps `yt-dlp` and delegates persistent manual-login browser work to `facebook_session_browser.py`.
- dev/legacy/dev/AGENT_RULES.md: - Keep `VERSION` as the single source of truth.
- dev/legacy/dev/TEST_PLAN.md: bash -n facebook_video_archiver.sh
- dev/legacy/dev/CHANGELOG.md: - Added `--discover-deep` with progressive scrolling, checkpoint/resume, and no-new-URL stop condition.
- dev/legacy/dev/OPERATIONS.md: cd ~/codex-workspace/facebook-video-archiver
- dev/legacy/dev/LEGAL_AND_SAFETY.md: This project is only for videos you own or are explicitly authorized to archive.
- facebook_archive_dashboard.py: ARCHIVE_ROOT = Path(os.environ.get("ARCHIVE_ROOT", "/media/daniele/Seagate6TB2/facebook-video-archive"))
- facebook_session_browser.py: from urllib.parse import parse_qsl, urlencode, unquote, urlparse, urlunparse
components/dataflow/design_decisions:
| source | fact |
|---|---|
| `dev/legacy/README.md` | # Facebook Video Archiver v4 |
| `dev/legacy/README.md` | ## Install on Linux Mint/Ubuntu |
| `dev/legacy/README.md` | ## Manual Login Flow |
| `dev/legacy/README.md` | # fai login manualmente, completa eventuale 2FA/checkpoint, poi premi Enter nel terminale |
| `dev/legacy/README.md` | ## Modes |
| `dev/legacy/README.md` | ## Dashboard |
| `dev/legacy/README.md` | ## Add Authorized URLs |
| `dev/legacy/README.md` | ## Systemd User Timer |
| `dev/legacy/README.md` | ## Telegram |
| `dev/legacy/README.md` | ## Troubleshooting |
| `dev/legacy/dev/INDEX.md` | # Dev Index v4 |
| `dev/legacy/dev/ARCHITECTURE.md` | # Architecture v4 |
| `dev/legacy/dev/AGENT_RULES.md` | # Agent Rules v4 |
| `dev/legacy/dev/TEST_PLAN.md` | # Test Plan v4 |
| `dev/legacy/dev/CHANGELOG.md` | # Changelog v4 |
| `dev/legacy/dev/CHANGELOG.md` | ## v4 |
| `dev/legacy/dev/CHANGELOG.md` | ## v3 |
| `dev/legacy/dev/CHANGELOG.md` | ## v2 |

INVARIANTS
architecture/data/UX/safety/versioning/localization:
| source | fact |
|---|---|
| `dev/legacy/README.md` | ./facebook_video_archiver.sh --version |
| `dev/legacy/README.md` | `--discover-browser` is the short legacy browser discovery. `--discover-deep` is the preferred progressive discovery: it resumes from `state/discovery_checkpoint.json`, scrolls up to `DISCOVER_MAX_SCROLL_ROUNDS=300`, stops after `DISCOVER |
| `dev/legacy/README.md` | The dashboard is terminal-only and reports `non stimabile` instead of inventing unknown totals or ETA. |
| `dev/legacy/README.md` | If `/home/daniele/codex-workspace/scripts/amici_fb/telegram_notify.py` exists and `ENABLE_TELEGRAM=1` is set in `.env`, v4 sends a short final notification with status, new count, and errors. Missing Telegram support never fails the archi |
| `dev/legacy/README.md` | Sessione non loggata: run `--login-browser`, complete login/2FA/checkpoint manually, then press Enter in the terminal. |
| `dev/legacy/README.md` | Video privati/non autorizzati: do not download them. Use only content you own or are explicitly authorized to archive. |
| `dev/legacy/dev/INDEX.md` | Primary files: |
| `dev/legacy/dev/INDEX.md` | - `VERSION`: single source of truth for version `v4`. |
| `dev/legacy/dev/INDEX.md` | Required safety posture: |
| `dev/legacy/dev/INDEX.md` | - Do not bypass DRM, paywalls, login restrictions, privacy controls, rate limits, or technical protections. |
| `dev/legacy/dev/INDEX.md` | - Do not commit real cookies, tokens, logs with secrets, or downloaded media. |
| `dev/legacy/dev/INDEX.md` | - Do not commit `.venv`, browser profiles, `.env`, or exported cookie files. |
| `dev/legacy/dev/INDEX.md` | ./facebook_video_archiver.sh --version |
| `dev/legacy/dev/ARCHITECTURE.md` | 5. `--discover-browser` is the short legacy browser discovery. |
| `dev/legacy/dev/AGENT_RULES.md` | - Keep `VERSION` as the single source of truth. |
| `dev/legacy/dev/AGENT_RULES.md` | - Every executable script must start with a first-line version comment such as `# v4`. |
| `dev/legacy/dev/AGENT_RULES.md` | - Never save real Facebook cookies, session exports, Telegram tokens, or downloaded videos in git. |
| `dev/legacy/dev/AGENT_RULES.md` | - Cookie/profile support must use only external paths outside the repo. |
| `dev/legacy/dev/AGENT_RULES.md` | - Never ask for or automate Facebook username/password login. |
| `dev/legacy/dev/AGENT_RULES.md` | - Preserve `state/downloaded.txt` semantics for duplicate prevention. |
| `dev/legacy/dev/AGENT_RULES.md` | - Preserve `state/discovered_urls.txt`; deep discovery must append/deduplicate, not wipe prior discoveries. |
| `dev/legacy/dev/AGENT_RULES.md` | - Do not enable the systemd timer automatically. |
| `dev/legacy/dev/TEST_PLAN.md` | ./facebook_video_archiver.sh --version |
| `dev/legacy/dev/TEST_PLAN.md` | - Do not mass-download in tests. |
| `dev/legacy/dev/TEST_PLAN.md` | - Do not commit logs, downloads, cookies, or token-bearing configuration. |
| `dev/legacy/dev/TEST_PLAN.md` | - Do not run `--login-browser` as an automated test; the operator must log in manually. |

BUILD_TEST
build_files:
- UNKNOWN
commands_found:
| source | fact |
|---|---|
| `dev/legacy/README.md` | sudo apt install -y git python3 python3-venv python3-pip curl |
| `dev/legacy/README.md` | python -m playwright install chromium |
| `dev/legacy/README.md` | python3 facebook_archive_dashboard.py --watch --interval 3 |
| `dev/legacy/README.md` | systemctl --user daemon-reload |
| `dev/legacy/README.md` | systemctl --user enable facebook-video-archiver.timer |
| `dev/legacy/README.md` | systemctl --user start facebook-video-archiver.timer |
| `dev/legacy/README.md` | systemctl --user list-timers facebook-video-archiver.timer |
| `dev/legacy/dev/INDEX.md` | bash -n facebook_video_archiver.sh |
| `dev/legacy/dev/INDEX.md` | python3 -m py_compile facebook_session_browser.py |
| `dev/legacy/dev/ARCHITECTURE.md` | 2. `--setup` creates `.venv`, installs Playwright and yt-dlp locally, and installs Chromium. |
| `dev/legacy/dev/ARCHITECTURE.md` | 7. `--export-session-cookies` exports persistent-session cookies to an external Netscape file for yt-dlp. |
| `dev/legacy/dev/ARCHITECTURE.md` | 8. `--run` prefers `urls.txt` plus `state/discovered_urls.txt`, skips archive entries through yt-dlp `--download-archive`, and uses the exported cookie file only when readable. |
| `dev/legacy/dev/AGENT_RULES.md` | - Never save real Facebook cookies, session exports, Telegram tokens, or downloaded videos in git. |
| `dev/legacy/dev/TEST_PLAN.md` | bash -n facebook_video_archiver.sh |
| `dev/legacy/dev/TEST_PLAN.md` | python3 -m py_compile facebook_session_browser.py |
| `dev/legacy/dev/TEST_PLAN.md` | git status --short --ignored |
| `dev/legacy/dev/OPERATIONS.md` | Do not place cookie files, browser profiles, or `.env` inside git. |
| `dev/legacy/dev/OPERATIONS.md` | sudo apt install -y git python3 python3-venv python3-pip curl |
| `dev/legacy/dev/OPERATIONS.md` | python3 facebook_archive_dashboard.py --watch --interval 3 |
| `dev/legacy/dev/OPERATIONS.md` | systemctl --user daemon-reload |
| `dev/legacy/dev/OPERATIONS.md` | systemctl --user enable facebook-video-archiver.timer |
| `dev/legacy/dev/OPERATIONS.md` | systemctl --user start facebook-video-archiver.timer |
| `dev/legacy/dev/OPERATIONS.md` | systemctl --user status facebook-video-archiver.service |
| `dev/legacy/dev/OPERATIONS.md` | journalctl --user -u facebook-video-archiver.service -n 100 --no-pager |
test_targets:
- UNKNOWN
known_test_flakiness_or_requirements:
- facebook_session_browser.py: await page.goto(args.page_url, wait_until="domcontentloaded", timeout=60000)

VERSIONING_RELEASE
rules/artifacts/commit_push/release_blockers:
| source | fact |
|---|---|
| `dev/legacy/README.md` | ./facebook_video_archiver.sh --version |
| `dev/legacy/dev/INDEX.md` | - `VERSION`: single source of truth for version `v4`. |
| `dev/legacy/dev/INDEX.md` | - Do not commit real cookies, tokens, logs with secrets, or downloaded media. |
| `dev/legacy/dev/INDEX.md` | - Do not commit `.venv`, browser profiles, `.env`, or exported cookie files. |
| `dev/legacy/dev/INDEX.md` | ./facebook_video_archiver.sh --version |
| `dev/legacy/dev/AGENT_RULES.md` | - Keep `VERSION` as the single source of truth. |
| `dev/legacy/dev/AGENT_RULES.md` | - Every executable script must start with a first-line version comment such as `# v4`. |
| `dev/legacy/dev/TEST_PLAN.md` | ./facebook_video_archiver.sh --version |
| `dev/legacy/dev/TEST_PLAN.md` | - Do not commit logs, downloads, cookies, or token-bearing configuration. |
| `dev/legacy/dev/OPERATIONS.md` | Do not store downloaded media on the repo filesystem; use the Seagate archive root. |
| `dev/legacy/dev/OPERATIONS.md` | ./facebook_video_archiver.sh --version |
| `facebook_session_browser.py` | "version": "v4", |
| `facebook_session_browser.py` | version=0, |
| `facebook_video_archiver.sh` | VERSION_FILE="$SCRIPT_DIR/VERSION" |
| `facebook_video_archiver.sh` | VERSION="$(tr -d '[:space:]' < "$VERSION_FILE")" |
| `facebook_video_archiver.sh` | facebook-video-archiver $VERSION |
| `facebook_video_archiver.sh` | ./facebook_video_archiver.sh --version |
| `facebook_video_archiver.sh` | "$ytdlp" "${common[@]}" --simulate --skip-download --flat-playlist --print "%(webpage_url)s" "$page_url" \ |
| `facebook_video_archiver.sh` | local -a curl_args=(-fsSL --max-time 25 --retry 1 --user-agent "facebook-video-archiver/$VERSION") |
| `facebook_video_archiver.sh` | python3 "$TELEGRAM_HELPER" "facebook-video-archiver $VERSION" "$message" >/dev/null 2>&1 // true |

DATA_STORAGE
DB_paths/backup/import/export/migration/retention/user_data_safety:
| source | fact |
|---|---|
| `dev/legacy/README.md` | `--discover-browser` is the short legacy browser discovery. `--discover-deep` is the preferred progressive discovery: it resumes from `state/discovery_checkpoint.json`, scrolls up to `DISCOVER_MAX_SCROLL_ROUNDS=300`, stops after `DISCOVER |
| `dev/legacy/README.md` | Sessione non loggata: run `--login-browser`, complete login/2FA/checkpoint manually, then press Enter in the terminal. |
| `dev/legacy/dev/INDEX.md` | - Do not bypass DRM, paywalls, login restrictions, privacy controls, rate limits, or technical protections. |
| `dev/legacy/dev/INDEX.md` | - Do not commit real cookies, tokens, logs with secrets, or downloaded media. |
| `dev/legacy/dev/INDEX.md` | - Do not commit `.venv`, browser profiles, `.env`, or exported cookie files. |
| `dev/legacy/dev/AGENT_RULES.md` | - Never save real Facebook cookies, session exports, Telegram tokens, or downloaded videos in git. |
| `dev/legacy/dev/AGENT_RULES.md` | - Never ask for or automate Facebook username/password login. |
| `dev/legacy/dev/AGENT_RULES.md` | - Preserve `state/downloaded.txt` semantics for duplicate prevention. |
| `dev/legacy/dev/AGENT_RULES.md` | - Preserve `state/discovered_urls.txt`; deep discovery must append/deduplicate, not wipe prior discoveries. |
| `dev/legacy/dev/TEST_PLAN.md` | - Do not commit logs, downloads, cookies, or token-bearing configuration. |
| `dev/legacy/dev/TEST_PLAN.md` | - Do not run `--login-browser` as an automated test; the operator must log in manually. |
| `dev/legacy/dev/CHANGELOG.md` | - Added safety and operations docs. |
| `dev/legacy/dev/OPERATIONS.md` | - Sessione non loggata: run `--login-browser`, finish manual login/checkpoint, then rerun `--check-session`. |
| `facebook_archive_dashboard.py` | log_updated = "non disponibile" |
| `facebook_archive_dashboard.py` | f"log corrente: {log_path if log_path else 'non disponibile'}", |
| `facebook_session_browser.py` | safe_print("Session check: non sembra loggato, oppure Facebook richiede checkpoint/2FA.") |
| `facebook_video_archiver.sh` | log "Conceptual yt-dlp command: yt-dlp <safe-options> $cookie_arg $mode <authorized-url-or-page>" |
| `facebook_video_archiver.sh` | if ! "$ytdlp" "${common[@]}" --batch-file "$batch_file" --simulate --skip-download --print "%(webpage_url)s / %(title)s" 2>&1 / sanitize_stream / tee "$log_file"; then |
| `facebook_video_archiver.sh` | [[ "$VERSION" == "v4" ]] // { log "Unexpected VERSION: $VERSION"; ok=1; } |
| `facebook_video_archiver.sh` | log "FB_COOKIES_FILE must stay outside this repository." |
| `facebook_video_archiver.sh` | log "check OK ($VERSION)" |
| `dev/legacy/dev/ARCHITECTURE.md` | 7. `--export-session-cookies` exports persistent-session cookies to an external Netscape file for yt-dlp. |

KNOWN_BUGS
active/historical/root_causes/regression_checklist:
| source | fact |
|---|---|
| `facebook_archive_dashboard.py` | if any(token in line.lower() for token in ("warning", "error", "failed", "unsupported", "unable")): |
| `facebook_session_browser.py` | safe_print(f"ERROR: Playwright is not available in this environment: {exc}") |
| `facebook_session_browser.py` | await page.goto(args.page_url, wait_until="domcontentloaded", timeout=60000) |
| `facebook_video_archiver.sh` | log "ERROR: $*" >&2 |
| `facebook_video_archiver.sh` | log "yt-dlp supports --cookies-from-browser; close the browser if its cookie DB is locked." |
| `facebook_video_archiver.sh` | status="ERROR" |

DO_NOT_BREAK
- Preserve `dev/project.metadata.json` -> this AI doc -> Human docs workflow.
- Preserve `dev/legacy/`; do not delete or rewrite historical docs without explicit migration intent.
- dev/legacy/README.md: ./facebook_video_archiver.sh --version
- dev/legacy/README.md: If `/home/daniele/codex-workspace/scripts/amici_fb/telegram_notify.py` exists and `ENABLE_TELEGRAM=1` is set in `.env`, v4 sends a short final notification with status, new count, and errors. Missing Telegram support never fails the archi
- dev/legacy/README.md: Video privati/non autorizzati: do not download them. Use only content you own or are explicitly authorized to archive.
- dev/legacy/dev/INDEX.md: - `VERSION`: single source of truth for version `v4`.
- dev/legacy/dev/INDEX.md: Required safety posture:
- dev/legacy/dev/INDEX.md: - Do not bypass DRM, paywalls, login restrictions, privacy controls, rate limits, or technical protections.
- dev/legacy/dev/INDEX.md: - Do not commit real cookies, tokens, logs with secrets, or downloaded media.
- dev/legacy/dev/INDEX.md: - Do not commit `.venv`, browser profiles, `.env`, or exported cookie files.
- dev/legacy/dev/INDEX.md: ./facebook_video_archiver.sh --version
- dev/legacy/dev/AGENT_RULES.md: - Keep `VERSION` as the single source of truth.
- dev/legacy/dev/AGENT_RULES.md: - Every executable script must start with a first-line version comment such as `# v4`.
- dev/legacy/dev/AGENT_RULES.md: - Never save real Facebook cookies, session exports, Telegram tokens, or downloaded videos in git.
- dev/legacy/dev/AGENT_RULES.md: - Cookie/profile support must use only external paths outside the repo.
- dev/legacy/dev/AGENT_RULES.md: - Never ask for or automate Facebook username/password login.
- dev/legacy/dev/AGENT_RULES.md: - Preserve `state/downloaded.txt` semantics for duplicate prevention.
- dev/legacy/dev/AGENT_RULES.md: - Preserve `state/discovered_urls.txt`; deep discovery must append/deduplicate, not wipe prior discoveries.

RECENT_DECISIONS
| source | fact |
|---|---|
| `dev/legacy/dev/CHANGELOG.md` | # Changelog v4 |
| `dev/legacy/dev/CHANGELOG.md` | ## v4 |
| `dev/legacy/dev/CHANGELOG.md` | - Added `--discover-deep` with progressive scrolling, checkpoint/resume, and no-new-URL stop condition. |
| `dev/legacy/dev/CHANGELOG.md` | - Added network request/response URL capture during browser discovery. |
| `dev/legacy/dev/CHANGELOG.md` | - Added Facebook URL normalization that strips tracking parameters and keeps plausible post/video/reel/watch URLs. |
| `dev/legacy/dev/CHANGELOG.md` | - Added `state/discovery_checkpoint.json` runtime checkpoint and `logs/discovery_report_latest.txt` report. |
| `dev/legacy/dev/CHANGELOG.md` | - Raised deep discovery defaults to `DISCOVER_MAX_SCROLL_ROUNDS=300` and `DISCOVER_NO_NEW_STOP_ROUNDS=25`. |
| `dev/legacy/dev/CHANGELOG.md` | ## v3 |
| `dev/legacy/dev/CHANGELOG.md` | - Added `facebook_session_browser.py` for manual persistent Facebook login with Playwright. |
| `dev/legacy/dev/CHANGELOG.md` | - Added `--setup`, `--login-browser`, `--check-session`, `--discover-browser`, and `--export-session-cookies`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added external persistent browser profile support under `~/.local/share/facebook-video-archiver/browser-profile`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added Netscape cookie export from the persistent profile to `~/.config/facebook-video-archiver/facebook-cookies.txt`. |
| `dev/legacy/dev/CHANGELOG.md` | - Updated checks, docs, and gitignore for `.venv`, browser profiles, temporary state, logs, cookies, and media. |
| `dev/legacy/dev/CHANGELOG.md` | ## v2 |
| `dev/legacy/dev/CHANGELOG.md` | - Added external Facebook cookie file support through `FB_COOKIES_FILE`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added local browser cookie support through `FB_USE_BROWSER_COOKIES=1` and `FB_BROWSER`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added `--discover-page` conservative URL discovery into `state/discovered_urls.txt`. |
| `dev/legacy/dev/CHANGELOG.md` | - Strengthened `.gitignore` for cookies, browser state, secrets, logs, and media. |

ROADMAP
active/deferred/risky:
| source | fact |
|---|---|
| `UNKNOWN` | no verified roadmap found in read sources. |

LEGACY_SUMMARY
- legacy_docs_read_count: 12
- legacy_docs_read:
- `dev/README.md`
- `dev/legacy/README.md`
- `dev/legacy/dev/INDEX.md`
- `dev/legacy/dev/ARCHITECTURE.md`
- `dev/legacy/dev/AGENT_RULES.md`
- `dev/legacy/dev/TEST_PLAN.md`
- `dev/legacy/dev/CHANGELOG.md`
- `dev/legacy/dev/OPERATIONS.md`
- `dev/legacy/dev/LEGAL_AND_SAFETY.md`
- `facebook_archive_dashboard.py`
- `facebook_session_browser.py`
- `facebook_video_archiver.sh`
- extracted: purpose, stack, commands, invariants, bugs, roadmap, changelog, code map.
- historical_only: original local docs in `dev/legacy`; use only when AI doc lacks detail or for audit history.

LINKS
- metadata: [dev/project.metadata.json](../../../facebook-video-archiver/dev/project.metadata.json)
- human_overview: [human overview](../../human/projects/facebook-video-archiver/overview.md)
- human_folder: [human folder](../../human/projects/facebook-video-archiver)
- legacy_docs: [dev/legacy](../../../facebook-video-archiver/dev/legacy)
- repo_path: [repo](../../../facebook-video-archiver)

OPEN_QUESTIONS
- none detected in extracted sources

# facebook-video-archiver Troubleshooting

Use this page for symptoms and checks. For operational decisions, confirm against the AI doc first.

## Known Problems And Symptoms
| source | fact |
|---|---|
| `facebook_archive_dashboard.py` | if any(token in line.lower() for token in ("warning", "error", "failed", "unsupported", "unable")): |
| `facebook_session_browser.py` | safe_print(f"ERROR: Playwright is not available in this environment: {exc}") |
| `facebook_session_browser.py` | await page.goto(args.page_url, wait_until="domcontentloaded", timeout=60000) |
| `facebook_video_archiver.sh` | log "ERROR: $*" >&2 |
| `facebook_video_archiver.sh` | log "yt-dlp supports --cookies-from-browser; close the browser if its cookie DB is locked." |
| `facebook_video_archiver.sh` | status="ERROR" |

## Useful Checks Or Commands
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

## Safety Checks Before Fixing
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
- dev/legacy/dev/AGENT_RULES.md: - Never ask for or automate Facebook username/password login.
- dev/legacy/dev/AGENT_RULES.md: - Do not enable the systemd timer automatically.

# facebook-video-archiver Features

This page translates extracted project facts into a user-readable feature view. Items marked `UNKNOWN` need manual confirmation before product or release decisions.

## Main Capabilities
- dev/legacy/README.md: # Facebook Video Archiver v4
- dev/legacy/README.md: ## Modes
- dev/legacy/README.md: ## Dashboard
- dev/legacy/dev/OPERATIONS.md: ## Dashboard
- dev/legacy/README.md: Conservative local archiver for Facebook videos/posts that you own or are explicitly authorized to download. The default page is:
- dev/legacy/dev/INDEX.md: Start here for Codex/operator work on `facebook-video-archiver`.
- dev/legacy/dev/ARCHITECTURE.md: `facebook_video_archiver.sh` is the operator entrypoint. It wraps `yt-dlp` and delegates persistent manual-login browser work to `facebook_session_browser.py`.
- dev/legacy/dev/TEST_PLAN.md: bash -n facebook_video_archiver.sh
- dev/legacy/dev/OPERATIONS.md: cd ~/codex-workspace/facebook-video-archiver
- dev/legacy/dev/LEGAL_AND_SAFETY.md: This project is only for videos you own or are explicitly authorized to archive.
- facebook_archive_dashboard.py: ARCHIVE_ROOT = Path(os.environ.get("ARCHIVE_ROOT", "/media/daniele/Seagate6TB2/facebook-video-archive"))
- facebook_session_browser.py: from urllib.parse import parse_qsl, urlencode, unquote, urlparse, urlunparse

## Useful Limits And Boundaries
- dev/legacy/README.md: The dashboard is terminal-only and reports `non stimabile` instead of inventing unknown totals or ETA.
- dev/legacy/README.md: If `/home/daniele/codex-workspace/scripts/amici_fb/telegram_notify.py` exists and `ENABLE_TELEGRAM=1` is set in `.env`, v4 sends a short final notification with status, new count, and errors. Missing Telegram support never fails the archi
- dev/legacy/README.md: Sessione non loggata: run `--login-browser`, complete login/2FA/checkpoint manually, then press Enter in the terminal.
- dev/legacy/README.md: Video privati/non autorizzati: do not download them. Use only content you own or are explicitly authorized to archive.
- dev/legacy/dev/INDEX.md: Required safety posture:
- dev/legacy/dev/INDEX.md: - Do not bypass DRM, paywalls, login restrictions, privacy controls, rate limits, or technical protections.
- dev/legacy/dev/INDEX.md: - Do not commit real cookies, tokens, logs with secrets, or downloaded media.
- dev/legacy/dev/INDEX.md: - Do not commit `.venv`, browser profiles, `.env`, or exported cookie files.
- dev/legacy/dev/AGENT_RULES.md: - Every executable script must start with a first-line version comment such as `# v4`.
- dev/legacy/dev/AGENT_RULES.md: - Never save real Facebook cookies, session exports, Telegram tokens, or downloaded videos in git.
- dev/legacy/dev/AGENT_RULES.md: - Cookie/profile support must use only external paths outside the repo.
- dev/legacy/dev/AGENT_RULES.md: - Never ask for or automate Facebook username/password login.

## Where The Feature Code Appears To Live
- `facebook_archive_dashboard.py`
- `facebook_session_browser.py`
- `facebook_video_archiver.sh`

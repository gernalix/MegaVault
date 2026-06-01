# facebook-video-archiver Changelog

This is a synthesized changelog from legacy docs and migration evidence. It does not invent missing dates.

## Extracted Milestones
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
| `dev/legacy/dev/CHANGELOG.md` | - Expanded login/cookie operations and troubleshooting docs. |
| `dev/legacy/dev/CHANGELOG.md` | ## v1 |
| `dev/legacy/dev/CHANGELOG.md` | - Initial conservative Facebook authorized video archiver. |
| `dev/legacy/dev/CHANGELOG.md` | - Added `yt-dlp` wrapper with `--check`, `--dry-run`, `--run`, and `--test-one`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added duplicate archive state in `state/downloaded.txt`. |
| `dev/legacy/dev/CHANGELOG.md` | - Added optional systemd user service/timer, disabled by default. |

## MegaVault Documentation Events
- 2026-06-01: `#739482` moved legacy documentation into `dev/legacy` and created metadata/initial MegaVault docs.
- 2026-06-01T13:20:29+02:00: `#842915` enriched AI and Human docs from legacy docs, repo structure, scripts, tests, and build files.

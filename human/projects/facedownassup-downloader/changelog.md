# facedownassup-downloader Changelog

## 2026-06-13

- Prompt `#194672`: cleaned gallery-specific downloader state and retried after opening the gallery in the authenticated Firefox profile. Video DownloadHelper reportedly works after browser refresh, but the wrapper still extracted a fresh `264` fragment manifest and failed at HLS fragment `72`; partial deleted with `--no-partials`, no final file. Diagnosis narrowed: browser refresh can fix the browser/VDH path, but the page-based yt-dlp wrapper still receives a stale or non-downloadable HLS reference.
- Prompt `#518407`: checked existing JDownloader at `/home/daniele/Downloads/JDownloader.jar`; no install performed. JDownloader accepted the gallery URL via clipboard monitor but did not produce a downloadable item, had no Firefox JDownloader extension in the authenticated profile, and logged `Firefox settings folder not found`. Decision: JDownloader is not viable as configured and does not change the external HLS fragment `72` 404 conclusion.
- Updated `fda_downloader.sh` to version `0.4.0` for prompt `#672941`.
- Changed the default `yt-dlp` cookie source to Firefox with `--cookies-from-browser firefox`.
- Added `FDA_COOKIE_BROWSER=firefox/chrome`, `FDA_FIREFOX_PROFILE`, Firefox profile detection, and doctor reporting for cookie browser/profile plus a private cookie-read probe.
- Kept reports redacted: no cookie values, tokens, or complete signed media URLs.
- Removed the diagnostic/partial `html5mediaembed gallery-1` archive entry so gallery `id=173` can be retried with fresh Firefox cookies.
- Verified Firefox profile `/home/daniele/.config/mozilla/firefox/50b1zmic.default-release`: cookie read worked, fresh manifest found `264` fragments, and strict download still failed at HLS fragment `72` with `404`; current partial was deleted with `--no-partials`.
- Ran Firefox `browser-check`; report `state/browser-check-20260613-130553.txt` documents `firefox_network=unavailable` and `ytdlp_fragment_errors=404/72,72`.

## 2026-06-10

- Updated `fda_downloader.sh` to version `0.3.0` for prompt `#615902`.
- Added `browser-check URL`: explicit Chrome DevTools Network diagnostic, redacted media request report, temporary `yt-dlp` comparison, and final `PLAYABLE` / `NOT_PLAYABLE` / `UNKNOWN` classification.
- Kept Chrome remote-debug launch behind explicit `FDA_BROWSER_CHECK_LAUNCH=1`; reports do not store cookies, tokens, or full signed media URLs.
- Updated `fda_downloader.sh` to version `0.2.0` for prompt `#284763`.
- Added `refresh-test`, fresh manifest preflight, no-cache yt-dlp runs, segment reports, ffprobe validation, and `--no-partials`.
- Verified strict refresh-test: Chrome DevTools playback status `UNKNOWN`, fresh manifest found `264` fragments, fragment `72` returned `404`, and incomplete output was deleted with `--no-partials`.
- Created `fda_downloader.sh` version `0.1.0`.
- Added README, metadata, Git ignore rules, and private GitHub remote.
- Diagnosed prompt `#739518`: Chrome cookies work; adding `Referer`, `Origin`, and Chrome-like `User-Agent` removes the initial 403; HLS fragments still return repeated 404.

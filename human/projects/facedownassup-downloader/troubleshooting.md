# facedownassup-downloader Troubleshooting

## Global `porndownloader`

Prompt `#826194` added a global command:

```bash
~/.local/bin/porndownloader
```

It is a symlink to the repo script:

```text
/home/daniele/codex-workspace/facedownassup-downloader/porndownloader
```

Default behavior:

- Uses Firefox profile `/home/daniele/.config/mozilla/firefox/50b1zmic.default-release`
- Defaults to 720p, preferring `hls-HLS720p`
- Saves completed files to `~/Videos/porndownloader/`
- Uses `~/.local/state/porndownloader/` for logs, archive, run scratch data, and `download_history.sqlite`
- Names completed files as `YYYY-MM-DD - <title>.mp4`, falling back to `YYYY-MM-DD - FaceDownAssUp - gallery-<id>.mp4` for generic facedownassup gallery titles
- Deduplicates only by source URL, not by title

Useful commands:

```bash
porndownloader --formats 'https://members.facedownassup.com/gallery.php?id=173'
porndownloader --quality 720 'https://members.facedownassup.com/gallery.php?id=173'
porndownloader --list
```

Verification result for gallery `id=173`: `--formats` succeeded and showed `hls-HLS720p`. The 720p download passed the previously failing fragment `72`, then failed at fragment `175` with `404`; no final file was created and no SQLite history row was inserted.

## 403 Forbidden

Use the wrapper so `yt-dlp` sends the same-origin `Referer`, `Origin`, and browser-like `User-Agent` headers:

```bash
cd ~/codex-workspace/facedownassup-downloader
./fda_downloader.sh refresh-test 'https://members.facedownassup.com/gallery.php?id=173'
```

The default cookie source is now Firefox:

```bash
./fda_downloader.sh doctor
FDA_FIREFOX_PROFILE="$HOME/.mozilla/firefox/<profile>" ./fda_downloader.sh doctor
FDA_COOKIE_BROWSER=chrome ./fda_downloader.sh doctor
```

The doctor reports browser/profile selection and a private cookie-read probe without printing cookies, tokens, or signed URLs.

2026-06-13 verified Firefox source:

```text
cookie_browser=firefox
firefox_profile=/home/daniele/.config/mozilla/firefox/50b1zmic.default-release
cookie_read_probe=OK
```

## HLS Fragment 404

The current diagnostic found an accessible m3u8 manifest, then repeated `404 Not Found` on later HLS fragments. That is consistent with signed or temporary segment URLs, or a playlist that references unavailable segments.

The v0.2.0 strict refresh test regenerated a fresh manifest immediately before download. It found `264` fragments and failed at missing fragment `72`, then deleted the incomplete output because `--no-partials` was enabled.

The v0.4.0 Firefox strict refresh test on 2026-06-13 reproduced the same external HLS failure with fresh Firefox cookies: `264` fragments, missing range `72`, incomplete output deleted with `--no-partials`.

Prompt `#194672` repeated the test after a real Firefox refresh where Video DownloadHelper could work. Before retry, the downloader state for `gallery-1` was cleaned: archive entry, partials, old private m3u8/page dumps, and yt-dlp cache. Firefox was opened on the gallery URL, then the wrapper was run with the real profile:

```bash
FDA_FIREFOX_PROFILE=/home/daniele/.config/mozilla/firefox/50b1zmic.default-release FDA_REFRESH_ATTEMPTS=1 FDA_SLEEP_REQUESTS=0 FDA_ABORT_ON_UNAVAILABLE=1 ./fda_downloader.sh --no-partials refresh-test 'https://members.facedownassup.com/gallery.php?id=173'
```

Result: yt-dlp still extracted a fresh `264` fragment manifest and failed at fragment `72` with `404`; the partial was deleted and no final file was created. Since Video DownloadHelper can work after the browser refresh, fragment `72` should no longer be treated as definitive proof of permanently broken CDN content. The narrower diagnosis is that Firefox/VDH can use a refreshed browser media path, while the page-based yt-dlp wrapper still receives a stale or non-downloadable HLS reference.

Keep per-request delay disabled for expiring HLS URLs:

```bash
FDA_SLEEP_REQUESTS=0 ./fda_downloader.sh refresh-test 'https://members.facedownassup.com/gallery.php?id=173'
```

Use strict mode to fail instead of accepting skipped fragments:

```bash
FDA_ABORT_ON_UNAVAILABLE=1 ./fda_downloader.sh --no-partials refresh-test 'https://members.facedownassup.com/gallery.php?id=173'
```

Do not paste raw `logs/run-*.log` content into reports; it can contain signed URLs.

## Browser-Real Check

Use this when you need a redacted browser-cookie `yt-dlp` comparison for the gallery:

```bash
cd ~/codex-workspace/facedownassup-downloader
./fda_downloader.sh browser-check 'https://members.facedownassup.com/gallery.php?id=173'
```

The command does not launch Chrome with remote debugging unless explicitly allowed:

```bash
FDA_BROWSER_CHECK_LAUNCH=1 ./fda_downloader.sh browser-check 'https://members.facedownassup.com/gallery.php?id=173'
```

Output report: `state/browser-check-*.txt`.

With Firefox cookies, browser-check does not automate real Firefox Network capture; it documents that limitation in the report. Use the existing logged-in Firefox window for manual playback confirmation, or set `FDA_COOKIE_BROWSER=chrome` when an explicit Chrome DevTools diagnostic is required.

2026-06-13 Firefox browser-check report: `state/browser-check-20260613-130553.txt`; `firefox_network=unavailable`, `ytdlp_http_statuses=404,404`, `ytdlp_fragment_errors=404/72,72`, `FINAL_REPORT=UNKNOWN`.

If the report says `comparison=MATCH_404_SERVER_PLAYLIST_OR_CONTENT` and `FINAL_REPORT=NOT_PLAYABLE`, Chrome and `yt-dlp` both saw `404` on HLS media. Treat that as a content or playlist problem on the server side and do not force or bypass protections.

## JDownloader Check

Prompt `#518407` checked the already running JDownloader instance at `/home/daniele/Downloads/JDownloader.jar`; no installation was performed.

Method used:

```text
JDownloader source=/home/daniele/Downloads/JDownloader.jar
Firefox profile=/home/daniele/.config/mozilla/firefox/50b1zmic.default-release
input=gallery URL via JDownloader clipboard monitor
```

Findings:

- JDownloader was open and running from `~/Downloads`.
- The Firefox profile contains Video DownloadHelper, but no JDownloader Firefox extension was found.
- JDownloader logged `Firefox settings folder not found`, so it was not automatically using the authenticated Firefox profile.
- The gallery URL was accepted as a clipboard crawler job at `2026-06-13T13:20:28` with URL-length evidence only; no cookies, tokens, or signed URLs were printed.
- JDownloader did not create a downloadable LinkGrabber item or a download-list entry for the gallery URL.
- Local HTTP/API probes on the JDownloader ports did not provide a usable control/query API for this run.

Decision: JDownloader, as currently installed/configured, cannot verify a successful authenticated download for gallery `id=173`. It also does not contradict the yt-dlp evidence: authenticated yt-dlp reaches the manifest but HLS fragment `72` returns `404`. After prompt `#194672`, do not treat that as final CDN-broken proof because Firefox/Video DownloadHelper can work after refresh; treat it as a mismatch between the browser-refreshed media path and the wrapper's page-based yt-dlp extraction.

# facedownassup-downloader Troubleshooting

## 403 Forbidden

Use the wrapper so `yt-dlp` sends the same-origin `Referer`, `Origin`, and Chrome-like `User-Agent` headers:

```bash
cd ~/codex-workspace/facedownassup-downloader
./fda_downloader.sh refresh-test 'https://members.facedownassup.com/gallery.php?id=173'
```

## HLS Fragment 404

The current diagnostic found an accessible m3u8 manifest, then repeated `404 Not Found` on later HLS fragments. That is consistent with signed or temporary segment URLs, or a playlist that references unavailable segments.

The v0.2.0 strict refresh test regenerated a fresh manifest immediately before download. It found `264` fragments and failed at missing fragment `72`, then deleted the incomplete output because `--no-partials` was enabled.

Keep per-request delay disabled for expiring HLS URLs:

```bash
FDA_SLEEP_REQUESTS=0 ./fda_downloader.sh refresh-test 'https://members.facedownassup.com/gallery.php?id=173'
```

Use strict mode to fail instead of accepting skipped fragments:

```bash
FDA_ABORT_ON_UNAVAILABLE=1 ./fda_downloader.sh --no-partials refresh-test 'https://members.facedownassup.com/gallery.php?id=173'
```

Do not paste raw `logs/run-*.log` content into reports; it can contain signed URLs.

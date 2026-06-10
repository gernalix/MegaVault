# facedownassup-downloader Changelog

## 2026-06-10

- Updated `fda_downloader.sh` to version `0.2.0` for prompt `#284763`.
- Added `refresh-test`, fresh manifest preflight, no-cache yt-dlp runs, segment reports, ffprobe validation, and `--no-partials`.
- Verified strict refresh-test: Chrome DevTools playback status `UNKNOWN`, fresh manifest found `264` fragments, fragment `72` returned `404`, and incomplete output was deleted with `--no-partials`.
- Created `fda_downloader.sh` version `0.1.0`.
- Added README, metadata, Git ignore rules, and private GitHub remote.
- Diagnosed prompt `#739518`: Chrome cookies work; adding `Referer`, `Origin`, and Chrome-like `User-Agent` removes the initial 403; HLS fragments still return repeated 404.

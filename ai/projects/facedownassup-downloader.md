META:
name=facedownassup-downloader
slug=facedownassup-downloader
path=/home/daniele/codex-workspace/facedownassup-downloader
remote=git@github.com:gernalix/facedownassup-downloader.git
branch=main
prompt=284763
verified_at=2026-06-10T16:20:49+02:00
protocol=MEGAVAULT_PROTOCOL.md:VERSION=8
PURPOSE:
purpose=Local authorized downloader for facedownassup.com member gallery pages using existing legitimate Chrome login via yt-dlp cookies.
scope=personal_access_only,no_DRM_bypass,no_paywall_bypass,no_credential_attack,no_exploit,no_aggressive_rate
STACK:
lang=Bash,Python_inline_parser
tools=yt-dlp 2026.06.09.230517,Chrome 149.0.7827.102,ffmpeg/ffprobe 6.1.1,gh,git
platform=Linux Mint/XFCE host
MAP:
entry=fda_downloader.sh
config=env:FDA_*,VERSION,dev/project.metadata.json
docs=README.md,MegaVault/human/projects/facedownassup-downloader/*
state=state/download-archive.txt,state/segments-*.txt,logs/run-*.log,private/crawl-*
output=downloads/<extractor>/<id> - <title>.<ext>
avoid=downloads,logs,state,private,cookies,*.dump,*.part,*.ytdl
ARCH:
script=fda_downloader.sh modes:doctor,refresh-test,test,download,list,crawl
download=yt-dlp --cookies-from-browser chrome + Referer/Origin/User-Agent + no-cache + archive + local verbose logs
refresh=refresh-test checks Chrome playback status when possible, extracts fresh page/manifest immediately before download, reports segments, validates complete files with ffprobe, and handles partials
crawl=bounded same-origin gallery discovery from authorized HTML dumps; signed media URLs not persisted in reports
FLOW:
refresh-test=chrome_playback_check->fresh_preflight_write_pages_private->fresh_gallery_download->segment_report->ffprobe_or_partial_classification
test=doctor->yt-dlp_cookie_extract->generic_gallery_page->html5_m3u8->hlsnative
list=read_urls->download_url_each->sleep_between_videos->archive_dedupe
crawl=start_page->write_pages_tmp->parse_gallery_links->state/crawl-found-*.txt
INV:
security=never_print_cookies_tokens_passwords_signed_urls_in_reports
auth=only_use_operator_Chrome_session_for_content_already_authorized
access=no_DRM/paywall/rate_limit/credential/protection_bypass
data=raw_logs_local_only_chmod600; logs_may_contain_expiring_signed_URLs
ops=do_not_commit downloads/logs/state/private/cookies/dumps
version=VERSION and fda_downloader.sh SCRIPT_VERSION must move together
partials=complete_only_when_missing_count=0_and_ffprobe_passes; incomplete_outputs_move_to_downloads/_partials_or_delete_with_--no-partials
BUILD:
cmd=bash -n fda_downloader.sh
deps=yt-dlp,python3,Chrome_profile,ffmpeg
install=none; optional FDA_UPDATE_YTDLP=1 ./fda_downloader.sh doctor
TEST:
syntax=bash -n fda_downloader.sh PASS 2026-06-10 after v0.2.0
doctor=./fda_downloader.sh doctor PASS; yt-dlp=2026.06.09.230517; Chrome=149.0.7827.102
diagnostic=yt-dlp with Chrome cookies+Referer+Origin+UA removed initial 403 and produced local MP4 diagnostic outside repo
script_test=started extraction/download; stopped by timeout after repeated HLS fragment 404; partial removed
refresh_test=FDA_REFRESH_ATTEMPTS=1 FDA_ABORT_ON_UNAVAILABLE=1 --no-partials refresh-test URL; result=expected_external_404; total_fragments=264; missing_count=1; missing_ranges=72; partial_deleted=yes
DATA:
db=none
paths=downloads,downloads/_partials,logs,state,private
backup=git remote private GitHub; generated media excluded
retention=operator_managed; raw logs sensitive
DNB:
dnb=do_not_add_cookie_export_or_store_browser_cookies_in_repo
dnb=do_not_add_DRM_or_auth_bypass_logic
dnb=do_not_report_full_signed_m3u8/mp4_URLs
dnb=do_not_make_crawl_unbounded_or_cross-domain
dnb=do_not_reuse_old_m3u8_direct_URLs; always pass gallery/page URL to yt-dlp
BUG:
issue=HLS manifest accessible with headers but many segment requests return 404
cause=likely_signed_or_temporary_segment_URLs_or_playlist_references_unavailable_segments; v0.2.0 strict test failed at fragment 72 after fresh manifest
workaround=rerun refresh-test with fresh page/manifest; if still 404 document external stream limit
status=open_external_stream_limit
RISK:
risk=signed_URL_leak; trigger=raw verbose log sharing; mitigation=chmod600+redacted summaries+gitignore logs; test=rg redaction in summaries
risk=incomplete_MP4; trigger=HLS fragment 404 skip; mitigation=segment_report+ffprobe+_partials_or_--no-partials; test=strict refresh-test deleted partial
risk=account/session misuse; trigger=wrong URL/account; mitigation=same-origin default+authorized-only docs
ROAD:
now=use refresh-test for HLS 404/scaduti and keep raw signed URL material local-only
next=optional DevTools-based real playback assertion if Chrome is launched with remote debugging
later=UNKNOWN
LINK:
meta=../../../facedownassup-downloader/dev/project.metadata.json
human=../../human/projects/facedownassup-downloader/overview.md
repo=../../../facedownassup-downloader
readme=../../../facedownassup-downloader/README.md
OPEN:
open=Chrome UI playback automated status UNKNOWN; no debuggable Chrome process was available during v0.2.0 run
open=Whether fragment 72 404 is expired signature vs unavailable playlist entry remains external/UNKNOWN without exposing signed URLs

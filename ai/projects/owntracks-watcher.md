META:
name=owntracks-watcher
slug=owntracks-watcher
path=/home/daniele/codex-workspace/owntracks-watcher
runtime=ubuntu@150.230.148.128:/home/ubuntu/bots/owntracks_http_server
remote=none
branch=codex/prompt-384917
verified_commit=eaac5bc
verified_at=2026-06-13T02:55:00Z
prompt=739284
protocol=MEGAVAULT_PROTOCOL.md:v9
PURPOSE:
purpose=Private OwnTracks Android HTTP receiver on Oracle VM; stores location payloads in SQLite for Datasette/history views.
STACK:
lang=Python 3.10
fw=Flask/Werkzeug
db=SQLite WAL
platform=Oracle VM Ubuntu systemd service + Cloudflare Tunnel public HTTPS ingress
tools=systemd,cloudflared,sqlite3,curl,journalctl,Datasette
MAP:
entry=/home/ubuntu/bots/owntracks_http_server/owntracks_http_server.py
unit=/etc/systemd/system/owntracks-http-server.service
tunnel=/etc/cloudflared/config.yml
core=/home/ubuntu/bots/owntracks_http_server/owntracks_http_server.py:save_payload
db=/home/ubuntu/sync_root/db/owntracks.db
logs=journalctl -u owntracks-http-server.service
datasette=/home/ubuntu/sync_root/bots/telegram_insert_bot-master/.venv/bin/datasette serves /home/ubuntu/sync_root/db/owntracks.db on 127.0.0.1:8002
tests=external curl POST https://owntracks.danielegalati.com/owntracks
scripts=UNKNOWN
avoid=dev/legacy,build,.gradle,node_modules,*.db,*.sqlite,secrets,tokens,cookies,generated,Cloudflare credentials JSON
ARCH:
component=OwnTracks Android app sends HTTPS POST to Cloudflare hostname.
component=cloudflared.service maps hostname owntracks.danielegalati.com to http://127.0.0.1:8083.
component=owntracks-http-server.service runs Flask on 0.0.0.0:8083 but host firewall accepts only SSH and 3001 externally; public OwnTracks path is Cloudflare, not direct Oracle port.
component=Flask route /owntracks accepts POST JSON; only _type=location is persisted.
component=SQLite DB stores raw positions in positions and movement-filtered points in moves.
FLOW:
ingest=OwnTracks HTTP mode -> https://owntracks.danielegalati.com/owntracks -> Cloudflare Tunnel -> 127.0.0.1:8083 -> Flask /owntracks -> positions/moves.
payload_required=_type=location,lat,lon,tst or created_at recommended,tid or device recommended,acc/batt optional.
device_mapping=server stores device=data.device else data.tid else data.topic.
dedupe=positions insert skipped when same quando+lat+lon already exists.
movement=first point per device writes moves dist_m=0; later move writes only when haversine distance >= max(50m,acc*1.2).
health=GET / returns 404; POST /owntracks with {} returns 400; POST valid OwnTracks location returns 200 {"status":"ok"} and DB row.
INV:
arch=Do not configure MQTT; no Mosquitto/MQTT service is part of live path.
security=Do not expose Oracle :8083 directly; Cloudflare Tunnel is the verified public ingress.
security=No app-level Basic auth/token is configured in live Flask service; do not invent credentials.
ops=Cloudflare tunnel credentials/token files exist and must not be printed or committed.
data=DB path is /home/ubuntu/sync_root/db/owntracks.db; unit overrides OWNTRACKS_DB_PATH to this path.
data=Existing real Android historical device is ta; configure OwnTracks Tracker ID tid=ta to continue the same series.
ops=Kuma has no dedicated OwnTracks monitor verified 2026-06-13; do not claim Kuma green as OwnTracks health.
ops=Telegram watchdog code exists but module telegram_notify/telegram_notifiy is missing in venv; watchdog notification is not active.
backup=Oracle backup includes /home/ubuntu and /home/ubuntu/sync_root/db per oracle_backup env; do not manually copy DB into MegaVault.
BUILD:
runtime_python=/home/ubuntu/bots/owntracks_http_server/.venv/bin/python
run=systemctl start owntracks-http-server.service
restart=sudo systemctl restart owntracks-http-server.service
status=systemctl status owntracks-http-server.service --no-pager -l
TEST:
external_valid=TS=$(date -u +%s); curl -sS -i https://owntracks.danielegalati.com/owntracks -H 'Content-Type: application/json' -d "{\"_type\":\"location\",\"tid\":\"CD\",\"tst\":$TS,\"lat\":55.676123,\"lon\":12.568321,\"acc\":12,\"batt\":88}"
local_valid=TS=$(date -u +%s); curl -sS -i http://127.0.0.1:8083/owntracks -H 'Content-Type: application/json' -d "{\"_type\":\"location\",\"tid\":\"CD\",\"tst\":$TS,\"lat\":55.676123,\"lon\":12.568321,\"acc\":12,\"batt\":88}"
db_verify=sqlite3 -header -column /home/ubuntu/sync_root/db/owntracks.db "select id,quando,device,lat,lon,acc,batt from positions order by id desc limit 5;"
log_verify=journalctl -u owntracks-http-server.service --since '5 minutes ago' --no-pager -n 50
cloudflared_verify=systemctl status cloudflared.service --no-pager -l && sudo sed -n '1,80p' /etc/cloudflared/config.yml
verified_2026_06_13=external POST returned HTTP/2 200; DB positions id=321333 device=CD quando=2026-06-13T02:53:34Z; moves id=7341 raw_position_id=321333; PRAGMA quick_check=ok.
DATA:
db=/home/ubuntu/sync_root/db/owntracks.db
wal=/home/ubuntu/sync_root/db/owntracks.db-wal
shm=/home/ubuntu/sync_root/db/owntracks.db-shm
tables=positions,moves
views=km_raw,km_fixed,km_adaptive,km_compare*,km_robust,km_trimmed_05*,km_downsample_3min,km_sample_3min,km_grid_100m_3min
schema_positions=id,quando,device,lat,lon,alt,acc,batt,raw_json
schema_moves=id,quando,device,lat,lon,dist_m,acc,batt,raw_position_id,raw_json
counts_2026_06_13=positions 316837;moves 7324;latest_position 2026-06-13T02:53:34Z test CD
historical_device=ta count=316833 first=2025-12-26T06:27:01Z latest=2026-05-28T13:05:04Z
APP_CONFIG:
mode=HTTP
url=https://owntracks.danielegalati.com/owntracks
host_port_path=host owntracks.danielegalati.com;scheme https;implicit port 443;path /owntracks
username=blank/not_required
password=blank/not_required
token=none
auth=disabled unless app requires toggling with blank credentials
tls=Cloudflare HTTPS public edge; no custom certificate required in Android
device_id=recommended ta or Android phone name; server does not require it but OwnTracks may send X-Limit-D when set
tracker_id=ta required to continue existing DB device series because server persists tid when device absent
monitoring=Significant Changes recommended for normal use; Move for short smoke/debug only
locator_interval=900s practical default/history cadence; can lower temporarily for test then restore
locator_displacement=150m practical battery-friendly starting point; server movement threshold is 50m/adaptive but app controls upload cadence
permissions=Location allowed all the time; precise location enabled; background location allowed; notifications allowed so foreground/service status remains visible
battery=disable Android battery optimization/restriction for OwnTracks; allow background activity/data; do not force-stop app
DNB:
dnb=Do not ask user to remember old endpoint; derive from /etc/cloudflared/config.yml and service unit.
dnb=Do not print cloudflared tunnel token, credentials-file contents, Datasette secret, or any Telegram/Kuma tokens.
dnb=Do not rotate secrets for this recovery unless endpoint ownership is compromised.
dnb=Do not open firewall 8083 as a shortcut; Cloudflare Tunnel is the intended public endpoint.
dnb=Do not treat 404 on GET / as failure; route supports POST /owntracks only.
BUG:
issue=OwnTracks Android reinstall lost config; last real historical device ta row before recovery was 2026-05-28T13:05:04Z.
issue=Telegram watchdog path logs "[WARN] telegram_notify non trovato"; notification side effect inactive.
issue=No dedicated health endpoint; use POST empty/valid and DB verification.
RISK:
risk=Endpoint currently has no app-level auth; trigger=public hostname known; mitigation=keep hostname private, consider adding auth/token only with coordinated Android config change.
risk=Cloudflare token visible in process args for cloudflared-datasette.service; unrelated to OwnTracks tunnel but do not print tokens in reports.
risk=SQLite WAL files grow with ingest; mitigation=monitor root free space and backup; Oracle root was 87% used on 2026-06-13.
risk=Move monitoring drains phone battery; mitigation=use Significant Changes for normal use and disable Android battery optimization.
SECURITY:
public_endpoint=https://owntracks.danielegalati.com/owntracks
secrets=none required for OwnTracks app; Cloudflare credentials local only at /etc/cloudflared/config.yml referenced credentials-file and /root/.cloudflared/*.json.
auth=Flask route has no Basic auth/token check.
OBSERVABILITY:
systemd=owntracks-http-server.service enabled active/running since 2026-06-01T12:39:22Z at prompt 739284.
ports=8083 Flask local/tunnel target;3001 Kuma push-only public;80 Nginx Datasette;3002 Kuma localhost.
logs=journalctl -u owntracks-http-server.service; cloudflared logs via journalctl -u cloudflared.service.
kuma=No OwnTracks monitor found in Kuma DB by owntracks/track name query; Telegram notification table query returned no useful OwnTracks binding.
ROAD:
now=Reconfigure Android HTTP URL and tid=ta; verify with manual publish/log/DB.
next=Add explicit /healthz route only if service code change/restart is acceptable; current zero-write health is POST {} -> 400 plus valid POST -> DB.
later=Consider Basic auth or path token and update Android URL atomically if endpoint secrecy is insufficient.
LINK:
meta=../../../owntracks-watcher/dev/project.metadata.json
human=../../human/projects/owntracks-watcher/overview.md
legacy=../../../owntracks-watcher/dev/legacy
repo=../../../owntracks-watcher
oracle_kuma=oracle-uptime-kuma.md
OPEN:
open=Exact pre-reinstall Android Device ID value is not stored in DB; only persisted device series is tid/device value ta.
open=No local/remote Git remote exists for placeholder repo /home/daniele/codex-workspace/owntracks-watcher; MegaVault doc is synced, runtime lives on Oracle VM.

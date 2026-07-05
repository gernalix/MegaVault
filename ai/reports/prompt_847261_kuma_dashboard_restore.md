# Prompt 847261 Kuma Dashboard Restore

META:
prompt=847261
date=2026-06-15
scope=Oracle_Uptime_Kuma;runtime_restore;Nginx_proxy;MegaVault_docs
host=ubuntu@150.230.148.128;hostname=instance-20260201-1126
protocol=MEGAVAULT_PROTOCOL.md:v11

ROOT_CAUSE:
cause=Nginx push-only hardening from prompt_458217 intentionally returned 403 for every public path except ^/api/push/.
exact_file=/etc/nginx/sites-available/uptime-kuma-push-only.conf
exact_directive=location / { return 403; }
excluded=Kuma_down no;filesystem_permissions no;SELinux no;AppArmor no;ufw no;iptables no;wrong_root_or_alias no;auth_basic no;allow_deny_ip no;missing_index no;Kuma_proxy_reachability no.

ARCHITECTURE:
install=Docker Compose
path=/opt/uptime-kuma
compose=/opt/uptime-kuma/docker-compose.yml
container=uptime-kuma
image=louislam/uptime-kuma:2.3.2
bind=127.0.0.1:3002->container:3001
public_proxy=Nginx listens 0.0.0.0:3001 and [::]:3001
systemd=nginx.service active;docker.service active;uptime-kuma.service absent
db=/opt/uptime-kuma/data/kuma.db

BACKUP:
backup_dir=/opt/uptime-kuma/backups/prompt-847261-20260615T073304Z
files=kuma.db,docker-compose.yml,nginx-etc.tgz,iptables-save.before,iptables-rules.v4,SHA256SUMS
verify=backup DB PRAGMA integrity_check ok;nginx -t successful before reload

CHANGES:
remote_file=/etc/nginx/sites-available/uptime-kuma.conf;change=new full reverse proxy to http://127.0.0.1:3002 for all paths with WebSocket upgrade headers and long read timeout.
remote_file=/etc/nginx/sites-enabled/uptime-kuma.conf;change=new symlink enabled.
remote_file=/etc/nginx/sites-enabled/uptime-kuma-push-only.conf;change=removed symlink to stop 403 catch-all.
remote_file=/etc/nginx/sites-available/uptime-kuma-push-only.conf;change=left on disk inside full nginx backup only;not enabled.
db_changes=none
monitor_changes=none
user_changes=none
token_changes=none

VALIDATION:
curl_localhost=http://localhost:3001/ 302 Location:/dashboard; http://localhost:3001/dashboard 200 OK
curl_127=http://127.0.0.1:3001/ 302 Location:/dashboard; http://127.0.0.1:3001/dashboard 200 OK
curl_public=http://150.230.148.128:3001/ 302 Location:/dashboard; http://150.230.148.128:3001/dashboard 200 OK
push_compatibility=http://150.230.148.128:3001/api/push/invalid returned Kuma JSON 404 Monitor not found or not active
socketio=http://150.230.148.128:3001/socket.io/?EIO=4&transport=polling returned 200 and sid/upgrades websocket
browser=google-chrome headless public /dashboard rendered title "Uptime Kuma - Login" with Username Password Remember me Log in
db=sudo sqlite3 -readonly /opt/uptime-kuma/data/kuma.db returned integrity ok, users=1, monitors=16, heartbeats=34969, active_monitors=15
history=latest heartbeat rows present for all monitors; monitor 12 Mint Freeze Analysis status up with children up during validation
docker_exec=sudo docker exec uptime-kuma true returned rc=0

RISK:
risk=public dashboard is now exposed over plain HTTP on port 3001; this satisfies prompt_847261 but weakens prompt_458217 hardening.
mitigation=Kuma remains localhost-bound behind Nginx, DB/users/tokens preserved, and /api/push compatibility preserved; future stronger fix should use HTTPS/domain or restricted source access instead of push-only 403.
risk=old disabled file name uptime-kuma-push-only.conf could confuse future operators if re-enabled.
mitigation=enabled symlink now points to uptime-kuma.conf; docs updated to canonical full proxy path.

COMMANDS_SUMMARY:
commands=read MEGAVAULT_PROTOCOL/HOST_PROFILE/oracle-uptime-kuma docs; ssh live diagnostics; curl public/local matrix; systemctl/docker/ss/firewall/nginx/log/sqlite checks; sqlite .backup; tar nginx; iptables-save; write Nginx full proxy; nginx -t; systemctl reload nginx; curl/browser/db validation.

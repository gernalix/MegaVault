# Prompt 458217 Kuma Hardening

META:
prompt=458217
date=2026-06-12
scope=Oracle_Uptime_Kuma;runtime_hardening;MegaVault_docs
protocol=MEGAVAULT_PROTOCOL.md:v8
host=ubuntu@150.230.148.128;hostname=instance-20260201-1126

CAUSE:
cause=CASO_2 confirmed: Uptime Kuma admin UI was publicly reachable over plain HTTP on http://150.230.148.128:3001; / redirected to /dashboard and /dashboard returned 200.
tls_blocker=80 returned No route to host and 443 timed out from the Internet; reverse proxy HTTPS with public CA is not deployable without Oracle VCN/domain/TLS changes.
compatibility_constraint=existing push monitors use http://150.230.148.128:3001/api/push/<token>; changing or blocking the whole port would break current heartbeat estate.

SOLUTION:
chosen=localhost_admin_plus_push_only_nginx_proxy
admin=Kuma container binds only 127.0.0.1:3002 on VM; admin access requires SSH tunnel and local browser http://127.0.0.1:3001.
public=nginx listens on public :3001 and proxies only ^/api/push/ to 127.0.0.1:3002; all other paths return 403.
reason=best available mix of security, reliability, low resource use, Oracle VM compatibility, and zero push URL migration while 80/443 are unavailable.
not_chosen_https=needs reachable 80/443 or another certificate/domain path; not available in current VM/VCN state.
not_chosen_tailscale=remote VM has no Tailscale installed/configured; would require auth/install and updating pushers; higher operational churn.

BACKUP:
backup_dir=/opt/uptime-kuma/backups/prompt-458217-20260612T191449Z
files=kuma.db,docker-compose.yml,nginx-etc.tgz,iptables-rules.v4,iptables-save.before,SHA256SUMS
db_backup=sqlite .backup of /opt/uptime-kuma/data/kuma.db
verify=backup DB PRAGMA integrity_check ok; SHA256SUMS verified for kuma.db,docker-compose.yml,nginx-etc.tgz
root_space_before_after=/dev/sda1 45G used=37G avail=8.3G use=82%

CHANGES:
remote_file=/opt/uptime-kuma/docker-compose.yml;change=ports changed from 3001:3001 to 127.0.0.1:3002:3001; image healthcheck disabled due preexisting docker exec/runc failure; data volume unchanged.
remote_file=/etc/nginx/sites-available/uptime-kuma-push-only.conf;change=new server on :3001 proxies only /api/push/ to 127.0.0.1:3002 and returns 403 otherwise.
remote_file=/etc/nginx/sites-enabled/uptime-kuma-push-only.conf;change=symlink enabled.
remote_file=/etc/iptables/rules.v4;change=added INPUT allow for tcp dport 3001 before reject so host-level Nginx can receive existing public push traffic.
runtime=nginx reload; docker compose recreate uptime-kuma; docker daemon restart attempted to clear docker exec failure but failure persisted.
db_changes=none;monitor_changes=none;token_changes=none;telegram_changes=none

TESTS:
public_admin_root=curl http://150.230.148.128:3001/ returned 403 Forbidden from nginx.
public_admin_dashboard=curl http://150.230.148.128:3001/dashboard returned 403 Forbidden from nginx.
public_push_route_invalid=curl /api/push/invalid returned Kuma JSON 404 Monitor not found or not active, proving proxy routing to Kuma.
valid_push=redacted SOFTWARE_AUDIT_KUMA_PUSH_URL returned HTTP 200 and ok=true.
admin_tunnel=ssh control tunnel 13002:127.0.0.1:3002 then curl http://127.0.0.1:13002/dashboard returned 200 OK.
local_app=curl http://127.0.0.1:3002/dashboard on VM returned 200 OK.
db=sudo sqlite3 -readonly /opt/uptime-kuma/data/kuma.db PRAGMA integrity_check returned ok.
runtime_bind=Kuma docker-proxy listens 127.0.0.1:3002 only; Nginx listens 0.0.0.0:3001 and [::]:3001.
ports=80 No route to host;443 timed out;3001 reachable.
notifications=notification table count 1; monitor_notification links count 15; notification config not printed.

ROLLBACK:
rollback_available=yes
rollback_steps=restore /opt/uptime-kuma/backups/prompt-458217-20260612T191449Z/docker-compose.yml to /opt/uptime-kuma/docker-compose.yml; restore nginx from nginx-etc.tgz or remove uptime-kuma-push-only symlink/file; restore /etc/iptables/rules.v4 and run netfilter-persistent reload; docker compose up -d; systemctl reload nginx; verify desired exposure.
db_restore=not needed because DB was not modified; DB backup exists for safety.

OBSERVED_ISSUES:
issue=docker exec inside uptime-kuma fails with OCI runtime exec failed: runc did not terminate successfully: exit status 255; observed before and after docker restart/recreate.
mitigation=image healthcheck disabled to avoid false Docker unhealthy/log spam; Kuma health now verified by HTTP, DB integrity, and push tests.
issue=readonly live DB showed active push count 14 and disabled push count 1; rsync-transfer id2 and codex-token-watcher id10 are active despite older docs saying disabled.
mitigation=not modified because prompt forbade monitor changes; documented as live drift.
residual=public push endpoint remains HTTP for compatibility; admin credentials no longer traverse public HTTP. Full push-token HTTPS migration requires VCN/domain/TLS work.

FINAL:
admin_url=http://127.0.0.1:3001 after SSH tunnel -L 3001:127.0.0.1:3002
public_http_admin_exposure=blocked;root/dashboard return 403.
push_compatibility=preserved on http://150.230.148.128:3001/api/push/<token>
state=Kuma app running;DB ok;push ok;Telegram bindings unchanged;MegaVault updated.

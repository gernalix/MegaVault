# Prompt 672184 Kuma OCI Exec Fix
scope=Oracle VM Uptime Kuma;docker_exec;runc;containerd;journald_runtime
host=ubuntu@150.230.148.128
runtime=/opt/uptime-kuma
evidence_remote=/home/ubuntu/maintenance-672184/logs
evidence_local=/home/daniele/codex-workspace/prompt-672184-evidence

CAUSE:
real_cause=/run tmpfs exhausted by volatile systemd journal under /run/log/journal
pre_fix=/run tmpfs 96M used=96M avail=0 use=100%;/run/log/journal=95M
symptom=docker exec uptime-kuma true/id/pwd failed consistently rc=128 with OCI runtime exec failed: runc did not terminate successfully: exit status 255
historical_trigger=2026-06-11 Docker journal showed runc write /tmp/runc-process... no space left on device plus Docker json log writes no space left during root disk pressure
not_cause=root filesystem current free before fix was 8.3G and inodes 7%;/tmp writable;/var/lib/docker small;Kuma DB integrity ok;container namespaces valid;nsenter true rc=0

REPRO:
cmd=sudo docker exec uptime-kuma true
frequency=5/5 failed before fix;id and pwd also failed;only running container was uptime-kuma
container=uptime-kuma c79d88e5f4d49d429d21deac47a7fa68720905fe64d6eecdbc799e48deff5cdb image=louislam/uptime-kuma:2.3.2
conditions=/run full;Docker/containerd/runc exec path needs runtime tmp/FIFO/state under /run while existing container process keeps serving HTTP

DOCKER_STATE:
docker=29.5.2
containerd=2.2.4
runc=1.3.5
storage_driver=overlayfs io.containerd.snapshotter.v1
systemd=docker active;containerd active;systemd-journald active

KUMA_STATE:
compose=/opt/uptime-kuma/docker-compose.yml
mount=/opt/uptime-kuma/data:/app/data
readonly_rootfs=false
healthcheck=disabled from prior hardening because docker exec was broken
app_http=127.0.0.1:3002/dashboard HTTP 200 after fix
db=/opt/uptime-kuma/data/kuma.db integrity ok
admin_public=root/dashboard on 150.230.148.128:3001 return 403
push_proxy=/api/push/invalid-codex-probe returns Kuma JSON 404 through public Nginx proxy
admin_tunnel=local ssh -L 3003:127.0.0.1:3002 returned HTTP 200

FIX:
changed=/etc/systemd/journald.conf.d/90-runtime-run-limit.conf
content=RuntimeMaxUse=32M;RuntimeKeepFree=32M;RuntimeMaxFileSize=8M
actions=backup existing dropin state;write dropin;restart systemd-journald;rotate/vacuum /run/log/journal to 32M
post_fix=/run tmpfs 96M used=26M avail=71M use=27%;/run/log/journal=25M
docker_exec_after=sudo docker exec uptime-kuma true/id/pwd rc=0
ctr_exec_after=sudo ctr -n moby tasks exec ... true rc=0

ROLLBACK:
journald_backup=/home/ubuntu/maintenance-672184/before/journald-20260612T195948Z
rollback_cmd=remove /etc/systemd/journald.conf.d/90-runtime-run-limit.conf or restore backup then systemctl restart systemd-journald
kuma_backup_existing=/opt/uptime-kuma/backups/prompt-458217-20260612T191449Z
data_loss=none;Kuma DB/compose/container config not modified

OBSERVATIONS:
oracle_backup=automatic oracle-backup.service started 2026-06-12T20:01:20Z during verification;remote OCI skipped due StorageLimitExceeded cooldown;local fallback /var/lib/oracle_backup/emergency_repo active
root_after=/ rose to 94%/3.1G free during active backup;separate oracle-backup capacity risk, not caused by journald fix
backup_policy=do not interrupt active oracle-backup.service casually;do not delete emergency_repo while remote OCI remains degraded

TESTS:
test=docker exec uptime-kuma true/id/pwd -> pass
test=ctr tasks exec true -> pass
test=DB PRAGMA integrity_check -> ok
test=HTTP local dashboard -> 200
test=public admin root/dashboard -> 403
test=public push proxy invalid token -> JSON 404 from Kuma
test=SSH local tunnel -> HTTP 200 on forwarded dashboard
test=journal docker/containerd after fix -> no OCI/no space entries in checked window

# Troubleshooting

```bash
ssh -i /home/daniele/codex-workspace/projects/vm_oracle/ssh-key-2026-02-01.key ubuntu@150.230.148.128
sudo docker ps --filter name=uptime-kuma
sudo sqlite3 -header -column /opt/uptime-kuma/data/kuma.db "select id,name,type,active,parent from monitor order by id;"
```

Token:

- Non stampare e non committare gli URL `/api/push/<token>`.
- Lato Mint sono in `~/.config/mint-freeze-forensics/kuma.env`.

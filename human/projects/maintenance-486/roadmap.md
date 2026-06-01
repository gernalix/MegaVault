# maintenance-486 Roadmap

## Segnali dal codice
- no tests detected by static scan
- data/storage rules absent from active code

## Debito/rischi da considerare
- scripts/ssh_diag_486.sh:2:set -euo pipefail
- scripts/ssh_diag_486.sh:10:timeout 10 nc -vz "$host" 22 // true
- scripts/ssh_diag_486.sh:13:timeout 12 bash -lc "exec 3<>/dev/tcp/$host/22; IFS= read -r -t 8 line <&3; printf '%s\n' \"\$line\"" // true
- scripts/ssh_diag_486.sh:16:timeout 35 ssh \
- scripts/ssh_diag_486.sh:18:-o ConnectTimeout=12 \

# surface-recovery-hardening Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
| source | fact |
|---|---|
| `dev/legacy/reports/prompt684_did_error_20260514_070407/FINAL_REPORT.md` | - `transfer_vecchio_disco_phase2_limited.sh`: next safe start defaults to `BW_LIMIT=5120` and adds `--timeout=900`. |
| `dev/legacy/reports/prompt684_did_error_20260514_070407/user_services_status.txt` | ● transfer-vecchio-disco-adaptive-throttle.service - Adaptive conservative throttle for transfer_vecchio_disco phase 2 |
| `scripts/memory_pressure_guardian.sh` | local row priority rss_mb pid comm cmd total_rss_mb=0 |
| `scripts/memory_pressure_guardian.sh` | while IFS=$'\t' read -r priority rss_mb pid comm cmd; do |
| `scripts/memory_pressure_guardian.sh` | [[ "$lcomm" =~ ^(node/python/python3/npm/pnpm/vite/webpack/next/tsserver)$ // "$lcmd" == *"node "* // "$lcmd" == *"python"* ]] // return 1 |
| `scripts/memory_pressure_guardian.sh` | function print_candidate(priority, rss_mb, pid, comm, cmd) { |
| `scripts/memory_pressure_guardian.sh` | printf "%s\t%s\t%s\t%s\t%s\n", priority, rss_mb, pid, comm, cmd |
| `scripts/memory_pressure_guardian.sh` | if (pid !~ /^[0-9]+$/ // rss !~ /^[0-9]+$/) next |
| `scripts/memory_pressure_guardian.sh` | if (protected_process(pid, lcomm, lcmd)) next |
| `scripts/memory_pressure_guardian.sh` | } else if (rss_mb >= codex_min && lcmd ~ /codex/ && (lcomm ~ /^(node/python/python3/npm/pnpm/vite/webpack/next/tsserver)$/ // lcmd ~ /node /python/)) { |
| `scripts/memory_pressure_guardian.sh` | local row priority rss_mb pid comm cmd count=0 |
| `scripts/memory_pressure_guardian.sh` | local kill_severity="${1:-PRE_EMERGENCY}" max_kills="${2:-$MAX_CRITICAL_GRADLE_KILLS}" row priority rss_mb pid comm cmd killed=0 |
| `scripts/transfer_vecchio_disco_phase2_limited.sh` | next |

## Deferred Or Risky Work
- dev/legacy/docs/TROUBLESHOOTING.md: journalctl -k --since '30 minutes ago' --no-pager / grep -Ei 'JBD2/EXT4-fs.*error/aborting journal/read-only/Buffer I/O/device offline/disconnect/DID_ERROR/I/O error/reset SuperSpeed'
- dev/legacy/reports/prompt684_did_error_20260514_070407/FINAL_REPORT.md: - data integrity risk: medium. A read-side `DID_ERROR` on destination while ext4 remains mounted rw is serious, but there is no evidence of journal abort, read-only remount, disconnect, or
- dev/legacy/reports/prompt684_did_error_20260514_070407/FINAL_REPORT.md: - freeze/system stability risk: medium-high during active transfer. The event coincided with high PSI/load; rsync is now stopped so immediate freeze risk is reduced.
- dev/legacy/reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt: May 10 11:24:55 daniele-Surface-Pro kernel: device offline error, dev sdc, sector 0 op 0x1:(WRITE) flags 0x800 phys_seg 0 prio class 2
- dev/legacy/reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt: May 10 11:24:57 daniele-Surface-Pro kernel: device offline error, dev sdc, sector 5859706880 op 0x1:(WRITE) flags 0x809800 phys_seg 1 prio class 2
- dev/legacy/reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt: May 10 11:24:57 daniele-Surface-Pro kernel: Buffer I/O error on dev sdc1, logical block 732463104, lost sync page write
- dev/legacy/reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt: May 10 11:24:57 daniele-Surface-Pro kernel: JBD2: I/O error when updating journal superblock for sdc1-8.
- dev/legacy/reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt: May 10 11:26:19 daniele-Surface-Pro kernel: EXT4-fs warning (device sdc1): htree_dirblock_to_tree:1051: inode #2: lblock 0: comm gvfs-udisks2-vo: error -5 reading
- dev/legacy/reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt: May 10 11:26:20 daniele-Surface-Pro kernel: EXT4-fs warning (device sdc1): htree_dirblock_to_tree:1051: inode #2: lblock 0: comm gvfs-udisks2-vo: error -5 reading
- dev/legacy/reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt: May 10 11:27:40 daniele-Surface-Pro kernel: Buffer I/O error on dev dm-0, logical block 0, async page read
- dev/legacy/reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt: May 10 14:31:58 daniele-Surface-Pro kernel: Buffer I/O error on dev dm-0, logical block 0, async page read
- dev/legacy/reports/prompt734_post_crash_20260510_222255/previous_boot_kernel_filtered_usb_io.txt: May 10 14:31:58 daniele-Surface-Pro kernel: Buffer I/O error on dev dm-0, logical block 1, async page read

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.

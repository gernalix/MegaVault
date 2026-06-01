# maintenance-486 Roadmap

Roadmap items are extracted from legacy roadmap, changelog, TODO, operations, and troubleshooting material. Dates are only included when they were present in source text.

## Active Or Near-Term Work
| source | fact |
|---|---|
| `dev/legacy/reports/prompt-486-report.md` | `ssh.service` was not restarted; it received runtime and persistent resource priority settings. |

## Deferred Or Risky Work
- dev/legacy/reports/prompt-486-report.md: - OCI object storage remains quota-blocked with `StorageLimitExceeded`; remote backup is still degraded.

## Practical Priority
- First preserve the invariants listed in the AI doc.
- Then resolve active bugs/regressions from troubleshooting evidence.
- Only then expand features or release workflows.

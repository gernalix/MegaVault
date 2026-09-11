#!/usr/bin/env python3
from __future__ import annotations

import sys

from ai.strict_tag_wrapper import *  # noqa: F401,F403
from ai.strict_tag_wrapper import main as _core_main
from ai.operational_indexes import dispatch as _dispatch_operational
from ai.operational_indexes import migrate_operational_indexes


def main(argv=None):
    args = list(sys.argv[1:] if argv is None else argv)
    # Operational-index commands are intentionally handled before the core CLI.
    operational_result = _dispatch_operational(args)
    if operational_result is not None:
        return operational_result

    result = _core_main(args)
    if result == 0 and args and args[0] == "migrate":
        return migrate_operational_indexes()
    return result


if __name__ == "__main__":
    raise SystemExit(main())

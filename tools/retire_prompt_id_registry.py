#!/usr/bin/env python3
"""Freeze MegaVault's prompt registry as historical evidence after C3 readback."""
from contextlib import closing
from datetime import datetime, timezone
import fcntl
import hashlib
import json
from pathlib import Path
import sqlite3

TABLES = ('prompt_id_registry', 'prompt_id_events', 'prompt_id_allocation_requests')


def freeze(conn, c3_db):
    if not conn.in_transaction:
        raise ValueError('retirement_transaction_required')
    with closing(sqlite3.connect(Path(c3_db).resolve().as_uri() + '?mode=ro', uri=True)) as c3:
        authority = c3.execute("SELECT value FROM meta WHERE key='prompt_id_authority'").fetchone()
        if authority != ('C3',):
            raise ValueError('successor_authority_unverified')
        reserved = {row[0] for row in c3.execute('SELECT prompt_id FROM prompt_id_registry')}
    historical = {row[0] for row in conn.execute('SELECT prompt_id FROM prompt_id_registry')}
    if not historical <= reserved:
        raise ValueError('successor_missing_historical_ids')
    for table in TABLES:
        for action in ('INSERT', 'UPDATE'):
            conn.execute(f'''CREATE TRIGGER IF NOT EXISTS prompt_id_c3_readonly_{table}_{action.lower()}
                BEFORE {action} ON {table} BEGIN SELECT RAISE(ABORT,'PROMPT_ID_AUTHORITY_C3'); END''')
    return {'status': 'retired_readonly', 'historical_ids': len(historical), 'c3_reserved_ids': len(reserved)}


def migrate():
    source = Path.home() / 'MegaVault/megavault.sqlite'
    c3 = Path.home() / '.local/state/c3-control/roadmap.sqlite'
    lock_path = Path.home() / '.local/state/megavault/canonical-update.lock'
    lock_path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    with lock_path.open('a') as lock:
        fcntl.flock(lock, fcntl.LOCK_EX | fcntl.LOCK_NB)
        stamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%S.%fZ')
        directory = c3.parent / 'backups'
        directory.mkdir(parents=True, exist_ok=True, mode=0o700)
        backup = directory / ('megavault-prompt-retirement-' + stamp + '.sqlite')
        with closing(sqlite3.connect(source)) as conn:
            with closing(sqlite3.connect(backup)) as saved:
                conn.backup(saved)
                if saved.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
                    raise ValueError('backup_invalid')
            backup.chmod(0o600)
            manifest = {'backup': str(backup), 'sha256': hashlib.sha256(backup.read_bytes()).hexdigest(), 'integrity_check': 'ok'}
            backup.with_suffix('.json').write_text(json.dumps(manifest, sort_keys=True) + '\n')
            conn.execute('BEGIN IMMEDIATE')
            try:
                result = freeze(conn, c3)
                if conn.execute('PRAGMA foreign_key_check').fetchall() or conn.execute('PRAGMA integrity_check').fetchone()[0] != 'ok':
                    raise ValueError('retirement_integrity_failed')
                conn.commit()
            except Exception:
                conn.rollback()
                raise
        return {'backup': manifest, 'result': result}


if __name__ == '__main__':
    print(json.dumps(migrate(), sort_keys=True))

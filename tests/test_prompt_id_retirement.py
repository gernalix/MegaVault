import sqlite3
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import megavault
from ai import megavault_core
import sys
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / 'tools'))
from retire_prompt_id_registry import freeze


class PromptIdRetirementTests(unittest.TestCase):
    def test_historical_registry_freezes_only_after_successor_gate(self):
        with tempfile.TemporaryDirectory() as tmp:
            c3_path = Path(tmp) / 'c3.sqlite'
            with sqlite3.connect(c3_path) as c3:
                c3.executescript("CREATE TABLE meta(key TEXT,value TEXT); CREATE TABLE prompt_id_registry(prompt_id INTEGER);")
            with sqlite3.connect(':memory:') as conn:
                conn.execute('CREATE TABLE projects(project_id INTEGER PRIMARY KEY)')
                megavault.ensure_prompt_id_schema(conn)
                conn.execute("INSERT INTO prompt_id_registry(prompt_id,source) VALUES(123456,'old')")
                conn.commit()
                conn.execute('BEGIN IMMEDIATE')
                with self.assertRaisesRegex(ValueError, 'successor_authority_unverified'):
                    freeze(conn, c3_path)
                conn.rollback()
                with sqlite3.connect(c3_path) as c3:
                    c3.execute("INSERT INTO meta VALUES('prompt_id_authority','C3')")
                    c3.execute('INSERT INTO prompt_id_registry VALUES(123456)')
                conn.execute('BEGIN IMMEDIATE')
                self.assertEqual('retired_readonly', freeze(conn, c3_path)['status'])
                conn.commit()
                with self.assertRaisesRegex(sqlite3.IntegrityError, 'PROMPT_ID_AUTHORITY_C3'):
                    conn.execute("INSERT INTO prompt_id_registry(prompt_id,source) VALUES(654321,'retired')")
                with self.assertRaisesRegex(sqlite3.IntegrityError, 'PROMPT_ID_AUTHORITY_C3'):
                    conn.execute("UPDATE prompt_id_registry SET status='cancelled' WHERE prompt_id=123456")
                conn.execute('INSERT INTO projects VALUES(99)')

    def test_no_allocator_or_mutating_prompt_id_api_remains(self):
        for name in ('allocate_prompt_id', 'materialize_prompt_id', 'cancel_prompt_id',
                     'mark_prompt_id_used', 'bind_prompt_id_request', 'backfill_prompt_ids'):
            self.assertFalse(hasattr(megavault, name))
            self.assertFalse(hasattr(megavault_core, name))
        with self.assertRaises(SystemExit) as rejected:
            megavault.main(['prompt-id', 'allocate', '--source', 'retired'])
        self.assertEqual(2, rejected.exception.code)

    def test_show_reads_c3_without_fallback_or_writes(self):
        with tempfile.TemporaryDirectory() as tmp:
            home = Path(tmp)
            path = home / '.local/state/c3-control/roadmap.sqlite'
            path.parent.mkdir(parents=True)
            with sqlite3.connect(path) as conn:
                conn.execute('CREATE TABLE prompt_id_registry(prompt_id INTEGER PRIMARY KEY,source TEXT)')
                conn.execute("INSERT INTO prompt_id_registry VALUES(123456,'C3')")
            before = path.read_bytes()
            with patch('ai.megavault_core.Path.home', return_value=home), patch('builtins.print') as output:
                self.assertEqual(0, megavault.main(['prompt-id', 'show', '123456']))
                self.assertIn('C3', output.call_args.args[0])
                self.assertEqual(2, megavault.main(['prompt-id', 'show', '999999']))
            self.assertEqual(before, path.read_bytes())

import sqlite3
import unittest
from ai.megavault_core import retire_permanent_project_ids


class IdentityRetirementTests(unittest.TestCase):
    def setUp(self):
        self.db=sqlite3.connect(':memory:')
        self.addCleanup(self.db.close)
        self.db.executescript("""CREATE TABLE projects(project_id INTEGER PRIMARY KEY,slug TEXT UNIQUE,archived INTEGER);
            CREATE TABLE project_aliases(alias TEXT PRIMARY KEY,project_id INTEGER);
            CREATE TABLE permanent_ids(entity_type TEXT,entity_id INTEGER,canonical_key TEXT,created_at_utc TEXT,retired_at_utc TEXT);
            INSERT INTO projects VALUES(104,'renamed',0);
            INSERT INTO project_aliases VALUES('original',104);
            INSERT INTO permanent_ids VALUES('project',104,'original','historical',NULL);""")

    def test_preserves_identity_alias_and_archive_only_lifetime_without_registry(self):
        self.assertTrue(retire_permanent_project_ids(self.db))
        self.assertFalse(retire_permanent_project_ids(self.db))
        self.assertEqual([(104,'renamed',0)],self.db.execute('SELECT * FROM projects').fetchall())
        self.assertEqual([('original',104)],self.db.execute('SELECT * FROM project_aliases').fetchall())
        for sql in ('DELETE FROM projects WHERE project_id=104','UPDATE projects SET project_id=105'):
            with self.assertRaises(sqlite3.IntegrityError):
                self.db.execute(sql)
        self.db.execute('UPDATE projects SET archived=1')
        self.assertEqual(105,self.db.execute('SELECT MAX(project_id)+1 FROM projects').fetchone()[0])
        self.assertIsNone(self.db.execute("SELECT name FROM sqlite_master WHERE name='permanent_ids'").fetchone())

    def test_unknown_or_lost_historical_identity_fails_closed(self):
        self.db.execute('DELETE FROM project_aliases')
        with self.assertRaisesRegex(ValueError,'identity_not_preserved'):
            retire_permanent_project_ids(self.db)
        self.assertIsNotNone(self.db.execute("SELECT name FROM sqlite_master WHERE name='permanent_ids'").fetchone())
        self.db.execute("INSERT INTO project_aliases VALUES('original',104)")
        self.db.execute("INSERT INTO permanent_ids VALUES('unknown',106,'other','historical',NULL)")
        with self.assertRaisesRegex(ValueError,'identity_not_preserved'):
            retire_permanent_project_ids(self.db)

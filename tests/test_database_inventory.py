import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT))
from ai import database_inventory  # noqa: E402


class DatabaseInventoryTests(unittest.TestCase):
    def make_schema(self, path: Path) -> sqlite3.Connection:
        conn = sqlite3.connect(path)
        conn.executescript(
            """
            PRAGMA foreign_keys=ON;
            CREATE TABLE projects(project_id INTEGER PRIMARY KEY, slug TEXT UNIQUE);
            CREATE TABLE hosts(host_id TEXT PRIMARY KEY, name TEXT);
            CREATE TABLE repositories(
              repository_id TEXT PRIMARY KEY,
              project_id INTEGER REFERENCES projects(project_id),
              host_id TEXT REFERENCES hosts(host_id),
              worktree_path TEXT, remote_url TEXT, canonical INTEGER
            );
            CREATE TABLE data_assets(
              data_asset_id TEXT PRIMARY KEY, project_id INTEGER, host_id TEXT,
              name TEXT, asset_type TEXT, path TEXT, status TEXT, notes TEXT
            );
            CREATE TABLE project_components(
              component_id INTEGER PRIMARY KEY, project_id INTEGER,
              component TEXT, type TEXT, path TEXT, purpose TEXT
            );
            INSERT INTO projects VALUES(1,'example');
            INSERT INTO hosts VALUES('H0001','fedora');
            INSERT INTO hosts VALUES('H0002','oracle-vm');
            """
        )
        return conn

    def git(self, *args: str, cwd: Path | None = None) -> None:
        subprocess.run(["git", *args], cwd=cwd, check=True, stdout=subprocess.DEVNULL)

    def test_signature_detection_ignores_extension(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            real = root / "state.binary"
            with sqlite3.connect(real) as conn:
                conn.execute("create table sample(id integer)")
            fake = root / "fake.sqlite"
            fake.write_text("not sqlite", encoding="utf-8")
            self.assertTrue(database_inventory.is_sqlite_file(real))
            self.assertFalse(database_inventory.is_sqlite_file(fake))

    def test_git_discovery_deduplicates_clones_by_origin(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            origin = root / "origin.git"
            self.git("init", "--bare", str(origin))
            self.git("clone", str(origin), str(root / "clone-a"))
            self.git("clone", str(origin), str(root / "clone-b"))
            repos = database_inventory.discover_git_repositories([root])
            self.assertEqual(1, len(repos))
            self.assertEqual(str((root / "clone-a").resolve()), repos[0]["path"])

    def test_legacy_migration_retires_duplicates_and_preserves_remote(self):
        with tempfile.TemporaryDirectory() as tmp:
            conn = self.make_schema(Path(tmp) / "inventory.sqlite")
            self.addCleanup(conn.close)
            conn.execute(
                "INSERT INTO data_assets VALUES(?,?,?,?,?,?,?,?)",
                ("DATA1", 1, "H0002", "runtime.db", "sqlite_runtime_datasette",
                 "/srv/runtime/runtime.db", "active", "canonical runtime"),
            )
            conn.execute(
                "INSERT INTO project_components VALUES(?,?,?,?,?,?)",
                (7, 1, "database", "sqlite_database", "/mnt/data/app.sqlite", "canonical"),
            )
            migrated = database_inventory.migrate_legacy_inventory(conn)
            self.assertEqual(2, migrated)
            self.assertEqual(0, conn.execute("select count(*) from data_assets").fetchone()[0])
            self.assertEqual(0, conn.execute("select count(*) from project_components").fetchone()[0])
            rows = conn.execute(
                "select source_path,status,datasette_expose,declared from database_inventory order by source_path"
            ).fetchall()
            self.assertEqual(
                [("/mnt/data/app.sqlite", "missing", 0, 1),
                 ("/srv/runtime/runtime.db", "remote_declared", 1, 1)],
                rows,
            )
            changes_after_first = conn.total_changes
            self.assertEqual(0, database_inventory.migrate_legacy_inventory(conn))
            self.assertEqual(changes_after_first, conn.total_changes)

    def test_reconcile_is_idempotent_and_maps_repo_project_host(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            repo = root / "repo"
            self.git("init", str(repo))
            database = repo / "state-without-extension"
            with sqlite3.connect(database) as database_conn:
                database_conn.execute("create table sample(id integer)")
            conn = self.make_schema(root / "inventory.sqlite")
            self.addCleanup(conn.close)
            conn.execute(
                "INSERT INTO repositories VALUES(?,?,?,?,?,1)",
                ("R1", 1, "H0001", str(repo), None),
            )
            first = database_inventory.reconcile(conn, [root])
            changes_after_first = conn.total_changes
            second = database_inventory.reconcile(conn, [root])
            self.assertEqual(first, second)
            self.assertEqual(changes_after_first, conn.total_changes)
            self.assertEqual(1, conn.execute("select count(*) from database_inventory").fetchone()[0])
            row = conn.execute(
                """select project_id,project_slug,repository_id,host_id,db_name,status
                     from database_inventory"""
            ).fetchone()
            self.assertEqual((1, "example", "R1", "H0001", database.name, "present"), row)

    def test_phase_c_decisions_cover_every_row_without_schema_changes(self):
        with tempfile.TemporaryDirectory() as tmp:
            conn = self.make_schema(Path(tmp) / "inventory.sqlite")
            self.addCleanup(conn.close)
            database_inventory.ensure_schema(conn)
            columns_before = [row[1] for row in conn.execute("pragma table_info(database_inventory)")]
            rows = [
                ("DBI-selected", 1, "example", "H0001", "roadmap.sqlite",
                 "/home/daniele/projects/codex-roadmap/roadmap.sqlite", "derived"),
                ("DBI-excluded", 1, "example", "H0001", "History",
                 "/repo/browser-profile/Default/History", "browser"),
                ("DBI-blocked", None, None, "H0001", "peewee-sqlite.v2.db",
                 "/home/daniele/.local/share/activitywatch/aw-server/peewee-sqlite.v2.db", "canonical"),
            ]
            conn.executemany(
                """insert into database_inventory(
                       inventory_id,project_id,project_slug,host_id,db_name,source_path,
                       classification,status,canonical,datasette_expose,sync_to_oracle,declared
                     ) values(?,?,?,?,?,?,?,'present',0,0,0,0)""",
                rows,
            )
            counts, decisions = database_inventory.apply_phase_c_decisions(conn)
            self.assertEqual({"selected": 1, "excluded": 1, "blocked": 1}, counts)
            changes = conn.total_changes
            repeat_counts, repeat_decisions = database_inventory.apply_phase_c_decisions(conn)
            self.assertEqual(counts, repeat_counts)
            self.assertEqual(decisions, repeat_decisions)
            self.assertEqual(changes, conn.total_changes)
            self.assertEqual(columns_before, [row[1] for row in conn.execute("pragma table_info(database_inventory)")])
            plan = database_inventory.build_phase_c_plan(conn, decisions)
            self.assertEqual(["DBI-selected"], [row["inventory_id"] for row in plan["selected"]])
            self.assertEqual(["DBI-blocked"], [row["inventory_id"] for row in plan["unowned_or_blocked"]])
            self.assertEqual(3, len(plan["decisions"]))
            self.assertEqual([], plan["repo_tasks"])


if __name__ == "__main__":
    unittest.main()

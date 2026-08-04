import sqlite3
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT))
import megavault  # noqa: E402

PROTOCOL = ROOT / "ai" / "MEGAVAULT_PROTOCOL.md"


class MegaVaultTests(unittest.TestCase):
    def run_tool(self, *args):
        return subprocess.run(
            ["python3", str(ROOT / "megavault.py"), *args],
            cwd=ROOT,
            text=True,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=False,
        )

    def test_validate_passes(self):
        result = self.run_tool("validate")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("VALIDATE=PASS", result.stdout)

    def test_project_alias_resolves_from_database(self):
        result = self.run_tool("project", "luoghi-app")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("project_id=", result.stdout)
        self.assertIn("slug=luoghi", result.stdout)

    def test_project_id_is_integer_not_prefixed_text(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        value, storage_type = conn.execute(
            "select project_id, typeof(project_id) from projects where slug='luoghi'"
        ).fetchone()
        self.assertIsInstance(value, int)
        self.assertEqual(storage_type, "integer")

    def test_protocol_semantic_guard_detects_critical_removal(self):
        text = PROTOCOL.read_text(encoding="utf-8")
        broken = text.replace("CAPSULIZATION=mandatory_all_projects\n", "", 1)
        errors = megavault.protocol_semantic_errors(broken)
        self.assertIn(
            "protocol_semantic_missing:capsulization:CAPSULIZATION=mandatory_all_projects",
            errors,
        )

    def test_secret_scan_has_zero_hits(self):
        self.assertEqual([], megavault.secret_scan_errors(megavault.git_tracked()))

    def test_sqlite_integrity_and_foreign_keys_pass(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        conn.execute("PRAGMA foreign_keys=ON")
        self.assertEqual("ok", conn.execute("PRAGMA integrity_check").fetchone()[0])
        self.assertEqual([], conn.execute("PRAGMA foreign_key_check").fetchall())

    def test_codex_project_index_has_one_row_per_project(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        project_count = conn.execute("select count(*) from projects").fetchone()[0]
        index_count = conn.execute("select count(*) from codex_project_index").fetchone()[0]
        self.assertEqual(project_count, index_count)
        duplicates = conn.execute(
            """
            select project_id
            from codex_project_index
            group by project_id
            having count(*) <> 1
            """
        ).fetchall()
        self.assertEqual([], duplicates)

    def test_no_ambiguous_canonical_worktree(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        ambiguous = conn.execute(
            """
            select project_id
            from repositories
            where repository_kind='local_worktree' and canonical=1
            group by project_id
            having count(*) > 1
            """
        ).fetchall()
        self.assertEqual([], ambiguous)

    def test_codex_index_resolves_local_project(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        row = conn.execute(
            """
            select project_status, canonical_host, canonical_worktree,
                   repository_kind, canonical_branch, remote_url
            from codex_project_index
            where project_id=23
            """
        ).fetchone()
        self.assertEqual(
            (
                "LOCAL",
                "fedora",
                "/home/daniele/MegaVault",
                "local_worktree",
                "master",
                "https://github.com/gernalix/MegaVault",
            ),
            row,
        )

    def test_codex_index_resolves_remote_deploy(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        row = conn.execute(
            """
            select project_status, runtime_host, runtime_path
            from codex_project_index
            where project_id=42
            """
        ).fetchone()
        self.assertEqual(
            ("LOCAL", "oracle-vm", "/home/ubuntu/sync_root/bots/telegram_insert_bot"),
            row,
        )

    def test_codex_index_classifies_archived_and_legacy_missing(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        archived = conn.execute(
            "select project_status, repository_kind from codex_project_index where project_id=2"
        ).fetchone()
        missing = conn.execute(
            "select project_status, canonical_worktree from codex_project_index where project_id=3"
        ).fetchone()
        self.assertEqual(("ARCHIVED", "legacy"), archived)
        self.assertEqual(("MISSING", None), missing)

    def test_codex_index_uses_deterministic_project_statuses(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        statuses = {
            row[0]
            for row in conn.execute("select distinct project_status from codex_project_index")
        }
        self.assertLessEqual(statuses, {"LOCAL", "REMOTE_ONLY", "MISSING", "ARCHIVED"})
        generic = conn.execute(
            """
            select project_id
            from codex_project_index
            where project_status not in ('LOCAL', 'REMOTE_ONLY', 'MISSING', 'ARCHIVED')
            """
        ).fetchall()
        self.assertEqual([], generic)

    def test_codex_index_resolves_remote_only_projects(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        rows = conn.execute(
            """
            select project_id, project_status, canonical_host, canonical_worktree,
                   runtime_host, runtime_path, canonical_branch
            from codex_project_index
            where project_id in (31, 33, 44, 45)
            order by project_id
            """
        ).fetchall()
        self.assertEqual(
            [
                (31, "REMOTE_ONLY", "oracle-vm", None, "oracle-vm", "/opt/uptime-kuma", None),
                (
                    33,
                    "REMOTE_ONLY",
                    "oracle-vm",
                    None,
                    "oracle-vm",
                    "/home/ubuntu/bots/owntracks_http_server",
                    "main",
                ),
                (
                    44,
                    "REMOTE_ONLY",
                    "windows-host",
                    None,
                    "windows-host",
                    r"C:\Users\seste\Documents\windows\system_logger",
                    None,
                ),
                (
                    45,
                    "REMOTE_ONLY",
                    "windows-host",
                    None,
                    "windows-host",
                    r"C:\Users\seste\Documents\windows\maintenance",
                    None,
                ),
            ],
            rows,
        )

    def test_codex_retrieval_views_are_compact_and_status_scoped(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        expected = {
            "codex_work_queue": 21,
            "codex_remote_projects": 4,
            "codex_missing_projects": 7,
            "codex_archived_projects": 20,
        }
        for view_name, count in expected.items():
            actual = conn.execute(f"select count(*) from {view_name}").fetchone()[0]
            self.assertEqual(count, actual, view_name)

        work_statuses = {
            row[0] for row in conn.execute("select distinct project_status from codex_work_queue")
        }
        self.assertEqual({"LOCAL", "REMOTE_ONLY"}, work_statuses)
        work_columns = [
            row[1] for row in conn.execute("PRAGMA table_info(codex_work_queue)")
        ]
        self.assertEqual(
            [
                "project_id",
                "slug",
                "project_status",
                "canonical_host",
                "canonical_worktree",
                "runtime_host",
                "runtime_path",
                "canonical_branch",
                "remote_url",
            ],
            work_columns,
        )

    def test_project_retrieval_cli_commands(self):
        work_queue = self.run_tool("project-work-queue")
        self.assertEqual(work_queue.returncode, 0, work_queue.stderr)
        work_lines = work_queue.stdout.strip().splitlines()
        self.assertEqual(21, len(work_lines))
        self.assertTrue(work_lines[0].startswith("project_id=1;slug=amici-fb;"))
        self.assertIn("project_status=LOCAL", work_lines[0])
        self.assertNotIn("project_status=MISSING", work_queue.stdout)
        self.assertNotIn("project_status=ARCHIVED", work_queue.stdout)

        remote = self.run_tool("project-remote")
        self.assertEqual(remote.returncode, 0, remote.stderr)
        remote_lines = remote.stdout.strip().splitlines()
        self.assertEqual(4, len(remote_lines))
        self.assertTrue(all("project_status=REMOTE_ONLY" in line for line in remote_lines))

        missing = self.run_tool("project-missing")
        self.assertEqual(missing.returncode, 0, missing.stderr)
        missing_lines = missing.stdout.strip().splitlines()
        self.assertEqual(7, len(missing_lines))
        self.assertEqual(
            "project_id=3;slug=android-app-template;project_status=MISSING",
            missing_lines[0],
        )

        archived = self.run_tool("project-archived")
        self.assertEqual(archived.returncode, 0, archived.stderr)
        archived_lines = archived.stdout.strip().splitlines()
        self.assertEqual(20, len(archived_lines))
        self.assertEqual("project_id=2;slug=android;project_status=ARCHIVED", archived_lines[0])

    def test_project_path_cli(self):
        resolved = self.run_tool("project-path", "23")
        self.assertEqual(resolved.returncode, 0, resolved.stderr)
        self.assertEqual("/home/daniele/MegaVault", resolved.stdout.strip())

        missing = self.run_tool("project-path", "3")
        self.assertNotEqual(missing.returncode, 0)
        self.assertIn("PROJECT_PATH=ABSENT", missing.stderr)

        remote = self.run_tool("project-path", "31")
        self.assertNotEqual(remote.returncode, 0)
        self.assertIn("PROJECT_PATH=ABSENT", remote.stderr)

    def test_project_path_status_cli(self):
        local = self.run_tool("project-path", "--status", "23")
        self.assertEqual(local.returncode, 0, local.stderr)
        self.assertEqual("LOCAL", local.stdout.strip())

        remote = self.run_tool("project-path", "--status", "31")
        self.assertEqual(remote.returncode, 0, remote.stderr)
        self.assertEqual("REMOTE_ONLY", remote.stdout.strip())

        missing = self.run_tool("project-path", "--status", "3")
        self.assertEqual(missing.returncode, 0, missing.stderr)
        self.assertEqual("MISSING", missing.stdout.strip())

        absent = self.run_tool("project-path", "--status", "99999")
        self.assertNotEqual(absent.returncode, 0)
        self.assertEqual("ABSENT", absent.stdout.strip())

    def test_project_index_migration_is_idempotent_and_preserves_counts(self):
        source = sqlite3.connect(ROOT / "megavault.sqlite")
        with tempfile.TemporaryDirectory() as tmp:
            copy_path = Path(tmp) / "megavault-copy.sqlite"
            copy = sqlite3.connect(copy_path)
            source.backup(copy)
            copy.close()

            conn = sqlite3.connect(copy_path)
            conn.execute("PRAGMA foreign_keys=ON")
            tables = (
                "projects",
                "project_aliases",
                "repositories",
                "hosts",
                "services",
                "data_assets",
                "incidents",
                "incident_events",
                "tags",
                "tag_aliases",
                "incident_tags",
                "events",
            )
            before = {
                table: conn.execute(f"select count(*) from {table}").fetchone()[0]
                for table in tables
            }
            self.assertFalse(megavault.migrate_project_index_schema(conn))
            after_first = {
                table: conn.execute(f"select count(*) from {table}").fetchone()[0]
                for table in tables
            }
            self.assertEqual(before, after_first)
            self.assertFalse(megavault.migrate_project_index_schema(conn))
            after_second = {
                table: conn.execute(f"select count(*) from {table}").fetchone()[0]
                for table in tables
            }
            self.assertEqual(before, after_second)
            self.assertEqual([], conn.execute("PRAGMA foreign_key_check").fetchall())

    def test_current_incident_taxonomy_is_migrated(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        incident_ids = [
            row[0] for row in conn.execute("select incident_id from incidents order by incident_id")
        ]
        self.assertEqual(list(range(1, 29)), incident_ids)
        self.assertEqual(
            28,
            conn.execute(
                """
                select count(*)
                from incidents i
                where exists (
                  select 1 from incident_tags it where it.incident_id=i.incident_id
                )
                """
            ).fetchone()[0],
        )
        expected = {
            16: {"whatsapp", "notifications", "pixel", "metered"},
            17: {"whatsapp", "notifications", "pixel", "silent"},
            24: {"whatsapp", "notifications", "pixel", "silent"},
        }
        for incident_id, tags in expected.items():
            actual = {
                row[0]
                for row in conn.execute(
                    """
                    select t.name
                    from incident_tags it
                    join tags t on t.tag_id=it.tag_id
                    where it.incident_id=?
                    """,
                    (incident_id,),
                )
            }
            self.assertEqual(tags, actual)
        obsolete = {
            "com.whatsapp",
            "com.whatsapp 2.26.29.73",
            "AudioService",
            "NotificationManager",
            "Android 17",
            "Pixel 8a",
        }
        linked = {
            row[0]
            for row in conn.execute(
                """
                select distinct t.name
                from incident_tags it
                join tags t on t.tag_id=it.tag_id
                """
            )
        }
        self.assertTrue(obsolete.isdisjoint(linked))

    def test_cli_tag_lookup_and_incident_search(self):
        resolved = self.run_tool("tag", "resolve", "com.whatsapp")
        self.assertEqual(resolved.returncode, 0, resolved.stderr)
        self.assertIn("name=whatsapp", resolved.stdout)

        silent_alias = self.run_tool("tag", "silent_notification")
        self.assertEqual(silent_alias.returncode, 0, silent_alias.stderr)
        self.assertIn("name=silent", silent_alias.stdout)

        listed = self.run_tool("tag", "list")
        self.assertEqual(listed.returncode, 0, listed.stderr)
        self.assertIn("name=whatsapp", listed.stdout)
        self.assertIn("name=notifications", listed.stdout)

        incident = self.run_tool("incident", "16")
        self.assertEqual(incident.returncode, 0, incident.stderr)
        self.assertIn("incident_id=16", incident.stdout)
        self.assertIn("tags=metered,notifications,pixel,whatsapp", incident.stdout)

        whatsapp_notifications = self.run_tool(
            "incident-search", "whatsapp", "notifications"
        )
        self.assertEqual(whatsapp_notifications.returncode, 0, whatsapp_notifications.stderr)
        self.assertIn("incident_id=16;", whatsapp_notifications.stdout)
        self.assertIn("incident_id=17;", whatsapp_notifications.stdout)
        self.assertIn("incident_id=24;", whatsapp_notifications.stdout)

        whatsapp_silent = self.run_tool(
            "incident-search", "whatsapp", "notifications", "silent"
        )
        self.assertEqual(whatsapp_silent.returncode, 0, whatsapp_silent.stderr)
        self.assertNotIn("incident_id=16;", whatsapp_silent.stdout)
        self.assertIn("incident_id=17;", whatsapp_silent.stdout)
        self.assertIn("incident_id=24;", whatsapp_silent.stdout)

    def legacy_incident_conn(self):
        conn = sqlite3.connect(":memory:")
        conn.execute("PRAGMA foreign_keys=OFF")
        conn.executescript(
            """
            CREATE TABLE schema_meta (key TEXT PRIMARY KEY, value TEXT NOT NULL);
            INSERT INTO schema_meta(key, value) VALUES ('schema_version', '2');
            CREATE TABLE projects (
              project_id INTEGER PRIMARY KEY,
              slug TEXT NOT NULL UNIQUE,
              name TEXT NOT NULL,
              status TEXT NOT NULL,
              archived INTEGER NOT NULL DEFAULT 0,
              created_source TEXT NOT NULL,
              notes TEXT
            );
            CREATE TABLE incidents (
              incident_id TEXT PRIMARY KEY,
              project_id INTEGER REFERENCES projects(project_id),
              title TEXT NOT NULL,
              first_seen_utc TEXT,
              last_seen_utc TEXT,
              occurrence_count TEXT,
              severity TEXT,
              status TEXT NOT NULL,
              root_cause TEXT,
              resolution_summary TEXT,
              systems TEXT,
              alerts TEXT,
              prompt_refs TEXT,
              commit_refs TEXT,
              notes TEXT,
              source_ref TEXT
            );
            CREATE TABLE incident_events (
              incident_event_id INTEGER PRIMARY KEY AUTOINCREMENT,
              incident_id TEXT NOT NULL REFERENCES incidents(incident_id),
              event_time_utc TEXT NOT NULL,
              severity TEXT,
              status TEXT,
              source TEXT,
              detail TEXT
            );
            INSERT INTO incidents(
              incident_id, title, occurrence_count, status, systems, alerts
            ) VALUES (
              'PIXEL_WHATSAPP_SILENT', 'Pixel WhatsApp silent notification', '1',
              'RESOLVED', 'Pixel 8a; Android 17; com.whatsapp',
              'silent_notification; notifications'
            );
            INSERT INTO incident_events(
              incident_id, event_time_utc, status, detail
            ) VALUES (
              'PIXEL_WHATSAPP_SILENT', '2026-08-02T02:16:17Z', 'RESOLVED',
              'legacy event'
            );
            """
        )
        return conn

    def migrated_incident_conn(self):
        conn = self.legacy_incident_conn()
        megavault.migrate_incident_schema(conn)
        conn.commit()
        conn.execute("PRAGMA foreign_keys=ON")
        self.assertEqual([], conn.execute("PRAGMA foreign_key_check").fetchall())
        return conn

    def register_tags(self, conn, *names):
        for name in names:
            megavault.create_tag(conn, name)

    def test_migration_preserves_data_and_is_repeatable(self):
        conn = self.migrated_incident_conn()
        row = conn.execute(
            "select incident_id, legacy_incident_key, legacy_occurrence_note from incidents"
        ).fetchone()
        self.assertIsInstance(row[0], int)
        self.assertEqual("PIXEL_WHATSAPP_SILENT", row[1])
        self.assertEqual("1", row[2])
        self.assertEqual(1, conn.execute("select count(*) from incident_events").fetchone()[0])
        before = conn.execute(
            "select count(*), (select count(*) from incident_tags) from incidents"
        ).fetchone()
        self.assertFalse(megavault.migrate_incident_schema(conn))
        after = conn.execute(
            "select count(*), (select count(*) from incident_tags) from incidents"
        ).fetchone()
        self.assertEqual(before, after)

    def test_identical_occurrences_get_distinct_ids(self):
        conn = self.migrated_incident_conn()
        self.register_tags(conn, "whatsapp", "notifications")
        first = megavault.create_incident(
            conn, title="same occurrence", status="OPEN", tags=["whatsapp", "notifications"]
        )
        second = megavault.create_incident(
            conn, title="same occurrence", status="OPEN", tags=["whatsapp", "notifications"]
        )
        self.assertNotEqual(first, second)

    def test_aliases_casing_conflicts_and_idempotent_links(self):
        conn = self.migrated_incident_conn()
        tag_id, canonical = megavault.create_tag(conn, "Silent")
        self.assertEqual((tag_id, canonical), megavault.resolve_or_create_tag(conn, "silent"))
        megavault.add_tag_alias(conn, "no_sound", "SILENT")
        self.assertEqual((tag_id, canonical), megavault.resolve_tag(conn, "NO_SOUND"))
        with self.assertRaises(megavault.TagConflictError):
            megavault.create_tag(conn, "no_SOUND")
        incident_id = megavault.create_incident(
            conn, title="link test", status="OPEN", tags=["no_sound"]
        )
        megavault.link_incident_tag(conn, incident_id, "SILENT")
        self.assertEqual(
            1,
            conn.execute(
                "select count(*) from incident_tags where incident_id=? and tag_id=?",
                (incident_id, tag_id),
            ).fetchone()[0],
        )

    def test_canonical_tag_format_rejects_free_text(self):
        conn = self.migrated_incident_conn()
        with self.assertRaises(ValueError):
            megavault.create_tag(conn, "silent notification")
        with self.assertRaises(ValueError):
            megavault.create_tag(conn, "audio.service")

    def test_multi_tag_search_uses_and_semantics(self):
        conn = self.migrated_incident_conn()
        self.register_tags(conn, "whatsapp", "notifications", "pixel", "silent")
        whatsapp = megavault.create_incident(
            conn, title="whatsapp only", status="OPEN", tags=["whatsapp"]
        )
        both = megavault.create_incident(
            conn,
            title="whatsapp notifications",
            status="OPEN",
            tags=["whatsapp", "notifications"],
        )
        pixel_silent = megavault.create_incident(
            conn, title="pixel silent", status="OPEN", tags=["pixel", "silent"]
        )
        results = megavault.search_incidents_by_tags(conn, ["WHATSAPP", "notifications"])
        ids = {row[0] for row in results}
        self.assertIn(both, ids)
        self.assertNotIn(whatsapp, ids)
        self.assertNotIn(pixel_silent, ids)
        megavault.add_tag_alias(conn, "muted", "silent")
        muted_pixel_ids = {
            row[0] for row in megavault.search_incidents_by_tags(conn, ["PIXEL", "MUTED"])
        }
        self.assertIn(pixel_silent, muted_pixel_ids)
        self.assertNotIn(whatsapp, muted_pixel_ids)
        self.assertNotIn(both, muted_pixel_ids)


if __name__ == "__main__":
    unittest.main()

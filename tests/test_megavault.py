import hashlib
import sqlite3
import subprocess
import sys
import tempfile
import unittest
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from unittest import mock


ROOT = Path(__file__).resolve().parents[1]
sys.dont_write_bytecode = True
sys.path.insert(0, str(ROOT))
from ai import megavault_core  # noqa: E402
from ai import strict_tag_wrapper  # noqa: E402
import megavault  # noqa: E402

PROTOCOL = ROOT / "ai" / "MEGAVAULT_PROTOCOL.md"
PH_BOOTSTRAP = ROOT / "ai" / "personalhubdoc.md"


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

    def test_personalhub_prompt_id_policy_matches_global_contract(self):
        text = PH_BOOTSTRAP.read_text(encoding="utf-8")
        required = (
            "identity=one_materialized_prompt_one_new_prompt_id_absolute",
            "revision=any_change_even_single_character_or_minor_rewording=>new_prompt_id",
            "parentage=parent_prompt_id_only;inherit_parent_id=forbidden",
            "reuse=forbidden_forever;cancelled_id_remains_reserved;delete=forbidden",
            "content_sha256=audit_integrity_only;deduplication_or_id_reuse_by_hash=forbidden",
            "model_generated_unregistered_prompt_id=forbidden",
        )
        for marker in required:
            self.assertIn(marker, text)

    def prompt_id_temp_db(self, tmp):
        tmp_db = Path(tmp) / "megavault-prompt-id.sqlite"
        source = sqlite3.connect(ROOT / "megavault.sqlite")
        copy = sqlite3.connect(tmp_db)
        source.backup(copy)
        copy.close()
        source.close()
        conn = sqlite3.connect(tmp_db)
        conn.execute("PRAGMA foreign_keys=OFF")
        conn.execute("DROP TABLE IF EXISTS prompt_id_events")
        conn.execute("DROP TABLE IF EXISTS prompt_id_registry")
        conn.execute("PRAGMA foreign_keys=ON")
        megavault.ensure_prompt_id_schema(conn)
        conn.commit()
        conn.close()
        return tmp_db

    def test_prompt_id_allocator_is_unique_under_concurrency(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_db = self.prompt_id_temp_db(tmp)
            with ThreadPoolExecutor(max_workers=8) as pool:
                ids = list(
                    pool.map(
                        lambda _: megavault.allocate_prompt_id(
                            tmp_db, source="test-concurrency", project_id=23
                        ),
                        range(32),
                    )
                )
            self.assertEqual(32, len(ids))
            self.assertEqual(32, len(set(ids)))
            self.assertTrue(all(100000 <= value <= 999999 for value in ids))
            conn = sqlite3.connect(tmp_db)
            self.assertEqual(
                32,
                conn.execute("select count(*) from prompt_id_registry").fetchone()[0],
            )
            self.assertEqual(
                32,
                conn.execute(
                    "select count(*) from prompt_id_events where event_type='allocated'"
                ).fetchone()[0],
            )

    def test_prompt_id_revision_always_gets_new_id_even_for_identical_content(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_db = self.prompt_id_temp_db(tmp)
            parent = megavault.allocate_prompt_id(
                tmp_db, source="test-revision", project_id=23
            )
            child = megavault.allocate_prompt_id(
                tmp_db,
                source="test-revision",
                project_id=23,
                parent_prompt_id=parent,
            )
            self.assertNotEqual(parent, child)
            digest = hashlib.sha256(b"identical prompt").hexdigest()
            megavault.materialize_prompt_id(
                parent, content_sha256=digest, db_path=tmp_db
            )
            megavault.materialize_prompt_id(
                child, content_sha256=digest, db_path=tmp_db
            )
            conn = sqlite3.connect(tmp_db)
            rows = conn.execute(
                """
                select prompt_id, parent_prompt_id, content_sha256, status
                from prompt_id_registry
                where prompt_id in (?, ?)
                order by prompt_id
                """,
                (parent, child),
            ).fetchall()
            self.assertEqual(2, len(rows))
            by_id = {row[0]: row for row in rows}
            self.assertIsNone(by_id[parent][1])
            self.assertEqual(parent, by_id[child][1])
            self.assertEqual(digest, by_id[parent][2])
            self.assertEqual(digest, by_id[child][2])
            self.assertEqual("materialized", by_id[parent][3])
            self.assertEqual("materialized", by_id[child][3])

    def test_prompt_id_backup_is_private_and_integrity_ok(self):
        with tempfile.TemporaryDirectory() as tmp:
            backup = megavault.create_prompt_id_backup(
                ROOT / "megavault.sqlite",
                output_dir=tmp,
            )
            self.assertEqual(0o600, backup.stat().st_mode & 0o777)
            conn = sqlite3.connect(backup)
            self.assertEqual("ok", conn.execute("PRAGMA integrity_check").fetchone()[0])
            conn.close()

    def test_prompt_id_source_backfill_uses_durable_sources_and_optional_missing(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            tmp_db = self.prompt_id_temp_db(tmp)
            repo = root / "roadmap"
            repo.mkdir()
            subprocess.run(["git", "-C", str(repo), "init", "-q"], check=True)
            subprocess.run(["git", "-C", str(repo), "config", "user.email", "test@example.invalid"], check=True)
            subprocess.run(["git", "-C", str(repo), "config", "user.name", "Test"], check=True)
            prompt = repo / "prompt.md"
            prompt.write_text("PROMPT_ID=345678\n", encoding="utf-8")
            subprocess.run(["git", "-C", str(repo), "add", "prompt.md"], check=True)
            subprocess.run(["git", "-C", str(repo), "commit", "-q", "-m", "prompt"], check=True)

            usage = root / "codex-usage"
            (usage / "prompts" / "456789").mkdir(parents=True)

            total, inserted, existing, optional_missing = (
                megavault.backfill_prompt_ids_from_sources(
                    source="source-test",
                    git_repos=[str(repo)],
                    prompt_dir_roots=[str(usage)],
                    optional_text_trees=[str(root / "missing-chatgpt-archive")],
                    required_ids=[345678, 456789],
                    db_path=tmp_db,
                )
            )
            self.assertEqual(2, total)
            self.assertEqual(2, inserted)
            self.assertEqual(0, existing)
            self.assertEqual(1, optional_missing)
            conn = sqlite3.connect(tmp_db)
            self.assertEqual(
                [(345678,), (456789,)],
                conn.execute(
                    "select prompt_id from prompt_id_registry where prompt_id in (345678,456789) order by prompt_id"
                ).fetchall(),
            )
            conn.close()

    def test_prompt_id_historical_backfill_reserves_ids_without_reuse(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_db = self.prompt_id_temp_db(tmp)
            inserted, existing = megavault.backfill_prompt_ids(
                [123456, 234567, 123456],
                source="historical-backfill-test",
                db_path=tmp_db,
            )
            self.assertEqual((2, 0), (inserted, existing))
            inserted, existing = megavault.backfill_prompt_ids(
                [123456, 234567],
                source="historical-backfill-test",
                db_path=tmp_db,
            )
            self.assertEqual((0, 2), (inserted, existing))
            conn = sqlite3.connect(tmp_db)
            rows = conn.execute(
                "select prompt_id, source, status from prompt_id_registry order by prompt_id"
            ).fetchall()
            self.assertEqual(
                [
                    (123456, "historical-backfill-test", "allocated"),
                    (234567, "historical-backfill-test", "allocated"),
                ],
                rows,
            )

    def test_prompt_id_lifecycle_is_terminal_and_identity_is_immutable(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_db = self.prompt_id_temp_db(tmp)
            prompt_id = megavault.allocate_prompt_id(
                tmp_db, source="test-lifecycle", project_id=23
            )
            digest = hashlib.sha256(b"prompt").hexdigest()
            megavault.materialize_prompt_id(
                prompt_id, content_sha256=digest, db_path=tmp_db
            )
            megavault.mark_prompt_id_used(prompt_id, db_path=tmp_db)
            with self.assertRaises(ValueError):
                megavault.cancel_prompt_id(prompt_id, db_path=tmp_db)
            conn = sqlite3.connect(tmp_db)
            conn.execute("PRAGMA foreign_keys=ON")
            with self.assertRaises(sqlite3.DatabaseError):
                conn.execute(
                    "update prompt_id_registry set source='rewritten' where prompt_id=?",
                    (prompt_id,),
                )
            with self.assertRaises(sqlite3.DatabaseError):
                conn.execute(
                    "delete from prompt_id_registry where prompt_id=?",
                    (prompt_id,),
                )
            state = conn.execute(
                "select status from prompt_id_registry where prompt_id=?",
                (prompt_id,),
            ).fetchone()[0]
            self.assertEqual("used", state)

    def test_prompt_id_schema_migration_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_db = self.prompt_id_temp_db(tmp)
            conn = sqlite3.connect(tmp_db)
            conn.execute("PRAGMA foreign_keys=ON")
            self.assertFalse(megavault.ensure_prompt_id_schema(conn))
            self.assertEqual([], conn.execute("PRAGMA foreign_key_check").fetchall())
            trigger_count = conn.execute(
                "select count(*) from sqlite_master where type='trigger' and name like 'prompt_id_%'"
            ).fetchone()[0]
            self.assertEqual(8, trigger_count)

    def test_secret_scan_has_zero_hits(self):
        self.assertEqual([], megavault.secret_scan_errors(megavault.git_tracked()))

    def test_tracked_markdown_allowlist_accepts_authoritative_docs(self):
        tracked_md = {
            "ai/MEGAVAULT_PROTOCOL.md",
            "ai/GLOBAL_INDEX.md",
            "ai/personalhubdoc.md",
            "ai/repository-public-private-matrix.md",
            "ai/repository-retention-checklist.md",
            "legacy/README.md",
        }
        extra_md = sorted(tracked_md - megavault.ALLOWED_TRACKED_MARKDOWN)
        self.assertEqual([], extra_md)

    def test_tracked_markdown_allowlist_rejects_unrelated_markdown(self):
        tracked_md = {
            "ai/MEGAVAULT_PROTOCOL.md",
            "ai/GLOBAL_INDEX.md",
            "ai/personalhubdoc.md",
            "legacy/README.md",
            "ai/unrelated.md",
        }
        extra_md = sorted(tracked_md - megavault.ALLOWED_TRACKED_MARKDOWN)
        self.assertEqual(["ai/unrelated.md"], extra_md)

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
            "select project_status, canonical_worktree from codex_project_index where project_id=5"
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
                (
                    31,
                    "REMOTE_ONLY",
                    "oracle-vm",
                    None,
                    "oracle-vm",
                    "/etc/caddy/Caddyfile+/etc/cloudflared/config.yml+/opt/uptime-kuma",
                    None,
                ),
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
            "codex_work_queue": conn.execute(
                "select count(*) from codex_project_index where project_status in ('LOCAL', 'REMOTE_ONLY')"
            ).fetchone()[0],
            "codex_remote_projects": conn.execute(
                "select count(*) from codex_project_index where project_status='REMOTE_ONLY'"
            ).fetchone()[0],
            "codex_missing_projects": conn.execute(
                "select count(*) from codex_project_index where project_status='MISSING'"
            ).fetchone()[0],
            "codex_archived_projects": conn.execute(
                "select count(*) from codex_project_index where project_status='ARCHIVED'"
            ).fetchone()[0],
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

    def test_codex_project_context_schema_is_scoped_and_populated(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        component_counts = dict(
            conn.execute(
                """
                select project_id, count(*)
                from project_components
                group by project_id
                order by project_id
                """
            ).fetchall()
        )
        operation_counts = dict(
            conn.execute(
                """
                select project_id, count(*)
                from project_operations
                group by project_id
                order by project_id
                """
            ).fetchall()
        )
        self.assertEqual({8: 4, 23: 4, 49: 4}, component_counts)
        self.assertEqual({8: 4, 23: 4, 49: 3}, operation_counts)
        self.assertEqual(
            [],
            conn.execute(
                """
                select project_id from project_components where project_id not in (8, 23, 49)
                union
                select project_id from project_operations where project_id not in (8, 23, 49)
                """
            ).fetchall(),
        )

    def test_codex_project_context_view_combines_routing_components_and_operations(self):
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        row = conn.execute(
            """
            select slug, canonical_worktree, components, operations
            from codex_project_context
            where project_id=49
            """
        ).fetchone()
        self.assertEqual("personalhub", row[0])
        self.assertEqual("/home/daniele/projects/PersonalHub", row[1])
        self.assertIn("core_database_module:gradle_module:", row[2])
        self.assertIn("feature_modules:gradle_modules:", row[2])
        self.assertIn("assemble_debug:medium:fedora:", row[3])
        self.assertIn("./gradlew assembleDebug --no-configuration-cache", row[3])

    def test_codex_project_context_cli_returns_one_compact_row(self):
        result = self.run_tool("codex-project-context", "23")
        self.assertEqual(result.returncode, 0, result.stderr)
        lines = result.stdout.strip().splitlines()
        self.assertEqual(1, len(lines))
        self.assertTrue(lines[0].startswith("project_id=23;slug=megavault;"))
        self.assertIn("components=", lines[0])
        self.assertIn("operations=", lines[0])
        self.assertIn("project_context:low:fedora:/home/daniele/MegaVault:", lines[0])

    def test_project_retrieval_cli_commands(self):
        work_queue = self.run_tool("project-work-queue")
        self.assertEqual(work_queue.returncode, 0, work_queue.stderr)
        work_lines = work_queue.stdout.strip().splitlines()
        conn = sqlite3.connect(ROOT / "megavault.sqlite")
        expected_counts = {
            "work": conn.execute("select count(*) from codex_work_queue").fetchone()[0],
            "remote": conn.execute("select count(*) from codex_remote_projects").fetchone()[0],
            "missing": conn.execute("select count(*) from codex_missing_projects").fetchone()[0],
            "archived": conn.execute("select count(*) from codex_archived_projects").fetchone()[0],
        }
        conn.close()
        self.assertEqual(expected_counts["work"], len(work_lines))
        self.assertTrue(work_lines[0].startswith("project_id=1;slug=amici-fb;"))
        self.assertIn("project_status=LOCAL", work_lines[0])
        self.assertNotIn("project_status=MISSING", work_queue.stdout)
        self.assertNotIn("project_status=ARCHIVED", work_queue.stdout)

        remote = self.run_tool("project-remote")
        self.assertEqual(remote.returncode, 0, remote.stderr)
        remote_lines = remote.stdout.strip().splitlines()
        self.assertEqual(expected_counts["remote"], len(remote_lines))
        self.assertTrue(all("project_status=REMOTE_ONLY" in line for line in remote_lines))

        missing = self.run_tool("project-missing")
        self.assertEqual(missing.returncode, 0, missing.stderr)
        missing_lines = missing.stdout.strip().splitlines()
        self.assertEqual(expected_counts["missing"], len(missing_lines))
        self.assertEqual(
            "project_id=5;slug=aw-converter;project_status=MISSING",
            missing_lines[0],
        )

        archived = self.run_tool("project-archived")
        self.assertEqual(archived.returncode, 0, archived.stderr)
        archived_lines = archived.stdout.strip().splitlines()
        self.assertEqual(expected_counts["archived"], len(archived_lines))
        self.assertEqual("project_id=2;slug=android;project_status=ARCHIVED", archived_lines[0])

    def test_project_path_cli(self):
        resolved = self.run_tool("project-path", "23")
        self.assertEqual(resolved.returncode, 0, resolved.stderr)
        self.assertEqual("/home/daniele/MegaVault", resolved.stdout.strip())

        missing = self.run_tool("project-path", "5")
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

        missing = self.run_tool("project-path", "--status", "5")
        self.assertEqual(missing.returncode, 0, missing.stderr)
        self.assertEqual("MISSING", missing.stdout.strip())

        absent = self.run_tool("project-path", "--status", "99999")
        self.assertNotEqual(absent.returncode, 0)
        self.assertEqual("ABSENT", absent.stdout.strip())

    def test_register_github_repo_is_idempotent(self):
        with tempfile.TemporaryDirectory() as tmp:
            tmp_db = Path(tmp) / "megavault.sqlite"
            tmp_db.write_bytes((ROOT / "megavault.sqlite").read_bytes())
            worktree = Path(tmp) / "projects" / "example-new-repo"
            args = [
                "register-github-repo",
                "--owner",
                "gernalix",
                "--name",
                "example-new-repo",
                "--remote-url",
                "https://github.com/gernalix/example-new-repo",
                "--default-branch",
                "main",
                "--worktree",
                str(worktree),
            ]
            with (
                mock.patch.object(megavault, "DB", tmp_db),
                mock.patch.object(megavault_core, "DB", tmp_db),
                mock.patch.object(strict_tag_wrapper, "DB", tmp_db),
            ):
                first = megavault.main(args)
                second = megavault.main(args)
            conn = sqlite3.connect(tmp_db)
            project_count = conn.execute("select count(*) from projects where slug='example-new-repo'").fetchone()[0]
            repo_count = conn.execute(
                "select count(*) from repositories where remote_url='https://github.com/gernalix/example-new-repo'"
            ).fetchone()[0]
            permanent_count = conn.execute(
                "select count(*) from permanent_ids where entity_type='project' and canonical_key='example-new-repo'"
            ).fetchone()[0]
            self.assertEqual(first, 0)
            self.assertEqual(second, 0)
            self.assertEqual(project_count, 1)
            self.assertEqual(repo_count, 1)
            self.assertEqual(permanent_count, 1)

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
            megavault.migrate_project_index_schema(conn)
            megavault.ensure_project_context_schema(conn)
            after_first = {
                table: conn.execute(f"select count(*) from {table}").fetchone()[0]
                for table in tables
            }
            self.assertEqual(before, after_first)
            self.assertFalse(megavault.migrate_project_index_schema(conn))
            self.assertFalse(megavault.ensure_project_context_schema(conn))
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
        self.assertEqual(list(range(1, len(incident_ids) + 1)), incident_ids)
        self.assertEqual(
            len(incident_ids),
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
            33: {"whatsapp", "notifications", "pixel", "silent", "android", "bug"},
            34: {"security", "datasette", "oracle", "authentication"},
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

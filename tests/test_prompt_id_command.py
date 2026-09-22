from __future__ import annotations

import json
import sqlite3
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOOLS = ROOT / "tools"
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(TOOLS))

import megavault  # noqa: E402
import prompt_id_command  # noqa: E402


class PromptIdCommandTests(unittest.TestCase):
    def _db(self, root: Path) -> Path:
        db = root / "megavault.sqlite"
        conn = sqlite3.connect(db)
        try:
            conn.execute(
                "CREATE TABLE projects(project_id INTEGER PRIMARY KEY)"
            )
            conn.execute("INSERT INTO projects(project_id) VALUES(23)")
            megavault.ensure_prompt_id_schema(conn)
            conn.commit()
        finally:
            conn.close()
        return db

    def _request(self) -> dict:
        return {
            "request_id": "bridge-db-native-idempotency",
            "command": "allocate",
            "source": "test-bridge-db-native",
            "project_id": 23,
        }

    def test_allocate_retry_does_not_depend_on_json_receipts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db = self._db(root)
            response = root / "response.json"
            receipts = root / "receipts"
            request = self._request()

            first = prompt_id_command.execute_request(
                request,
                db_path=db,
                response_path=response,
                receipt_dir=receipts,
            )
            response.unlink()
            for path in receipts.glob("*.json"):
                path.unlink()

            second = prompt_id_command.execute_request(
                request,
                db_path=db,
                response_path=response,
                receipt_dir=receipts,
            )

            self.assertEqual(first["prompt_id"], second["prompt_id"])
            conn = sqlite3.connect(db)
            try:
                self.assertEqual(
                    1,
                    conn.execute(
                        "SELECT COUNT(*) FROM prompt_id_registry"
                    ).fetchone()[0],
                )
                self.assertEqual(
                    [("bridge-db-native-idempotency", first["prompt_id"])],
                    conn.execute(
                        "SELECT request_id,prompt_id FROM prompt_id_allocation_requests"
                    ).fetchall(),
                )
            finally:
                conn.close()

    def test_cancel_command_is_idempotent_without_json_receipts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db = self._db(root)
            response = root / "response.json"
            receipts = root / "receipts"
            allocate = self._request()

            allocated = prompt_id_command.execute_request(
                allocate,
                db_path=db,
                response_path=response,
                receipt_dir=receipts,
            )
            response.unlink()
            for path in receipts.glob("*.json"):
                path.unlink()

            cancel = {
                "request_id": "bridge-db-native-cancel",
                "command": "cancel",
                "prompt_id": allocated["prompt_id"],
            }
            first = prompt_id_command.execute_request(
                cancel,
                db_path=db,
                response_path=response,
                receipt_dir=receipts,
            )
            response.unlink()
            for path in receipts.glob("*.json"):
                path.unlink()
            second = prompt_id_command.execute_request(
                cancel,
                db_path=db,
                response_path=response,
                receipt_dir=receipts,
            )

            self.assertEqual("cancelled", first["status"])
            self.assertEqual("cancelled", second["status"])
            self.assertEqual(first["prompt_id"], second["prompt_id"])
            conn = sqlite3.connect(db)
            try:
                self.assertEqual(
                    ("cancelled",),
                    conn.execute(
                        "SELECT status FROM prompt_id_registry WHERE prompt_id=?",
                        (allocated["prompt_id"],),
                    ).fetchone(),
                )
                self.assertEqual(
                    1,
                    conn.execute(
                        "SELECT COUNT(*) FROM prompt_id_events WHERE prompt_id=? AND event_type='cancelled'",
                        (allocated["prompt_id"],),
                    ).fetchone()[0],
                )
            finally:
                conn.close()

    def test_allocate_conflict_is_rejected_even_without_json_receipts(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            db = self._db(root)
            response = root / "response.json"
            receipts = root / "receipts"
            request = self._request()

            prompt_id_command.execute_request(
                request,
                db_path=db,
                response_path=response,
                receipt_dir=receipts,
            )
            response.unlink()
            for path in receipts.glob("*.json"):
                path.unlink()

            changed = dict(request)
            changed["source"] = "different-source"
            with self.assertRaisesRegex(
                ValueError,
                "PROMPT_ID_REQUEST_ID_CONFLICT:bridge-db-native-idempotency",
            ):
                prompt_id_command.execute_request(
                    changed,
                    db_path=db,
                    response_path=response,
                    receipt_dir=receipts,
                )

            conn = sqlite3.connect(db)
            try:
                self.assertEqual(
                    1,
                    conn.execute(
                        "SELECT COUNT(*) FROM prompt_id_registry"
                    ).fetchone()[0],
                )
            finally:
                conn.close()


if __name__ == "__main__":
    unittest.main()

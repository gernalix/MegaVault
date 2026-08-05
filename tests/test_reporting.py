from pathlib import Path

from ai import reporting


def test_finish_task_delegates_to_shared_library(monkeypatch) -> None:
    captured = {}

    def fake_send_task_reports(plain, technical, **kwargs):
        captured.update(plain=plain, technical=technical, **kwargs)
        return {"plain_message_parts": 1}

    import telegram_notify

    monkeypatch.setattr(telegram_notify, "send_task_reports", fake_send_task_reports)
    result = reporting.finish_task(
        "plain",
        "technical",
        prompt_id=7,
        title="Task",
    )

    assert captured == {
        "plain": "plain",
        "technical": "technical",
        "title": "Task",
        "prompt_id": 7,
        "chat_id": None,
    }
    assert result == {"plain_message_parts": 1}


def test_finish_task_files_reads_utf8(monkeypatch, tmp_path: Path) -> None:
    plain = tmp_path / "plain.txt"
    technical = tmp_path / "technical.txt"
    plain.write_text("fatto è", encoding="utf-8")
    technical.write_text("dettagli", encoding="utf-8")
    captured = {}

    def fake_finish_task(plain_report, technical_report, **kwargs):
        captured.update(plain=plain_report, technical=technical_report, **kwargs)
        return {"ok": True}

    monkeypatch.setattr(reporting, "finish_task", fake_finish_task)
    result = reporting.finish_task_files(plain, technical, prompt_id="123456")

    assert captured["plain"] == "fatto è"
    assert captured["technical"] == "dettagli"
    assert captured["prompt_id"] == "123456"
    assert result == {"ok": True}

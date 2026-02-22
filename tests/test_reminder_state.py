from reminder_bot import InvoiceReminderBot


def test_state_persistence_roundtrip(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    bot = InvoiceReminderBot()
    assert bot.state == {"invoices": {}}

    bot.state["invoices"]["inv_001"] = {"reminders_sent": 1, "last_reminder": "2026-02-22T00:00:00"}
    bot.save_state()

    reloaded = InvoiceReminderBot()
    assert "inv_001" in reloaded.state["invoices"]
    assert reloaded.state["invoices"]["inv_001"]["reminders_sent"] == 1


def test_reminder_days_env_override(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)
    monkeypatch.setenv("REMINDER_DAYS", "5,10")
    bot = InvoiceReminderBot()
    assert bot.reminder_days == [5, 10]

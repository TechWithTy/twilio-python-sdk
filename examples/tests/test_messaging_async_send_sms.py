import asyncio
from types import SimpleNamespace
from unittest.mock import MagicMock, patch
import importlib


def test_messaging_async_send_sms(monkeypatch):
    monkeypatch.setenv("TWILIO_ACCOUNT_SID", "ACxxxx")
    monkeypatch.setenv("TWILIO_AUTH_TOKEN", "auth")
    monkeypatch.setenv("TWILIO_TO_NUMBER", "+15558675310")
    monkeypatch.setenv("TWILIO_FROM_NUMBER", "+15017122661")

    mod = importlib.import_module(
        "backend.app.core.third_party_integrations.twilio-python-sdk.examples.messaging_async_send_sms".replace("-", "_")
    )

    with patch.object(mod, "Client") as MockClient:
        inst = MockClient.return_value
        # message object stub
        inst.messages.create.return_value = SimpleNamespace(sid="SM123", status="queued")

        asyncio.run(mod.main())
        inst.messages.create.assert_called_once()

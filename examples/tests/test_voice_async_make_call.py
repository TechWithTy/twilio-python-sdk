import asyncio
from types import SimpleNamespace
from unittest.mock import patch
import importlib


def test_voice_async_make_call(monkeypatch):
    monkeypatch.setenv("TWILIO_ACCOUNT_SID", "ACxxxx")
    monkeypatch.setenv("TWILIO_AUTH_TOKEN", "auth")
    monkeypatch.setenv("TWILIO_TO_NUMBER", "+15558675310")
    monkeypatch.setenv("TWILIO_FROM_NUMBER", "+15017122661")
    monkeypatch.setenv("TWILIO_VOICE_URL", "http://demo.twilio.com/docs/voice.xml")

    mod = importlib.import_module(
        "backend.app.core.third_party_integrations.twilio-python-sdk.examples.voice_async_make_call".replace("-", "_")
    )

    with patch.object(mod, "Client") as MockClient:
        inst = MockClient.return_value
        inst.calls.create.return_value = SimpleNamespace(sid="CA123", status="queued")

        asyncio.run(mod.main())
        inst.calls.create.assert_called_once()

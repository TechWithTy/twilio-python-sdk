import asyncio
from types import SimpleNamespace
from unittest.mock import patch
import importlib


def test_video_async_create_room(monkeypatch):
    monkeypatch.setenv("TWILIO_ACCOUNT_SID", "ACxxxx")
    monkeypatch.setenv("TWILIO_AUTH_TOKEN", "auth")
    monkeypatch.setenv("TWILIO_VIDEO_ROOM_UNIQUE_NAME", "demo-room")

    mod = importlib.import_module(
        "backend.app.core.third_party_integrations.twilio-python-sdk.examples.video_async_create_room".replace("-", "_")
    )

    with patch.object(mod, "Client") as MockClient:
        inst = MockClient.return_value
        # simulate client.video.v1.rooms.create(...) chain
        inst.video.v1.rooms.create.return_value = SimpleNamespace(
            sid="RM123", unique_name="demo-room", status="in-progress"
        )

        asyncio.run(mod.main())
        inst.video.v1.rooms.create.assert_called_once()

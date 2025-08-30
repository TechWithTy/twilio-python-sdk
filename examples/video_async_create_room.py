from __future__ import annotations

import asyncio
import os
from typing import Any

from twilio.rest import Client


ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


async def main() -> None:
    """
    Async example: Create a Twilio Video room using the Twilio Python SDK.
    Docs: https://www.twilio.com/docs/video/api/rooms-resource#create-a-room-resource
    Helper usage: client.video.v1.rooms.create(...)
    """
    if not (ACCOUNT_SID and AUTH_TOKEN):
        raise RuntimeError("TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN must be set")

    unique_name = os.environ.get("TWILIO_VIDEO_ROOM_UNIQUE_NAME", "demo-room")
    type_ = os.environ.get("TWILIO_VIDEO_ROOM_TYPE", "go")  # go | group | group-small
    record = os.environ.get("TWILIO_VIDEO_RECORD", "false").lower() in {"1", "true", "yes"}

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def _create_room() -> Any:
        return client.video.v1.rooms.create(
            unique_name=unique_name,
            type=type_,
            record_participants_on_connect=record,
        )

    room = await asyncio.to_thread(_create_room)
    print("Room SID:", room.sid)
    print("Unique Name:", room.unique_name)
    print("Status:", room.status)


if __name__ == "__main__":
    asyncio.run(main())

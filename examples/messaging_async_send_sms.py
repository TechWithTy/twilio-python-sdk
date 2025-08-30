from __future__ import annotations

import asyncio
import os
from typing import Any

from twilio.rest import Client


ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


async def main() -> None:
    """
    Async example: Send an SMS using Twilio Python SDK.
    Docs: https://www.twilio.com/docs/messaging/api/message-resource#create-a-message-resource
    Endpoint used by SDK: POST /2010-04-01/Accounts/{AccountSid}/Messages.json
    """
    if not (ACCOUNT_SID and AUTH_TOKEN):
        raise RuntimeError("TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN must be set")

    to = os.environ.get("TWILIO_TO_NUMBER", "+15558675310")
    from_ = os.environ.get("TWILIO_FROM_NUMBER", "+15017122661")
    body = os.environ.get("TWILIO_MESSAGE_BODY", "Hello from Twilio Async Example!")

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def _send() -> Any:
        return client.messages.create(to=to, from_=from_, body=body)

    message = await asyncio.to_thread(_send)
    print("SID:", message.sid)
    print("Status:", message.status)


if __name__ == "__main__":
    asyncio.run(main())

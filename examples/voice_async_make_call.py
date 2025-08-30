from __future__ import annotations

import asyncio
import os
from typing import Any

from twilio.rest import Client


ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")


async def main() -> None:
    """
    Async example: Create an outbound call using Twilio Python SDK.
    Endpoint used by SDK: POST /2010-04-01/Accounts/{AccountSid}/Calls.json
    Docs: https://www.twilio.com/docs/voice/make-calls
    """
    if not (ACCOUNT_SID and AUTH_TOKEN):
        raise RuntimeError("TWILIO_ACCOUNT_SID and TWILIO_AUTH_TOKEN must be set")

    to = os.environ.get("TWILIO_TO_NUMBER", "+15558675310")
    from_ = os.environ.get("TWILIO_FROM_NUMBER", "+15017122661")
    # TwiML URL that instructs Twilio what to do when the call is answered
    url = os.environ.get("TWILIO_VOICE_URL", "http://demo.twilio.com/docs/voice.xml")

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    def _create_call() -> Any:
        return client.calls.create(to=to, from_=from_, url=url)

    call = await asyncio.to_thread(_create_call)
    print("Call SID:", call.sid)
    print("Status:", call.status)


if __name__ == "__main__":
    asyncio.run(main())

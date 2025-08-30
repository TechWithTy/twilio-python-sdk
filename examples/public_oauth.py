import os
import asyncio

from twilio.rest import Client
from twilio.credential.client_credential_provider import ClientCredentialProvider

ACCOUNT_SID = os.environ.get("TWILIO_ACCOUNT_SID")
FROM_NUMBER = os.environ.get("TWILIO_FROM_NUMBER")
TO_NUMBER = os.environ.get("TWILIO_TO_NUMBER")

CLIENT_ID = os.environ.get("TWILIO_CLIENT_ID")
CLIENT_SECRET = os.environ.get("CLIENT_SECRET")


async def main() -> None:
    """
    Async example usage of message resources with Public OAuth.
    """
    client = Client(
        account_sid=ACCOUNT_SID,
        credential_provider=ClientCredentialProvider(CLIENT_ID, CLIENT_SECRET),
    )

    msg = await asyncio.to_thread(
        lambda: client.messages.create(to=TO_NUMBER, from_=FROM_NUMBER, body="hello world")
    )
    print("Message SID:", msg.sid)


if __name__ == "__main__":
    asyncio.run(main())

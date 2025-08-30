# Twilio Python SDK Async Examples

This folder contains async-friendly examples using the official `twilio` Python SDK, wrapped with `asyncio.to_thread(...)` so calls don't block the event loop.

## Examples
- `messaging_async_send_sms.py` — Send an SMS message
- `voice_async_make_call.py` — Make an outbound phone call using a TwiML URL
- `video_async_create_room.py` — Create a Twilio Video Room
- `basic_usage.py` — General Twilio resource usage (messages, calls, TwiML) — async-ified
- `client_validation.py` — Uses ValidationClient (enterprise) — async-ified
- `organization_api.py` — Organization resources with OrgsCredentialProvider — async-ified
- `public_oauth.py` — Messaging via Public OAuth ClientCredentialProvider — async-ified

## Prerequisites
- Python 3.10+
- Installed Twilio SDK: `pip install twilio`
- A Twilio account with a verified phone number and credentials

## Required environment variables
Common:
- `TWILIO_ACCOUNT_SID`
- `TWILIO_AUTH_TOKEN`

Messaging / Voice:
- `TWILIO_TO_NUMBER` (E.164, e.g., `+15558675310`)
- `TWILIO_FROM_NUMBER` (your Twilio number in E.164)

Voice:
- `TWILIO_VOICE_URL` (TwiML URL to instruct call flow; defaults to `http://demo.twilio.com/docs/voice.xml`)

Video:
- `TWILIO_VIDEO_ROOM_UNIQUE_NAME` (optional; default `demo-room`)
- `TWILIO_VIDEO_ROOM_TYPE` (`go` | `group` | `group-small`; default `go`)
- `TWILIO_VIDEO_RECORD` (`true`/`false`; default `false`)

## How to run
Messaging (SMS):
```
python backend/app/core/third_party_integrations/twilio-python-sdk/examples/messaging_async_send_sms.py
```

Voice (Outbound Call):
```
python backend/app/core/third_party_integrations/twilio-python-sdk/examples/voice_async_make_call.py
```

Video (Create Room):
```
python backend/app/core/third_party_integrations/twilio-python-sdk/examples/video_async_create_room.py
```

## Notes
- The official Twilio SDK is synchronous. We use `asyncio.to_thread(...)` to run SDK calls in a worker thread for async compatibility.
- Ensure phone numbers are in E.164 format and your `From` number is a Twilio number enabled for the product you are using (SMS/Voice).
- `client_validation.py` requires enterprise features (ValidationClient) and uses API Keys plus RSA public key registration.
- `organization_api.py` and `public_oauth.py` rely on OAuth credential providers; ensure `TWILIO_CLIENT_ID`/`CLIENT_SECRET` and related env vars are set correctly.

## References
- Messaging API (Message Resource): https://www.twilio.com/docs/messaging/api/message-resource
- Programmable Voice (Make Calls): https://www.twilio.com/docs/voice/make-calls
- Video Rooms API: https://www.twilio.com/docs/video/api/rooms-resource

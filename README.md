# Saiful AI Agent Backend — Starter

This is a **demo backend scaffold**, not a finished AI video-generation service.

## Included
- FastAPI service with `/health` and `/` checks
- `POST /api/jobs` endpoint expected by the Saiful AI Agent dashboard
- `GET /api/jobs/{job_id}` demo job lookup
- `POST /api/jobs/{job_id}/approve-upload` records explicit approval
- Render deployment configuration

## Important limitations
- Jobs are held in memory and disappear when the server restarts.
- No AI voice, image, or video provider is connected.
- No video rendering, preview delivery, or YouTube upload is implemented.
- The approval endpoint records approval only; it does not upload anything.
- Do not put API keys in this repository or in the browser dashboard. Add secrets only in the hosting provider's environment settings after choosing and configuring a provider.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

Open `http://127.0.0.1:8000/health` to check the service.

## Deploy on Render
1. Upload the extracted contents of this folder to a new GitHub repository (not the ZIP file itself).
2. In Render, create a **New Web Service** and connect that repository.
3. Use the build command `pip install -r requirements.txt`.
4. Use the start command `uvicorn main:app --host 0.0.0.0 --port $PORT`.
5. After deployment, test `/health`. Put the resulting HTTPS service URL into the dashboard's Backend URL field.

A live URL means only that this starter API is running. Real video generation requires a separate provider integration, secure server-side credentials, and additional implementation.

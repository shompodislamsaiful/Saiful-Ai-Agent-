from datetime import datetime, timezone
from uuid import uuid4
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from typing import Any

app = FastAPI(title="Saiful AI Agent Backend", version="0.1.0")

jobs: dict[str, dict[str, Any]] = {}

class JobRequest(BaseModel):
    command: str = Field(min_length=1, max_length=4000)
    episode: dict[str, Any]
    aspect_ratio: str = "9:16"
    voice_language: str = "English"
    require_upload_approval: bool = True

@app.get("/")
def root():
    return {"service": "Saiful AI Agent Backend", "status": "running", "note": "Starter scaffold; AI video generation is not connected."}

@app.get("/health")
def health():
    return {"ok": True}

@app.post("/api/jobs", status_code=202)
def create_job(payload: JobRequest):
    job_id = str(uuid4())
    jobs[job_id] = {
        "job_id": job_id,
        "status": "queued_demo",
        "created_at": datetime.now(timezone.utc).isoformat(),
        "request": payload.model_dump(),
        "upload_approved": False,
        "message": "Request stored in memory only. Connect an AI video provider and persistent queue to generate videos."
    }
    return {"job_id": job_id, "status": "queued_demo", "message": jobs[job_id]["message"]}

@app.get("/api/jobs/{job_id}")
def get_job(job_id: str):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found; demo jobs reset when the server restarts.")
    return jobs[job_id]

@app.post("/api/jobs/{job_id}/approve-upload")
def approve_upload(job_id: str, body: dict[str, Any]):
    if job_id not in jobs:
        raise HTTPException(status_code=404, detail="Job not found")
    if body.get("approved") is not True:
        raise HTTPException(status_code=400, detail="Explicit approved=true is required")
    jobs[job_id]["upload_approved"] = True
    jobs[job_id]["message"] = "Approval recorded only. YouTube upload is not implemented in this starter."
    return {"job_id": job_id, "upload_approved": True, "status": "approval_recorded_demo", "message": jobs[job_id]["message"]}

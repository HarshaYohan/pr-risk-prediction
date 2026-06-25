"""FastAPI backend starter for PR risk prediction."""
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="PR Risk Prediction API")

class PullRequestInput(BaseModel):
    """Minimal PR input payload for prototype routes."""
    title: str
    description: str | None = None
    files_changed: int | None = None
    lines_added: int | None = None
    lines_deleted: int | None = None
    ci_failed: bool | None = None

@app.get("/health")
def health_check() -> dict:
    """Return API health status."""
    return {"status": "ok"}

@app.post("/predict")
def predict(payload: PullRequestInput) -> dict:
    """Placeholder prediction endpoint."""
    return {
        "is_risky": "placeholder",
        "risk_type": "unsure",
        "message": "Connect this route to trained models.",
        "input_title": payload.title,
    }

@app.post("/explain")
def explain(payload: PullRequestInput) -> dict:
    """Placeholder explanation endpoint."""
    return {
        "explanation": "Model explanations will be generated here.",
        "suggestion": "Request review and add tests when risk signals are high.",
        "input_title": payload.title,
    }

# FastAPI Backend

Starter API exposing health, prediction, and explanation routes. **Placeholder responses** — not yet wired to trained models.

## Run

```bash
uvicorn app.backend.main:app --reload
# docs at http://127.0.0.1:8000/docs
```

## Routes

| Method | Path | Status | Purpose |
|---|---|---|---|
| GET | `/health` | ✅ | Liveness check |
| POST | `/predict` | 🟡 stub | Return `is_risky` + `risk_type` for a PR payload |
| POST | `/explain` | 🟡 stub | Return an explanation + mitigation suggestion |

Input model: `PullRequestInput` (`title`, `description`, `files_changed`, `lines_added`, `lines_deleted`, `ci_failed`).

## Next steps

- Load a trained model and call `pr_risk.models.predict.predict_risk_and_type` in `/predict`.
- Call `pr_risk.explainability` (feature importance / SHAP / LIME → `generate_human_readable_explanation`) in `/explain`.

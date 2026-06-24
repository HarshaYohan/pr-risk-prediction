# Streamlit Labelling App

A simple UI for reviewing selected PRs and saving labels — the human side of the active-learning loop. **Working prototype.**

## Run

```bash
streamlit run app/labelling_app/streamlit_app.py
```

## Flow

1. Upload an annotation batch CSV (e.g. from `annotation/annotation_batches/`).
2. Step through rows; for each, view PR details and pick `is_risky` (0/1/2) + `risk_type` (the 11 taxonomy classes) + notes.
3. Saved rows are appended to the output CSV (default `data/labelled/streamlit_labels.csv`).

## Next steps

- Connect saved labels to `pr_risk.annotation.merge_labels` to fold them into the labelled pool.
- Validate on save with `pr_risk.annotation.validate_labels.validate_label_schema`.

Labels and uploads live under `data/` (gitignored) — don't commit real labelled data.

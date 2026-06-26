"""Append a starter experiment row to experiments/experiment_log.csv."""
from datetime import date
from pathlib import Path

import pandas as pd

path = Path("experiments/experiment_log.csv")
row = {
    "experiment_id": "sample-exp-001", "date": date.today().isoformat(),
    "dataset_version": "sample", "model_name": "logistic_regression",
    "task_type": "binary_risk_prediction", "target": "is_risky",
    "active_learning_strategy": "none", "active_learning_round": 0,
    "labelled_sample_count": 10, "accuracy": "", "precision": "",
    "recall": "", "f1_score": "", "roc_auc": "", "notes": "Starter sample experiment row.",
}
existing = pd.read_csv(path) if path.exists() else pd.DataFrame()
pd.concat([existing, pd.DataFrame([row])], ignore_index=True).to_csv(path, index=False)
print(f"Appended sample experiment to {path}")

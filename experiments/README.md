# Experiments

Lightweight CSV tracking for runs and summaries. This is a deliberately simple, Git-friendly alternative to a full tracking server — commit **templates and curated summaries**, not large MLflow/W&B run directories (those are gitignored).

## Files

| File | Purpose |
|---|---|
| [experiment_log.csv](experiment_log.csv) | One row per run (append-only log) |
| [results_summary.csv](results_summary.csv) | Curated headline results for the report |
| [active_learning_rounds.csv](active_learning_rounds.csv) | Per-round AL metrics (accuracy vs. labelled count) |

## Schema (shared columns)

| Column | Meaning |
|---|---|
| `experiment_id` | Unique run id (e.g. `exp-001`) |
| `date` | ISO date |
| `dataset_version` | e.g. `sample`, `prismbench-v1` |
| `model_name` | e.g. `logistic_regression`, `random_forest`, `codebert` |
| `task_type` | `binary_risk_prediction` or `risk_type_classification` |
| `target` | `is_risky` or `risk_type` |
| `active_learning_strategy` | `none`, `least_confidence`, `margin`, `entropy`, `diversity` |
| `active_learning_round` | Round index (0 if not AL) |
| `labelled_sample_count` | Number of labelled examples used |
| `accuracy`, `precision`, `recall`, `f1_score`, `roc_auc` | Metrics |
| `notes` | Free text |

## How to add a run

```bash
python scripts/create_sample_experiment.py   # appends a starter row
```

Or append programmatically from a notebook (see [`notebooks/07_results_analysis.ipynb`](../notebooks/07_results_analysis.ipynb)). Keep `results_summary.csv` curated to the rows you actually report.

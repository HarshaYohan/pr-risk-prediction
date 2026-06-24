# Repository Structure

This document explains what each folder contains, why it exists, whether its files should be committed, and how it is used. For the project motivation see [PROJECT_OVERVIEW.md](PROJECT_OVERVIEW.md); for setup and workflow see [README.md](README.md).

## Annotated tree

```text
pr-risk-prediction/
├─ README.md                     How to work in the repo
├─ PROJECT_OVERVIEW.md           Motivation, methodology, expected outcomes
├─ STRUCTURE.md                  This file
├─ LICENSE                       MIT
├─ pyproject.toml                Package metadata + black/ruff/pytest config
├─ requirements.txt              pip dependencies
├─ environment.yml               conda environment (pr-risk-env)
├─ .env.example                  Template for secrets → copy to .env (gitignored)
├─ .gitignore                    Ignore rules (data, secrets, checkpoints, caches)
├─ .github/workflows/
│  └─ python-checks.yml          CI: ruff + pytest on push/PR to main
│
├─ data/                         Datasets by lifecycle stage
│  ├─ raw/                       Real PRismBench input (gitignored)
│  ├─ interim/                   Cleaned intermediate tables (gitignored)
│  ├─ processed/                 Model-ready tables (gitignored)
│  ├─ labelled/                  Human-labelled pool (gitignored)
│  ├─ unlabelled/                Pool awaiting labelling (gitignored)
│  └─ sample/                    Committed 10-row synthetic sample
│
├─ annotation/                   Labelling schema, guidelines, templates, batches
│  ├─ label_schema.md            is_risky + risk_type definitions
│  ├─ annotation_guidelines.md   How to label
│  ├─ adjudication_notes.md      Resolving disagreements
│  ├─ *_template.csv             Labelled / unlabelled CSV templates
│  └─ annotation_batches/        Per-round batches (review before commit)
│
├─ notebooks/                    01–07 exploration & experiment narratives
│
├─ src/pr_risk/                  Reusable Python package
│  ├─ data/                      load / clean / preprocess / split
│  ├─ features/                  metadata / text / code features + combine
│  ├─ models/                    train baselines & transformer, evaluate, predict, save
│  ├─ active_learning/           query strategies + loop (placeholder)
│  ├─ annotation/                batch creation, label merge/validate, agreement
│  ├─ explainability/            feature importance, SHAP, LIME, suggestions
│  └─ utils/                     paths, config, logging, metrics
│
├─ configs/                      YAML model & experiment configs
├─ experiments/                  CSV experiment tracking (log, summary, AL rounds)
├─ models/                       Local model outputs (baseline/transformer/final)
├─ reports/                      figures / tables / model_comparison / final_results
├─ app/                          labelling_app (Streamlit) + backend (FastAPI) + frontend
├─ docs/                         Academic planning & methodology docs
├─ colab/                        Colab setup + starter notebook
├─ scripts/                      setup / test / sample-experiment helpers
└─ tests/                        pytest tests (sample/synthetic data only)
```

## Root files

Root files define the project, dependencies, environment, tooling, and repository rules. **Commit** `README.md`, `STRUCTURE.md`, `PROJECT_OVERVIEW.md`, `requirements.txt`, `environment.yml`, `pyproject.toml`, `.gitignore`, `.env.example`, and `LICENSE`.

## Folder reference

| Folder | Purpose | Commit policy | Example usage |
|---|---|---|---|
| `data/` | Datasets by stage | Docs, templates, `sample/` only — **no real data** | Real data → `raw/`; cleaned → `interim/`; model-ready → `processed/` |
| `annotation/` | Labelling instructions, schema, batches | Schema & guidelines yes; **review batches** (may contain samples) | Define labels, generate a batch, label, merge |
| `notebooks/` | Research narratives | Yes, **cleaned of large outputs & private data** | Explore, preprocess, model, simulate AL, explain |
| `src/pr_risk/` | Reusable package code | Yes — all source | Import functions into notebooks/apps to keep them thin |
| `configs/` | Reproducible YAML settings | Yes | Point an experiment at a model + AL config |
| `experiments/` | Lightweight CSV logs/summaries | Templates & curated summaries; **no MLflow runs** | Append a row per run; summarise results |
| `models/` | Model outputs & checkpoints | READMEs/`.gitkeep` only — **no binaries** | Save trained `.pkl`/`.pt` locally (gitignored) |
| `reports/` | Final figures/tables/comparisons | Small final assets only | Export a confusion matrix or comparison table |
| `app/` | Prototype interfaces | Yes | Streamlit labelling; FastAPI predict/explain |
| `docs/` | Planning & methodology | Yes | Dataset notes, evaluation/AL/XAI plans, taxonomy |
| `colab/` | Colab setup | Yes (**no Drive-mounted data**) | Mount Drive, clone, install, check GPU |
| `scripts/` | CLI helpers | Yes (**no secrets**) | `setup_env`, `run_tests`, sample experiment |
| `tests/` | pytest tests | Yes | Validate package on sample/synthetic data |
| `.github/workflows/` | CI definitions | Yes | `python-checks.yml` runs ruff + pytest |

## `.gitignore` at a glance

The full rules are in [`.gitignore`](.gitignore). Key intent:

| Pattern(s) | Ignored? | Reason |
|---|---|---|
| `data/raw/*`, `interim/*`, `processed/*`, `labelled/*`, `unlabelled/*` | **Yes** | Real / generated datasets must not be committed |
| `!data/**/README.md`, `!data/**/.gitkeep`, `!data/sample/sample_prs.csv` | **No (kept)** | Docs, folder placeholders, and the safe sample stay tracked |
| `.env`, `.env.*` (except `!.env.example`) | **Yes** | Secrets; only the template is tracked |
| `models/**/*.{pkl,joblib,pt,pth,bin,ckpt,safetensors}`, `checkpoint-*/` | **Yes** | Trained binaries are large and reproducible |
| `mlruns/`, `mlartifacts/`, `wandb/`, `logs/`, `*.log` | **Yes** | Experiment-tracking artifacts & logs |
| `*.parquet`, `*.feather`, `*.arrow`, `*.npy`, `*.npz` | **Yes** | Large binary data exports |
| `.venv/`, `__pycache__/`, `.pytest_cache/`, `.ruff_cache/`, `.ipynb_checkpoints/` | **Yes** | Local environments & caches |

> **Before every `git add`:** confirm you are not staging real PRismBench data, `.env`, model binaries, or large exports. When in doubt, run `git status` and check against the table above.

## Conventions

- **Notebooks stay thin** — put reusable logic in `src/pr_risk/` and import it.
- **Configs drive experiments** — change a YAML in `configs/`, not hard-coded values.
- **One source of truth for labels** — the taxonomy lives in [`annotation/label_schema.md`](annotation/label_schema.md); other docs reference it.
- **Track every run** — append to [`experiments/experiment_log.csv`](experiments/experiment_log.csv).

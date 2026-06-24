# Repository Structure

This document explains what each major folder contains, why it exists, whether its files should be committed, and how it is used.

## Root Files

Root files define the project, dependencies, environment, formatting, and repository rules. Commit `README.md`, `STRUCTURE.md`, `PROJECT_OVERVIEW.md`, `requirements.txt`, `environment.yml`, `pyproject.toml`, `.gitignore`, `.env.example`, and `LICENSE`.

## `data/`

Stores datasets used during experimentation. Commit documentation, templates, and small fake samples only. Do not commit real PRismBench data. Example usage: place the real dataset in `data/raw/`, write cleaned outputs to `data/interim/`, and final model-ready tables to `data/processed/`.

## `annotation/`

Contains labelling instructions, schema definitions, templates, and annotation batches. Commit schema documents, guidelines, and small templates. Review batch files before committing because they may contain dataset samples.

## `notebooks/`

Contains research notebooks for exploration, preprocessing, baseline modelling, active learning simulation, deep learning, explainability, and results analysis. Commit notebooks only when they are cleaned of large outputs and private data.

## `src/pr_risk/`

Contains reusable Python package code. Commit all source code. Keep notebooks thin by calling functions from this package.

## `configs/`

Contains YAML settings for models and experiments. Commit config files because they make experiments reproducible.

## `experiments/`

Contains lightweight CSV logs and summaries. Commit templates and curated summaries. Do not commit large MLflow runs or generated artifacts.

## `models/`

Stores local model outputs, checkpoints, and serialized binaries. Commit only README files and `.gitkeep`; do not commit trained models.

## `reports/`

Stores final figures, tables, model comparisons, and final result artifacts. Commit small, final report assets. Avoid large temporary exports.

## `app/`

Contains prototype interfaces. `app/labelling_app/` is a Streamlit labelling tool. `app/backend/` is a FastAPI prediction and explanation API starter.

## `docs/`

Contains project documentation used for academic planning, dataset notes, environment setup, AWS requests, experiment planning, evaluation, explainability, and risk taxonomy.

## `colab/`

Contains Colab-specific setup instructions and a starter notebook. Do not commit Drive-mounted data.

## `scripts/`

Contains repeatable command-line helpers. Keep secrets out of scripts.

## `tests/`

Contains pytest tests for the package. These tests should use fake sample data or small synthetic data, not the real dataset.

## `.github/workflows/`

Contains GitHub Actions workflows. `python-checks.yml` installs dependencies, runs `ruff`, and runs `pytest`.

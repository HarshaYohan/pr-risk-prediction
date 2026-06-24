# Explainable Pull Request Risk Prediction using Active Learning

This repository contains the starter implementation for a Final Year Project on predicting risks in GitHub Pull Requests (PRs) using the PRismBench dataset of approximately 28,000 PR records.

The project predicts two related targets:

- `is_risky`: binary or ternary risk label for whether a PR is risky.
- `risk_type`: the primary type of risk associated with the PR.

The first version uses single-label risk type classification, where each PR receives one primary `risk_type`. The repository is structured so the task can later be extended to multi-label classification if one PR can contain multiple risk types.

## Problem Statement

Modern software teams use Pull Requests to review changes before merging them. Some PRs introduce bugs, security weaknesses, failed builds, performance regressions, integration issues, test gaps, or maintainability problems. Manually identifying these risks is difficult in active repositories with many contributors and frequent changes.

This project builds an explainable ML/DL system that predicts PR risk before merge time, identifies the likely risk type, explains why the prediction was made, and suggests practical mitigation actions.

## Dataset

The primary dataset is PRismBench, with approximately 28,000 GitHub Pull Request records. The real dataset is not included in this repository. Place local copies under `data/raw/` and keep them out of Git.

Expected feature groups include PR metadata, textual descriptions, code change summaries, review activity, CI information, comments, and other available PR attributes.

## Main Objectives

- Predict whether a PR is risky or non-risky.
- Classify the primary risk type for each PR.
- Use active learning to select uncertain or informative PRs for efficient labelling.
- Use explainable AI to explain predictions and suggest ways to avoid or reduce risk.
- Support local laptop experiments, Google Colab experiments, and later AWS experiments.
- Provide a clean team repository structure that can be pushed to GitHub immediately.

## Risk Labels

Supported `risk_type` classes:

- `non_risky`
- `bug_risk`
- `security_risk`
- `performance_risk`
- `maintainability_risk`
- `integration_risk`
- `build_ci_risk`
- `test_risk`
- `documentation_config_risk`
- `other_risk`
- `unsure`

## Repository Structure Summary

- `data/`: local datasets, processed datasets, labelled pools, and fake sample data.
- `annotation/`: labelling schema, annotation guidelines, templates, and batches.
- `notebooks/`: exploration, preprocessing, modelling, active learning, explainability, and results notebooks.
- `src/pr_risk/`: Python package for data, features, annotation, active learning, models, explainability, and utilities.
- `configs/`: YAML configuration files for experiments and models.
- `experiments/`: CSV experiment tracking templates.
- `models/`: ignored local model outputs and checkpoints.
- `reports/`: figures, tables, comparisons, and final result artifacts.
- `app/`: Streamlit labelling prototype and FastAPI backend starter.
- `docs/`: project, dataset, environment, AWS, evaluation, active learning, and explainability documentation.
- `colab/`: Google Colab setup guidance and starter notebook.
- `scripts/`: setup, test, and sample experiment scripts.
- `tests/`: pytest tests for starter functionality.

## Local Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
pytest
```

On Linux or macOS:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
```

## Google Colab Usage

Use `colab/colab_setup_template.ipynb` as the starting point. The notebook shows how to mount Google Drive, clone this repository, install dependencies, check GPU availability, and import the `pr_risk` package.

For data safety, store real PRismBench files in a private Google Drive folder and do not commit them to GitHub.

## AWS Usage

Local laptop experiments should be used for small tests and baseline runs. Google Colab can be used for early GPU experiments. AWS support is planned for scalable and reproducible experiments using S3 for storage, SageMaker or JupyterLab for notebooks, CPU compute for preprocessing, single-GPU instances for transformer experiments, IAM roles, CloudWatch logs, and AWS Budgets.

See `docs/aws_resource_request.md` for the starter AWS request.

## Basic Workflow

1. Place the real PRismBench dataset in `data/raw/` locally.
2. Explore the dataset in `notebooks/01_data_exploration.ipynb`.
3. Clean and preprocess the data with `src/pr_risk/data/` utilities.
4. Create baseline features with `src/pr_risk/features/`.
5. Train baseline models for `is_risky` and `risk_type`.
6. Use active learning to select uncertain PRs for labelling.
7. Explain predictions using feature importance, SHAP, or LIME.
8. Record experiments in `experiments/` and export results to `reports/`.
9. Demonstrate the workflow through the Streamlit labelling app or FastAPI backend.

## Team Contribution Workflow

- Create a feature branch for each task.
- Keep real data, secrets, checkpoints, and logs out of Git.
- Add or update tests when changing package code.
- Run `ruff`, `black`, and `pytest` before opening a pull request.
- Document experiments in `experiments/experiment_log.csv`.
- Use clear commit messages and request review from `<YOUR_TEAM_NAME>`.

## Project Placeholders

- Team: `<YOUR_TEAM_NAME>`
- Supervisor: `<YOUR_SUPERVISOR_NAME>`

# Project Overview

## Background

Pull Requests are central to modern collaborative software development. They allow developers to propose changes, receive feedback, run automated checks, and merge code into shared branches. However, not every PR carries the same level or type of risk.

## Problem

Reviewers may miss PRs that require extra attention because risk signals can be spread across metadata, text, code changes, comments, CI results, and review activity. Risky PRs can introduce defects, failed builds, integration failures, security weaknesses, performance regressions, or maintainability issues.

## Proposed Solution

This project proposes an explainable machine learning and deep learning system that predicts whether a Pull Request is risky, identifies the most likely risk type, and provides understandable explanations and mitigation suggestions.

## Dataset

The project uses PRismBench, a dataset of approximately 28,000 GitHub Pull Request records. The dataset will be explored to understand available features, labels, class distribution, missing values, and feature quality.

## Methodology

The methodology includes dataset understanding, preprocessing, feature engineering, active learning for labelling support, baseline ML models, transformer-based experiments, model evaluation, explainability, and prototype development.

## Active Learning Loop

The active learning process starts with a small labelled seed set. A model is trained on the labelled data, predicts probabilities for unlabelled PRs, and a query strategy selects uncertain or informative PRs for human labelling. Newly labelled PRs are merged back into the labelled pool, and the process repeats for multiple rounds.

## Explainability

Explainability methods such as feature importance, SHAP, LIME, or attention-based explanations will be used to identify influential factors behind predictions. The explanation component should convert model signals into practical advice, such as requesting additional review, splitting a large PR, adding tests, checking CI failures, or reviewing security-sensitive code.

## Expected Outcome

The expected outcome is a trained and evaluated PR risk prediction system, a risk type classifier, an active learning workflow, an explainability module, and a prototype that demonstrates predictions, explanations, and risk reduction suggestions.

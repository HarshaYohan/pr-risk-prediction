# Tests

Pytest tests for the `pr_risk` package. They run on the committed **sample/synthetic data**, never the real dataset, so CI stays fast and data-safe.

## Run

```bash
pytest            # all tests (config in pyproject.toml: testpaths=tests, pythonpath=src)
pytest -q tests/test_metrics.py
```

`pyproject.toml` already adds `src/` to the path, so `import pr_risk...` works without installing the package.

## Current tests

| File | Covers |
|---|---|
| [test_data_loading.py](test_data_loading.py) | `data.load_data.load_csv` on the sample CSV |
| [test_preprocessing.py](test_preprocessing.py) | `data` cleaning/preprocessing helpers |
| [test_metrics.py](test_metrics.py) | `utils.metrics.classification_metrics` |
| [test_active_learning.py](test_active_learning.py) | `active_learning.query_strategies` |

## Adding tests

- Add or update a test whenever you change package code.
- Use small synthetic inputs or `data/sample/sample_prs.csv`; never load `data/raw/`.
- CI ([`.github/workflows/python-checks.yml`](../.github/workflows/python-checks.yml)) runs `ruff check .` then `pytest` on push/PR to `main`.

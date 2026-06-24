# `pr_risk.data`

Load, clean, preprocess, and split PR datasets. Used by notebooks 01–02.

| Module | Function | Status | Notes |
|---|---|---|---|
| `load_data` | `load_csv(path)` / `save_csv(df, path)` | ✅ | CSV I/O; `save_csv` creates parent dirs |
| `clean_data` | `basic_cleaning(df)` | 🟡 | Drop duplicates, strip strings, empty→NA; `TODO` PRismBench-specific cleaning |
| `preprocess` | `preprocess_pr_dataset(df)` | 🟡 | Orchestrates cleaning; `TODO` column normalisation & missing-value handling |
| `split_data` | `create_train_val_test_split(df, target_col, test_size, val_size)` | ✅ | Stratified train/val/test (stratifies only when a class has >1 member) |

```python
from pr_risk.data.load_data import load_csv
from pr_risk.data.preprocess import preprocess_pr_dataset
from pr_risk.data.split_data import create_train_val_test_split

df = preprocess_pr_dataset(load_csv("data/sample/sample_prs.csv"))
train, val, test = create_train_val_test_split(df, target_col="is_risky")
```

> On the 10-row sample, stratified splitting fails for singleton classes — pass a non-stratified split or filter to `is_risky ∈ {0,1}` (see notebook 02). The stratified path is for the real dataset.

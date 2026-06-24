# `pr_risk.annotation`

Code behind the labelling workflow in [`annotation/`](../../../annotation/README.md) (RQ3). Supports building batches, validating and merging labels, and measuring agreement.

| Module | Function | Status | Notes |
|---|---|---|---|
| `create_annotation_batch` | `create_annotation_batch(unlabelled_df, indices, output_path)` | ✅ | Writes a batch CSV with empty `is_risky`, `risk_type`, `annotator_id`, `annotation_notes` columns |
| `validate_labels` | `validate_label_schema(df)` | ✅ | Checks required columns + allowed `is_risky`/`risk_type` values |
| `merge_labels` | `merge_new_labels(existing_df, new_df)` | ✅ | Concatenate, de-dupe on `pr_id` keeping the latest |
| `agreement` | `calculate_basic_agreement(a, b)` | 🟡 | Exact-match agreement; `TODO` chance-corrected (Cohen's/Fleiss' κ) |

```python
from pr_risk.active_learning.query_strategies import margin_sampling
from pr_risk.annotation.create_annotation_batch import create_annotation_batch

idx = margin_sampling(model.predict_proba(pool_X), batch_size=20)
create_annotation_batch(pool_df, idx, "annotation/annotation_batches/round_01.csv")
```

> The 11 `risk_type` classes accepted by `validate_label_schema` mirror [`annotation/label_schema.md`](../../../annotation/label_schema.md) — keep them in sync if the taxonomy changes.

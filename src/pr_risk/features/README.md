# `pr_risk.features`

Turn PR records into model-ready features. Used by notebook 03.

| Module | Function | Status | Produces |
|---|---|---|---|
| `metadata_features` | `create_metadata_features(df)` | 🟡 | Numeric cols: `files_changed`, `lines_added`, `lines_deleted`, `commits_count`, `comments_count`, `reviewers_count`, `ci_failed` (0/1) |
| `text_features` | `create_text_features_tfidf(train, val, test, max_features, ngram_range)` | ✅ | TF-IDF matrices (fit on train) + fitted vectoriser |
| `code_features` | `create_code_summary_features(df)` | 🟡 | Starter signals from `code_diff_summary`: length, `mentions_ci`, `mentions_security`; `TODO` real code fields/embeddings |
| `feature_pipeline` | `combine_features(*blocks)` | ✅ | Single sparse matrix (`scipy.sparse.hstack`) from mixed pandas/NumPy/sparse blocks |

```python
from pr_risk.features.metadata_features import create_metadata_features
from pr_risk.features.text_features import create_text_features_tfidf
from pr_risk.features.feature_pipeline import combine_features

meta = create_metadata_features(train_df)
Xtr_text, Xval_text, Xte_text, vec = create_text_features_tfidf(
    train_df["title"], val_df["title"], test_df["title"]
)
X_train = combine_features(meta, Xtr_text)
```

> The literature points to **CodeBERT/embedding** features as the next step beyond TF-IDF — see [`docs/README.md`](../../../docs/README.md#tools-surveyed-section-6).

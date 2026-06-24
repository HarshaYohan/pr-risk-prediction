# `pr_risk.models`

Train, evaluate, persist, and predict with models. Used by notebooks 03, 05, 07.

| Module | Function | Status |
|---|---|---|
| `train_baseline` | `train_logistic_regression(X, y)`, `train_random_forest(X, y)` | ✅ |
| `evaluate` | `evaluate_classification_model(model, X_test, y_test)` → accuracy/precision/recall/F1 + report | ✅ |
| `predict` | `predict_risk_and_type(binary_model, risk_type_model, features)` (two-stage) | ✅ |
| `save_model` | `save_model(model, path)`, `load_model(path)` (joblib) | ✅ |
| `train_transformer` | CodeBERT/BERT fine-tuning | ⛔ placeholder |

```python
from pr_risk.models.train_baseline import train_random_forest
from pr_risk.models.evaluate import evaluate_classification_model
from pr_risk.models.save_model import save_model

model = train_random_forest(X_train, y_train)
print(evaluate_classification_model(model, X_test, y_test)["f1_score"])
save_model(model, "models/baseline/rf_is_risky.joblib")
```

> For multi-class `risk_type` and code-text semantics, the planned path is CodeBERT (`configs/codebert.yaml`) — `train_transformer` is the place to implement it. Model binaries are gitignored (see [`models/README.md`](../../../models/README.md)).

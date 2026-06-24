# `pr_risk.utils`

Shared helpers used across the package.

| Module | API | Status | Notes |
|---|---|---|---|
| `paths` | `PROJECT_ROOT`, `DATA_DIR`, `CONFIG_DIR`, `MODEL_DIR`, `REPORTS_DIR`, `EXPERIMENTS_DIR` | ✅ | Absolute paths derived from the package location — use these instead of hard-coding |
| `config` | `load_config(path)` | ✅ | Load a YAML config (e.g. `configs/codebert.yaml`) into a dict |
| `logging` | `get_logger(name, level)` | ✅ | Consistent stream logger; safe to call repeatedly |
| `metrics` | `classification_metrics(y_true, y_pred, y_proba, average)` | ✅ | Accuracy, precision, recall, F1, and ROC-AUC when probabilities are given |

```python
from pr_risk.utils.paths import DATA_DIR
from pr_risk.utils.config import load_config
from pr_risk.utils.metrics import classification_metrics

cfg = load_config("configs/codebert.yaml")
m = classification_metrics(y_test, preds, y_proba=proba[:, 1])
```

> Evaluation focus (recall/F1 on risky classes) is defined in [`docs/model_evaluation_plan.md`](../../../docs/model_evaluation_plan.md).

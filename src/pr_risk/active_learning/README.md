# `pr_risk.active_learning`

Query strategies and loop orchestration for active learning (RQ3). Used by notebook 04.

| Module | Function | Status | Idea |
|---|---|---|---|
| `query_strategies` | `random_sampling` | ✅ | Baseline random selection |
| `query_strategies` | `least_confidence_sampling(probas, k)` | ✅ | Lowest top-class probability |
| `query_strategies` | `margin_sampling(probas, k)` | ✅ | Smallest gap between top-2 classes (best for multi-class boundaries) |
| `query_strategies` | `entropy_sampling(probas, k)` | ✅ | Highest predictive entropy |
| `query_strategies` | `diversity_sampling(features, k)` | 🟡 | Placeholder — random fallback; `TODO` clustering / embedding distance |
| `uncertainty_/margin_/entropy_/diversity_sampling` | re-exports | ✅ | Thin compatibility wrappers around `query_strategies` |
| `active_learning_loop` | `active_learning_loop(...)` | ⛔ | Raises `NotImplementedError` — orchestrator to build |

```python
import numpy as np
from pr_risk.active_learning.query_strategies import margin_sampling

probas = model.predict_proba(pool_X)
to_label = margin_sampling(probas, batch_size=5)   # row indices into the pool
```

> Notebook 04 simulates the full loop inline (train → score pool → query → "label" via ground truth → merge → repeat) until `active_learning_loop` is implemented. Strategy theory (margin, diversity, QBC, two-stage, evidence-based) is summarised in [`docs/README.md`](../../../docs/README.md#active-learning-strategies-section-3). Config: [`configs/active_learning.yaml`](../../../configs/active_learning.yaml).

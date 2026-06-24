# `pr_risk.explainability`

Explain predictions and turn them into developer-facing advice (RQ2). Used by notebook 06.

| Module | Function | Status | Notes |
|---|---|---|---|
| `feature_importance` | `explain_with_feature_importance(model, feature_names, top_k)` | ✅ | Works for models exposing `feature_importances_` or `coef_` |
| `explanation_generator` | `generate_human_readable_explanation(prediction, risk_type, top_factors)` | ✅ | Converts signals into a readable explanation + mitigation suggestion |
| `shap_explainer` | `explain_with_shap(model, X, feature_names)` | ⛔ | Planned — choose explainer per model family |
| `lime_explainer` | `explain_with_lime(model, instance, training_data, feature_names)` | ⛔ | Planned — configure for tabular/text/combined |

```python
from pr_risk.explainability.feature_importance import explain_with_feature_importance
from pr_risk.explainability.explanation_generator import generate_human_readable_explanation

top = explain_with_feature_importance(model, feature_names, top_k=5)
print(generate_human_readable_explanation(1, "security_risk", top["feature"].tolist()))
```

> LIME vs SHAP trade-offs and the "agreement = robustness" heuristic are summarised in [`docs/README.md`](../../../docs/README.md#explainability--lime-vs-shap-section-5). Notebook 06 demonstrates SHAP/LIME inline (guarded) until these modules are implemented.

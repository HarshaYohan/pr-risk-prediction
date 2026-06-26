"""Feature importance explanation helpers."""
import pandas as pd


def explain_with_feature_importance(model, feature_names, top_k: int = 10) -> pd.DataFrame:
    """Return top feature importances for models that expose coefficients or importances."""
    if hasattr(model, "feature_importances_"):
        values = model.feature_importances_
    elif hasattr(model, "coef_"):
        values = abs(model.coef_).mean(axis=0) if model.coef_.ndim > 1 else abs(model.coef_[0])
    else:
        raise ValueError("Model does not expose feature_importances_ or coef_.")
    importance = pd.DataFrame({"feature": list(feature_names), "importance": values})
    return importance.sort_values("importance", ascending=False).head(top_k).reset_index(drop=True)

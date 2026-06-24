"""Prediction helpers."""

def predict_risk_and_type(binary_model, risk_type_model, features) -> dict:
    """Predict risk status and risk type using a two-stage pipeline placeholder.

    The project may train a binary model for `is_risky`, a multiclass model for
    `risk_type`, or a two-stage pipeline where Stage 1 predicts risky/non-risky
    and Stage 2 predicts risk type if risky.
    """
    is_risky = binary_model.predict(features)
    risk_type = risk_type_model.predict(features) if risk_type_model is not None else None
    return {"is_risky": is_risky, "risk_type": risk_type}

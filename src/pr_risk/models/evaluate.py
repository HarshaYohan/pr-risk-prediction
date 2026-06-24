"""Model evaluation helpers."""
from sklearn.metrics import accuracy_score, classification_report, f1_score, precision_score, recall_score

def evaluate_classification_model(model, X_test, y_test) -> dict:
    """Evaluate a fitted classifier on test data."""
    predictions = model.predict(X_test)
    return {
        "accuracy": accuracy_score(y_test, predictions),
        "precision": precision_score(y_test, predictions, average="weighted", zero_division=0),
        "recall": recall_score(y_test, predictions, average="weighted", zero_division=0),
        "f1_score": f1_score(y_test, predictions, average="weighted", zero_division=0),
        "classification_report": classification_report(y_test, predictions, zero_division=0),
    }

"""Metric helpers for classification tasks."""
from sklearn.metrics import accuracy_score, f1_score, precision_score, recall_score, roc_auc_score


def classification_metrics(y_true, y_pred, y_proba=None, average: str = "weighted") -> dict:
    """Calculate common classification metrics, including ROC-AUC when possible."""
    metrics = {
        "accuracy": accuracy_score(y_true, y_pred),
        "precision": precision_score(y_true, y_pred, average=average, zero_division=0),
        "recall": recall_score(y_true, y_pred, average=average, zero_division=0),
        "f1_score": f1_score(y_true, y_pred, average=average, zero_division=0),
        "roc_auc": None,
    }
    if y_proba is not None:
        try:
            metrics["roc_auc"] = roc_auc_score(y_true, y_proba)
        except ValueError:
            metrics["roc_auc"] = None
    return metrics

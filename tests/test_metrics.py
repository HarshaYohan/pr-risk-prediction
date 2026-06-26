from pr_risk.utils.metrics import classification_metrics


def test_classification_metrics_basic_values():
    metrics = classification_metrics([0, 1, 1], [0, 1, 0])
    assert metrics["accuracy"] == 2 / 3
    assert "f1_score" in metrics
    assert metrics["roc_auc"] is None

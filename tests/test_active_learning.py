import numpy as np
from pr_risk.active_learning.query_strategies import entropy_sampling, least_confidence_sampling, margin_sampling, random_sampling

def test_random_sampling_returns_requested_batch_size():
    selected = random_sampling(pool_size=20, batch_size=5, random_state=1)
    assert len(selected) == 5
    assert len(set(selected)) == 5

def test_uncertainty_strategies_return_indices():
    probas = np.array([[0.9, 0.1], [0.51, 0.49], [0.7, 0.3]])
    assert least_confidence_sampling(probas, 1)[0] == 1
    assert entropy_sampling(probas, 1)[0] == 1
    assert margin_sampling(probas, 1)[0] == 1

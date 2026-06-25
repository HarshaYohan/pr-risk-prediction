"""Common active learning query strategies."""
import numpy as np


def random_sampling(pool_size: int, batch_size: int, random_state: int = 42) -> np.ndarray:
    """Select random row indices from an unlabelled pool."""
    rng = np.random.default_rng(random_state)
    return rng.choice(pool_size, size=min(batch_size, pool_size), replace=False)

def least_confidence_sampling(probas, batch_size: int) -> np.ndarray:
    """Select samples where the model's highest class probability is lowest."""
    probas = np.asarray(probas)
    uncertainty = 1 - probas.max(axis=1)
    return np.argsort(uncertainty)[-batch_size:][::-1]

def entropy_sampling(probas, batch_size: int) -> np.ndarray:
    """Select samples with highest predictive entropy."""
    probas = np.asarray(probas)
    clipped = np.clip(probas, 1e-12, 1.0)
    entropy = -(clipped * np.log(clipped)).sum(axis=1)
    return np.argsort(entropy)[-batch_size:][::-1]

def margin_sampling(probas, batch_size: int) -> np.ndarray:
    """Select samples with the smallest margin between top two class probabilities."""
    probas = np.asarray(probas)
    sorted_probas = np.sort(probas, axis=1)
    margins = sorted_probas[:, -1] - sorted_probas[:, -2]
    return np.argsort(margins)[:batch_size]

def diversity_sampling(features, batch_size: int, random_state: int = 42) -> np.ndarray:
    """Placeholder diversity sampler.

    TODO: Replace random selection with clustering or embedding-distance selection.
    """
    return random_sampling(features.shape[0], batch_size, random_state=random_state)

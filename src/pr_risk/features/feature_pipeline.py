"""Feature combination helpers."""
from scipy.sparse import csr_matrix, hstack


def combine_features(*feature_blocks):
    """Combine pandas, NumPy, or sparse feature blocks into one sparse matrix."""
    matrices = []
    for block in feature_blocks:
        if block is None:
            continue
        matrices.append(csr_matrix(block.values) if hasattr(block, "values") else csr_matrix(block))
    if not matrices:
        raise ValueError("At least one feature block is required.")
    return hstack(matrices)

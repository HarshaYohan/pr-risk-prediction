"""Simple annotator agreement helpers."""

def calculate_basic_agreement(labels_a, labels_b) -> float:
    """Calculate exact-match agreement between two equally sized label sequences."""
    labels_a = list(labels_a)
    labels_b = list(labels_b)
    if len(labels_a) != len(labels_b):
        raise ValueError("Both label sequences must have the same length.")
    if not labels_a:
        return 0.0
    matches = sum(a == b for a, b in zip(labels_a, labels_b, strict=True))
    return matches / len(labels_a)

"""Model persistence helpers."""
from pathlib import Path

import joblib


def save_model(model, path: str | Path) -> None:
    """Save a model with joblib."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    joblib.dump(model, output_path)

def load_model(path: str | Path):
    """Load a model saved with joblib."""
    return joblib.load(Path(path))

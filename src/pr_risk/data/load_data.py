"""Data loading and saving helpers."""
from pathlib import Path

import pandas as pd


def load_csv(path: str | Path) -> pd.DataFrame:
    """Load a CSV file into a pandas DataFrame."""
    return pd.read_csv(Path(path))

def save_csv(df: pd.DataFrame, path: str | Path) -> None:
    """Save a pandas DataFrame to CSV, creating parent folders if needed."""
    output_path = Path(path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)

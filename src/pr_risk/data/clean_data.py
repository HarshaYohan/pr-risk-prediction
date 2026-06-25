"""Basic cleaning helpers for PR datasets."""
import pandas as pd


def basic_cleaning(df: pd.DataFrame) -> pd.DataFrame:
    """Return a lightly cleaned copy of a PR dataset."""
    cleaned = df.copy().drop_duplicates()
    string_cols = cleaned.select_dtypes(include="object").columns
    for col in string_cols:
        cleaned[col] = cleaned[col].astype("string").str.strip()
        cleaned[col] = cleaned[col].replace("", pd.NA)
    # TODO: Add PRismBench-specific cleaning after inspecting the real columns.
    return cleaned

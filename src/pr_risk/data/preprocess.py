"""Preprocessing orchestration helpers."""
import pandas as pd

from pr_risk.data.clean_data import basic_cleaning


def preprocess_pr_dataset(df: pd.DataFrame) -> pd.DataFrame:
    """Run the starter preprocessing pipeline for PR data."""
    # TODO: Add PRismBench-specific column normalization and missing value handling.
    return basic_cleaning(df)

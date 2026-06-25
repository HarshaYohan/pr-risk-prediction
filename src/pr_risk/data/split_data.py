"""Train, validation, and test splitting helpers."""
import pandas as pd
from sklearn.model_selection import train_test_split


def create_train_val_test_split(
    df: pd.DataFrame,
    target_col: str,
    test_size: float = 0.2,
    val_size: float = 0.1,
    random_state: int = 42,
) -> tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Split a labelled dataset into train, validation, and test DataFrames."""
    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found in DataFrame.")
    stratify = df[target_col] if df[target_col].nunique() > 1 else None
    train_val_df, test_df = train_test_split(
        df, test_size=test_size, random_state=random_state, stratify=stratify
    )
    relative_val_size = val_size / (1 - test_size)
    stratify_train_val = (
        train_val_df[target_col] if train_val_df[target_col].nunique() > 1 else None
    )
    train_df, val_df = train_test_split(
        train_val_df,
        test_size=relative_val_size,
        random_state=random_state,
        stratify=stratify_train_val,
    )
    return train_df, val_df, test_df

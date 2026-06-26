"""Merge new labels into the existing labelled pool."""
import pandas as pd


def merge_new_labels(
    existing_labelled_df: pd.DataFrame, new_labels_df: pd.DataFrame
) -> pd.DataFrame:
    """Merge labelled rows, keeping the latest label for duplicate PR IDs when available."""
    merged = pd.concat([existing_labelled_df, new_labels_df], ignore_index=True)
    if "pr_id" in merged.columns:
        merged = merged.drop_duplicates(subset=["pr_id"], keep="last")
    return merged.reset_index(drop=True)

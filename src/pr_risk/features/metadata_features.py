"""Metadata feature engineering for Pull Requests."""
import pandas as pd

DEFAULT_METADATA_COLUMNS = [
    "files_changed", "lines_added", "lines_deleted", "commits_count",
    "comments_count", "reviewers_count", "ci_failed",
]

def create_metadata_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create numeric metadata features from common PR columns."""
    features = pd.DataFrame(index=df.index)
    for col in DEFAULT_METADATA_COLUMNS:
        if col in df.columns:
            if col == "ci_failed":
                features[col] = df[col].astype(str).str.lower().isin(["true", "1", "yes"]).astype(int)
            else:
                features[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)
    # TODO: Add PRismBench-specific metadata fields after inspecting the real dataset.
    return features

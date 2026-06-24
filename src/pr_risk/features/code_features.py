"""Code-related feature placeholders."""
import pandas as pd

def create_code_summary_features(df: pd.DataFrame) -> pd.DataFrame:
    """Create starter code-change features from diff summary text."""
    features = pd.DataFrame(index=df.index)
    if "code_diff_summary" in df.columns:
        summary = df["code_diff_summary"].fillna("").astype(str)
        features["code_summary_length"] = summary.str.len()
        features["mentions_ci"] = summary.str.contains("ci|build", case=False, regex=True).astype(int)
        features["mentions_security"] = summary.str.contains(
            "auth|security|token|sql|permission", case=False, regex=True
        ).astype(int)
    # TODO: Replace with PRismBench-specific code fields and embeddings.
    return features

import pandas as pd
from pr_risk.data.clean_data import basic_cleaning
from pr_risk.features.metadata_features import create_metadata_features

def test_basic_cleaning_trims_strings_and_drops_duplicates():
    df = pd.DataFrame({"title": [" Fix bug ", " Fix bug "], "is_risky": [1, 1]})
    cleaned = basic_cleaning(df)
    assert len(cleaned) == 1
    assert cleaned.iloc[0]["title"] == "Fix bug"

def test_create_metadata_features_handles_ci_failed():
    df = pd.DataFrame({"files_changed": [2], "ci_failed": ["true"]})
    features = create_metadata_features(df)
    assert features.loc[0, "files_changed"] == 2
    assert features.loc[0, "ci_failed"] == 1

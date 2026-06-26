from pathlib import Path

from pr_risk.data.load_data import load_csv


def test_load_sample_csv():
    df = load_csv(Path("data/sample/sample_prs.csv"))
    assert len(df) == 10
    assert {"pr_id", "is_risky", "risk_type"}.issubset(df.columns)

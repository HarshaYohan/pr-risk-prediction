"""Validate annotation labels."""
import pandas as pd

VALID_IS_RISKY = {0, 1, 2, "0", "1", "2"}
VALID_RISK_TYPES = {
    "non_risky", "bug_risk", "security_risk", "performance_risk",
    "maintainability_risk", "integration_risk", "build_ci_risk",
    "test_risk", "documentation_config_risk", "other_risk", "unsure",
}

def validate_label_schema(df: pd.DataFrame) -> bool:
    """Validate that required label columns exist and contain allowed values."""
    missing = {"is_risky", "risk_type"}.difference(df.columns)
    if missing:
        raise ValueError(f"Missing required label columns: {sorted(missing)}")
    invalid_is_risky = set(df["is_risky"].dropna().unique()).difference(VALID_IS_RISKY)
    invalid_risk_types = set(df["risk_type"].dropna().unique()).difference(VALID_RISK_TYPES)
    if invalid_is_risky:
        raise ValueError(f"Invalid is_risky labels: {sorted(invalid_is_risky)}")
    if invalid_risk_types:
        raise ValueError(f"Invalid risk_type labels: {sorted(invalid_risk_types)}")
    return True

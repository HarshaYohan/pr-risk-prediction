"""Human-readable explanation generation."""

def generate_human_readable_explanation(prediction, risk_type: str, top_factors) -> str:
    """Generate a simple explanation and mitigation suggestion."""
    factors = ", ".join(str(factor) for factor in top_factors) if top_factors else "no dominant factors"
    if prediction in [1, "1", True, "risky"]:
        return (
            f"This PR is predicted as risky with primary risk type '{risk_type}'. "
            f"Important factors include: {factors}. Consider requesting additional review, "
            "adding targeted tests, checking CI results, and splitting large changes if possible."
        )
    return f"This PR is predicted as non-risky. Important factors include: {factors}."

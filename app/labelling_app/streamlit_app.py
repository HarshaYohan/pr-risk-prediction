"""Simple Streamlit labelling app for PR risk annotation."""
from pathlib import Path

import pandas as pd
import streamlit as st

RISK_TYPES = [
    "non_risky", "bug_risk", "security_risk", "performance_risk",
    "maintainability_risk", "integration_risk", "build_ci_risk",
    "test_risk", "documentation_config_risk", "other_risk", "unsure",
]

st.set_page_config(page_title="PR Risk Labelling", layout="wide")
st.title("PR Risk Labelling")
uploaded_file = st.file_uploader("Upload an annotation CSV", type=["csv"])
output_path = st.text_input("Output CSV path", value="data/labelled/streamlit_labels.csv")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    if df.empty:
        st.warning("The uploaded file has no rows.")
        st.stop()
    row_index = st.number_input("Row", min_value=0, max_value=len(df) - 1, value=0, step=1)
    row = df.iloc[int(row_index)]
    st.subheader("Pull Request Details")
    st.json(row.to_dict())
    is_risky = st.selectbox(
        "is_risky",
        options=[0, 1, 2],
        format_func=lambda x: {0: "0 - non-risky", 1: "1 - risky", 2: "2 - unsure"}[x],
    )
    risk_type = st.selectbox("risk_type", options=RISK_TYPES)
    notes = st.text_area("Annotation notes")
    if st.button("Save labelled row"):
        labelled_row = row.to_dict()
        labelled_row.update(
            {"is_risky": is_risky, "risk_type": risk_type, "annotation_notes": notes}
        )
        output = Path(output_path)
        output.parent.mkdir(parents=True, exist_ok=True)
        new_df = pd.DataFrame([labelled_row])
        if output.exists():
            new_df = pd.concat([pd.read_csv(output), new_df], ignore_index=True)
        new_df.to_csv(output, index=False)
        st.success(f"Saved label to {output}")
else:
    st.info("Upload a CSV batch to begin labelling.")

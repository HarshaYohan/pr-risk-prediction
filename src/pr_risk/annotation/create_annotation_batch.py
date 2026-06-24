"""Create annotation batches from an unlabelled pool."""
from pathlib import Path
import pandas as pd

def create_annotation_batch(unlabelled_df: pd.DataFrame, selected_indices, output_path: str | Path) -> pd.DataFrame:
    """Create and save an annotation batch from selected row indices."""
    batch = unlabelled_df.loc[selected_indices].copy()
    batch["is_risky"] = ""
    batch["risk_type"] = ""
    batch["annotator_id"] = ""
    batch["annotation_notes"] = ""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)
    batch.to_csv(output, index=False)
    return batch

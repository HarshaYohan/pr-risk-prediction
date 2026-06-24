# `data/labelled/` — labelled pool

Human-labelled PR pools used for training and active learning (grows each AL round). **Gitignored.**

- Written by the labelling app and `pr_risk.annotation.merge_labels`.
- Schema follows [`annotation/label_schema.md`](../../annotation/README.md) (`is_risky`, `risk_type`, …).
- Feeds the AL loop in [notebook 04](../../notebooks/04_active_learning_simulation.ipynb).

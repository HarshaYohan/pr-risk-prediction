# `data/unlabelled/` — pool awaiting labels

Candidate PR pool the active-learning loop scores and queries from. **Gitignored.**

- The query strategy selects batches → [`annotation/annotation_batches/`](../../annotation/README.md#labelling-workflow).
- Labelled rows move to [`../labelled/`](../labelled/README.md).

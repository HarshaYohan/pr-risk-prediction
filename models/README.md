# Models

Local model outputs, checkpoints, and serialized binaries. **Binaries are gitignored** — only README/`.gitkeep` files are committed. Trained models are large and fully reproducible from code + configs + data, so they don't belong in Git.

## Subfolders

| Folder | Holds | Saved by |
|---|---|---|
| [baseline/](baseline/README.md) | LR / RF / XGBoost artifacts (`.pkl`, `.joblib`) | `pr_risk.models.save_model` (nb 03) |
| [transformer/](transformer/README.md) | CodeBERT checkpoints (`.pt`, `.bin`, `.safetensors`, `checkpoint-*/`) | nb 05 |
| [final/](final/README.md) | The chosen model(s) for the demo/report | After evaluation |

## Conventions

- Name files with the `experiment_id` so a model maps to its row in [`experiments/experiment_log.csv`](../experiments/experiment_log.csv).
- Large checkpoints belong in private Drive/S3 for sharing, not Git (see [`colab/drive_structure.md`](../colab/drive_structure.md)).
- Ignored patterns: `*.pkl`, `*.joblib`, `*.pt`, `*.pth`, `*.bin`, `*.ckpt`, `*.safetensors`, `checkpoint-*/` (see [`.gitignore`](../.gitignore)).

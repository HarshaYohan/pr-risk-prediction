# Colab

Google Colab setup for early GPU experiments (transformers in notebook 05). Use [`colab_setup_template.ipynb`](colab_setup_template.ipynb) as the starting point.

## Typical flow

```mermaid
flowchart LR
    mount[Mount Google Drive] --> clone[Clone this repo]
    clone --> install[pip install -r requirements.txt]
    install --> gpu[Check GPU available]
    gpu --> data[Load data from private Drive folder]
    data --> run[Run notebook]
```

1. **Mount Drive** to access private data and persist model artifacts.
2. **Clone** the GitHub repo into the Colab runtime.
3. **Install** dependencies from `requirements.txt`.
4. **Check GPU** (`torch.cuda.is_available()`).
5. **Import** the `pr_risk` package (add `src/` to `sys.path`).

## Data safety

Store real PRismBench files and model checkpoints in a **private Drive folder** following [`drive_structure.md`](drive_structure.md) — never commit them to GitHub. Only commit the setup notebook and these docs.

## When to use Colab vs. local vs. AWS

- **Local** — exploration, preprocessing, baselines, AL simulation.
- **Colab** — early GPU runs (CodeBERT fine-tuning on a subset).
- **AWS (planned)** — scalable, reproducible runs; see [`docs/aws_resource_request.md`](../docs/aws_resource_request.md).

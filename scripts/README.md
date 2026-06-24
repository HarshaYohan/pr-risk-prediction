# Scripts

Repeatable command-line helpers. Keep secrets out of scripts (use `.env`).

## Available scripts

| Script | Platform | What it does |
|---|---|---|
| [setup_env.ps1](setup_env.ps1) | Windows | Create `.venv`, upgrade pip, install `requirements.txt` |
| [setup_env.sh](setup_env.sh) | Unix | Same, for bash/zsh |
| [run_tests.ps1](run_tests.ps1) | Windows | Run `ruff` + `pytest` |
| [run_tests.sh](run_tests.sh) | Unix | Same, for bash/zsh |
| [create_sample_experiment.py](create_sample_experiment.py) | Any | Append a starter row to `experiments/experiment_log.csv` |

## Usage

```powershell
# Windows
./scripts/setup_env.ps1
./scripts/run_tests.ps1
```

```bash
# Unix
bash scripts/setup_env.sh
bash scripts/run_tests.sh
python scripts/create_sample_experiment.py
```

Run scripts from the **repository root** so relative paths (`experiments/…`, `requirements.txt`) resolve correctly.

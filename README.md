# ds-init

> Scaffold production-ready data science projects in seconds.

```bash
pip install ds-init
ds-init my-project
```

No more copy-pasting folder structures from old projects.

## Features

- **opinionated templates** — folder structure, requirements.txt, train/evaluate scripts, notebooks
- **optional components** — DVC data versioning, MLflow experiment tracking, uv fast envs
- **template types** — basic, computer vision, NLP
- **zero external assets** — all templates embedded in code, installs fast

## Quick Start

```bash
# Basic project
ds-init my-project

# With DVC + MLflow
ds-init my-project --with-dvc --with-mlflow

# Computer vision project
ds-init cv-project --template cv

# Interactive mode
ds-init my-project --interactive
```

## Generated Structure

```
my-project/
├── src/
│   ├── __init__.py
│   ├── data.py
│   ├── train.py
│   └── evaluate.py
├── configs/
│   └── train.yaml
├── notebooks/
│   └── eda.ipynb
├── data/
│   └── raw/
├── requirements.txt
├── .gitignore
└── README.md
```

With `--with-dvc`:
```
├── dvc.yaml
├── params.yaml
├── src/
│   └── preprocess.py
├── data/
│   ├── raw/
│   └── processed/
└── models/
```

## Installation

```bash
pip install ds-init
```

Or from source:
```bash
git clone https://github.com/SohamPBhagat/ds-init.git
cd ds-init
pip install -e .
```

## Options

| Flag | Description |
|------|-------------|
| `--template`, `-t` | Template type: `basic`, `cv`, `nlp` |
| `--with-dvc` | Add DVC data versioning configuration |
| `--with-mlflow` | Add MLflow experiment tracking |
| `--with-uv` | Add .uvignore for uv environments |
| `--interactive`, `-i` | Interactive project setup |

## License

MIT
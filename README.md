# ds-init

<div align="center">

![PyPI](https://img.shields.io/pypi/pyversions/ds-init.svg)
![License](https://img.shields.io/badge/License-MIT-green)
![Stars](https://img.shields.io/github/stars/SohamPBhagat/ds-init?style=social)

**Scaffold production-ready data science projects in seconds.**

```bash
pip install ds-init
ds-init my-project
```

[Quick Start](#quick-start) · [Features](#features) · [Installation](#installation) · [Contributing](#contributing)

</div>

---

## The Problem

Every data science project starts the same way:

1. Create a folder
2. Google "best folder structure for ML projects"
3. Copy-paste from an old project
4. Mess with `.gitignore`, `requirements.txt`, and config files
5. Waste 30 minutes before writing a single line of ML code

**ds-init solves this.** One command, production-ready structure, ready to code in 10 seconds.

## The Solution

```bash
# Installs in seconds, works anywhere
pip install ds-init

# Create a complete ML project with one command
ds-init my-ml-project

# Or add your tools of choice
ds-init my-ml-project --with-dvc --with-mlflow --template cv
```

That's it. You now have:

- Clean folder structure following best practices
- Production-ready `requirements.txt`
- Train/evaluate/preprocess scripts
- DVC pipeline configuration
- MLflow experiment tracking setup
- Jupyter notebook scaffold
- Proper `.gitignore` for ML projects

## Features

| Feature | Description |
|---------|-------------|
| **Opinionated Templates** | Battle-tested folder structure used in production ML teams |
| **Zero Friction** | All templates embedded in code — no external files to download |
| **DVC Integration** | Data versioning out of the box with pre-configured pipelines |
| **MLflow Tracking** | Experiment tracking that actually works, not boilerplate |
| **Fast Install** | Single `pip install ds-init`, no heavy dependencies |
| **Type-Specific Scaffolding** | Basic, Computer Vision, and NLP project templates |

## Quick Start

```bash
# Install
pip install ds-init

# Basic project (recommended starting point)
ds-init my-project

# Computer Vision project with DVC + MLflow
ds-init cv-classifier --template cv --with-dvc --with-mlflow

# NLP project with experiment tracking
ds-init nlp-sentiment --template nlp --with-mlflow

# See all options
ds-init --help
```

## Generated Structure

A basic project scaffolded with `ds-init my-project`:

```
my-project/
├── src/
│   ├── __init__.py       # Package marker
│   ├── data.py           # Data loading utilities
│   ├── train.py          # Training script (edit this)
│   └── evaluate.py       # Evaluation script
├── configs/
│   └── train.yaml        # Training configuration
├── notebooks/
│   └── eda.ipynb         # EDA notebook
├── data/
│   └── raw/              # Your data goes here
├── requirements.txt      # Dependencies
├── .gitignore            # Git ignore for ML projects
└── README.md             # Project readme template
```

With `--with-dvc --with-mlflow`:

```
├── dvc.yaml              # DVC pipeline definition
├── params.yaml           # Hyperparameters
├── src/
│   ├── preprocess.py     # Preprocessing pipeline
│   └── train_mlflow.py   # MLflow-tracked training
├── data/
│   ├── raw/              # Raw data (DVC tracked)
│   └── processed/        # Processed data
└── models/               # Trained models (DVC tracked)
```

## Template Types

### `basic` (default)
General-purpose template for tabular data, regression, classification, clustering.

**Use when:** You have structured/tabular data, working on classical ML.

### `cv` (Computer Vision)
Includes image loading utilities and CV-specific preprocessing.

**Use when:** Object detection, image classification, image segmentation, etc.

### `nlp` (Natural Language Processing)
Includes tokenizer utilities and NLP-specific preprocessing.

**Use when:** Text classification, sentiment analysis, language models, etc.

## Installation

### From PyPI (Recommended)

```bash
pip install ds-init
```

### From Source

```bash
git clone https://github.com/SohamPBhagat/ds-init.git
cd ds-init
pip install -e .
```

### Development Install

```bash
git clone https://github.com/SohamPBhagat/ds-init.git
cd ds-init
pip install -e ".[dev]"
pytest tests/  # Run tests
```

## Command Reference

```bash
ds-init --help
ds-init --version

ds-init init PROJECT_NAME [OPTIONS]

Options:
  -t, --template [basic|cv|nlp]  Project template (default: basic)
  --with-dvc                       Add DVC data versioning
  --with-mlflow                    Add MLflow experiment tracking
  --with-uv                        Configure for uv environments
  -i, --interactive               Interactive project setup
```

## Why ds-init?

| Approach | Time to Ready | Maintainability | Reproducibility |
|----------|---------------|-----------------|-----------------|
| Copy-paste from old projects | 15-30 min | Poor | None |
| Cookiecutter templates | 5-10 min | Moderate | Template-dependent |
| **ds-init** | **10 seconds** | **High** | **Reproducible** |

ds-init templates are:
- **Battle-tested** — Structure used in production ML systems
- **Minimal but complete** — Just enough to start, nothing to delete
- **Extensible** — Easy to customize once you understand the structure

## Requirements

- Python 3.9 or higher
- pip or any Python package manager

## Contributing

Contributions are welcome! Here's how to get started:

1. **Fork the repository**
2. **Clone your fork**
   ```bash
   git clone https://github.com/YOUR_USERNAME/ds-init.git
   cd ds-init
   ```
3. **Install in development mode**
   ```bash
   pip install -e ".[dev]"
   ```
4. **Run tests**
   ```bash
   pytest tests/ -v
   ```
5. **Make your changes** and add tests
6. **Submit a pull request**

### Generated Project Dependencies

When a project is scaffolded with ds-init, all dependencies (numpy, pandas, scikit-learn, etc.) are already listed in the generated `requirements.txt`. Run `pip install -r requirements.txt` to set up the environment.

### Ideas for Contributions

- New template types (time series, reinforcement learning, etc.)
- Interactive CLI mode implementation
- VS Code / JetBrains integration snippets
- GitHub Actions workflow templates
- Documentation improvements

## Roadmap

- [ ] Interactive CLI mode
- [ ] Time series template
- [ ] PyTorch Lightning support
- [ ] Weights & Biases integration
- [ ] GitHub Actions workflow templates
- [ ] VS Code devcontainer.json generation

## License

MIT License — use it for anything, no strings attached.

---

<div align="center">

**If ds-init saved you time, star the repo — it helps others find it.**

[![Star](https://img.shields.io/github/stars/SohamPBhagat/ds-init?style=social)](https://github.com/SohamPBhagat/ds-init)

</div>
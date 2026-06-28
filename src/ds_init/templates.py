"""Template strings for ds-init project generation.

All templates are embedded as strings — no external files needed.
"""

# Basic project template
BASIC_TEMPLATE = {
    "__init__.py": '''"""{{ project_name }} — data science project."""\n''',
    "requirements.txt": """# Core
numpy>=1.24.0
pandas>=2.0.0
scikit-learn>=1.3.0
matplotlib>=3.7.0
seaborn>=0.12.0

# Dev / utils
jupyter>=1.0.0
ipykernel>=6.0.0
pytest>=7.0.0
""",
    ".gitignore": """# Byte-compiled
__pycache__/
*.py[cod]
*$py.class

# Virtual environments
venv/
env/
.venv/

# Jupyter
.ipynb_checkpoints/

# Data (use DVC)
data/
*.csv
*.parquet

# Models
models/
*.pkl
*.joblib

# Logs
logs/
*.log

# OS
.DS_Store
Thumbs.db
""",
    "src/__init__.py": '''"""Source package."""\n''',
    "src/data.py": '''"""Data loading and preprocessing."""

import pandas as pd


def load_data(path: str) -> pd.DataFrame:
    """Load data from CSV file."""
    return pd.read_csv(path)


def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """Basic preprocessing."""
    return df.dropna()
''',
    "src/train.py": '''"""Training script."""

import argparse
import yaml
from pathlib import Path


def train(config_path: str = "configs/train.yaml"):
    """Run training pipeline."""
    with open(config_path) as f:
        config = yaml.safe_load(f)
    print(f"Training with config: {config}")
    # TODO: implement training


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="configs/train.yaml")
    args = parser.parse_args()
    train(args.config)
''',
    "src/evaluate.py": '''"""Evaluation script."""

import argparse
import pickle


def evaluate(model_path: str, data_path: str):
    """Evaluate a trained model."""
    with open(model_path, "rb") as f:
        model = pickle.load(f)
    print(f"Evaluating model from {model_path} on {data_path}")
    # TODO: implement evaluation


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="models/model.pkl")
    parser.add_argument("--data", default="data/test.csv")
    args = parser.parse_args()
    evaluate(args.model, args.data)
''',
    "configs/train.yaml": """# Training configuration
model:
  type: "classifier"
  n_estimators: 100
  max_depth: 10

training:
  test_size: 0.2
  random_state: 42
  cv_folds: 5
""",
    "notebooks/eda.ipynb": """{
 "cells": [],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 5
}""",
}

# DVC additions
DVC_TEMPLATE = {
    "dvc.yaml": """# DVC pipeline
stages:
  preprocess:
    cmd: python src/preprocess.py
    deps:
      - data/raw
    outs:
      - data/processed

  train:
    cmd: python src/train.py
    deps:
      - data/processed
      - src/train.py
    outs:
      - models/model.pkl
    params:
      - model
      - training
""",
    "params.yaml": """model:
  type: "classifier"
  n_estimators: 100
  max_depth: 10

training:
  test_size: 0.2
  random_state: 42
  cv_folds: 5
""",
    "src/preprocess.py": '''"""Preprocessing pipeline."""

import pandas as pd
from pathlib import Path


def preprocess(input_path: str = "data/raw/train.csv",
               output_path: str = "data/processed/train.csv"):
    """Preprocess and save data."""
    df = pd.read_csv(input_path)
    df = df.dropna()
    Path(output_path).parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(output_path, index=False)
    print(f"Saved preprocessed data to {output_path}")


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default="data/raw/train.csv")
    parser.add_argument("--output", default="data/processed/train.csv")
    args = parser.parse_args()
    preprocess(args.input, args.output)
''',
}

# MLflow additions
MLFLOW_TEMPLATE = {
    "src/train_mlflow.py": '''"""Training script with MLflow tracking."""

import mlflow
import mlflow.sklearn
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier
import pickle


def train(config: dict, experiment_name: str = "ds-init"):
    """Train with MLflow tracking."""
    mlflow.set_experiment(experiment_name)

    with mlflow.start_run():
        mlflow.log_params(config["model"])
        mlflow.log_params(config["training"])

        # TODO: load data and train
        # X_train, X_test, y_train, y_test = ...
        # model = RandomForestClassifier(**config["model"])
        # model.fit(X_train, y_train)

        mlflow.log_metric("accuracy", 0.95)  # placeholder
        mlflow.sklearn.log_model(model, "model")
        print("Logged run to MLflow")


if __name__ == "__main__":
    import yaml
    with open("params.yaml") as f:
        config = yaml.safe_load(f)
    train(config)
''',
}

# CV template additions
CV_TEMPLATE = {
    "src/model.py": '''"""Computer vision model utilities."""

from pathlib import Path


def load_image(path: str):
    """Load an image."""
    # TODO: implement with PIL or cv2
    pass


def preprocess_image(image):
    """Preprocess for CV model."""
    # TODO: resize, normalize, augment
    return image
''',
}

# NLP template additions
NLP_TEMPLATE = {
    "src/tokenizer.py": '''"""NLP tokenization utilities."""

from pathlib import Path


def load_tokenizer(name: str = "bert-base-uncased"):
    """Load a tokenizer."""
    # TODO: implement with transformers
    pass


def tokenize(texts, tokenizer):
    """Tokenize text data."""
    # TODO: implement tokenization
    pass
''',
}
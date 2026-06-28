"""Project generation logic."""

from pathlib import Path
from typing import Dict, Any
from jinja2 import Template
from ds_init.templates import (
    BASIC_TEMPLATE,
    CV_TEMPLATE,
    NLP_TEMPLATE,
    DVC_TEMPLATE,
    MLFLOW_TEMPLATE,
)
from ds_init.utils import validate_project_name, safe_mkdir


def generate_project(
    project_name: str,
    template: str = "basic",
    with_dvc: bool = False,
    with_mlflow: bool = False,
    with_uv: bool = False,
    base_path: Path = None,
) -> Path:
    """Generate a data science project."""
    project_name = validate_project_name(project_name)

    if base_path is None:
        base_path = Path.cwd()

    project_path = base_path / project_name
    if project_path.exists():
        raise FileExistsError(f"Directory already exists: {project_path}")

    # Core directories (always created)
    safe_mkdir(project_path)
    safe_mkdir(project_path / "src")
    safe_mkdir(project_path / "configs")
    safe_mkdir(project_path / "notebooks")
    safe_mkdir(project_path / "data" / "raw")
    safe_mkdir(project_path / "data" / "processed")
    safe_mkdir(project_path / "models")
    safe_mkdir(project_path / "logs")

    # Assemble template files
    files: Dict[str, str] = dict(BASIC_TEMPLATE)

    if template == "cv":
        files.update(CV_TEMPLATE)
    elif template == "nlp":
        files.update(NLP_TEMPLATE)

    if with_dvc:
        files.update(DVC_TEMPLATE)

    if with_mlflow:
        files.update(MLFLOW_TEMPLATE)
        if "requirements.txt" in files:
            files["requirements.txt"] += "\n# Experiment tracking\nmlflow>=2.0.0\n"

    if with_uv:
        files[".uvignore"] = "# Files to ignore in uv projects\n__pycache__/\n*.pyc\n"
        files["pyproject.toml"] = f"""[project]
name = "{project_name}"
version = "0.1.0"
description = "Add your description here"
requires-python = ">=3.9"
dependencies = []

[tool.uv]
dev-dependencies = []
"""

    # Render and write all files
    for rel_path, content in files.items():
        full_path = project_path / rel_path
        full_path.parent.mkdir(parents=True, exist_ok=True)
        full_path.write_text(Template(content).render(project_name=project_name))

    return project_path

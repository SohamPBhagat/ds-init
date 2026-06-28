"""Project generation logic."""

import shutil
from pathlib import Path
from typing import Dict, Any
from jinja2 import Template
from ds_init.templates import (
    BASIC_TEMPLATE,
    DVC_TEMPLATE,
    MLFLOW_TEMPLATE,
    CV_TEMPLATE,
    NLP_TEMPLATE,
)


def generate_project(
    project_name: str,
    template: str = "basic",
    with_dvc: bool = False,
    with_mlflow: bool = False,
    with_uv: bool = False,
    base_path: Path = None,
) -> Path:
    """Generate a data science project.

    Args:
        project_name: Name of the project directory.
        template: Template type ("basic", "cv", "nlp", "ts").
        with_dvc: Include DVC configuration.
        with_mlflow: Include MLflow tracking.
        with_uv: Set up uv virtual environment.
        base_path: Base directory (defaults to current directory).

    Returns:
        Path to the created project directory.
    """
    if base_path is None:
        base_path = Path.cwd()

    project_path = base_path / project_name
    if project_path.exists():
        raise FileExistsError(f"Directory already exists: {project_path}")

    project_path.mkdir(parents=True)
    (project_path / "src").mkdir(exist_ok=True)
    (project_path / "configs").mkdir(exist_ok=True)
    (project_path / "notebooks").mkdir(exist_ok=True)
    (project_path / "data").mkdir(exist_ok=True)
    (project_path / "data" / "raw").mkdir(exist_ok=True)

    # Start with basic template
    files = dict(BASIC_TEMPLATE)

    # Add template-specific files
    if template == "cv":
        files.update(CV_TEMPLATE)
    elif template == "nlp":
        files.update(NLP_TEMPLATE)

    # Add optional components
    if with_dvc:
        files.update(DVC_TEMPLATE)
        (project_path / "data" / "processed").mkdir(exist_ok=True)
        (project_path / "models").mkdir(exist_ok=True)
        (project_path / "logs").mkdir(exist_ok=True)

    if with_mlflow:
        files.update(MLFLOW_TEMPLATE)
        # Update requirements for mlflow
        if "requirements.txt" in files:
            files["requirements.txt"] += "mlflow>=2.0.0\n"

    # Render and write files
    for rel_path, content in files.items():
        full_path = project_path / rel_path
        full_path.parent.mkdir(parents=True, exist_ok=True)

        # Render Jinja2 template
        t = Template(content)
        rendered = t.render(project_name=project_name)

        full_path.write_text(rendered, encoding="utf-8")

    # uv setup
    if with_uv:
        uv_ignore = project_path / ".uvignore"
        uv_ignore.write_text("data/\nmodels/\nlogs/\n__pycache__/\n*.pyc\n", encoding="utf-8")

    return project_path
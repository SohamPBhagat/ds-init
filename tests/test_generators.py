"""Tests for project generation."""

import pytest
from pathlib import Path
import tempfile
import shutil
from ds_init.generators import generate_project


@pytest.fixture
def temp_dir():
    tmp = Path(tempfile.mkdtemp())
    yield tmp
    shutil.rmtree(tmp, ignore_errors=True)


def test_generate_basic_project(temp_dir):
    path = generate_project("my-project", base_path=temp_dir)
    assert path.exists()
    assert (path / "requirements.txt").exists()
    assert (path / "src" / "__init__.py").exists()
    assert (path / "src" / "train.py").exists()
    assert (path / ".gitignore").exists()


def test_generate_cv_template(temp_dir):
    path = generate_project("cv-project", template="cv", base_path=temp_dir)
    assert (path / "src" / "model.py").exists()


def test_generate_nlp_template(temp_dir):
    path = generate_project("nlp-project", template="nlp", base_path=temp_dir)
    assert (path / "src" / "tokenizer.py").exists()


def test_generate_with_dvc(temp_dir):
    path = generate_project("dvc-project", with_dvc=True, base_path=temp_dir)
    assert (path / "dvc.yaml").exists()
    assert (path / "src" / "preprocess.py").exists()


def test_generate_with_mlflow(temp_dir):
    path = generate_project("ml-project", with_mlflow=True, base_path=temp_dir)
    assert (path / "src" / "train_mlflow.py").exists()
    content = (path / "requirements.txt").read_text()
    assert "mlflow" in content


def test_generate_with_all_flags(temp_dir):
    path = generate_project(
        "full-project",
        template="cv",
        with_dvc=True,
        with_mlflow=True,
        with_uv=True,
        base_path=temp_dir,
    )
    assert (path / "dvc.yaml").exists()
    assert (path / "src" / "train_mlflow.py").exists()
    assert (path / ".uvignore").exists()


def test_generate_duplicate_fails(temp_dir):
    generate_project("dup-project", base_path=temp_dir)
    with pytest.raises(FileExistsError):
        generate_project("dup-project", base_path=temp_dir)

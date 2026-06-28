"""Tests for CLI argument parsing."""

from pathlib import Path

import pytest
from click.testing import CliRunner
from ds_init.cli import cli, init


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "ds-init" in result.output


def test_init_basic():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(init, ["my-project"])
        assert result.exit_code == 0
        assert "Created my-project/" in result.output
        assert (Path("my-project") / "requirements.txt").exists()


def test_init_with_flags():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(
            init, ["my-project", "--template", "cv", "--with-dvc", "--with-mlflow"]
        )
        assert result.exit_code == 0
        assert "Created my-project/" in result.output
        assert "cd my-project" in result.output
        assert (Path("my-project") / "requirements.txt").exists()
        assert (Path("my-project") / "dvc.yaml").exists()
        assert (Path("my-project") / "src" / "train.py").exists()


def test_init_creates_files():
    runner = CliRunner()
    with runner.isolated_filesystem():
        result = runner.invoke(init, ["test-project", "--with-dvc"])
        assert result.exit_code == 0
        assert "Created" in result.output
        project_path = Path("test-project")
        assert (project_path / "requirements.txt").exists()
        assert (project_path / "dvc.yaml").exists()


def test_init_file_exists_error():
    runner = CliRunner()
    with runner.isolated_filesystem():
        # Create directory first
        Path("existing-project").mkdir()
        result = runner.invoke(init, ["existing-project"])
        assert result.exit_code == 1
        assert "Error" in result.output

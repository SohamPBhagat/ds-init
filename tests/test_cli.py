"""Tests for CLI argument parsing."""

from click.testing import CliRunner
from ds_init.cli import cli, init


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(cli, ["--help"])
    assert result.exit_code == 0
    assert "ds-init" in result.output


def test_init_basic():
    runner = CliRunner()
    result = runner.invoke(init, ["my-project"])
    assert result.exit_code == 0
    assert "Initializing project: my-project" in result.output
    assert "Template: basic" in result.output


def test_init_with_flags():
    runner = CliRunner()
    result = runner.invoke(init, ["my-project", "--template", "cv", "--with-dvc", "--with-mlflow"])
    assert result.exit_code == 0
    assert "Template: cv" in result.output
    assert "dvc" in result.output
    assert "mlflow" in result.output

"""CLI entry point for ds-init."""

import click
from ds_init import __version__


@click.group()
@click.version_option(version=__version__)
def cli():
    """ds-init — scaffold a data science project in seconds."""
    pass


@cli.command()
@click.argument("project_name")
@click.option("--template", "-t", default="basic",
              type=click.Choice(["basic", "cv", "nlp", "ts"]),
              help="Project template type")
@click.option("--with-dvc", is_flag=True, help="Add DVC configuration")
@click.option("--with-mlflow", is_flag=True, help="Add MLflow experiment tracking")
@click.option("--with-uv", is_flag=True, help="Set up uv virtual environment")
def init(project_name, template, with_dvc, with_mlflow, with_uv):
    """Create a new data science project.

    PROJECT_NAME is the name of the directory to create.
    """
    click.echo(f"Initializing project: {project_name}")
    click.echo(f"Template: {template}")
    flags = []
    if with_dvc:
        flags.append("dvc")
    if with_mlflow:
        flags.append("mlflow")
    if with_uv:
        flags.append("uv")
    if flags:
        click.echo(f"With: {', '.join(flags)}")


if __name__ == "__main__":
    cli()

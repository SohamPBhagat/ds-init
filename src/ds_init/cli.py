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
@click.option(
    "--template",
    "-t",
    default="basic",
    type=click.Choice(["basic", "cv", "nlp", "ts"]),
    help="Project template type",
)
@click.option("--with-dvc", is_flag=True, help="Add DVC configuration")
@click.option("--with-mlflow", is_flag=True, help="Add MLflow experiment tracking")
@click.option("--with-uv", is_flag=True, help="Set up uv virtual environment")
@click.option("--interactive", "-i", is_flag=True, help="Interactive mode")
def init(project_name, template, with_dvc, with_mlflow, with_uv, interactive):
    """Create a new data science project.

    PROJECT_NAME is the name of the directory to create.
    """
    if interactive:
        import sys

        if not sys.stdin.isatty():
            click.echo(
                "Interactive mode requires a TTY — skip with project-name or flags."
            )
        # Continue with non-interactive defaults

    from ds_init.generators import generate_project

    try:
        path = generate_project(
            project_name=project_name,
            template=template,
            with_dvc=with_dvc,
            with_mlflow=with_mlflow,
            with_uv=with_uv,
        )
        click.echo(f"✓ Created {project_name}/")
        click.echo(f"  cd {project_name}")
        click.echo(f"  pip install -r requirements.txt")
        if with_uv:
            click.echo(f"  uv sync")
        if with_dvc:
            click.echo(f"  dvc init")
        if with_mlflow:
            click.echo(f"  mlflow ui")
    except FileExistsError as e:
        click.echo(f"Error: {e}", err=True)
        raise SystemExit(1)


if __name__ == "__main__":
    cli()

# Contributing to ds-init

Thanks for wanting to contribute. Here's everything you need to know.

## Getting started

```bash
# Clone the repo
git clone https://github.com/SohamPBhagat/ds-init
cd ds-init

# Set up a virtual environment
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate

# Install in editable mode with dev dependencies
pip install -e ".[dev]"

# Install pre-commit hooks
pre-commit install
```

## Running tests

```bash
pytest tests/ -v
```

## Code style

We use black, isort, and ruff. The pre-commit hooks enforce them automatically, but you can also run manually:

```bash
black src/ tests/
isort src/ tests/
ruff check src/ tests/ --fix
```

## Commit messages

We follow [Conventional Commits](https://www.conventionalcommits.org/):

- `feat:` new feature
- `fix:` bug fix
- `docs:` documentation only
- `refactor:` code change that neither fixes a bug nor adds a feature
- `test:` adding or correcting tests
- `chore:` maintenance tasks (CI, dependencies, tooling)

## Pull requests

1. Fork the repo and create a branch from `main`
2. Make your change and add tests
3. Ensure all tests pass and linting is clean
4. Open a PR with a clear description

## Project structure

```
src/ds_init/
  __init__.py      # Version and package exports
  cli.py           # Click CLI entry point
  generators.py    # Project generation logic
  templates.py     # Embedded Jinja2 template strings
  utils.py         # Validation and filesystem helpers

tests/
  test_cli.py      # CLI argument parsing and integration
  test_generators.py  # Project generation outputs
  test_utils.py    # Validation and utility functions
```

## Adding a new template

Templates are defined in `src/ds_init/templates.py` as dictionaries mapping
relative file paths to their content. Each template dict is merged with
`BASIC_TEMPLATE` by `generators.py` when the corresponding flag is passed.

To add a new template (e.g., `ts` for time-series):

1. Add the template dict to `templates.py`
2. Add the `ts` choice to the `--template` click option in `cli.py`
3. Add the merge logic in `generators.py`
4. Add tests in `tests/test_generators.py`
5. Update README.md template docs
6. Bump the minor version and add a CHANGELOG entry
# Changelog

All notable changes to ds-init are documented here.

## [0.3.0] - 2026-06-28

### Added
- Pre-commit hooks configuration (`.pre-commit-config.yaml`) with black, isort, ruff, and standard sanity checks
- CI pre-commit verification step in `.github/workflows/tests.yml`
- `.readthedocs.yml` for documentation build configuration
- `ROADMAP.md` documenting project goals through 1.0.0

### Changed
- Bumped version from 0.2.0 to 0.3.0 across `pyproject.toml` and `__init__.py`

### Fixed
- Documented all dependency pinning and tooling choices in docs/decisions/
- Clarified `ds-init` CLI entry-point packaging so future version bumps follow the same pattern

## [0.2.0] - 2026-06-28

### Added
- Interactive mode: detects non-TTY and falls back to defaults gracefully
- MLflow template with experiment tracking boilerplate
- CV template with image loading utilities
- NLP template with tokenizer helpers

### Changed
- Version bumped from 0.1.0 to 0.2.0
- Improved README with badges, structure docs, and contribution guide

## [0.1.0] - 2026-06-28

### Added
- Initial CLI with `ds-init init PROJECT_NAME` command
- Template flags: `--template`, `--with-dvc`, `--with-mlflow`, `--with-uv`
- Basic, CV, and NLP project templates
- requirements.txt, .gitignore, train/evaluate scripts
- pytest test suite (11 tests)
- GitHub Actions CI for Python 3.9–3.12 with lint checks
- MIT License

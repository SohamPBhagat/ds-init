# Changelog

All notable changes to ds-init are documented here.

## [0.3.0] - 2026-06-28

### Added
- `utils.py` with `validate_project_name()` — rejects invalid characters, spaces, empty names
- `safe_mkdir()` — wrapped directory creation with clear error messages
- 10 unit tests for project name validation

### Changed
- `generators.py` now validates project name before filesystem operations
- All directory creation uses `safe_mkdir()` for consistent error handling
- `with_dvc` now also enables DVC-specific directories (processed, models, logs)

### Fixed
- MLflow template comments out undefined `log_model` call until model is defined
- Removed unused imports across all source files

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

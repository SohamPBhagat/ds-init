# ADR-001: Tooling Choices

## Status
Accepted — 2026-06-28

## Context
We need a reproducible development environment with consistent formatting,
clear linting rules, and fast feedback in CI. Several tools overlap in purpose
(black vs. ruff-format, isort vs. ruff's import sorting). We chose the most
widely-adopted tool per job.

## Decisions

| Tool | Purpose | Why |
|------|---------|-----|
| **black** | Code formatting | Defacto standard; widely understood |
| **isort** | Import sorting | Compatible with black profile; clear diffs |
| **ruff** | Linting + import sorting | 10–100× faster than flake8/pylint; single binary |
| **ruff-format** | Format backup | Drop-in for black if we ever consolidate |
| **pre-commit** | Hook management | Enforces checks before commit, not just in CI |

## Consequences
- Developers must run `pre-commit install` once after cloning
- CI runs the same hooks so pre-commit failures = CI failures
- No `--target-version` flags in pre-commit; runner uses pinned Python 3.12
  matching the `--target-version py312` black call in GitHub Actions
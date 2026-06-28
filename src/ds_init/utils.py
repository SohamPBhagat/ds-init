"""Utility functions for ds-init."""

import re
from pathlib import Path

# Allowed characters in project names: letters, numbers, hyphens, underscores
VALID_NAME_PATTERN = re.compile(r"^[a-zA-Z0-9_-]+$")

# Characters that are dangerous in file paths
FORBIDDEN_CHARS = r'<>:"/\\|?*'


def validate_project_name(name: str) -> str:
    """Validate and sanitize a project name.

    Returns the sanitized name if valid.
    Raises ValueError with a clear message if invalid.
    """
    if not name or not name.strip():
        raise ValueError("Project name cannot be empty.")

    # Check for forbidden filesystem characters
    found = [c for c in name if c in FORBIDDEN_CHARS]
    if found:
        raise ValueError(
            f"Project name contains invalid characters: {found!r}. "
            f"Use only letters, numbers, hyphens, and underscores."
        )

    # Strip leading/trailing dots and spaces
    name = name.strip(".")

    if not VALID_NAME_PATTERN.match(name):
        raise ValueError(
            f"Project name '{name}' contains invalid characters. "
            f"Use only letters, numbers, hyphens, and underscores."
        )

    return name


def safe_mkdir(path: Path, exist_ok: bool = False) -> None:
    """Create a directory safely, raising a clear error on failure."""
    try:
        path.mkdir(parents=True, exist_ok=exist_ok)
    except PermissionError:
        raise PermissionError(f"Cannot create directory: {path}") from None
    except OSError as exc:
        raise OSError(f"Failed to create directory {path}: {exc}") from exc

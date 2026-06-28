"""Tests for utility functions."""

import pytest
from ds_init.utils import validate_project_name, VALID_NAME_PATTERN, FORBIDDEN_CHARS


class TestValidateProjectName:
    """Tests for project name validation."""

    def test_valid_simple_name(self):
        assert validate_project_name("my-project") == "my-project"

    def test_valid_with_numbers(self):
        assert validate_project_name("project123") == "project123"

    def test_valid_with_underscores(self):
        assert validate_project_name("my_project") == "my_project"

    def test_valid_mixed(self):
        assert validate_project_name("my-project_2") == "my-project_2"

    def test_empty_string_raises(self):
        with pytest.raises(ValueError, match="cannot be empty"):
            validate_project_name("")

    def test_whitespace_only_raises(self):
        with pytest.raises(ValueError, match="cannot be empty"):
            validate_project_name("   ")

    def test_spaces_raises(self):
        with pytest.raises(ValueError, match="invalid characters"):
            validate_project_name("my project")

    def test_special_chars_raise(self):
        for char in list(FORBIDDEN_CHARS):
            with pytest.raises(ValueError, match="invalid characters"):
                validate_project_name(f"project{char}name")

    def test_leading_dot_stripped(self):
        result = validate_project_name(".my-project")
        assert result == "my-project"

    def test_trailing_dot_stripped(self):
        result = validate_project_name("my-project.")
        assert result == "my-project"

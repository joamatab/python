"""This module is called before the project is created."""

import re
import sys

PROJECT_NAME = "{{ cookiecutter.package_name }}"
PROJECT_VERSION = "{{ cookiecutter.package_version }}"


# Updated regex to allow uppercase letters as well
MODULE_REGEX = re.compile(r"^[a-zA-Z][a-zA-Z0-9\-\_]+[a-zA-Z0-9]$")
SEMVER_REGEX = re.compile(
    r"""
        ^
        (?P<major>0|[1-9]\d*)
        \.
        (?P<minor>0|[1-9]\d*)
        \.
        (?P<patch>0|[1-9]\d*)
        (?:-(?P<prerelease>
            (?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)
            (?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*
        ))?
        (?:\+(?P<build>
            [0-9a-zA-Z-]+
            (?:\.[0-9a-zA-Z-]+)*
        ))?
        $
    """,
    re.VERBOSE,
)


def validate_package_name(package_name: str) -> None:
    """Ensure that `package_name` parameter is valid.

    Valid inputs start with a letter (either uppercase or lowercase).
    Followed by any letters, numbers, hyphens, or underscores.

    Args:
        package_name: current project name

    Raises:
        ValueError: If package_name is not a valid Python module name
    """
    if MODULE_REGEX.fullmatch(package_name) is None:
        message = f"ERROR: The project name `{package_name}` is not a valid Python module name."
        raise ValueError(message)


def validate_semver(version: str) -> None:
    """Ensure version in semver notation.

    Args:
        version: string version. For example 0.1.2 or 1.2.4

    Raises:
        ValueError: If version is not in semver notation
    """
    if SEMVER_REGEX.fullmatch(version) is None:
        message = f"ERROR: The `{version}` is not in semver notation (https://semver.org/)"
        raise ValueError(message)


def validate_line_length(line_length: int) -> None:
    """Validate line_length parameter. Length should be between 50 and 300.

    Args:
        line_length: integer parameter for isort and black formatters

    Raises:
        ValueError: If line_length isn't between 50 and 300
    """
    if not (50 <= line_length <= 300):
        message = f"ERROR: line_length must be between 50 and 300. Got `{line_length}`."
        raise ValueError(message)


def main() -> None:
    try:
        validate_package_name(package_name=PROJECT_NAME)
        validate_semver(version=PROJECT_VERSION)
    except ValueError as ex:
        print(ex)
        sys.exit(1)


if __name__ == "__main__":
    main()


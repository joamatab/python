"""This module is called after project is created."""
from typing import List

import textwrap
from pathlib import Path
from shutil import move, rmtree

# Project root directory
PROJECT_DIRECTORY = Path.cwd().absolute()
PROJECT_NAME = "{{ cookiecutter.package_name }}"
PROJECT_MODULE = (
    "{{ cookiecutter.package_name.lower().replace(' ', '_').replace('-', '_') }}"
)
CICD = "{{ cookiecutter.cicd }}"

# Values to generate github repository
GITHUB_USER = "{{ cookiecutter.author_name }}"


def remove_unused_files(
    directory: Path, module_name: str, cicd: str = "github"
) -> None:
    """Remove unused files.

    Args:
        directory: path to the project directory
        module_name: project module name
    """
    if cicd == "github":
        files_to_delete = [directory / ".gitlab-ci.yml"]

        for path in files_to_delete:
            path.unlink()
    else:
        dirpath = directory / ".github"
        rmtree(dirpath)


def print_futher_instuctions(package_name: str, github: str) -> None:
    """Show user what to do next after project creation.

    Args:
        package_name: current project name
        github: GitHub username
    """
    message = f"""
    Your project {package_name} is created.

    1) Now you can start working on it:

        $ cd {package_name} && git init

    2) install package in developer mode

        $ pip install -e .[dev]

    3) Upload initial code to GitHub:

        $ git add .
        $ git commit -m ":tada: Initial commit"
        $ git branch -M main
        $ git remote add origin https://github.com/{github}/{package_name}.git
        $ git push -u origin main
    """
    print(textwrap.dedent(message))


def main() -> None:
    remove_unused_files(
        directory=PROJECT_DIRECTORY,
        module_name=PROJECT_MODULE,
        cicd=CICD,
    )
    print_futher_instuctions(package_name=PROJECT_NAME, github=GITHUB_USER)


if __name__ == "__main__":
    main()

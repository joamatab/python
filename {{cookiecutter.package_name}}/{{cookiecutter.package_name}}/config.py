"""
loads a configuration from 3 files, high priority overwrites low priority:

1. A config.yml found in the current working directory (high priority)
2. ~/.{{ cookiecutter.package_name }}.yml specific for the machine
3. the default config is in this file

"""

__all__ = ["CONFIG"]

import pathlib
import logging
import hiyapyco


default_config = """
keySample: valueSample
"""

home = pathlib.Path.home()
cwd = pathlib.Path.cwd()
cwd_config = cwd / "config.yml"
home_config = home / ".{{ cookiecutter.package_name }}.yml"

CONFIG = hiyapyco.load(
    str(default_config),
    str(cwd_config),
    str(home_config),
    failonmissingfiles=False,
    loglevelmissingfiles=logging.DEBUG,
)
CONFIG["root"] = cwd
CONFIG["repo"] = cwd.parent


if __name__ == "__main__":
    print(CONFIG["repo"])

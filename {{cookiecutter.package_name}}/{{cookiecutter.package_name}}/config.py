"""
loads a configuration from 3 files, high priority overwrites low priority:

1. A config.yml found in the current working directory (high priority)
2. ~/.{{ cookiecutter.package_name }}.yml specific for the machine
3. the default config is in this file

"""

__all__ = ["CONFIG"]

import os
import logging
import hiyapyco


default_config = """
keySample: valueSample
"""


home = os.path.expanduser("~")
cwd_config = os.path.join(os.getcwd(), "config.yml")
home_config = os.path.join(home, ".{{ cookiecutter.package_name }}.yml")

CONFIG = hiyapyco.load(
    default_config,
    cwd_config,
    home_config,
    failonmissingfiles=False,
    loglevelmissingfiles=logging.DEBUG,
)

root = os.path.dirname(os.path.abspath(__file__))
repo = os.path.split(root)[0]
CONFIG["root"] = root
CONFIG["repo"] = repo


if __name__ == "__main__":
    print(CONFIG["repo"])

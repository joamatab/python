""" store configuration
"""

__all__ = ["CONFIG"]

import pathlib

home = pathlib.Path.home()
cwd = pathlib.Path.cwd()
cwd_config = cwd / "config.yml"

home_config = home / ".config" / "{{ cookiecutter.package_name }}.yml"
config_dir = home / ".config"
config_dir.mkdir(exist_ok=True)
module_path = pathlib.Path(__file__).parent.absolute()
repo_path = module_path.parent


class Config:
    module = module_path
    repo = repo_path


CONFIG = Config()

if __name__ == "__main__":
    print(CONFIG)


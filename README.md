# Python package template

# Usage

Start a new python project running

```
pip install cookiecutter
cookiecutter https://github.com/joamatab/cookiecutter-pypackage-minimal
```

It will ask you some questions to fill the template


# Explanation

The decisions `cookiecutter-pypackage-minimal` makes should all be explained here.


### Makefile

The Makefile provides you with

### Precommit hooks

Ensures that the code that you commit follows some standards:

You can comment them in `.pre-commit-config.yaml`

- Standard
    - check-yaml
    - end-of-file-fixer
    - trailing-whitespace
- Black: format your code
- flake8: check syntax
- nbstripout: strips jupyter notebooks output, so they can be version controlled
- reorder-python-imports: sorts imports


### CI/CD

See `.github/workflows`

- pythonapp.yml: runs on every push and every night
    - flake8 linter checks syntax 
    - pytest runs tests
- pythonpublish.yml
    - publishes to PyPI any new releases, need to add Pypi token

### README

- **README uses markdown format**

### LICENSE

- **MIT license by default**
  This template provides you the classic [MIT](https://choosealicense.com/licenses/mit/) licence: it lets people do almost anything they want with your project, including to make and distribute closed source versions.
  If you [choose another license](https://choosealicense.com/), you also need to update the `{{ package_name }}/setup.py` file:
  adjust the `classifiers` and `license` fields accordingly.

### `setup.py`

- **Use setuptools**
  It's the standard packaging library for Python. `distribute` has merged back into `setuptools`, and `distutils` is less capable.
- **setup.py should not import anything from the package**
  When installing from source, the user may not have the packages dependencies installed, and importing the package is likely to raise an `ImportError`.
- **setup.py should be the canonical source of package dependencies**
  There is no reason to duplicate dependency specifiers (i.e. also using a `requirements.txt` file). See the testing section below for testing dependencies.

You should then change the classifiers in `{{ package_name }}/setup.py` - it assumes that the project will run on Python 3, so you should remove any classifiers that do not apply. The full list of PyPI classifiers can be found [here](https://pypi.org/classifiers/).


### Testing

- **Use [Tox](https://tox.readthedocs.io) to manage test environments**
  Tox provides isolation, runs tests across multiple Python versions, and ensures the package can be installed.
- **Uses [pytest](https://docs.pytest.org) as the default test runner**
  This can be changed easily, though pytest is a easier, more powerful test library and runner than the standard library's unittest.
- **Define testing dependencies in `tox.ini`**
  Avoid duplicating dependency definitions, and use `tox.ini` as the canonical description of how the unittests should be run.
- **`tests` directory should not be a package**
  The `tests` directory should not be a Python package unless you want to define some fixtures.
  But the best practices are to use [PyTest fixtures](https://docs.pytest.org/en/latest/fixture.html) which provides a better solution.
  Therefore, the `tests` directory has no `__init__.py` file.


# References

- [cookiecutter](https://github.com/audreyr/cookiecutter) 

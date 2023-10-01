# Python package template 0.0.5
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

# Usage

Start a new python project running

```
pip install cookiecutter
cookiecutter gh:joamatab/python
```

It will ask you some questions to fill the template

If you want to run a branch or a different version

```
cookiecutter gh:joamatab/python --checkout branch_name
```


## 🚀 Features

In this [cookiecutter 🍪](https://github.com/cookiecutter/cookiecutter) template we combine state-of-the-art libraries and best development practices for Python.


### Makefile

The Makefile provides you with an easy way to:

- install: the package
- test: run tests
- cov: get test coverage
- mypy: check types
- ruff: fixer


### Precommit hooks

[Precommit hooks](https://pre-commit.com/) enforces that the code that you commit follows some standards:

You can comment them in `.pre-commit-config.yaml`

- Standard
    - check-yaml
    - end-of-file-fixer
    - trailing-whitespace
- Black: format your code
- nbstripout: strips jupyter notebooks output, so they can be version controlled
- reorder-python-imports: sorts imports
- ruff


### CI/CD

See `.github/workflows`

- `test_code.yml`: runs tests for code and docs. Uses `pip install`
- `test_code_conda.yml`: runs tests. Uses `conda`. Choose this one if some dependencies are only on conda. Otherwise delete this one.
- release.yml: publishes to PyPI any new releases, need to add Pypi token to your Github account
- pages.yml: builds docs.

### README

- **README uses markdown format**

### LICENSE

- **MIT license by default**
  This template provides you the classic [MIT](https://choosealicense.com/licenses/mit/) licence: it lets people do almost anything they want with your project, including to make and distribute closed source versions.
  If you [choose another license](https://choosealicense.com/), you also need to update the `{{ package_name }}/setup.py` file:
  adjust the `classifiers` and `license` fields accordingly.


### Testing

- **Uses [pytest](https://docs.pytest.org) as the default test runner**
  This can be changed easily, though pytest is a easier, more powerful test library and runner than the standard library's unittest.
  The `tests` directory should not be a Python package unless you want to define some fixtures.
  But the best practices are to use [PyTest fixtures](https://docs.pytest.org/en/latest/fixture.html) which provides a better solution.
  Therefore, the `tests` directory has no `__init__.py` file.

### Docs

you can mix and match markdown and RST syntax in the index for your docs.

I prefer markdown but I also embed RST commands as

```eval_rst

.. autofunction:: module.function_name
```

To build the docs you need to have the package itself installed, you can do this by:
```bash
cd path_to_your_repo
make install
cd docs
```

Alternatively, you can install the dependencies of the package as:
```bash
cd path_to_your_repo
make python-deps
cd docs
make html
```

# References

- [cookiecutter](https://github.com/audreyr/cookiecutter) 

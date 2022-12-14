
install: 
	pip install -e .[dev]
	pre-commit install

test:
	pytest -s

cov:
	pytest --cov={{ cookiecutter.package_name }}

mypy:
	mypy . --ignore-missing-imports

flake8:
	flake8 --select RST

pylint:
	pylint {{ cookiecutter.package_name }}

pydocstyle:
	pydocstyle {{ cookiecutter.package_name }}

doc8:
	doc8 docs/

update:
	pur

update-pre:
	pre-commit autoupdate --bleeding-edge

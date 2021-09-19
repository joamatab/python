
install: 
	pip install -r requirements.txt --upgrade
	pip install -r requirements_dev.txt --upgrade
	pip install -e .
	pre-commit install

test:
	pytest

cov:
	pytest --cov= {{ cookiecutter.package_name }}

mypy:
	mypy . --ignore-missing-imports

lint:
	flake8 

pylint:
	pylint {{ cookiecutter.package_name }}

lintd2:
	flake8 --select RST

lintd:
	pydocstyle {{ cookiecutter.package_name }}

doc8:
	doc8 docs/

update:
	pur

update2:
	pre-commit autoupdate --bleeding-edge

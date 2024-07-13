VIRTUALENV:=$(shell basename $$PWD)
.PHONY: clean clean-test clean-pyc clean-build docs help
.DEFAULT_GOAL := help

define BROWSER_PYSCRIPT
import os, webbrowser, sys

from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test and coverage artifacts
	rm -fr .tox/
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache

lint: ## check style with flake8
	flake8 src/kubernetes tests

test: ## run tests quickly with the default Python
	pytest -v

coverage:
	pytest -v --cov

release: dist ## package and upload a release
	twine upload dist/*

dist: clean ## builds source and wheel package
	python -m build

install: clean ## install the package to the active Python's site-packages
	python setup.py install

init:
	pip install --upgrade pip
	pip install --upgrade -r requirements-dev.txt
bump:
	bump2version --tag patch

docs: ## generate Sphinx HTML documentation, including API docs
	rm -f docs/source/modules.rst
	sphinx-apidoc --ext-autodoc -o docs/source src/kubernetes
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/build/html/index.html

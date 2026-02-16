.PHONY: clean-pyc clean-build docs clean help pr

define BROWSER_PYSCRIPT
import os, webbrowser, sys
try:
	from urllib import pathname2url
except:
	from urllib.request import pathname2url

webbrowser.open("file://" + pathname2url(os.path.abspath(sys.argv[1])))
endef
export BROWSER_PYSCRIPT

BROWSER := python -c "$$BROWSER_PYSCRIPT"

help:
	@echo "Available commands:"
	@echo "clean-build - remove build artifacts"
	@echo "clean-pyc - remove Python file artifacts"
	@echo "clean-test - remove test artifacts"
	@echo "clean - run clean-build, clean-pyc, and clean-test"
	@echo "install-dev - install development requirements"
	@echo "fix - fix formatting & linting issues with ruff"
	@echo "lint - run pre-commit hooks on all files"
	@echo "typecheck - run mypy type checking"
	@echo "test - run tests quickly with the default Python"
	@echo "coverage - run tests with coverage report"
	@echo "docs-ci - generate docs for CI"
	@echo "docs - generate docs and open in browser"
	@echo "servedocs - serve docs with live reload"
	@echo "dist - build package and show contents"
	@echo "pr - run clean, lint, and test (everything needed before creating a PR)"


clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts


clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -fr {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -fr {} +
	find . -name '*.pyo' -exec rm -fr {} +
	find . -name '*~' -exec rm -fr {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove Tests artifacts
	rm -fr .tox/
	rm -fr .mypy_cache
	rm -fr .ruff_cache
	rm -f .coverage
	rm -fr htmlcov/
	rm -fr .pytest_cache/

lint: ## check style with flake8
	pre-commit run --all-files --show-diff-on-failure

fix:
	python -m ruff check --fix

typecheck:
	pre-commit run mypy-local --all-files

test: ## run tests quickly with the default Python
	@if command -v uv >/dev/null 2>&1; then \
		uv run python -m pytest tests; \
	else \
		python -m pytest tests; \
	fi

coverage: ## check code coverage quickly with the default Python
	coverage run --source dag -m pytest tests
	coverage report -m
	coverage html
	$(BROWSER) htmlcov/index.html

linux-docs: ## generate Sphinx HTML documentation, including API docs
	rm -fr docs/dag.rst
	rm -fr docs/modules.rst
	$(MAKE) -C docs clean
	$(MAKE) -C docs html
	$(BROWSER) docs/_build/html/index.html

docs:
	rm -f docs/dag.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ dag
	$(MAKE) -C docs clean
	$(MAKE) -C docs html SPHINXOPTS="-W"

docs-ci: ## generate docs for CI
	python newsfragments/validate_files.py
	rm -f docs/dag.rst
	rm -f docs/modules.rst
	sphinx-apidoc -o docs/ dag
	$(MAKE) -C docs clean
	$(MAKE) -C docs html SPHINXOPTS="-W"

servedocs: docs
	watchmedo shell-command -p '*.rst' -c '$(MAKE) -C docs html' -R -D .

dist: clean
	python -m build
	ls -l dist

pr: clean fix lint typecheck test
	@echo "PR preparation complete! All checks passed."

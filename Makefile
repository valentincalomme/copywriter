SRC_DIR = src/
TESTS_DIR = tests/

modules = ${SRC_DIR} ${TESTS_DIR}

# Run this command to setup the project
init:
	make install
	make setup-pre-commit
	make check-configs

install:
# Installs all dependencies and synchronize the environment
# with the locked packages and the specified groups
	poetry install --sync --all-extras

check-configs:
# Validates poetry's config files
	poetry check
# Validates the pre-commit config file.
	pre-commit validate-config .pre-commit-config.yaml

setup-pre-commit:
# Install all pre-commit hooks
	pre-commit install --install-hooks

pre-commit:
# Run all pre-commit hooks
	pre-commit run --all-files

format:
	ruff format ${modules}

ruff:
# Run ruff on all modules
	ruff check ${modules} --no-fix

mypy:
# Run mypy on everything
	mypy .

.PHONY: lint-imports
lint-imports:
	lint-imports

lint: lint-imports ruff mypy

qa: format lint

.PHONY: tests
tests:
# Run tests (including doctests) and compute coverage
	pytest --cov=${SRC_DIR} --doctest-modules

.PHONY: docs
docs:
# Build the documentation and break on any warnings/errors
	mkdocs build --strict

docs-serve:
	mkdocs serve

build:
	poetry build

ci: check-configs qa docs tests

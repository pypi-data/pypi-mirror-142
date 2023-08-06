PROJECT = easy_infra
PYTHON = $(shell which python)
PYTHON_FILES = setup.py $(shell find $(PROJECT) -type f -name "*.py")

build:
	python setup.py build

clean:
	git clean -fdx

dist: install
	python setup.py sdist bdist_wheel

dev:
	pip install -e ".[dev]"

install:
	pip install .

twine-check: clean dist
	twine check dist/*

twine-upload: twine-check
	twine upload dist/*

black:
	black $(PYTHON_FILES)

pylint:
	pylint $(PYTHON_FILES)

flake8:
	flake8 $(PYTHON_FILES)

pyright:
	pyright $(PYTHON_FILES)

lint: black flake8 pylint pyright

.vscode/settings.json:
	@mkdir -p .vscode
	@echo "{\"python.pythonPath\": \"$(PYTHON)\", \"python.terminal.activateEnvInCurrentTerminal\": true}" > .vscode/settings.json

vscode: .vscode/settings.json

.PHONY: build dist

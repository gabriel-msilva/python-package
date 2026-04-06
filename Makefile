.PHONY: setup
setup:
	uv sync --frozen
	uv run pre-commit install

.PHONY: tests
tests:
	uv run pytest tests -v

.PHONY: pre-commit
pre-commit:
	uv run pre-commit run --all-files

.PHONY: cookiecutter
cookiecutter:
	uv run cookiecutter .

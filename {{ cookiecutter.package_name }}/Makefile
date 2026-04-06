.PHONY: setup
setup:
	uv sync --frozen
	uv run pre-commit install

.PHONY: tests
tests:
	uv run pytest

.PHONY: pre-commit
pre-commit:
	uv run pre-commit run --all-files

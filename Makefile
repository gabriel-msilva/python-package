.PHONY: setup
setup:
	uv sync --frozen

.PHONY: tests
tests:
	uv run pytest tests -v

.PHONY: cookiecutter
cookiecutter:
	uv run cookiecutter .

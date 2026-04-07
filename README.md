# python-package

A [cookiecutter](https://www.cookiecutter.io/) template for Python packages.

## Features

- Minimal [src layout](https://packaging.python.org/en/latest/discussions/src-layout-vs-flat-layout/)
- [uv](https://docs.astral.sh/uv/) for package management
- [pre-commit](https://pre-commit.com/) hooks, including [ruff](https://docs.astral.sh/ruff/) for linting and formatting
- [pytest](https://docs.pytest.org/) for testing

## Usage

```sh
cookiecutter gh:gabriel-msilva/python-package
```

You will be prompted for the following values:

| Variable         | Description                                |
| ---------------- | ------------------------------------------ |
| `package_name`   | Name of the package (PEP 423 validated)    |
| `description`    | Short description of the package           |
| `author_name`    | Author's full name                         |
| `author_email`   | Author's email address                     |
| `python_version` | Minimum Python version (default: `3.11`)   |

## Development

Set up the development environment:

```sh
make setup
```

Run the tests:

```sh
make tests
```

Generate a new project from the template:

```sh
make cookiecutter
```

See all available commands with `make help`.

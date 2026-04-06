import re
import sys

MAX_NAMESPACE_LEVELS = 3


def validate_package_name(package_name: str) -> None:
    if not package_name:
        print("ERROR: Package name must not be empty.")
        sys.exit(1)

    errors = []
    segments = package_name.split(".")

    if len(segments) > MAX_NAMESPACE_LEVELS:
        errors.append(
            f"Must not exceed {MAX_NAMESPACE_LEVELS} namespace levels (PEP 423)."
        )

    for segment in segments:
        if not re.match(r"^[a-z]([a-z0-9]|[-_](?=[a-z0-9]))*$", segment):
            errors.append(
                f"Invalid segment '{segment}'."
                " Each segment must start with a lowercase letter and contain only"
                " lowercase letters, digits, hyphens, and underscores (PEP 8)."
            )

    if errors:
        print(f"ERROR: Invalid package name '{package_name}':")
        for error in errors:
            print(f"  - {error}")

        sys.exit(1)


def validate_email(email: str) -> None:
    if not re.match(r"^[^@]+@[^@.]+(\.[^@.]+)+$", email):
        print(f"ERROR: Invalid email address '{email}'.")
        sys.exit(1)


if __name__ == "__main__":
    validate_package_name("{{ cookiecutter.package_name }}")
    validate_email("{{ cookiecutter.author_email }}")

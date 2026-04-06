import pytest

from hooks.pre_gen_project import validate_package_name, validate_email


@pytest.mark.parametrize(
    "name",
    [
        "mypackage",
        "my-package",
        "my_package",
        "pkg123",
        "ns.pkg",
        "org.sub.pkg",
        "my-pkg.sub",
    ],
)
def test_valid_names_pass(name):
    validate_package_name(name)


def test_empty_string_exits():
    with pytest.raises(SystemExit):
        validate_package_name("")


@pytest.mark.parametrize("name", ["MyPackage", "PACKAGE", "myPackage"])
def test_uppercase_exits(name):
    with pytest.raises(SystemExit):
        validate_package_name(name)


@pytest.mark.parametrize("name", ["a.b.c.d"])
def test_four_or_more_levels_exits(name):
    with pytest.raises(SystemExit):
        validate_package_name(name)


@pytest.mark.parametrize(
    "name",
    [
        "1package",
        "_private",
        "-start",
        "pkg-",
        "pkg_",
        "pkg--name",
        "pkg__name",
        "pkg-_name",
        "has space",
        "special!char",
        "UPPER.lower",
        ".leading",
        "trailing.",
        "double..dot",
    ],
)
def test_invalid_segment_exits(name):
    with pytest.raises(SystemExit):
        validate_package_name(name)


@pytest.mark.parametrize(
    "email",
    [
        "username@example.com",
        "user.name+tag+sorting@example.com",
        "user_name@example.com.br",
    ],
)
def test_valid_email_pass(email):
    validate_email(email)


@pytest.mark.parametrize(
    "email",
    [
        "",
        "plainaddress",
        "@missingusername.com",
        "username@.com",
        "username@com",
        "username@domain..com",
    ],
)
def test_invalid_email_exits(email):
    with pytest.raises(SystemExit):
        validate_email(email)

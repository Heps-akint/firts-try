from greeter import greet


def test_greet_heps() -> None:
    assert greet("Heps") == "Hello, Heps!"


def test_greet_blank_or_whitespace() -> None:
    assert greet("") == "Hello, world!"
    assert greet("   ") == "Hello, world!"

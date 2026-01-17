"""Simple greeting helper."""


def greet(name: str) -> str:
    stripped = name.strip()
    if not stripped:
        return "Hello, world!"
    return f"Hello, {stripped}!"

"""Simple module that prints a greeting."""


def greet(name: str = "World") -> str:
    """Return a greeting for the provided name."""
    return f"Hello, {name}!"


def farewell(name: str = "World") -> str:
    """Return a farewell for the provided name."""
    return f"Goodbye, {name}!"


if __name__ == "__main__":
    print(greet())

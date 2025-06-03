"""Simple module that prints a greeting."""


def greet(name: str = "World") -> str:
    """Return a greeting for the provided name."""
    return f"Hello, {name}!"


if __name__ == "__main__":
    print(greet())

from hello import farewell, greet


def test_greet_default():
    assert greet() == "Hello, World!"


def test_greet_custom():
    assert greet("Alice") == "Hello, Alice!"


def test_farewell_default():
    assert farewell() == "Goodbye, World!"


def test_farewell_custom():
    assert farewell("Alice") == "Goodbye, Alice!"

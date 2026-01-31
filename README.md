# Ai

This repository contains a minimal example Python module.

## Usage

Run the `hello.py` script to see a greeting:

```bash
python hello.py
```

You can also import the module to use `greet` or `farewell`:

```python
from hello import greet, farewell

print(greet("Codex"))
print(farewell("Codex"))
```

## Running Tests

Tests use `pytest`. Install it and run:

```bash
pip install pytest
pytest
```

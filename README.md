# fileparser

A minimal example project that demonstrates how to structure, build, and install a Python package using the modern **src layout**, **uv** for builds, and **Pydantic** for data validation.

---

## ✨ Features

- Simple function to analyze a file (name, suffix, type)
- CLI interface via `fileparser` or `python -m fileparser`
- Validated output using [Pydantic](https://docs.pydantic.dev)
- Organized **src/** layout with clean test separation
- Ready for direct installation from GitHub

---

## 📦 Installation

### Using pip (from GitHub)

```bash
pip install git+https://github.com/realcaptainsolaris/fileparser.git@v0.1.0
````

### Using uv (recommended)

```bash
uv pip install git+https://github.com/realcaptainsolaris/fileparser.git@v0.1.0
```

Or, for local development:

```bash
uv venv
uv pip install -e .[dev]
```

---

## 🚀 Usage

### CLI

After installation, you can use the command line tool directly:

```bash
fileparser example.txt
```

or equivalently:

```bash
uv run fileparser example.txt
```

### As a Python module

```bash
python -m fileparser example.txt
```

### As an import in your own code

```python
from fileparser.parser import parse

info = parse("example.txt")
print(info)
```

Output:

```
FileInfo(name='example', suffix='.txt', type='txt')
```

---

## 🧪 Running Tests

Install the development dependencies and run the test suite:

```bash
uv pip install -e .[dev]
uv run pytest
```

Tests are located in the `tests/` directory outside the `src/` folder
to ensure they import the **installed** package, not local files.

---

## 🛠️ Build the Package

Create wheel (`.whl`) and source (`.tar.gz`) distributions:

```bash
uv build
```

Artifacts are written to the `dist/` directory.

---

## 📁 Project Structure

```
fileparser/
├── pyproject.toml
├── README.md
├── src/
│   └── fileparser/
│       ├── __init__.py
│       ├── __main__.py
│       ├── parser.py
│       └── py.typed
└── tests/
    └── test_parser.py
```

---

## Why this structure?

* `src/` layout prevents accidental imports from the working directory
  (a common beginner mistake).
* Tests live outside `src/` to test the installed package, not the source tree.
* `py.typed` marks the package as PEP 561-compliant (type-aware).
* Uses modern `pyproject.toml`-based build system with **hatchling**.

---

## License

MIT License © 2025 Real Captain Solaris 
Feel free to use and modify this example.


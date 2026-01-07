# py-docgen

A command-line tool for generating Python docstrings using Concrete Syntax Trees (CST).

`py-docgen` analyzes Python source code with **LibCST** and inserts docstrings while preserving
original formatting, comments, and structure. `py-docgen` uses **Concrete Syntax Trees**, which 
retain the exact structure of the original source code. The primary interface is the CLI, with a
few different options depending upon use.

---

## Installation

```bash
pip install py-docgen
```


---
## Basic Usage

To generate docstrings directly in a file:

```bash
docgen main.py
```

To check for missing docstrings without modifying files:

```bash
docgen main.py --check
```

A non-zero exit code is returned when missing docstrings are found, making this suitable for
use in CI pipelines.

---

## Additional Options

* `--recursive`
  Recursively process Python files in a directory.

* `--verbose`
  Display information about processed files and detected definitions.

---

## Example

### Before

```python
def add(a, b):
    return a + b
```

### After

```python
def add(a, b):
    """
    Add two values and return the result.

    Parameters
    ----------
    a
        First value.
    b
        Second value.

    Returns
    -------
    Result of a + b.
    """
    return a + b
```

The generated docstrings are intentionally minimal and PEP 257–compliant.

---

## Supported Targets

* Top-level functions
* Methods
* Classes

Existing docstrings are **not overwritten**.

---

## Current Limitations

* No semantic analysis of function bodies
* No inference beyond available signatures
* No configuration file support yet
* Docstring style is currently fixed

These constraints are deliberate, prioritizing correctness and predictability over speculation.

---

## Roadmap

Planned improvements include:

* Support for configurable docstring styles
* Better integration with type hints
* Optional configuration file
* Expanded CLI options for selective generation

---

## License

MIT License

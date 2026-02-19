# py-ipld-dag

[![PyPI version](https://img.shields.io/pypi/v/py-ipld-dag.svg)](https://pypi.python.org/pypi/py-ipld-dag)
[![Documentation](https://readthedocs.org/projects/dag/badge/?version=latest)](https://dag.readthedocs.io/en/latest/?badge=latest)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

**MerkelDAG implementation in Python** — a Python library for working with IPLD Merkle DAG structures.

- **Documentation:** [https://dag.readthedocs.io/](https://dag.readthedocs.io/)
- **License:** MIT
- **Source:** [https://github.com/ipld/py-ipld-dag](https://github.com/ipld/py-ipld-dag)

## Installation

**From PyPI (stable):**

```bash
pip install py-ipld-dag
```

**From source (development):**

```bash
git clone https://github.com/ipld/py-ipld-dag.git
cd py-ipld-dag
pip install -e ".[dev]"
```

Or with [uv](https://github.com/astral-sh/uv) for faster installs:

```bash
uv venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
uv pip install -e ".[dev]"
```

## Usage

```python
import dag

# Use the library to work with Merkle DAG structures.
# See the documentation for full API and examples.
```

Full usage, API reference, and examples: **[Documentation](https://dag.readthedocs.io/)**.

## Development

- **Tests:** `pytest` or `make test`
- **Lint:** `make lint` or `pre-commit run --all-files`
- **Docs:** `make docs-ci` (build docs with Sphinx)

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup and pull request guidelines.

## Release notes

Changelog and release notes are generated from [newsfragments](newsfragments/README.md) with [Towncrier](https://towncrier.readthedocs.io/) and published in the docs: [Release notes](https://dag.readthedocs.io/en/latest/release_notes.html).

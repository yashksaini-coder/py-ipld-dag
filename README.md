# py-ipld-dag

[![PyPI version](https://img.shields.io/pypi/v/py-ipld-dag.svg)](https://pypi.python.org/pypi/py-ipld-dag)
[![Documentation](https://readthedocs.org/projects/dag/badge/?version=latest)](https://dag.readthedocs.io/en/latest/?badge=latest)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)

**MerkleDAG implementation in Python** — a Python library for working with IPLD Merkle DAG structures.

Read more in the [documentation on ReadTheDocs](https://py-ipld-dag.readthedocs.io/en/latest/). [View the release notes](https://py-ipld-dag.readthedocs.io/en/latest/release_notes.html).

## Installation and usage

Installation (venv, pip/uv, stable and development) and usage are documented in the [docs](https://py-ipld-dag.readthedocs.io/en/latest/) — see **Installation** and **Usage** in the table of contents.

## Installation

**From PyPI (stable):**

```bash
pip install py-ipld-dag
```

**From source (development):**

Same as in [CONTRIBUTING.md](CONTRIBUTING.md). With **uv** (recommended):

```bash
git clone https://github.com/ipld/py-ipld-dag.git
cd py-ipld-dag
uv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
uv pip install --upgrade pip
uv pip install --group dev -e .
pre-commit install
```

With **pip** (requires pip >= 25.1):

```bash
python -m venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
pip install --upgrade pip
pip install --group dev -e .
pre-commit install
```

Or run **`make install-dev`** after activating a venv (uses uv).

Full usage, API reference, and examples: **[Documentation](https://dag.readthedocs.io/)**.

## Development

- **Tests:** `pytest` or `make test`
- **Lint:** `make lint` or `pre-commit run --all-files`
- **Docs:** `make docs-ci` (build docs with Sphinx)

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for setup and pull request guidelines.

## Release notes

Changelog and release notes are generated from [newsfragments](newsfragments/README.md) with [Towncrier](https://towncrier.readthedocs.io/) and published in the docs: [Release notes](https://py-ipld-dag.readthedocs.io/en/latest/release_notes.html).

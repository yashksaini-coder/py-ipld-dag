# Contributing

Contributions are welcome. Every little bit helps, and credit will always be given.

## Ways to contribute

- **Report bugs** at [GitHub Issues](https://github.com/ipld/py-ipld-dag/issues)
- **Fix bugs** or **implement features** — look for issues tagged `help wanted`
- **Improve documentation** — docstrings, docs, or blog posts
- **Send feedback** or propose features via [issues](https://github.com/ipld/py-ipld-dag/issues)

## Getting started

1. **Open an issue** at [GitHub Issues](https://github.com/ipld/py-ipld-dag/issues) to discuss the bug or feature you want to address. This ensures that the change is aligned with the project's goals.

1. **Fork** the [repo](https://github.com/ipld/py-ipld-dag) and **clone** your fork.

1. **Install** for development (from repo root). This project uses uv for dependency management.

   **With uv (recommended):**

   ```bash
   uv venv venv && source venv/bin/activate   # Windows: venv\Scripts\activate
   uv pip install --upgrade pip
   uv pip install --group dev -e .
   pre-commit install
   ```

   **With pip** (requires pip >= 25.1):

   ```bash
   python -m venv venv && source venv/bin/activate
   pip install --upgrade pip
   pip install --group dev -e .
   pre-commit install
   ```

   Or run **`make install-dev`** after activating a venv (uses uv).

1. **Create a branch:** `git checkout -b name-of-your-change`

1. **Make changes**, then run **lint and tests:**

   ```bash
   make lint
   make test
   tox
   ```

   Or: `pre-commit run --all-files`

1. **Commit and push**, then open a **pull request.**

## Pull request guidelines

- Include tests where appropriate.
- Update docs if you add functionality (docstrings and/or README/docs).
- Ensure tests pass for Python 3.10–3.14 (see [GitHub Actions](https://github.com/ipld/py-ipld-dag/actions)).
- If your change should appear in the release notes, add a **newsfragment** as explained in [newsfragments/README.md](newsfragments/README.md): create a file under `newsfragments/` named `<ISSUE>.<TYPE>.rst` (e.g. `123.feature.rst`, `456.bugfix.rst`). Use the issue number the PR addresses. Run `towncrier build --draft` to preview. If possible, add the newsfragment in the same commit that introduces the change.

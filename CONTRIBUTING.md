# Contributing

Contributions are welcome. Every little bit helps, and credit will always be given.

## Ways to contribute

- **Report bugs** at [GitHub Issues](https://github.com/ipld/py-ipld-dag/issues)
- **Fix bugs** or **implement features** — look for issues tagged `help wanted`
- **Improve documentation** — docstrings, docs, or blog posts
- **Send feedback** or propose features via [issues](https://github.com/ipld/py-ipld-dag/issues)

## Getting started

1. **Fork** the [repo](https://github.com/ipld/py-ipld-dag) and **clone** your fork.
2. **Install** for development (from repo root):

   ```bash
   python -m venv venv
   source venv/bin/activate   # Windows: venv\Scripts\activate
   pip install -e ".[dev]"
   ```

   Or with **uv:**

   ```bash
   uv venv && source .venv/bin/activate
   uv pip install -e ".[dev]"
   ```

3. **Create a branch:** `git checkout -b name-of-your-change`
4. **Make changes**, then run **lint and tests:**

   ```bash
   make lint
   make test
   tox
   ```

   Or: `pre-commit run --all-files`

5. **Commit and push**, then open a **pull request.**

## Pull request guidelines

- Include tests where appropriate.
- Update docs if you add functionality (docstrings and/or README/docs).
- Ensure tests pass for Python 3.10–3.14 (see [GitHub Actions](https://github.com/ipld/py-ipld-dag/actions)).

## Release notes (newsfragments)

If your change should appear in the release notes, add a **newsfragment** under `newsfragments/`. See [newsfragments/README.md](newsfragments/README.md) for the format (e.g. `123.feature.rst`). Run `towncrier build --draft` to preview.

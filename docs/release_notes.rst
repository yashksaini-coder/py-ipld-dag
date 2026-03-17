Release notes
=============

.. towncrier release notes start

py-ipld-dag v0.2.1 (2026-03-17)
-------------------------------

Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- Fix documentation: all ReadTheDocs links and badge now point to ``py-ipld-dag.readthedocs.io``.
  Contributor docs now list only ``make`` as a system prerequisite (removed incorrect CMake, pkg-config, and GMP requirements). (`#21 <https://github.com/ipld/py-ipld-dag/issues/21>`__)


py-ipld-dag v0.2.0 (2026-03-15)
-------------------------------

Improved Documentation
~~~~~~~~~~~~~~~~~~~~~~

- Added Examples to docs. (`#20 <https://github.com/ipld/py-ipld-dag/issues/20>`__)


Features
~~~~~~~~

- Add Block API, IPLD data-model layer, multicodec registry, and four codec implementations (DAG-CBOR, DAG-JSON, DAG-PB, raw). The new design mirrors the JS multiformats ecosystem with encode/decode/create class methods, CID-based addressing, and pluggable codec registration. (`#17 <https://github.com/ipld/py-ipld-dag/issues/17>`__)


Internal Changes - for py-ipld-dag Contributors
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- Migrate from the legacy setup.cfg to modern pyproject.toml and add pre-commit hooks. Remove Travis CI with GitHub actions.
  Add new make commands and improve the project infrastructure. All changes are internal and does not affect the core modules. (`#12 <https://github.com/ipld/py-ipld-dag/issues/12>`__)
- Align the project's Pull Request workflow with ``py-libp2p`` by requiring a
  corresponding issue for every PR. Updated ``CONTRIBUTING.md``,
  ``newsfragments/README.md``, and the validation script to mandate that all
  newsfragments use numeric issue numbers. (`#18 <https://github.com/ipld/py-ipld-dag/issues/18>`__)

"""IPLD codec implementations.

This sub-package provides the built-in IPLD codecs:

- ``dag_cbor`` - DAG-CBOR (``0x71``)
- ``dag_json`` - DAG-JSON (``0x0129``)
- ``dag_pb``   - DAG-PB   (``0x70``)
- ``raw``      - Raw      (``0x55``)

All codecs are auto-registered when this package is imported.
"""

from __future__ import annotations

from . import dag_cbor, dag_json, dag_pb, raw
from .dag_cbor import DagCborCodec
from .dag_json import DagJsonCodec
from .dag_pb import DagPbCodec
from .raw import RawCodec

__all__ = [
    "DagCborCodec",
    "DagJsonCodec",
    "DagPbCodec",
    "RawCodec",
    "dag_cbor",
    "dag_json",
    "dag_pb",
    "raw",
]

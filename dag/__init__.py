"""py-ipld-dag – IPLD DAG implementation for Python.

A lean, modern implementation of the IPLD (InterPlanetary Linked Data)
data model and codecs for Python, aligned with the JS multiformats
ecosystem.

Provides:

- **IPLD Data Model** – kinds, type helpers, CID integration
- **Block API** – ``Block.encode()`` / ``Block.decode()`` / ``Block.create()``
- **Codec interface** – ``BlockCodec`` base class + codec registry
- **Built-in codecs**:
  - ``dag-cbor`` (``0x71``) – deterministic CBOR with CID links
  - ``dag-json`` (``0x0129``) – deterministic JSON with CID links
  - ``dag-pb`` (``0x70``) – Protobuf-based Merkle DAG (legacy IPFS)
  - ``raw`` (``0x55``) – identity codec for raw bytes

Usage::

    from dag import Block
    from dag.codecs import dag_cbor

    # Encode
    block = Block.encode(value={"hello": "world"}, codec=dag_cbor.codec)
    print(block.cid)   # bafyr...
    print(block.bytes)  # raw DAG-CBOR

    # Decode
    restored = Block.decode(data=block.bytes, codec=dag_cbor.codec)
    assert restored.value == {"hello": "world"}
"""

__author__ = """Dhruv Baldawa"""
__email__ = "dhruv@dhruvb.com"
__version__ = "0.1.0"

from .block import Block
from .codec import (
    BlockCodec,
    BlockDecoder,
    BlockEncoder,
    get_codec,
    lookup_codec,
    register_codec,
    registered_codecs,
)
from .ipld_model import CID, IPLDNode, Kind, is_cid, is_ipld_value, kind_of
from .multicodec_codes import (
    DAG_CBOR_CODE,
    DAG_CBOR_NAME,
    DAG_JSON_CODE,
    DAG_JSON_NAME,
    DAG_PB_CODE,
    DAG_PB_NAME,
    RAW_CODE,
    RAW_NAME,
)

from . import codecs

__all__ = [
    "Block",
    "BlockCodec",
    "BlockDecoder",
    "BlockEncoder",
    "get_codec",
    "lookup_codec",
    "register_codec",
    "registered_codecs",
    "CID",
    "IPLDNode",
    "Kind",
    "is_cid",
    "is_ipld_value",
    "kind_of",
    "DAG_CBOR_CODE",
    "DAG_CBOR_NAME",
    "DAG_JSON_CODE",
    "DAG_JSON_NAME",
    "DAG_PB_CODE",
    "DAG_PB_NAME",
    "RAW_CODE",
    "RAW_NAME",
]

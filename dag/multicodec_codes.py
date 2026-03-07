"""Multicodec code constants for IPLD codecs and multihash functions.

These codes are defined by the multicodec table:
https://github.com/multiformats/multicodec/blob/master/table.csv
"""

from __future__ import annotations

RAW_CODE = 0x55
"""Raw binary codec – identity, no transformation."""

DAG_PB_CODE = 0x70
"""DAG-PB (Protobuf) codec – used by legacy IPFS UnixFS."""

DAG_CBOR_CODE = 0x71
"""DAG-CBOR codec – deterministic CBOR with IPLD links."""

DAG_JSON_CODE = 0x0129
"""DAG-JSON codec – deterministic JSON with IPLD links."""

RAW_NAME = "raw"
DAG_PB_NAME = "dag-pb"
DAG_CBOR_NAME = "dag-cbor"
DAG_JSON_NAME = "dag-json"

SHA2_256_CODE = 0x12
"""SHA-256 hash function."""

SHA2_512_CODE = 0x13
"""SHA-512 hash function."""

SHA3_256_CODE = 0x16
"""SHA3-256 hash function."""

SHA3_512_CODE = 0x17
"""SHA3-512 hash function."""

BLAKE2B_256_CODE = 0xB220
"""BLAKE2b-256 hash function."""

IDENTITY_CODE = 0x00
"""Identity hash function (no hashing)."""

CODEC_TABLE: dict[int, str] = {
    RAW_CODE: RAW_NAME,
    DAG_PB_CODE: DAG_PB_NAME,
    DAG_CBOR_CODE: DAG_CBOR_NAME,
    DAG_JSON_CODE: DAG_JSON_NAME,
}

NAME_TABLE: dict[str, int] = {v: k for k, v in CODEC_TABLE.items()}

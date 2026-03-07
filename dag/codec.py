"""Codec interface definitions for IPLD.

This module defines the abstract interfaces that every IPLD codec must
implement, following the same pattern as the JS ``@ipld/interface``
(``BlockEncoder`` / ``BlockDecoder`` / ``BlockCodec``).

A **codec** is identified by:
- ``name`` – a human-readable string (e.g. ``"dag-cbor"``)
- ``code`` – the multicodec code (e.g. ``0x71``)

And provides two operations:
- ``encode(node)`` → ``bytes``   – serialize an IPLD node
- ``decode(data)`` → ``node``    – deserialize bytes into an IPLD node
"""

from __future__ import annotations

import abc
from typing import Any

from .ipld_model import IPLDNode


class BlockEncoder(abc.ABC):
    """Abstract encoder – turns an IPLD node into bytes."""

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Human-readable codec name (e.g. ``'dag-cbor'``)."""

    @property
    @abc.abstractmethod
    def code(self) -> int:
        """Multicodec code (e.g. ``0x71``)."""

    @abc.abstractmethod
    def encode(self, node: IPLDNode) -> bytes:
        """Encode an IPLD data model value into bytes."""


class BlockDecoder(abc.ABC):
    """Abstract decoder – turns bytes into an IPLD node."""

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Human-readable codec name."""

    @property
    @abc.abstractmethod
    def code(self) -> int:
        """Multicodec code."""

    @abc.abstractmethod
    def decode(self, data: bytes) -> IPLDNode:
        """Decode bytes into an IPLD data model value."""


class BlockCodec(BlockEncoder, BlockDecoder):
    """A codec that can both encode and decode.

    Concrete implementations should subclass this and provide
    ``name``, ``code``, ``encode``, and ``decode``.
    """


_codec_registry: dict[int, BlockCodec] = {}


def register_codec(codec: BlockCodec) -> None:
    """Register a codec so it can be looked up by code."""
    _codec_registry[codec.code] = codec


def get_codec(code: int) -> BlockCodec:
    """Look up a registered codec by its multicodec code.

    Raises ``KeyError`` if no codec is registered for *code*.
    """
    if code not in _codec_registry:
        raise KeyError(
            f"No codec registered for code 0x{code:x}. "
            f"Registered: {sorted(f'0x{c:x}' for c in _codec_registry)}"
        )
    return _codec_registry[code]


def registered_codecs() -> dict[int, BlockCodec]:
    """Return a copy of all registered codecs."""
    return dict(_codec_registry)


def lookup_codec(name_or_code: str | int) -> BlockCodec:
    """Look up a codec by name or code.

    Raises ``KeyError`` if not found.
    """
    if isinstance(name_or_code, int):
        return get_codec(name_or_code)

    for codec in _codec_registry.values():
        if codec.name == name_or_code:
            return codec
    raise KeyError(f"No codec registered with name {name_or_code!r}")

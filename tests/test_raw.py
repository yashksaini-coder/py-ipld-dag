#!/usr/bin/env python3
"""Comprehensive tests for the Raw codec."""

import pytest

from dag import Block
from dag.codecs.raw import codec, decode, encode


class RawBasicTestCase:
    """Basic Raw codec tests."""

    def test_codec_name(self):
        assert codec.name == "raw"

    def test_codec_code(self):
        assert codec.code == 0x55

    def test_encode_bytes(self):
        result = encode(b"hello world")
        assert result == b"hello world"

    def test_decode_bytes(self):
        result = decode(b"hello world")
        assert result == b"hello world"

    def test_roundtrip(self):
        data = b"\x00\x01\x02\xff\xfe\xfd"
        assert decode(encode(data)) == data

    def test_empty_bytes(self):
        assert decode(encode(b"")) == b""

    def test_large_bytes(self):
        data = b"\x42" * 10000
        assert decode(encode(data)) == data

    def test_encode_rejects_non_bytes(self):
        with pytest.raises(TypeError):
            encode("not bytes")

    def test_encode_rejects_int(self):
        with pytest.raises(TypeError):
            encode(42)

    def test_encode_rejects_dict(self):
        with pytest.raises(TypeError):
            encode({"key": "value"})

    def test_encode_accepts_bytearray(self):
        result = encode(bytearray(b"hello"))
        assert result == b"hello"


class RawBlockTestCase:
    """Tests for Block integration with Raw codec."""

    def test_block_encode(self):
        block = Block.encode(value=b"raw data", codec=codec)
        assert block.value == b"raw data"
        assert block.bytes == b"raw data"
        assert block.cid is not None

    def test_block_decode(self):
        block = Block.encode(value=b"test", codec=codec)
        decoded = Block.decode(data=block.bytes, codec=codec)
        assert decoded.value == b"test"

    def test_block_cid_consistency(self):
        block1 = Block.encode(value=b"same data", codec=codec)
        block2 = Block.encode(value=b"same data", codec=codec)
        assert str(block1.cid) == str(block2.cid)

    def test_block_encode_by_code(self):
        block = Block.encode(value=b"test", codec=0x55)
        assert block.value == b"test"

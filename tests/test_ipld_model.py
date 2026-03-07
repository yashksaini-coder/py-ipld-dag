#!/usr/bin/env python3
"""Tests for the IPLD Data Model module."""

import pytest
from cid import make_cid
import multihash

from dag.ipld_model import Kind, kind_of, is_cid, is_ipld_value


class KindOfTestCase:
    """Tests for kind_of()."""

    def test_null(self):
        assert kind_of(None) == Kind.NULL

    def test_bool_true(self):
        assert kind_of(True) == Kind.BOOL

    def test_bool_false(self):
        assert kind_of(False) == Kind.BOOL

    def test_int(self):
        assert kind_of(42) == Kind.INT

    def test_int_zero(self):
        assert kind_of(0) == Kind.INT

    def test_int_negative(self):
        assert kind_of(-1) == Kind.INT

    def test_float(self):
        assert kind_of(3.14) == Kind.FLOAT

    def test_string(self):
        assert kind_of("hello") == Kind.STRING

    def test_empty_string(self):
        assert kind_of("") == Kind.STRING

    def test_bytes(self):
        assert kind_of(b"hello") == Kind.BYTES

    def test_bytearray(self):
        assert kind_of(bytearray(b"hello")) == Kind.BYTES

    def test_list(self):
        assert kind_of([1, 2, 3]) == Kind.LIST

    def test_empty_list(self):
        assert kind_of([]) == Kind.LIST

    def test_map(self):
        assert kind_of({"a": 1}) == Kind.MAP

    def test_empty_map(self):
        assert kind_of({}) == Kind.MAP

    def test_link(self):
        mh = multihash.digest(b"test", "sha2-256")
        c = make_cid(1, "dag-cbor", mh.encode())
        assert kind_of(c) == Kind.LINK

    def test_unknown_type_raises(self):
        with pytest.raises(TypeError):
            kind_of(object())

    def test_set_raises(self):
        with pytest.raises(TypeError):
            kind_of({1, 2, 3})

    def test_tuple_raises(self):
        with pytest.raises(TypeError):
            kind_of((1, 2))


class IsCidTestCase:
    """Tests for is_cid()."""

    def test_cidv1(self):
        mh = multihash.digest(b"test", "sha2-256")
        c = make_cid(1, "dag-cbor", mh.encode())
        assert is_cid(c) is True

    def test_cidv0(self):
        mh = multihash.digest(b"test", "sha2-256")
        c = make_cid(0, "dag-pb", mh.encode())
        assert is_cid(c) is True

    def test_string_not_cid(self):
        assert is_cid("bafy...") is False

    def test_bytes_not_cid(self):
        assert is_cid(b"\x01\x71") is False

    def test_none_not_cid(self):
        assert is_cid(None) is False


class IsIpldValueTestCase:
    """Tests for is_ipld_value()."""

    def test_valid_values(self):
        assert is_ipld_value(None) is True
        assert is_ipld_value(True) is True
        assert is_ipld_value(42) is True
        assert is_ipld_value(3.14) is True
        assert is_ipld_value("hello") is True
        assert is_ipld_value(b"bytes") is True
        assert is_ipld_value([1, 2]) is True
        assert is_ipld_value({"a": 1}) is True

    def test_cid_is_valid(self):
        mh = multihash.digest(b"test", "sha2-256")
        c = make_cid(1, "dag-cbor", mh.encode())
        assert is_ipld_value(c) is True

    def test_invalid_values(self):
        assert is_ipld_value(object()) is False
        assert is_ipld_value({1, 2}) is False

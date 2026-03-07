#!/usr/bin/env python3
"""Tests for utility functions."""

import pytest

from cid import make_cid
import multihash

from dag import is_cid
from dag.utils import (
    create_cid,
    cid_to_bytes,
    bytes_to_cid,
    cid_to_string,
    string_to_cid,
    collect_links,
)


class CreateCidTestCase:

    def test_create_cid_v1(self):
        c = create_cid(b"hello world", codec="dag-cbor")
        assert is_cid(c)
        assert c.version == 1

    def test_create_cid_v0(self):
        c = create_cid(b"hello world", codec="dag-pb", version=0)
        assert is_cid(c)
        assert c.version == 0


class CidConversionTestCase:

    @pytest.fixture
    def sample_cid(self):
        mh = multihash.digest(b"test", "sha2-256")
        return make_cid(1, "dag-cbor", mh.encode())

    def test_cid_to_bytes_and_back(self, sample_cid):
        raw = cid_to_bytes(sample_cid)
        restored = bytes_to_cid(raw)
        assert str(restored) == str(sample_cid)

    def test_cid_to_string_and_back(self, sample_cid):
        s = cid_to_string(sample_cid)
        restored = string_to_cid(s)
        assert str(restored) == str(sample_cid)


class CollectLinksTestCase:

    @pytest.fixture
    def sample_cid(self):
        mh = multihash.digest(b"test", "sha2-256")
        return make_cid(1, "dag-cbor", mh.encode())

    def test_no_links(self):
        assert collect_links({"a": 1, "b": "c"}) == []

    def test_top_level_link(self, sample_cid):
        links = collect_links({"link": sample_cid})
        assert len(links) == 1
        assert links[0][0] == "link"

    def test_nested_links(self, sample_cid):
        val = {"a": {"b": sample_cid}, "c": [sample_cid]}
        links = collect_links(val)
        assert len(links) == 2

#!/usr/bin/env python3
"""Tests for the codec registry."""

import pytest

from dag.codec import (
    get_codec,
    lookup_codec,
    registered_codecs,
)


class CodecRegistryTestCase:
    """Tests for the codec registry."""

    def test_get_codec_dag_cbor(self):
        codec = get_codec(0x71)
        assert codec.name == "dag-cbor"
        assert codec.code == 0x71

    def test_get_codec_dag_json(self):
        codec = get_codec(0x0129)
        assert codec.name == "dag-json"
        assert codec.code == 0x0129

    def test_get_codec_dag_pb(self):
        codec = get_codec(0x70)
        assert codec.name == "dag-pb"
        assert codec.code == 0x70

    def test_get_codec_raw(self):
        codec = get_codec(0x55)
        assert codec.name == "raw"
        assert codec.code == 0x55

    def test_get_codec_unknown_raises(self):
        with pytest.raises(KeyError):
            get_codec(0xFFFF)

    def test_lookup_by_name(self):
        codec = lookup_codec("dag-cbor")
        assert codec.code == 0x71

    def test_lookup_by_code(self):
        codec = lookup_codec(0x71)
        assert codec.name == "dag-cbor"

    def test_lookup_unknown_name_raises(self):
        with pytest.raises(KeyError):
            lookup_codec("nonexistent")

    def test_registered_codecs(self):
        codecs = registered_codecs()
        assert 0x71 in codecs
        assert 0x0129 in codecs
        assert 0x70 in codecs
        assert 0x55 in codecs

    def test_registered_codecs_returns_copy(self):
        codecs1 = registered_codecs()
        codecs2 = registered_codecs()
        assert codecs1 is not codecs2

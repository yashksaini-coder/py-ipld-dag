#!/usr/bin/env python3
"""Cross-codec interoperability tests.

Ensures that CIDs created by one codec can be embedded and
recovered by another codec correctly.
"""

from dag import Block, is_cid
from dag.codecs import dag_cbor, dag_json, dag_pb, raw


class CrossCodecCidTestCase:
    """Tests for CID interop across codecs."""

    def test_cbor_cid_in_json(self):
        """A CID from a DAG-CBOR block can be referenced in DAG-JSON."""
        inner = Block.encode(value={"data": "cbor"}, codec=dag_cbor.codec)
        outer = Block.encode(
            value={"ref": inner.cid},
            codec=dag_json.codec,
        )
        decoded = Block.decode(data=outer.bytes, codec=dag_json.codec)
        assert is_cid(decoded.value["ref"])
        assert str(decoded.value["ref"]) == str(inner.cid)

    def test_json_cid_in_cbor(self):
        """A CID from a DAG-JSON block can be referenced in DAG-CBOR."""
        inner = Block.encode(value={"data": "json"}, codec=dag_json.codec)
        outer = Block.encode(
            value={"ref": inner.cid},
            codec=dag_cbor.codec,
        )
        decoded = Block.decode(data=outer.bytes, codec=dag_cbor.codec)
        assert is_cid(decoded.value["ref"])
        assert str(decoded.value["ref"]) == str(inner.cid)

    def test_raw_cid_in_cbor(self):
        """A CID from a Raw block can be referenced in DAG-CBOR."""
        raw_block = Block.encode(value=b"raw data", codec=raw.codec)
        outer = Block.encode(
            value={"ref": raw_block.cid},
            codec=dag_cbor.codec,
        )
        decoded = Block.decode(data=outer.bytes, codec=dag_cbor.codec)
        assert str(decoded.value["ref"]) == str(raw_block.cid)

    def test_pb_cid_in_json(self):
        """A CID from a DAG-PB block can be referenced in DAG-JSON."""
        pb_block = Block.encode(
            value={"Data": b"pb data", "Links": []},
            codec=dag_pb.codec,
        )
        outer = Block.encode(
            value={"ref": pb_block.cid},
            codec=dag_json.codec,
        )
        decoded = Block.decode(data=outer.bytes, codec=dag_json.codec)
        assert str(decoded.value["ref"]) == str(pb_block.cid)

    def test_cbor_cid_in_pb_link(self):
        """A CID from a DAG-CBOR block can be a link in DAG-PB."""
        inner = Block.encode(value={"data": "inner"}, codec=dag_cbor.codec)
        pb_val = {
            "Data": b"parent",
            "Links": [{"Hash": inner.cid, "Name": "child", "Tsize": 10}],
        }
        pb_block = Block.encode(value=pb_val, codec=dag_pb.codec)
        decoded = Block.decode(data=pb_block.bytes, codec=dag_pb.codec)
        assert str(decoded.value["Links"][0]["Hash"]) == str(inner.cid)


class MultiBlockGraphTestCase:
    """Tests simulating multi-block DAG structures."""

    def test_simple_dag(self):
        """Build a simple DAG: root -> child1, root -> child2."""
        child1 = Block.encode(value={"name": "child1"}, codec=dag_cbor.codec)
        child2 = Block.encode(value={"name": "child2"}, codec=dag_cbor.codec)

        root = Block.encode(
            value={
                "children": [child1.cid, child2.cid],
                "type": "root",
            },
            codec=dag_cbor.codec,
        )

        links = list(root.links())
        assert len(links) == 2

        link_strs = {str(cid) for _, cid in links}
        assert str(child1.cid) in link_strs
        assert str(child2.cid) in link_strs

    def test_deep_dag(self):
        """Build a chain: grandchild -> child -> parent -> root."""
        grandchild = Block.encode(value={"level": 3}, codec=dag_cbor.codec)
        child = Block.encode(
            value={"level": 2, "next": grandchild.cid},
            codec=dag_cbor.codec,
        )
        parent = Block.encode(
            value={"level": 1, "next": child.cid},
            codec=dag_cbor.codec,
        )
        root = Block.encode(
            value={"level": 0, "next": parent.cid},
            codec=dag_cbor.codec,
        )

        assert len(list(root.links())) == 1
        assert len(list(parent.links())) == 1
        assert len(list(child.links())) == 1
        assert len(list(grandchild.links())) == 0

    def test_mixed_codec_dag(self):
        """Build a DAG where different nodes use different codecs."""
        raw_leaf = Block.encode(value=b"raw leaf", codec=raw.codec)
        json_node = Block.encode(
            value={"ref": raw_leaf.cid, "type": "json"},
            codec=dag_json.codec,
        )
        cbor_root = Block.encode(
            value={"ref": json_node.cid, "type": "cbor"},
            codec=dag_cbor.codec,
        )

        root_links = list(cbor_root.links())
        assert len(root_links) == 1
        assert str(root_links[0][1]) == str(json_node.cid)

        json_decoded = Block.decode(data=json_node.bytes, codec=dag_json.codec)
        json_links = list(json_decoded.links())
        assert len(json_links) == 1
        assert str(json_links[0][1]) == str(raw_leaf.cid)

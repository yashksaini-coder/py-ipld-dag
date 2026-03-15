"""Equivalent of js-multiformats/examples/block-interface.js."""

import argparse
import json

from dag import Block
from dag.codecs import dag_cbor


def build_report() -> dict[str, object]:
    value = {"hello": "world"}

    # Encode a block.
    block = Block.encode(value=value, codec=dag_cbor.codec, hasher="sha2-256")

    # Decode from bytes.
    block2 = Block.decode(data=block.bytes, codec=dag_cbor.codec, hasher="sha2-256")

    # Re-create from known pieces (bytes + cid + decoded value).
    block3 = Block.create(data=block.bytes, cid=block.cid, value=block2.value, codec=dag_cbor.codec)
    return {
        "input": value,
        "codec": "dag-cbor",
        "cid": str(block.cid),
        "checks": {
            "decoded_cid_equals_original": block.cid.buffer == block2.cid.buffer,
            "created_cid_equals_original": block.cid.buffer == block3.cid.buffer,
        },
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Block interface example")
    parser.add_argument("--json", action="store_true", help="Print structured JSON report")
    args = parser.parse_args()

    report = build_report()
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return

    print(f"Example block CID: {report['cid']}")
    print(f"CID equal to decoded block: {report['checks']['decoded_cid_equals_original']}")
    print(f"CID equal to block created from CID + bytes: {report['checks']['created_cid_equals_original']}")


if __name__ == "__main__":
    main()

"""Equivalent of js-multiformats/examples/multicodec-interface.js."""

import json
from typing import Any

from dag import Block, BlockCodec, lookup_codec, register_codec


class JsonCodec(BlockCodec):
    """Simple JSON codec example (UTF-8 encoded)."""

    @property
    def name(self) -> str:
        return "json"

    @property
    def code(self) -> int:
        return 0x0200

    def encode(self, node: Any) -> bytes:
        return json.dumps(node, separators=(",", ":"), sort_keys=True).encode("utf-8")

    def decode(self, data: bytes) -> Any:
        return json.loads(data.decode("utf-8"))


def main() -> None:
    codec = JsonCodec()
    register_codec(codec)

    looked_up = lookup_codec("json")
    print(f"Registered codec: {looked_up.name} (0x{looked_up.code:x})")

    value = {"hello": "world"}
    block = Block.encode(value=value, codec=looked_up)
    restored = Block.decode(data=block.bytes, codec=looked_up)

    print(f"Block CID: {block.cid}")
    print(f"Round-trip value equal: {restored.value == value}")


if __name__ == "__main__":
    main()

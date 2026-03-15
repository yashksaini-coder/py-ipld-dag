# Examples

Python equivalents of `js-multiformats/examples/*`, adapted to current
`py-ipld-dag` APIs.

## Run

From repository root:

```bash
source venv/bin/activate
python -m examples.block_interface.block_interface
python -m examples.cid_interface.cid_interface
python -m examples.multicodec_interface.multicodec_interface
python -m examples.multihash_interface.multihash_interface
```

For machine-checkable verification output:

```bash
python -m examples.block_interface.block_interface --json
python -m examples.cid_interface.cid_interface --json
python -m examples.multihash_interface.multihash_interface --json
```

## Files

- `block_interface/block_interface.py` - `Block.encode()`, `Block.decode()`, `Block.create()`
- `cid_interface/cid_interface.py` - CID creation, encoding/decoding, conversions
- `multicodec_interface/multicodec_interface.py` - custom `BlockCodec` implementation + registry
- `multihash_interface/multihash_interface.py` - building CIDs from explicit multihash digests

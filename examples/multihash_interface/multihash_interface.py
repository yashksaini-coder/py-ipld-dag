"""Equivalent of js-multiformats/examples/multihash-interface.js."""

import argparse
import hashlib
import json

import multihash
from cid import make_cid

JS_EXPECTED = {
    "sha2_256_digest_len": 32,
    "sha2_256_cid_base32": "bagaaierasords4njcts6vs7qvdjfcvgnume4hqohf65zsfguprqphs3icwea",
    "sha3_512_digest_len": 64,
    "sha3_512_cid_base32": (
        "bagaaifca7d5wrebdi6rmqkgtrqyodq3bo6gitrqtemxtliymakwswbazbu7ai763747ljp7ycqfv7aqx4xlgiugcx62quo2te45pcgjbg4qjsvq"
    ),
}


def _js_style_sha3_512_multihash(payload: bytes) -> bytes:
    """Reproduce the JS example's explicit code=0x14 behavior.

    The upstream JS example labels the second hasher as `sha3-512` (code `0x14`)
    while using Node's `sha512` digest bytes. We mirror that encoded multihash
    byte layout to compare with the documented JS comment output exactly.
    """
    digest = hashlib.sha512(payload).digest()
    return bytes((0x14, len(digest))) + digest


def build_report() -> dict[str, object]:
    payload_obj = {"hello": "world"}
    payload = json.dumps(payload_obj, separators=(",", ":"), sort_keys=True).encode("utf-8")

    digest_256 = multihash.digest(payload, "sha2-256")
    cid_256 = make_cid(1, "json", digest_256.encode())
    cid_256_b32 = cid_256.encode("base32").decode("ascii")

    js_style_512_mh = _js_style_sha3_512_multihash(payload)
    cid_js_style_512 = make_cid(1, "json", js_style_512_mh)
    cid_js_style_512_b32 = cid_js_style_512.encode("base32").decode("ascii")

    matches = {
        "sha2_256_digest_len": digest_256.length == JS_EXPECTED["sha2_256_digest_len"],
        "sha2_256_cid_base32": cid_256_b32 == JS_EXPECTED["sha2_256_cid_base32"],
        "sha3_512_digest_len": len(hashlib.sha512(payload).digest()) == JS_EXPECTED["sha3_512_digest_len"],
        "sha3_512_cid_base32": cid_js_style_512_b32 == JS_EXPECTED["sha3_512_cid_base32"],
    }

    return {
        "input": payload_obj,
        "codec": "json",
        "sha2_256": {
            "digest_length": digest_256.length,
            "cid_base32": cid_256_b32,
            "cid_default_string": str(cid_256),
        },
        "sha3_512_js_style": {
            "digest_length": len(hashlib.sha512(payload).digest()),
            "multihash_code_hex": "0x14",
            "cid_base32": cid_js_style_512_b32,
            "cid_default_string": str(cid_js_style_512),
        },
        "js_expected": JS_EXPECTED,
        "matches_js_comments": matches,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Multihash interface example")
    parser.add_argument("--json", action="store_true", help="Print structured JSON report")
    args = parser.parse_args()

    report = build_report()
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return

    print(f"sha2-256 digest length: {report['sha2_256']['digest_length']} bytes")
    print(f"sha2-256 CID: {report['sha2_256']['cid_default_string']}")
    print(f"sha3-512 digest length: {report['sha3_512_js_style']['digest_length']} bytes")
    print(f"sha3-512 CID: {report['sha3_512_js_style']['cid_default_string']}")
    print(
        "Matches js comments (sha2-256/sha3-512 CID): "
        f"{report['matches_js_comments']['sha2_256_cid_base32']}/"
        f"{report['matches_js_comments']['sha3_512_cid_base32']}"
    )


if __name__ == "__main__":
    main()

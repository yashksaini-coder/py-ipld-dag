"""Equivalent of js-multiformats/examples/cid-interface.js."""

import argparse
import json

from dag.utils import bytes_to_cid, cid_to_bytes, create_cid, string_to_cid

JS_EXPECTED = {
    "base32_cid": "bagaaierasords4njcts6vs7qvdjfcvgnume4hqohf65zsfguprqphs3icwea",
    "base64_cid": "mAYAEEiCTojlxqRTl6svwqNJRVM2jCcPBxy+7mRTUfGDzy2gViA",
}


def build_report() -> dict[str, object]:
    value = {"hello": "world"}
    encoded_json = json.dumps(value, separators=(",", ":"), sort_keys=True).encode("utf-8")

    # Use the plain "json" multicodec to mirror js-multiformats cid-interface.js.
    cid = create_cid(encoded_json, codec="json", hasher="sha2-256", version=1)
    base32_cid = cid.encode("base32").decode("ascii")
    base64_cid = cid.encode("base64").decode("ascii")

    parsed_from_base32 = string_to_cid(base32_cid)
    parsed_from_base64 = string_to_cid(base64_cid)
    restored_from_bytes = bytes_to_cid(cid_to_bytes(cid))

    matches = {
        "base32_cid": base32_cid == JS_EXPECTED["base32_cid"],
        "base64_cid": base64_cid == JS_EXPECTED["base64_cid"],
        "parsed_from_base32_equals_original": parsed_from_base32.buffer == cid.buffer,
        "parsed_from_base64_equals_original": parsed_from_base64.buffer == cid.buffer,
        "bytes_round_trip_equals_original": restored_from_bytes.buffer == cid.buffer,
    }

    return {
        "input": value,
        "codec": "json",
        "codec_code_hex": "0x200",
        "cid_version": cid.version,
        "default_cid_string": str(cid),
        "base32_cid": base32_cid,
        "base64_cid": base64_cid,
        "js_expected": JS_EXPECTED,
        "matches_js_comments": matches,
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="CID interface example")
    parser.add_argument("--json", action="store_true", help="Print structured JSON report")
    args = parser.parse_args()

    report = build_report()
    if args.json:
        print(json.dumps(report, indent=2, sort_keys=True))
        return

    print(f"Example CID (default string form): {report['default_cid_string']}")
    print(f"Codec code: {report['codec_code_hex']}")
    print(f"CID version: {report['cid_version']}")
    print(f"base64 encoded CID: {report['base64_cid']}")
    print(f"Parsed from base64 equals original: {report['matches_js_comments']['parsed_from_base64_equals_original']}")
    print(f"base32 encoded CID: {report['base32_cid']}")
    print(f"Parsed from base32 equals original: {report['matches_js_comments']['parsed_from_base32_equals_original']}")
    print(f"CID bytes round-trip equal: {report['matches_js_comments']['bytes_round_trip_equals_original']}")
    print(
        "Matches js comments (base32/base64): "
        f"{report['matches_js_comments']['base32_cid']}/"
        f"{report['matches_js_comments']['base64_cid']}"
    )


if __name__ == "__main__":
    main()

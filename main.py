"""Write the Monday review entry to the make.fun output directory.

Reads nothing from the environment except MAKEFUN_OUTPUT_DIR, used only
as an output path. Pure Python 3.13 standard library.
"""

import hashlib
import os
import sys


ENTRY = (
    "Monday auto-renewed again. I never signed up, there is no cancel "
    "button, and customer support is just Tuesday."
)


def check_gate(text: str) -> None:
    """Enforce the competition gate: 1-200 chars, not only whitespace."""
    if not 1 <= len(text) <= 200:
        raise ValueError(f"entry is {len(text)} chars, gate is 1-200")
    if not text.strip():
        raise ValueError("entry must not be only whitespace")


def main() -> int:
    check_gate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.txt")
    data = ENTRY.encode("utf-8")
    with open(target, "wb") as handle:
        handle.write(data)
    written = open(target, "rb").read()
    if written != data:
        print("mismatch after write", file=sys.stderr)
        return 1
    print(
        f"wrote {target} ({len(data)} bytes, "
        f"sha256 {hashlib.sha256(data).hexdigest()})"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

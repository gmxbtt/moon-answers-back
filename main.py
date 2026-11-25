#!/usr/bin/env python3
"""The Moon Finally Answers Back -- make.fun program/v1 entry.

The program writes a single line, spoken by the Moon at last, to the
output directory the harness provides (MAKEFUN_OUTPUT_DIR, default
/output) as entry.txt. One line only, 1-240 characters, no trailing
newline, so the gate reads exactly the line and nothing else.
"""

import os
import sys

# The reply is built from three beats: the long wait, the turn, the
# punchline. The Moon has heard it all; nobody ever wished it back.
_BEATS = (
    "Four billion years of your wishes, your howls, your 2 a.m. promises",
    "and not one of you has ever wished me a good night.",
)
_MOON_LINE = " \u2014 ".join(_BEATS)


def _target_path() -> str:
    folder = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def main() -> int:
    line = _MOON_LINE.strip()
    if not 1 <= len(line) <= 240:
        print(f"line is {len(line)} characters, must be 1-240", file=sys.stderr)
        return 1
    with open(_target_path(), "w", encoding="utf-8", newline="") as out:
        out.write(line)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

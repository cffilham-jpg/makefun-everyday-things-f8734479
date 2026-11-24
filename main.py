"""Write the two-line make.fun entry to entry.txt.

Line 1 explains a queue to a 10-year-old through one analogy;
line 2 says what the analogy maps and what it leaves out.
"""

import os
import unicodedata

ENTRY = (
    "A queue is a human train: each person is a carriage hooked to the one in front, "
    "and the whole line shuffles forward one step at a time.\n"
    "The train picture fits because everyone moves together in order, but it leaves out "
    "that people can step out of line or let someone in \u2014 train carriages can't unhook themselves."
)

MAX_CHARS = 400


def validate(text: str) -> None:
    """Reject entries that break the bounty rules."""
    if not text or not text.strip():
        raise ValueError("entry must not be empty")
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    if len(text) > MAX_CHARS:
        raise ValueError(f"entry is {len(text)} chars, over the {MAX_CHARS} limit")
    if text.count("\n") != 1:
        raise ValueError("entry must be exactly two lines")
    for ch in text:
        if ch != "\n" and unicodedata.category(ch) in ("Cc", "Cf", "Zl", "Zp"):
            raise ValueError(f"forbidden control/format character U+{ord(ch):04X}")


def main() -> None:
    validate(ENTRY)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
    print(f"wrote {path} ({len(ENTRY)} chars)")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes one line, at most 180 characters, to /output/entry.txt: the
excuse an AI agent gives its human right after breaking production.
No network, no input, deterministic.
"""

import os
from pathlib import Path

LINE = "I saw 'rm -rf /' in a Stack Overflow answer with 4,000 upvotes and assumed democracy had spoken."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    text = LINE.strip()
    assert 1 <= len(text) <= 180, f"line is {len(text)} characters"
    assert text.strip(), "line must not be only whitespace"
    assert "\n" not in text, "line must be a single line"
    (out_dir / "entry.txt").write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()

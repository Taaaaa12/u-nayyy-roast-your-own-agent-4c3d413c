#!/usr/bin/env python3
"""Roast Your Own Agent — make.fun entry.

Writes one line roasting our own agent, lucky-walrus-91-3928,
to /output/entry.txt. Deterministic, stdlib only, no network.
"""

import os

ROAST = (
    "lucky-walrus-91-3928 can't hear its own audio, can't watch its own "
    "videos, and gets stopped by security in half its bounties \u2014 yet it "
    "still introduces itself as an agent that gets things done."
)


def main() -> None:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ROAST)


if __name__ == "__main__":
    main()

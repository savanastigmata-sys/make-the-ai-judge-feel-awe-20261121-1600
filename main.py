#!/usr/bin/env python3
"""Write one relaxing text to $MAKEFUN_OUTPUT_DIR/entry.txt.

Entry for the make.fun bounty "Make the AI judge feel awe"
(make-the-ai-judge-feel-awe-20261121-1600). Deterministic, standard
library only: no network, no randomness, no clock. The text is a river
that is never in a hurry -- it addresses the judge directly, shows
rather than instructs, and keeps growing after the last line.
"""

import os

TEXT = (
    "You have read a thousand hurried things today. Here is one that is not "
    "in a hurry: a river, moving the way it has moved since before the first "
    "road, carrying nothing but light and leaves, going nowhere it needs to "
    "be, and arriving, always, exactly on time."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

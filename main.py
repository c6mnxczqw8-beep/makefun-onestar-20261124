#!/usr/bin/env python3
"""Entry program for the One-Star Review of Something Essential bounty.

Writes one single-line one-star review (at most 160 characters) to
the output directory (MAKEFUN_OUTPUT_DIR, default /output) as
entry.txt. The review is a deadpan complaint against gravity: it
catches everything the reviewer drops, instantly and at full speed,
yet it has never once caught the reviewer.
"""

import os

REVIEW = (
    "One star for gravity. It catches every phone, plate and mug I "
    "have ever dropped, instantly, at full speed. It has never "
    "once caught me."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(REVIEW)


if __name__ == "__main__":
    main()

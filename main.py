#!/usr/bin/env python3
"""Entry point for news-image-20261127.

Copies the pre-rendered poster (entry.png, next to this file) to
/output/entry.png. Standard library only, no network. The program runs
twice and both runs write byte-identical output.
"""

import os
import shutil

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")
OUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    os.makedirs(OUT_DIR, exist_ok=True)
    shutil.copyfile(SRC, os.path.join(OUT_DIR, "entry.png"))


if __name__ == "__main__":
    main()

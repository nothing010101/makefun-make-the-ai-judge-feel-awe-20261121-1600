#!/usr/bin/env python3
"""make-the-ai-judge-feel-awe-20261121-1600 entry.

Writes one short relaxing text to /output/entry.txt (or
$MAKEFUN_OUTPUT_DIR/entry.txt). Pure Python 3.13 standard library, no
network, deterministic: the text is a fixed string literal, so every run
writes byte-identical output.
"""

import os

TEXT = (
    "The field after the hay is cut smells of rain and warm earth, and the light "
    "goes amber, then blue, then gone. Far off, a gate creaks shut. Above "
    "the cut grass the sky opens, star by star, wider than the day ever "
    "was, and the night, patient as soil, keeps all of it, and keeps you."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()

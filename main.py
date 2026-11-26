#!/usr/bin/env python3
"""The Dog Reviews the Mailman.

Writes one funny one-line review a dog gives the mailman, under 200
characters, to /output/entry.txt.
"""

import os
import shutil

MAX_CHARS = 199

LINE = "One star. He comes every day, drops paper, and never once lets me sniff him. Would not recommend. Will bark again."

assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line must be 1-199 non-blank chars"

OUT = os.environ.get("MAKEFUN_OUT", "/output")


def main():
    os.makedirs(OUT, exist_ok=True)
    for name in os.listdir(OUT):
        path = os.path.join(OUT, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(OUT, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

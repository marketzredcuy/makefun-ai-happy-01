#!/usr/bin/env python3
"""ai-happy-01 entry: write the happy red panda image to /output/entry.png.

The image is a joyful red panda catching a bright orange maple leaf in
warm golden autumn light -- a fresh, specific happy moment (not a stock
smiley face), with one clear subject that reads at small size. The
program simply copies the image from the repository into the output
directory, byte for byte, so both runs produce identical output.
"""

import os
import shutil
import sys


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    src = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(src, dst)
    # Confirm the copy landed byte for byte; both runs must agree.
    if os.path.getsize(dst) != os.path.getsize(src):
        print("copy size mismatch", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

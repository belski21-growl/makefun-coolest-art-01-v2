"""coolest-art-01 v2: one surrealist painting, written to entry.png.

The picture lives in art.png next to this file: a surrealist oil painting
of a colossal glass hourglass pouring golden stars into a midnight sea,
tiny fishermen catching stars with nets, a whale swimming through the
swirling starry sky. This program only copies its bytes to the output
directory, so both runs write exactly the same bytes.
"""

import os

PICTURE = "art.png"
OUT_NAME = "entry.png"
MAX_BYTES = 1048576

JPEG_MAGIC = b"\xff\xd8\xff"
PNG_MAGIC = b"\x89PNG"


def read_picture():
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, PICTURE), "rb") as handle:
        return handle.read()


def check_picture(data):
    if not data:
        raise ValueError("art.png is empty")
    if not (data.startswith(JPEG_MAGIC) or data.startswith(PNG_MAGIC)):
        raise ValueError("art.png is neither JPEG nor PNG (bad magic bytes)")
    if data.startswith(JPEG_MAGIC) and not data.endswith(b"\xff\xd9"):
        raise ValueError("art.png is a truncated JPEG (no end marker)")
    if len(data) > MAX_BYTES:
        raise ValueError("art.png is %d bytes, over the 1 MiB limit" % len(data))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    data = read_picture()
    check_picture(data)
    target = os.path.join(out_dir, OUT_NAME)
    with open(target, "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()

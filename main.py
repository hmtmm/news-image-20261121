"""Entry for make.fun bounty news-image-20261121.

Writes the finished one-image summary of 21 November 2026 world news
(entry.png, drawn for this entry) into the grader's output directory.
Pure standard library and deterministic: every run copies the same bytes.
"""
import os
import shutil
import sys
from pathlib import Path

SOURCE = Path(__file__).resolve().parent / "entry.png"
DEST_DIR = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
DEST = DEST_DIR / "entry.png"


def main() -> int:
    if not SOURCE.is_file():
        print(f"missing source image: {SOURCE}", file=sys.stderr)
        return 1
    DEST_DIR.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SOURCE, DEST)
    if DEST.stat().st_size != SOURCE.stat().st_size:
        print("copy incomplete: size mismatch", file=sys.stderr)
        return 1
    print(f"wrote {DEST} ({DEST.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

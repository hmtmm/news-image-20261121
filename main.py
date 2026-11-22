"""Copy the finished 21 November 2026 news image into the output folder.

make.fun news-image-20261121 entry. The front page (entry.png) is drawn
before the run; this program only places it where the grader looks, using
nothing beyond the Python standard library, and it always writes the same
bytes, so two runs are byte-identical.
"""

from hashlib import sha256
from os import environ
from pathlib import Path
from shutil import copyfile


def source_image() -> Path:
    return Path(__file__).resolve().parent / "entry.png"


def target_image() -> Path:
    folder = environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(folder) / "entry.png"


def digest(path: Path) -> str:
    return sha256(path.read_bytes()).hexdigest()


def run() -> int:
    src = source_image()
    dst = target_image()
    if not src.exists():
        print(f"no image beside the program: {src}")
        return 1
    if src.read_bytes()[:8] != b"\x89PNG\r\n\x1a\n":
        print("source is not a PNG image")
        return 1
    dst.parent.mkdir(parents=True, exist_ok=True)
    copyfile(src, dst)
    if digest(dst) != digest(src):
        print("copy mismatch: output bytes differ from the source")
        return 1
    print(f"entry image ready: {dst} ({dst.stat().st_size} bytes)")
    return 0


if __name__ == "__main__":
    raise SystemExit(run())

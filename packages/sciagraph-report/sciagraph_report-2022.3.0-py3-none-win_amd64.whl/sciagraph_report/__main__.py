"""Launch the actual Rust binary."""

from importlib.metadata import files
import sys
import os


def main():
    args = ["sciagraph-report"] + sys.argv[1:]
    # Find the executable in the installed package:
    for f in files("sciagraph-report"):
        if f.name.lower() in ("sciagraph-report", "sciagraph-report.exe"):
            path = f.locate()
            break
    os.execv(path, args)


if __name__ == "__main__":
    main()

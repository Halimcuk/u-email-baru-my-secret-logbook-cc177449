#!/usr/bin/env python3
"""My Secret Logbook entry: write one diary line to /output/entry.txt.

Run: python3 main.py [output_path]  (default /output/entry.txt)
"""
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent


def main() -> None:
    line = (HERE / "entry.txt").read_text(encoding="utf-8").strip()
    # Gate: /output/entry.txt must be UTF-8 text of 1 to 200 characters.
    if not 1 <= len(line) <= 200:
        raise SystemExit(f"entry must be 1-200 characters, got {len(line)}")
    out = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(line, encoding="utf-8")
    print(f"Wrote {len(line)} characters to {out}")


if __name__ == "__main__":
    main()

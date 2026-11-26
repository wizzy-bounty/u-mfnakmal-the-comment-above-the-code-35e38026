import os
from pathlib import Path

ENTRY = "// Do not touch: this works for reasons that have retired, moved abroad, and stopped answering emails."
OUTPUT_NAME = "entry.txt"
DEFAULT_OUTPUT_DIR = "/output"


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or DEFAULT_OUTPUT_DIR)
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / OUTPUT_NAME).write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()

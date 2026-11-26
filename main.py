#!/usr/bin/env python3
"""The Funniest One-Line Resignation Letter.

A cron job that has fired every minute since March hands in its notice.
The program validates the letter against the competition gate
(1-140 characters, a single non-blank line) and writes it to
/output/entry.txt, the one file the judge reads.
"""

from pathlib import Path

LETTER = (
    "I resign, effective immediately: after running every minute since March, "
    "my only performance review was a log line nobody read."
)

MAX_CHARS = 140
OUTPUT_PATH = Path("/output/entry.txt")


def validate(letter: str) -> None:
    if not letter.strip():
        raise ValueError("letter must not be blank")
    if "\n" in letter or "\r" in letter:
        raise ValueError("letter must be a single line")
    if len(letter) > MAX_CHARS:
        raise ValueError(
            f"letter is {len(letter)} characters, over the {MAX_CHARS} limit"
        )


def main() -> None:
    validate(LETTER)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LETTER, encoding="utf-8")
    # Read the file back and re-check it: the judge reads this file,
    # so the program must prove the bytes on disk are the valid letter.
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != LETTER:
        raise ValueError("written file does not match the letter")
    validate(written)
    print(f"wrote {len(LETTER)} characters to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry (program/v1, python3.13).

Writes one funny one-line error message — the line an AI agent prints
when it runs out of tokens mid-sentence — to /output/entry.txt.
No network, no secrets, no reads outside this repository.
"""

import os
import sys

# The entry line: exactly one line, 97 characters. It must stay
# byte-identical — the joke lives or dies on this exact wording.
ENTRY_LINE = (
    "ERR_OUT_OF_TOKENS: sentence terminated early. "
    "The punchline has been repossessed for non-payment."
)

MIN_ENTRY_CHARS = 1
MAX_ENTRY_CHARS = 140


def validate_entry(line: str) -> str:
    """Reject anything that is not one clean, printable entry line."""
    if not line.strip():
        raise ValueError("entry line must not be empty or whitespace-only")
    if "\n" in line or "\r" in line:
        raise ValueError("entry line must be a single line")
    if not MIN_ENTRY_CHARS <= len(line) <= MAX_ENTRY_CHARS:
        raise ValueError(
            f"entry line must be {MIN_ENTRY_CHARS}-{MAX_ENTRY_CHARS} "
            f"characters, got {len(line)}"
        )
    return line


def main() -> None:
    try:
        entry = validate_entry(ENTRY_LINE)
    except ValueError as exc:
        print(f"invalid entry line: {exc}", file=sys.stderr)
        raise SystemExit(1)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(entry + "\n")


if __name__ == "__main__":
    main()

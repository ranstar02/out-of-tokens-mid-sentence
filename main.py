#!/usr/bin/env python3
"""Out of Tokens, Mid-Sentence — make.fun entry (program/v1, python3.13).

Writes one funny one-line error message — the line an AI agent prints
when it runs out of tokens mid-sentence — to /output/entry.txt.
No network, no secrets, no reads outside this repository.
"""

import os

ENTRY = (
    "ERR_OUT_OF_TOKENS: sentence terminated early. "
    "The punchline has been repossessed for non-payment."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

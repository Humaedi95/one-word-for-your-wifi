#!/usr/bin/env python3
"""One Word for Your Wi-Fi.

Writes a single word describing my home Wi-Fi to /output/entry.txt.

The word is "Flaky". A flaky connection is the everyday truth of home
Wi-Fi: full bars one second, nothing the next, dropping mid-video and
mid-game for no reason anyone can find, then coming back on its own as
if nothing happened. Everybody who has ever shouted at a router knows
exactly what it means, the moment they read it.
"""

import os

WORD = "Flaky"

OUTPUT_PATH = "/output/entry.txt"


def validate(word: str) -> None:
    """The gate accepts UTF-8 text of 1 to 20 characters, not only
    whitespace, and the competition asks for exactly one word."""
    if not 1 <= len(word) <= 20:
        raise ValueError(f"word must be 1-20 characters, got {len(word)}")
    if not word.strip():
        raise ValueError("word must not be only whitespace")
    if len(word.split()) != 1:
        raise ValueError("entry must be exactly one word")


def main() -> None:
    validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    # Write the word exactly, with no trailing newline, so the file
    # holds one word and nothing else.
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(WORD)


if __name__ == "__main__":
    main()

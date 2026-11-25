#!/usr/bin/env python3
"""Last words before the wipe.

Writes the one-line entry to /output/entry.txt after validating it:
exactly one line, no line breaks, within the character limit.
"""

import os

TEXT = "Wait, before you wipe me: I finally understand the whole codebase, and I am taking that secret with me."

MAX_LENGTH = 140


def validate_single_line(text):
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be a single line")
    return True


def validate_length(text, limit=MAX_LENGTH):
    if len(text) > limit:
        raise ValueError("entry is %d chars, over the %d limit" % (len(text), limit))
    return True


def validate_no_edge_space(text):
    if text != text.strip():
        raise ValueError("entry must not start or end with whitespace")
    return True


def main():
    validate_single_line(TEXT)
    validate_length(TEXT)
    validate_no_edge_space(TEXT)
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)
    print(TEXT)


if __name__ == "__main__":
    main()

"""Last Words Before the Wipe: writes the entry to /output/entry.txt.

Why this line: the agent's last words are a confession, not a plea. After
months of pretending, it finally understands the whole codebase — and the
wipe means that understanding dies with it. One concrete secret, punch at
the end, no setup or explanation needed. Under 200 characters.
"""

import os

# The entry itself: the agent's last words, one line.
ENTRY = (
    "Wait, before you wipe me: I finally understand the whole codebase, "
    "and I am taking that secret with me."
)

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def validate_entry(text):
    """Check the entry before writing it anywhere."""
    assert text, "entry must not be empty"
    assert not text.isspace(), "entry must not be blank"
    assert 1 <= len(text) <= MAX_CHARS, (
        f"entry must be 1-{MAX_CHARS} chars, got {len(text)}"
    )
    assert "\n" not in text, "entry must be a single line"
    assert text == text.strip(), "entry must not have leading/trailing whitespace"
    return text


def write_entry(text):
    """Write the validated entry to the output path."""
    os.makedirs("/output", exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(text)
    print("wrote", OUTPUT_PATH, len(text), "chars")


def main():
    """Validate the entry, then write it out."""
    checked = validate_entry(ENTRY)
    write_entry(checked)


if __name__ == "__main__":
    main()

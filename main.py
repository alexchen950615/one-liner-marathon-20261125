#!/usr/bin/env python3
"""One-Liner Marathon entry: write a single one-line comedy joke to /output/entry.txt."""

JOKE = "I told my calendar I needed a break, so it scheduled one \u2014 for next year, in a meeting titled 'Rest (Optional).'"


def main() -> None:
    # Competition gate: entry must be a single line of 1-280 characters.
    assert 1 <= len(JOKE) <= 280, f"entry length {len(JOKE)} out of range"
    assert "\n" not in JOKE, "entry must be a single line"
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

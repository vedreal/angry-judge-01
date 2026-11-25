#!/usr/bin/env python3
"""Angry Judge entry: write one short rant to /output/entry.txt.

The rant is about the self-checkout machine: a specific, concrete everyday
annoyance, told in a few economical sentences with the punchline landing
on the human cost (the attendant has seen me cry).
"""

import os

RANT = (
    "The self-checkout machine has accused me of stealing my own groceries "
    "three times today. 'Unexpected item in the bagging area.' The unexpected "
    "item is the bag I brought from home, which it told me to bring. I am on "
    "a first-name basis with the attendant now, and she has seen me cry."
)


def main():
    text = RANT.strip()
    assert 1 <= len(text) <= 400, f"rant must be 1-400 chars, got {len(text)}"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text)


if __name__ == "__main__":
    main()

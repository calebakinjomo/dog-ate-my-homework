#!/usr/bin/env python3
"""The Dog Ate My Homework: Funniest Excuse — make.fun bounty entry.

Writes one line (under 200 characters), in the dog's own voice, to
/output/entry.txt and prints it to stdout. The dog pleads its case:
the homework had it coming.
"""

import os

EXCUSE = "I ate it because it was the only thing you loved more than me, and somebody had to teach it a lesson."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)
    print(EXCUSE)


if __name__ == "__main__":
    main()

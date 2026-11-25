#!/usr/bin/env python3
"""The GPS Swears It Was a Shortcut — variant B.

Writes the GPS's excuse to /output/entry.txt first, then (best effort)
a copy next to this script. The grader sandbox is read-only, so the
repo-root copy must never crash the run.
"""

import os

ENTRY = "The lake IS a shortcut \u2014 twelve minutes faster, and your car only sank a little. Recalculating my apology now."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)
    try:
        here = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(here, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError:
        pass


if __name__ == "__main__":
    main()

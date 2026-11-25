"""One-line review of the most boring everyday object.

Writes the entry text to ``$MAKEFUN_OUTPUT_DIR/entry.txt``.
The entry is a single funny, true review of a tea towel: the object
whose whole job is drying things is somehow always the dampest thing
in the kitchen. The dullness is the joke.
"""

import os

ENTRY = "This tea towel has dried a thousand dishes and is somehow always the dampest thing in the kitchen."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(ENTRY)


if __name__ == "__main__":
    main()

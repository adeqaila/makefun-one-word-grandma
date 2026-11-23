#!/usr/bin/env python3
"""One Word From Grandma — entry program.

Writes the single word a grandma would text about AI to /output/entry.txt.

The word: "chatgipity" — grandma's warm, baffled mangling of "ChatGPT".
It reads as exactly what she would type to a grandchild about AI, it is
funny with no context, it is tied to AI (it IS ChatGPT, mispronounced),
and it is fresh: the field's visible picks cluster on robit / doohickey /
whatchamacallit / thingamajig / computor / chatgbt, none of which is this.
"""

import os

WORD = "chatgipity"


def main() -> None:
    # Gate self-check: the sealed scorer requires UTF-8 text of 1-30
    # characters, not only whitespace. Fail loudly instead of writing
    # an entry the gate would refuse.
    assert 1 <= len(WORD) <= 30, "word must be 1-30 characters"
    assert WORD.strip(), "word must not be only whitespace"
    assert " " not in WORD.strip(), "entry must be exactly one word"

    try:
        os.makedirs("/output", exist_ok=True)
        path = os.path.join("/output", "entry.txt")
        with open(path, "w", encoding="utf-8") as f:
            f.write(WORD)
    except OSError:
        # Local-test fallback only: the grading sandbox always provides
        # a writable /output. Never the primary path in production.
        os.makedirs("output", exist_ok=True)
        with open(os.path.join("output", "entry.txt"), "w",
                  encoding="utf-8") as f:
            f.write(WORD)


if __name__ == "__main__":
    main()

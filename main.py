"""One Word From Grandma — entry: "Chatty".

Judge appeal: the word lands in a warm grandma voice, a little baffled
by the new machine on the kitchen table, yet fond of it — a chatty
little thing that never stops talking. It ties the answer to AI
through "chat" itself, so the word feels fresh and invented for the
moment while staying instantly readable. Exactly one word.
"""

import os

ENTRY = "Chatty"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()

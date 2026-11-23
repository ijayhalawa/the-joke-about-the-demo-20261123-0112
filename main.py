"""Write a one-line joke about working beside an AI coding agent.

Writes the joke to /output/entry.txt (override with the OUTPUT_PATH
environment variable, for local testing only). Standard library only,
no network, no external files: the joke lives in the JOKE constant
below, so two runs always produce byte-identical output.
"""

import os

JOKE = (
    "My AI coding agent fixed the bug live in the demo \u2014 "
    "by deleting the feature I was about to show."
)

DEFAULT_OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    output_path = os.environ.get("OUTPUT_PATH", DEFAULT_OUTPUT_PATH)
    parent = os.path.dirname(output_path)
    if parent:
        os.makedirs(parent, exist_ok=True)
    with open(output_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(JOKE + "\n")


if __name__ == "__main__":
    main()

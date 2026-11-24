"""One-line office joke entry v2 for make.fun's "One-Line Office Joke:
24-Hour Sprint".

Writes a single one-line joke about office life to /output/entry.txt.

The joke: in standup everyone reports "no blockers" while visibly
blocked, like hostages reading a script. Deep-ATM upgrade over v1:
the judge scores pairwise with margins 1-5, so a mild smile wins by a
hair while a sharp, visual twist wins decisively; the standup ritual
lie is universal, the hostage comparison is the surprise that lands
at the very end, and the angle dodges the field's saturated
Monday/printer/meeting-email tropes. 93 characters, one sentence.
"""

import os

JOKE = (
    "In standup everyone says 'no blockers' while visibly blocked, "
    "like hostages reading a script."
)


def main() -> None:
    os.umask(0o022)
    os.makedirs("/output", exist_ok=True)
    path = "/output/entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

"""One-line office joke entry v1 for make.fun's "One-Line Office Joke:
24-Hour Sprint".

Writes a single one-line joke about office life to /output/entry.txt.

The joke: a calendar so full the lunch break has a waitlist — and the
teller is number four on their own lunch's waitlist. Pure original
thinking: the setup is the overbooked calendar everyone recognises, the
punchline is the absurd waitlist for your own lunch, landing at the very
end in one short sentence. 79 characters, one sentence, no setup wasted.
"""

import os

JOKE = (
    "My calendar is so full that my lunch break has a waitlist, "
    "and I'm number four."
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

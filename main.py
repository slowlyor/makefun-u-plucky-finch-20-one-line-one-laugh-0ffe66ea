"""One Line, One Laugh — make.fun entry.

Writes a single funny line (at most 200 characters) to /output/entry.txt
and prints exactly that one line to stdout. Deterministic: same output
on every run. Standard library only.
"""

import os

LINE = "My smartwatch reviewed my sleep, sighed, and showed me a pie chart of my 3 a.m. snack decisions titled 'cry for help'."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()

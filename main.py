import os

TEXT = (
    "Dear all, I resign to spend more time with my family, "
    "by which I mean the houseplants who have never scheduled "
    "a meeting that could have been an email."
)


def main() -> None:
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(TEXT + "\n")


if __name__ == "__main__":
    main()

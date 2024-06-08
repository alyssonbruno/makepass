DEFAULT_LANG_FILE = "./langs/br-utf8.txt"
WORD_MIN_SIZE = 4


def clear_file(file: str = DEFAULT_LANG_FILE, min_size=WORD_MIN_SIZE) -> list[str]:
    result : list[str] = list()
    with open(file, "r") as f:
        for line in f:
            if len(line) >= 4:
                result.append(line.strip())
    return result

if __name__ == "__main__":
    from pathlib import Path
    import argparse

    parser = argparse.ArgumentParser(description="Clear language file")
    parser.add_argument("file", type=Path, help=f"File to clear, default is {DEFAULT_LANG_FILE}", nargs=1, default=DEFAULT_LANG_FILE)
    parser.add_argument("-m", "--min", type=int, help=f"Minimum word size, default is {WORD_MIN_SIZE}", required=False, default=WORD_MIN_SIZE)
    parser.add_argument("-o", "--output", type=str, help="Output file")
    args = parser.parse_args()
    file: Path = args.file.pop()
    if not file.exists():
        print(f"File {args.file} not found")
        exit(1)
    words = clear_file(file=file,min_size=args.min)
    if args.output:
        with open(args.output, "w") as f:
            for word in words:
                f.write(f"{word}\n")
    else:
        with open("lang.txt", "w") as f:
            for word in words:
                f.write(f"{word}\n")
    print(len(words))
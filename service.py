import random

DEFAULT_COUNT = 4
DEFAULT_LANG_FILE_PATH = "./langs/{lang}.txt"
DEFAULT_LANG="pt_br"

LANGS_DICT = {}
def read_lang_file(lang: str = DEFAULT_LANG) -> list[str]:
    if lang in LANGS_DICT:
        return LANGS_DICT[lang]

    result : list[str] = list()
    with open(DEFAULT_LANG_FILE_PATH.format(lang=lang), "r") as f:
        for line in f:
            result.append(line.strip())
    LANGS_DICT[lang] = result
    return result
def make_password(count: int = DEFAULT_COUNT, lang: str =DEFAULT_LANG, sep: str = " ") -> str:
    return sep.join(random.choices(read_lang_file(lang), k=count))

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Make password")
    parser.add_argument("-c", "--count", type=int, help=f"Number of words, default is {DEFAULT_COUNT}", required=False, default=DEFAULT_COUNT)
    parser.add_argument("-l", "--lang", type=str, help=f"Language, default is {DEFAULT_LANG}", required=False, default=DEFAULT_LANG)
    parser.add_argument("-s", "--sep", type=str, help="Separator", required=False, default=" ")
    args = parser.parse_args()
    print(make_password(count=args.count, lang=args.lang, sep=args.sep))

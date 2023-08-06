# fmt: off
T = {"а": "a", "б": "b", "в": "v", "г": "g", "д": "d", "е": "e",
     "ё": "e", "ж": "zh", "з": "z", "и": "i", "й": "i", "к": "k",
     "л": "l", "м": "m", "н": "n", "о": "o", "п": "p", "р": "r",
     "с": "s", "т": "t", "у": "u", "ф": "f", "х": "h", "ц": "c",
     "ч": "cz", "ш": "sh", "щ": "scz", "ъ": "", "ы": "y", "ь": "",
     "э": "e", "ю": "u", "я": "ja"}

FORBIDDEN_SYMBOLS = ["\\", "/", ":", "*", "?", "\"", "<", ">", "|"]


# fmt: off


def transliteration(sequence: str) -> str:
    new_txt = ""
    for i in sequence:
        if i in FORBIDDEN_SYMBOLS:
            continue
        lower_i = i.lower()
        if lower_i in T:
            if i.istitle():
                new_txt += T[lower_i].title()
            else:
                new_txt += T[lower_i]
        else:
            if i == " ":
                new_txt += "_"
            else:
                new_txt += i
    return new_txt

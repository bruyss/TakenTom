#! python3

INVOER = [("Toblerone", "Bern"), ("Coca-Cola", "Ocala")]


def surround_char(s: str, i: int, c1: str, c2: str):
    """
    Surround the character at index i of string s with the characters c1 & c2
    Example: surrounc("Hello", 1, "(", ")") -> H(e)llo

    Args:
        s (str): Input string
        i (int): Index of character to surround
        c1 (str): First surrounding character
        c2 (str): Second surrounding character

    Returns:
        str: Output string
    """
    return s[:i] + c1 + s[i] + c2 + s[i+1:]


def word_find(word: str, search: str) -> str:
    start_idx = 0
    found_idxs = []
    for c in search.lower():
        start_idx = word.lower().find(c, start_idx)
        found_idxs.append(start_idx)
    print(found_idxs)

    ret = word
    for i in reversed(found_idxs):
        ret = surround_char(ret, i, "[", "]")

    ret = ret.replace("][", "")

    return ret



def main():
    for t in INVOER:
        merknaam, stad = t
        ans = word_find(merknaam, stad)
        print(ans)

if __name__ == "__main__":
    main()

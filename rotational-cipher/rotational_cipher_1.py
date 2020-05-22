def rotate(text, key):
    res = []
    for ch in text:
        if ch.isalpha() and ch.upper() == ch:
            x = chr((ord(ch) - 64 + key) % 26 + 64)
            res.append(x)
        elif ch.isalpha() and ch.lower() == ch:
            x = chr((ord(ch) - 97 + key) % 26 + 97)
            res.append(x)
        elif not ch.isalpha():
            res.append(ch)
    return ''.join(res)


q = rotate("a", 0), "a"
q
q = rotate("a", 1), "b"
q
q = rotate("a", 26), "a"
q
q = rotate("m", 13), "z"
q
q = rotate("n", 13), "a"
q
q = rotate("OMG", 5)
#     "TRL"
q
q = rotate("O M G", 5)
q
#     "T R L"
q = rotate("Testing 1 2 3 testing", 4)
q
#     "Xiwxmrk 1 2 3 xiwxmrk"
q = rotate("Let's eat, Grandma!", 21)
q
#     "Gzo'n zvo, Bmviyhv!"
q = rotate("The quick brown fox jumps over the lazy dog.", 13)
q
#     "Gur dhvpx oebja sbk whzcf bire gur ynml qbt.",

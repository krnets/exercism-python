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
def rotate(text, key):
    cipher = ''
    for ch in text:
        if ch.isalpha() and ch.upper() == ch:
            cipher += chr((ord(ch) - 64 + key) % 26 + 64)
        elif ch.isalpha() and ch.lower() == ch:
            cipher += chr((ord(ch) - 97 + key) % 26 + 97)
        elif not ch.isalpha():
            cipher += ch
    return cipher
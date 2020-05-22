from string import ascii_lowercase as abc


def rotate(text, key):
    cipher = abc[key:] + abc[:key]
    table = str.maketrans(abc + abc.upper(), cipher + cipher.upper())
    return text.translate(table)

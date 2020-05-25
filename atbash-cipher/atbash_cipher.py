from string import ascii_lowercase as abc
from textwrap import wrap
from re import sub

CIPHER = str.maketrans(abc, abc[::-1])


def encode(plain_text):
    s = sub(r'\W', '', plain_text.lower()).translate(CIPHER)
    return ' '.join(wrap(s, 5))


def decode(ciphered_text):
    return ''.join(encode(ciphered_text).split())

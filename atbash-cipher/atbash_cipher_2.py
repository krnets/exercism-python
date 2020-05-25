from string import ascii_lowercase as abc
from re import sub


def encode(plain_text):
    s = sub(r'[\W]', '', plain_text.lower()).translate(str.maketrans(abc, abc[::-1]))
    return ' '.join(''.join(s[i:i+5]) for i in range(0, len(s), 5))


def decode(ciphered_text):
    return ''.join(encode(ciphered_text).split())
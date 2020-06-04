import re
from math import sqrt, ceil
from itertools import zip_longest


def transpose_and_flatten(matrix):
    return ' '.join(map(''.join, zip_longest(*matrix, fillvalue='')))


def cipher_text(plain_text):
    msg = re.sub(r'\W', '', plain_text.lower())
    size = ceil(sqrt(len(msg)))
    square = zip_longest(*[iter(msg)] * size, fillvalue=' ')
    return transpose_and_flatten(square)
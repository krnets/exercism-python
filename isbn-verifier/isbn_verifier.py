import re


def is_valid(isbn):
    if not isbn or not re.match(r'\d|X', isbn[-1]):
        return False
    isbn = re.sub('\D', '', isbn[:-1]) + isbn[-1]
    if len(isbn) != 10:
        return False
    mult_idx = [10 if isbn[10-i] == 'X' else int(isbn[10-i]) * i for i in range(10, 0, -1)]
    return sum(mult_idx) % 11 == 0
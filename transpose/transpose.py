from itertools import zip_longest


def transpose(lines):
    t = zip_longest(*lines.splitlines(), fillvalue='-')
    return '\n'.join(''.join(row).rstrip('-') for row in t).replace('-', ' ')
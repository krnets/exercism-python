import re


def decode(string):
    return re.sub(r'(\d+)(\D)', lambda m: int(m.group(1)) * m.group(2), string)


def encode(string):
    return re.sub(r'(\D)\1+', lambda m: str(len(m.group())) + m.group()[0], string)


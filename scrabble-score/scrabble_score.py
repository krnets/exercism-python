letter_values = {}

POINTS = {
    "AEIOULNRST": 1,
    "DG": 2,
    "BCMP": 3,
    "FHVWY": 4,
    "K": 5,
    "JX": 8,
    "QZ": 10}

for k, v in POINTS.items():
    letter_values.update({x: v for x in k})


def score(word):
    return sum(letter_values[ch] for ch in word.upper())

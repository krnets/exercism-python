from string import ascii_uppercase

ABC = set(ascii_uppercase)

def is_pangram(sentence):
    return ABC.issubset(sentence.upper())
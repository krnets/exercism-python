from string import ascii_lowercase

def is_pangram(sentence):
    s = filter(str.isalpha, sentence.lower())
    return sorted(set(s)) == list(ascii_lowercase)
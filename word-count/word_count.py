from collections import Counter
import re

def count_words(sentence):
    words = re.findall(r"[a-z\d]+(?:'\w)?", sentence.lower())
    return Counter(words)
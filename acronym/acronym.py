import re

def abbreviate(words):
    words = re.sub('-|_', ' ', words)
    return ''.join(w[0].upper() for w in words.split())
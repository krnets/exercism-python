import re

RE = re.compile(r'^(x(?!r)|y(?!t)|[^aeiouxqy]*(?:qu?)?)(.+)$')


def translate(phrase):
    return ' '.join(map(translate_word, phrase.split()))


def translate_word(word):
    return RE.sub(lambda m: '{1}{0}ay'.format(*m.groups()), word)

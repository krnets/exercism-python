def find_anagrams(word, candidates):
    is_anagram = lambda x: sorted(x.lower()) == sorted(word.lower())
    is_not_same_word = lambda x: x.lower() != word.lower()
    filters = (is_anagram, is_not_same_word)
    return list(filter(lambda x: all(f(x) for f in filters), candidates))


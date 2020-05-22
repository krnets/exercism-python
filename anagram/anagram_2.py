def find_anagrams(word, candidates):
    return [x for x in candidates if x.lower() != word.lower() and sorted(x.lower()) == sorted(word.lower())]

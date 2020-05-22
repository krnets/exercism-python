def find_anagrams(word, candidates):
    # return [x for x in candidates if sorted(x.lower()) == sorted(word.lower()) and x.lower() != word.lower()]
    # sorted(x.lower()) == sorted(word.lower()) and 
    # return [x for x in candidates if x.lower() != word.lower() and sorted(x.lower()) == sorted(word.lower())]
    pred1 = lambda x: x.lower() != word.lower()
    pred2 = lambda x: sorted(x.lower()) == sorted(word.lower())
    # return list(filter(pred2, candidates))
    filters = (pred1, pred2)
    return list(filter(lambda x: all(f(x) for f in filters), candidates))


candidates = ["stream", "pigeon", "maters"]
q = find_anagrams("master", candidates)
q
#      ["stream", "maters"]

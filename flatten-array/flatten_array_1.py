def flatten(iterable):
    res = []
    for x in iterable:
        if isinstance(x, list):
            res.extend(flatten(x))
        else:
            if x is not None:
                res.append(x)
    return res


inputs = [0, 2, [[2, 3], 8, 100, 4, [[[50]]]], -2]
q = flatten(inputs)
q
#      [0, 2, 2, 3, 8, 100, 4, 50, -2]

inputs = [1, [2, [[3]], [4, [[5]]], 6, 7], 8]
q = flatten(inputs)
q
#      [1, 2, 3, 4, 5, 6, 7, 8]

inputs = [0, 2, [[2, 3], 8, [[100]], None, [[None]]], -2]
q = flatten(inputs)
q
#      [0, 2, 2, 3, 8, 100, -2]

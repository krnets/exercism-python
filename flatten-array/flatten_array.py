from collections.abc import Iterable


def flatten(iterable):
    res = []
    for x in iterable:
        if isinstance(x, Iterable):
            res.extend(flatten(x))
        elif x is not None:
            res.append(x)
    return res

from operator import mul
from functools import reduce


def largest_product(series, size):
    if not size:
        return 1
    elif size < 0:
        raise ValueError('size cannot be negative')
    return max(reduce(mul, map(int, series[i:i+size])) for i in range(len(series)-size+1))


q = largest_product("29", 2), 18
q
q = largest_product("0123456789", 2), 72
q
q = largest_product("576802143", 2), 48
q
q = largest_product("0123456789", 3), 504
q
q = largest_product("1027839564", 3), 270
q
q = largest_product("0123456789", 5), 15120
q

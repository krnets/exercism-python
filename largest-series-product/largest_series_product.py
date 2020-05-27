from operator import mul
from functools import reduce


def largest_product(series, size):
    if size < 0:
        raise ValueError('size cannot be negative')
    return max(reduce(mul, map(int, series[i:i+size]), 1) for i in range(len(series)-size+1))

from itertools import chain
from math import sqrt


def factors(value):
    primes = []
    for divisor in chain([2], range(3, int(sqrt(value))+1, 2)):
        while value % divisor == 0:
            primes.append(divisor)
            value /= divisor
    if value > 1:
        primes.append(value)
    return primes

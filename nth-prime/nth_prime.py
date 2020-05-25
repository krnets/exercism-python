from math import log


def prime(number):
    primes = primes_generator(int(2 + 1.2 * number * log(number)))
    return list(primes)[number-1]


def primes_generator(n):
    yield 2
    composite = set()
    for i in range(3, n+1, 2):
        if i not in composite:
            composite.update(range(i*i, n+1, i))
            yield i

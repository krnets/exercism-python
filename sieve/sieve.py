from math import sqrt


def primes(limit):
    if limit < 2:
        return []
    sieve = [True] * (limit+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(sqrt(limit))+1):
        if sieve[i]:
            for j in range(2 * i, limit+1, i):
                sieve[j] = False
    return [i for i, x in enumerate(sieve) if x]
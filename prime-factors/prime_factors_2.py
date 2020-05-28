from math import sqrt


def factors(value):
    primes = []
    for divisor in range(2, int(sqrt(value)) + 1):
        while value % divisor == 0:
            value /= divisor
            primes.append(divisor)
    if value > 1:
        primes.append(value)
    return primes
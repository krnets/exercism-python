from functools import reduce


def square(number):
    if number > 64:
        raise ValueError('number should be between 1 and 64')
    return 1 << number-1


# def total():
#     res = []
#     for i in range(1, 65):
#         res.append(square(i))
#     return sum(res)

# def total():
#     return sum(square(i) for i in range(1, 65))

def total():
    return reduce(lambda x, y: x + square(y), range(1, 65))


q = square(1), 1
q
q = square(2), 2
q
q = square(3), 4
q
q = square(4), 8
q
q = square(16), 32768
q
q = square(32), 2147483648
q
q = square(64), 9223372036854775808
q


q = total(), 18446744073709551615
q

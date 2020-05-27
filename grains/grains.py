def square(number):
    if number > 64:
        raise ValueError('number should be between 1 and 64')
    return 1 << number-1


def total():
    return sum(square(i) for i in range(1, 65))

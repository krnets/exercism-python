def steps(number):
    if number < 1:
        raise ValueError("number must be positive")

    count = 0

    while number != 1:
        if number % 2 == 0:
            number /= 2
            count += 1
        else:
            number = 3 * number + 1
            count += 1

    return count


q = steps(1), 0
q
q = steps(16), 4
q
q = steps(12), 9
q
q = steps(1000000), 152
q

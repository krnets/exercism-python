ROMAN = 'M CM D CD C XC L XL X IX V IV I'.split()
NUMS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


def roman(number):
    out = ''
    for r, n in zip(ROMAN, NUMS):
        x, number = divmod(number, n)
        out += r * x
    return out
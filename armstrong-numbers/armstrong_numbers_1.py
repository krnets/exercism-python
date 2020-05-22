def is_armstrong_number(number):
    n = str(number)
    n_digits = len(n)
    return sum(int(x) ** n_digits for x in n) == number

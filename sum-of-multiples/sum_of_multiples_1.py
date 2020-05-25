def sum_of_multiples(limit, multiples):
    res = set()
    for x in filter(lambda x: x, multiples):
        temp = set(y for y in range(x, limit) if y % x == 0)
        res.update(temp)
    return sum(res)

    # multiples = filter(lambda x: x, multiples)
    # for x in multiples:

q = sum_of_multiples(1, [0]), 0
q
q = sum_of_multiples(4, [3, 0]), 3
q
q = sum_of_multiples(10000, [2, 3, 5, 7, 11]), 39614537
q
q = sum_of_multiples(20,  [3, 5])
q
# we get 3, 5, 6, 9, 10, 12, 15, and 18.
# The sum of these multiples is 78.

q = sum_of_multiples(1, [3, 5]), 0
q
q = sum_of_multiples(4, [3, 5]), 3
q
q = sum_of_multiples(7, [3]), 9
q
q = sum_of_multiples(10, [3, 5]), 23
q
q = sum_of_multiples(100, [3, 5]), 2318
q
q = sum_of_multiples(1000, [3, 5]), 233168
q
q = sum_of_multiples(20, [7, 13, 17]), 51
q
q = sum_of_multiples(15, [4, 6]), 30
q
q = sum_of_multiples(150, [5, 6, 8]), 4419
q
q = sum_of_multiples(51, [5, 25]), 275
q
q = sum_of_multiples(10000, [43, 47]), 2203160
q
q = sum_of_multiples(100, [1]), 4950
q
q = sum_of_multiples(10000, []), 0
q

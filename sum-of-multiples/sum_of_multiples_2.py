# def sum_of_multiples(limit, multiples):
#     res = set()
#     for x in filter(lambda x: x, multiples):
#         temp = set(y for y in range(x, limit) if x and y % x == 0)
#         res.update(temp)
#     return sum(res)

def sum_of_multiples(limit, multiples):
    return sum(x for mult in multiples if mult for x in range(mult, limit, mult))


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
# q = sum_of_multiples(1000, [3, 5]), 233168
# q
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

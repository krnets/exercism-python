def factors(value, fctr=2):
    if value < fctr:
        return []
    if value % fctr == 0:
        return [fctr] + factors(value / fctr, 2)
    return factors(value, fctr + 1)


q = factors(2)  # [2]
q
q = factors(9)  # [3, 3]
q
q = factors(8)  # [2, 2, 2]
q
q = factors(12)  # [2, 2, 3]
q
q = factors(901255), [5, 17, 23, 461]
q
q = factors(93819012551), [11, 9539, 894119]
q

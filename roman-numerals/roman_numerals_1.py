ROMAN = 'M CM D CD C XC L XL X IX V IV I'.split()
NUMS = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]


def roman(number):
    result = ''
    i = 0
    while number > 0:
        if number - NUMS[i] >= 0:
            result += ROMAN[i]
            number -= NUMS[i]
        else:
            i += 1
    return result


q = roman(1024), "MXXIV"
q
q = roman(1), "I"
q
q = roman(2), "II"
q
q = roman(3), "III"
q
q = roman(4), "IV"
q
q = roman(5), "V"
q
q = roman(6), "VI"
q
q = roman(9), "IX"
q
q = roman(27), "XXVII"
q
q = roman(48), "XLVIII"
q
q = roman(49), "XLIX"
q
q = roman(59), "LIX"
q
q = roman(93), "XCIII"
q
q = roman(141), "CXLI"
q
q = roman(163), "CLXIII"
q
q = roman(402), "CDII"
q
q = roman(575), "DLXXV"
q
q = roman(911), "CMXI"
q
q = roman(1024), "MXXIV"
q
q = roman(3000), "MMM"
q

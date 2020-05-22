def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

# on every year that is evenly divisible by 4
#   except every year that is evenly divisible by 100
#     unless the year is also evenly divisible by 400


q = leap_year(1960), True
q

q = leap_year(2000), True
q

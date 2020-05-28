def verse(n):
    if n == 0:
        return ('No more bottles of beer on the wall, no more bottles of beer.',
                'Go to the store and buy some more, 99 bottles of beer on the wall.')
    # elif n == 1:
    #     return ('1 bottle of beer on the wall, 1 bottle of beer.',
    #             'Take it down and pass it around, no more bottles of beer on the wall.')
    # elif n == 2:
    #     return ('2 bottles of beer on the wall, 2 bottles of beer.',
    #             'Take one down and pass it around, 1 bottle of beer on the wall.')

    elif n <= 2:
        return (f"{n} bottle{'s' if n > 1 else ''} of beer on the wall, {n} bottle{'s' if n > 1 else ''} of beer.",
                f"Take {'one' if n > 1 else 'it'} down and pass it around, {'no more' if n == 1 else n-1} bottle{'s' if n == 1 else ''} of beer on the wall.")

    return (f'{n} bottles of beer on the wall, {n} bottles of beer.',
            f'Take one down and pass it around, {n-1} bottles of beer on the wall.')

    # return (f"{n} bottle{'s' if n > 1 else ''} of beer on the wall, {n} bottle{'s' if n > 1 else ''} of beer.",
    #         f"Take {'one' if n > 1 else 'it'} down and pass it around, {'no more' if n == 1 else n-1} bottle{'s' if n == 1 else ''} of beer on the wall.")


def recite(start, take=1):
    result = []
    for i in range(start, start - take, -1):
        v1, v2 = verse(i)
        result.extend([v1, v2, ''])
    return result[:-1]


q = recite(start=99, take=100)
q
q = recite(start=99)
q
# ["99 bottles of beer on the wall, 99 bottles of beer.", "Take one down and pass it around, 98 bottles of beer on the wall.",]

q = recite(start=2)
q
# ["2 bottles of beer on the wall, 2 bottles of beer.", "Take one down and pass it around, 1 bottle of beer on the wall.",]

q = recite(start=99, take=2)
q
q = len([
    "99 bottles of beer on the wall, 99 bottles of beer.",
    "Take one down and pass it around, 98 bottles of beer on the wall.",
    "",
    "98 bottles of beer on the wall, 98 bottles of beer.",
    "Take one down and pass it around, 97 bottles of beer on the wall.",
])
q

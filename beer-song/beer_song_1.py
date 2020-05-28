def recite(start, take=1):
    res = []
    for i in range(start, start-take, -1):
        res.append(f"{i} bottles of beer on the wall, {i} bottles of beer.")
        res.append(
            f"Take one down and pass it around, {i-1 if i-1 > 0 else 'no more'} bottles of beer on the wall.")
        res.append('')
    # return [x for x in res if x]
    if i == 0:
        res.append(
            "No more bottles of beer on the wall, no more bottles of beer.")
        res.append(
            "Go to the store and buy some more, 99 bottles of beer on the wall.")
        return res
    else:
        return res[:-1]


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

GIFTS = [
    'Partridge in a Pear Tree',
    'Turtle Doves',
    'French Hens',
    'Calling Birds',
    'Gold Rings',
    'Geese-a-Laying',
    'Swans-a-Swimming',
    'Maids-a-Milking',
    'Ladies Dancing',
    'Lords-a-Leaping',
    'Pipers Piping',
    'Drummers Drumming'
]

DAYS = 'first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth'.split()
COUNT = 'a two three four five six seven eight nine ten eleven twelve'.split()


def recite(start_verse, end_verse):
    song = []
    lines = [f'{COUNT[i]} {GIFTS[i]}, ' for i in range(len(GIFTS))][::-1]
    for i in range(start_verse, end_verse+1):
        if i == 1:
            lines[11] = lines[11][:-2] + '.'
        else:
            lines[11] = 'and a Partridge in a Pear Tree.'
        intro = f'On the {DAYS[i-1]} day of Christmas my true love gave to me: '
        song.append(intro + ''.join(x for x in lines[-i:]))
    return song


q = recite(1, 1)
q
#       "On the first day of Christmas my true love gave to me: a Partridge in a Pear Tree."


q = recite(2, 2)
q
#       "On the second day of Christmas my true love gave to me: two Turtle Doves, and a Partridge in a Pear Tree."

q = recite(3, 3)
q
#       "On the third day of Christmas my true love gave to me: three French Hens, two Turtle Doves, and a Partridge in a Pear Tree."

q = recite(4, 4)
q
#       "On the fourth day of Christmas my true love gave to me: four Calling Birds, three French Hens, two Turtle Doves, ", "and a Partridge in a Pear Tree."

q = recite(5, 5)
q
# "On the fifth day of Christmas my true love gave to me: ", "five Gold Rings, ", "four Calling Birds, ", "three French Hens, ", "two Turtle Doves, ", "and a Partridge in a Pear Tree."

q = recite(6, 6)
q
# "On the sixth day of Christmas my true love gave to me: ", "six Geese-a-Laying, ", "five Gold Rings, ", "four Calling Birds, ", "three French Hens, ", "two Turtle Doves, ", "and a Partridge in a Pear Tree."

q = recite(7, 7)
q
# "On the seventh day of Christmas my true love gave to me: "
# "seven Swans-a-Swimming, "
# "six Geese-a-Laying, "
# "five Gold Rings, "
# "four Calling Birds, "
# "three French Hens, "
# "two Turtle Doves, "
# "and a Partridge in a Pear Tree."

q = recite(8, 8)
q
# "On the eighth day of Christmas my true love gave to me: "
# "eight Maids-a-Milking, "
# "seven Swans-a-Swimming, "
# "six Geese-a-Laying, "
# "five Gold Rings, "
# "four Calling Birds, "
# "three French Hens, "
# "two Turtle Doves, "
# "and a Partridge in a Pear Tree."

q = recite(9, 9)
q
# "On the ninth day of Christmas my true love gave to me: "
# "nine Ladies Dancing, "
# "eight Maids-a-Milking, "
# "seven Swans-a-Swimming, "
# "six Geese-a-Laying, "
# "five Gold Rings, "
# "four Calling Birds, "
# "three French Hens, "
# "two Turtle Doves, "
# "and a Partridge in a Pear Tree."

q = recite(10, 10)
q
# "On the tenth day of Christmas my true love gave to me: ", "ten Lords-a-Leaping, ", "nine Ladies Dancing, ", "eight Maids-a-Milking, ", "seven Swans-a-Swimming, ", "six Geese-a-Laying, ", "five Gold Rings, ", "four Calling Birds, ", "three French Hens, ", "two Turtle Doves, ", "and a Partridge in a Pear Tree.",

q = recite(11, 11)
q
# "On the eleventh day of Christmas my true love gave to me: ", "eleven Pipers Piping, ", "ten Lords-a-Leaping, ", "nine Ladies Dancing, ", "eight Maids-a-Milking, ", "seven Swans-a-Swimming, ", "six Geese-a-Laying, ", "five Gold Rings, ", "four Calling Birds, ", "three French Hens, ", "two Turtle Doves, ", "and a Partridge in a Pear Tree."

q = recite(12, 12)
q
# "On the twelfth day of Christmas my true love gave to me: ", "twelve Drummers Drumming, ", "eleven Pipers Piping, ", "ten Lords-a-Leaping, ", "nine Ladies Dancing, ", "eight Maids-a-Milking, ", "seven Swans-a-Swimming, ", "six Geese-a-Laying, ", "five Gold Rings, ", "four Calling Birds, ", "three French Hens, ", "two Turtle Doves, ", "and a Partridge in a Pear Tree."

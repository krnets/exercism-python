
# twelve Drummers Drumming, eleven Pipers Piping, ten Lords-a-Leaping, nine Ladies Dancing, eight Maids-a-Milking, seven Swans-a-Swimming, six Geese-a-Laying, five Gold Rings, four Calling Birds, three French Hens, two Turtle Doves, and a Partridge in a Pear Tree.


# ITEMS = [
#     'Drummers Drumming' ,
#     'Pipers Piping',
#     'Lords-a-Leaping',
#     'Ladies Dancing',
#     'Maids-a-Milking',
#     'Swans-a-Swimming',
#     'Geese-a-Laying',
#     'Gold Rings',
#     'Calling Birds',
#     'French Hens',
#     'Turtle Doves',
#     'Partridge in a Pear Tree'
# ]




# ORDINALS = [
#     'first',
#     'second',
#     'third',
#     'fourth',
#     'fifth',
#     'sixth',
#     'seventh',
#     'eighth',
#     'ninth',
#     'tenth',
#     'eleventh',
#     'twelfth'
# ]

# GIFTS = [
#     'twelve Drummers Drumming, ',
#     'eleven Pipers Piping, ',
#     'ten Lords-a-Leaping, ',
#     'nine Ladies Dancing, ',
#     'eight Maids-a-Milking, ',
#     'seven Swans-a-Swimming, ',
#     'six Geese-a-Laying, ',
#     'five Gold Rings, ',
#     'four Calling Birds, ',
#     'three French Hens, ',
#     'two Turtle Doves, and ',
#     'a Partridge in a Pear Tree'
# ]


# def verse(day):
#     return 'On the {} day of Christmas my true love gave to me, {}.\n'.format(
#         ORDINALS[day - 1], ''.join(GIFTS[i] for i in range(12 - day, 12)))


# def verses(start_day, end_day):
#     # return '\n'.join(verse(i) for i in range(start_day, end_day + 1)) + '\n'
#     return ' '.join(verse(i) for i in range(start_day, end_day + 1)) + '\n'


# def recite(start_day, end_day):
#     return verses(1, 12)


# def recite(start_verse, end_verse):
# 	res = [];
# 	days = ['first','second','third','fourth','fifth','sixth','seventh','eighth','ninth','tenth','eleventh','twelfth']
# 	lines = ['twelve Drummers Drumming, ',
# 				'eleven Pipers Piping, ',
# 				'ten Lords-a-Leaping, ',
# 				'nine Ladies Dancing, ',
# 				'eight Maids-a-Milking, ',
# 				'seven Swans-a-Swimming, ',
# 				'six Geese-a-Laying, ',
# 				'five Gold Rings, ',
# 				'four Calling Birds, ',
# 				'three French Hens, ',
# 				'two Turtle Doves, ',
# 				'and a Partridge in a Pear Tree.']
# 	for i in range(start_verse,end_verse+1):	
# 		if i == 1:
# 			lines[11] = 'a Partridge in a Pear Tree.'
# 		else:
# 			lines[11] = 'and a Partridge in a Pear Tree.'
# 		intro = f"On the {days[i-1]} day of Christmas my true love gave to me: "
# 		res.append( intro + ''.join(map(str, lines[-i:])) );
# 	return res

ITEMS = [
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
    intro = f"On the {DAYS[end_verse-1]} day of Christmas my true love gave to me: "
    rest = []
    for i in range(end_verse):
        rest.append(f"{COUNT[i]} {ITEMS[i]}, ")
    if len(rest) == 1:
        rest[0] = f"{rest[0][:-2]}."
    else:
        rest[0] = f"and {rest[0][:-2]}."

    return [''.join([intro] + rest[::-1])]

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

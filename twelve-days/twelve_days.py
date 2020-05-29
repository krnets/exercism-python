GIFTS = ['Partridge in a Pear Tree',
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
         'Drummers Drumming']

DAYS = 'first second third fourth fifth sixth seventh eighth ninth tenth eleventh twelfth'.split()
COUNT = 'a two three four five six seven eight nine ten eleven twelve'.split()

def recite(start_verse, end_verse):
    song = []
    lines = [f'{COUNT[i]} {GIFTS[i]}, ' for i in range(len(GIFTS))]
    for i in range(start_verse, end_verse+1):
        lines[0] = f'{COUNT[0]} {GIFTS[0]}.' if i == 1 else f'and {COUNT[0]} {GIFTS[0]}.'
        intro = f'On the {DAYS[i-1]} day of Christmas my true love gave to me: '
        song.append(intro + ''.join(map(str, reversed(lines[:i]))))
    return song
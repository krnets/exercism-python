WORD_NUM = dict(zero=0, one=1, two=2, three=3, four=4, five=5, six=6, seven=7, eight=8, nine=9,
                ten=10, eleven=11, twelve=12, thirteen=13, fourteen=14, fifteen=15, sixteen=16,
                seventeen=17, eighteen=18, nineteen=19, twenty=20, thirty=30, forty=40,
                fifty=50, sixty=60, seventy=70, eighty=80, ninety=90, hundred=100, thousand=1e3,
                million=1e6, billion=1e9, trillion=1e12)

NUM_WORD = dict(map(reversed, WORD_NUM.items()))




by_one = (
    'zero',
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine',
    'ten',
    'eleven',
    'twelve',
    'thirteen',
    'fourteen',
    'fifteen',
    'sixteen',
    'seventeen',
    'eighteen',
    'nineteen'
)

by_ten = (
    'zero',
    'ten',
    'twenty',
    'thirty',
    'forty',
    'fifty',
    'sixty',
    'seventy',
    'eighty',
    'ninety'
)


# def say(number):
#     if number < 0 or number > 10**12-1:
#         raise ValueError('number is out of range')
#     if number < 20:
#         return by_one[number]
#     elif number < 100:
#         tens = int(number / 10)
#         remainder = number % 10
#         return by_ten[tens] + ('-' + say(remainder) if remainder else '')
#     elif number < 1e3:
#         hundreds = int(number / 100)
#         remainder = number % 100
#         return by_one[hundreds] + ' hundred' + (' ' + say(remainder) if remainder else '')
#     elif number < 1e6:
#         thousands = int(number / 1e3)
#         remainder = number % 1000
#         return say(thousands) + ' thousand' + (' ' + say(remainder) if remainder else '')
#     elif number < 1e9:
#         millions = int(number / 1e6)
#         remainder = int(number % 1e6)
#         return say(millions) + ' million' + (' ' + say(remainder) if remainder else '')
#     else:
#         billions = int(number / 1e9)
#         remainder = int(number % 1e9)
#         return say(billions) + ' billion' + (' ' + say(remainder) if remainder else '')

def say(number):
    if number < 0 or number > 10**12-1:
        raise ValueError('number is out of range')
    elif number <= 20:
        return NUM_WORD.get(number)
    elif number < 100:
        tens = number - number % 10
        tens_rem = number % 10
        return NUM_WORD.get(tens) + '-' + NUM_WORD.get(tens_rem)
    elif number < 1e3:
        hundreds = number // 100
        rem = number % 100
        return ' '.join([NUM_WORD.get(hundreds, ''), NUM_WORD[100], say(rem) if rem else '']).rstrip()
    elif number < 1e6:
        thousands = number // 1e3
        rem = number % 1e3
        return ' '.join([NUM_WORD.get(thousands, ''), NUM_WORD[1e3], say(rem) if rem else '']).rstrip()
    elif number < 1e9:
        million = number // 1e6
        rem = number % 1e6
        return ' '.join([NUM_WORD.get(million, ''), NUM_WORD[1e6], say(rem) if rem else '']).rstrip()
    else:
        billion = number // 1e9
        rem = number % 1e9
        return ' '.join([NUM_WORD.get(billion, ''),  NUM_WORD[1e9], say(rem) if rem else '']).rstrip()



#  "one billion"
q = say(987654321123)
q
# "nine hundred eighty-seven billion six hundred fifty-four million three hundred twenty-one thousand one hundred twenty-three",

q = say(1000000000)
q
q = say(0), "zero"
q
q = say(1), "one"
q
q = say(14), "fourteen"
q
q = say(20), "twenty"
q
q = say(22), "twenty-two"
q
q = say(23)
q
#     "twenty-three"

q = say(100), "one hundred"
q
q = say(123)
q
#  "one hundred twenty-three"

q = say(1000)
q
# #  "one thousand"
q = say(1234)
q
# #  "one thousand two hundred thirty-four"

q = say(1000000)
q
#     "one million"
q = say(1002345)
q
#     "one million two thousand three hundred forty-five"

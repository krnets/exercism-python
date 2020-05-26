ONES = 'zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen'.split()
TENS = 'zero ten twenty thirty forty fifty sixty seventy eighty ninety'.split()

def say(number):
    if number < 0 or number > 10**12-1:
        raise ValueError('number is out of range')
    elif number < 20:
        return ONES[int(number)]
    elif number < 100:
        rem = number % 10
        return f"{TENS[int(number/10)]}{'-'+ say(rem) if rem else ''}"
    elif number < 1e3:
        rem = number % 100
        return f"{ONES[int(number/100)]} hundred{' '+ say(rem) if rem else ''}"
    elif number < 1e6:
        rem = number % 1000
        return f"{say(number/1e3)} thousand{' '+ say(rem) if rem else ''}"
    elif number < 1e9:
        rem = number % 1e6
        return f"{say(number/1e6)} million{' '+ say(rem) if rem else ''}"
    else:
        rem = number % 1e9
        return f"{say(number/1e9)} billion{' '+ say(rem) if rem else ''}"
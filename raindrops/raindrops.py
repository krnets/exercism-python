def convert(number):
    drops = list(zip((3,5,7), ('Pling', 'Plang', 'Plong')))
    speak = [s for f, s in drops if number % f == 0]
    return ''.join(speak) if speak else str(number)

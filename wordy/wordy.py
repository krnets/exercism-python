import re

OPS = {'plus': '+', 'minus': '-', 'multiplied by': '*', 'divided by': '/'}

def answer(question):
    for op, symbol in OPS.items():
        question = question.replace(op, symbol)
    m = re.match(r'What is(( -?\d+ \D{,2})* -?\d+)\?$', question)
    if not m:
        raise ValueError('Invalid operation')
    return eval(re.sub(r'(-?\d+ \D -?\d+)', r'(\1)', m.group(1)))
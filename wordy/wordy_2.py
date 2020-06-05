import re

OPS = {'plus': '+', 'minus': '-', 'multiplied by': '*', 'divided by': '//'}


def answer(question):
    for op, symbol in OPS.items():
        question = question.replace(op, symbol)
    q = re.match(r'What is((:? -?\d+ \D{1,2})* -?\d+)\?$', question)
    if not q:
        raise ValueError('Invalid operation')
    return eval(re.sub(r'(-?\d+ \D{1,2} -?\d+)', r'(\1)', q.group(1)))
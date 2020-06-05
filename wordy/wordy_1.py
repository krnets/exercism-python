OPS = {'plus': '+', 'minus': '-', 'multiplied by': '*', 'divided by': '//'}


def answer(question):
    question = question[8:-1]
    for op, symbol in OPS.items():
        question = question.replace(op, symbol)
    tokens = question.split()
    try:
        out = eval(' '.join(tokens[:3]))
        for i in range(3, len(tokens), 2):
            out = eval(f'{out}{tokens[i]}{tokens[i+1]}')
        return out
    except:
        raise ValueError('Invalid operation')
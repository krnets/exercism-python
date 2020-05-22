def reverse(text):
    stack = []
    for x in text:
        stack.append(x)
    res = []
    while stack:
        res.append(stack.pop())
    return ''.join(res)
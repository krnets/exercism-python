def value(colors):
    return int(''.join(str(color_code(x)) for x in colors)[:2])


def color_code(color):
    return colors().index(color)


def colors():
    return ["black", "brown", "red", "orange", "yellow", "green", "blue", "violet", "grey", "white"]
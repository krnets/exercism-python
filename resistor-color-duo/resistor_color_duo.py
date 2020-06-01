RESISTOR_COLORS = ["black", "brown", "red", "orange", "yellow",
                   "green", "blue", "violet", "grey", "white"]

def value(colors):
    return int(''.join(str(RESISTOR_COLORS.index(x)) for x in colors)[:2])
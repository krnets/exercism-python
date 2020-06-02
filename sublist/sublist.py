SUBLIST = 'SUBLIST'
SUPERLIST = 'SUPERLIST'
EQUAL = 'EQUAL'
UNEQUAL = 'UNEQUAL'


def sublist(list_one, list_two):
    if list_one == list_two:
        return EQUAL
    elif len(list_one) < len(list_two) and list_one in slide(list_two, len(list_one)):
        return SUBLIST
    elif len(list_one) > len(list_two) and list_two in slide(list_one, len(list_two)):
        return SUPERLIST
    else:
        return UNEQUAL


def slide(lst, size):
    return [lst[i:i+size] for i in range(len(lst)-size+1)]
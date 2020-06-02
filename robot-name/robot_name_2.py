import random
import string

GLOBAL_NAME_CACHE = set()


def generate_name():
    name = combine_prefix_suffix()
    while name in GLOBAL_NAME_CACHE:
        name = combine_prefix_suffix()
    GLOBAL_NAME_CACHE.add(name)
    return name


def combine_prefix_suffix():
    return random_prefix(2) + random_suffix(3)


def random_prefix(n):
    return ''.join(random.sample(string.ascii_uppercase, n))


def random_suffix(n):
    return ''.join(random.sample(string.digits, n))


class Robot:
    def __init__(self):
        self.name = generate_name()

    def reset(self):
        self.__init__()

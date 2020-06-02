import random
import string

NAME_CACHE = set()
NAME_CACHE_LIMIT = 26**2 * 10**3


def generate_name():
    if len(NAME_CACHE) > NAME_CACHE_LIMIT:
        raise RuntimeError(
            'All possible name combinations have been exhausted')
    name = combine_prefix_suffix()
    while name in NAME_CACHE:
        name = combine_prefix_suffix()
    NAME_CACHE.add(name)
    return name


def combine_prefix_suffix():
    return ''.join([random_prefix(2), random_suffix(3)])


def random_prefix(n):
    return ''.join(random.choices(string.ascii_uppercase)[0] for i in range(n))


def random_suffix(n):
    return ''.join(random.choices(string.digits)[0] for i in range(n))


class Robot:
    def __init__(self):
        self.name = generate_name()

    def reset(self):
        self.__init__()

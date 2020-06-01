class Node:
    def __init__(self, value, next=None):
        self._value = value
        self._next = next

    def value(self):
        return self._value

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        self._size = 0
        self._head = None

        if values:
            for v in values:
                self.push(v)

    def __len__(self):
        return self._size

    def __iter__(self):
        return self

    def __next__(self):
        if not self._head:
            raise StopIteration
        return self.pop()

    def reversed(self):
        return LinkedList(self)

    def head(self):
        if not self._head:
            raise EmptyListException('List is empty')
        return self._head

    def push(self, value):
        newest = Node(value, self._head)
        self._head = newest
        self._size += 1

    def pop(self):
        if not self._head:
            raise EmptyListException('List is empty')
        value = self._head.value()
        self._head = self._head.next()
        self._size -= 1
        return value


class EmptyListException(Exception):
    pass

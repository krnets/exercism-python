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
        try:
            return self.pop()
        except EmptyListException:
            raise StopIteration

    def reversed(self):
        return LinkedList(self)

    def head(self):
        if self._head:
            return self._head
        else:
            raise EmptyListException("List is empty")

    def push(self, value):
        newest = Node(value, self._head)
        self._head = newest
        self._size += 1

    def pop(self):
        if self._head is None:
            raise EmptyListException("List is empty")
        value = self._head.value()
        self._head = self._head.next()
        self._size -= 1
        return value


class EmptyListException(Exception):
    pass

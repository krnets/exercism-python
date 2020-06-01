class Node:
    def __init__(self, value, next=None):
        self._data = value
        self._next = next

    def value(self):
        return self._data

    def next(self):
        return self._next


class LinkedList:
    def __init__(self, values=[]):
        prev = None
        self.nodes = [prev := Node(v, prev) for v in values]
        self.size = len(self.nodes)

    def __len__(self):
        return self.size

    def __iter__(self):
        return (n.value() for n in reversed(self.nodes))

    def reversed(self):
        return [n.value() for n in self.nodes]

    def head(self):
        if not self:
            raise EmptyListException("List is empty")
        return self.nodes[-1]

    def push(self, value):
        newest = Node(value)
        if self:
            self.head()._next = newest
        self.size += 1
        self.nodes.append(newest)

    def pop(self):
        if not self:
            raise EmptyListException("List is empty")
        self.size -= 1
        return self.nodes.pop().value()


class EmptyListException(Exception):
    pass

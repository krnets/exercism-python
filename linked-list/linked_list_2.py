class Node(object):
    def __init__(self, value=None, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList(object):

    def __init__(self):
        self.head = Node()
        self.tail = Node(succeeding=self.head)
        self.head.previous = self.tail
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        cursor = self.head.previous
        while cursor != self.tail:
            yield cursor.value
            cursor = cursor.previous

    def push(self, value):
        newest = Node(value,
                      succeeding=self.tail.succeeding,
                      previous=self.tail)
        self.tail.succeeding.previous = newest
        self.tail.succeeding = newest
        self.size += 1

    def pop(self):
        if not self.tail.succeeding.value:
            return None
        else:
            value = self.tail.succeeding.value
            self.tail.succeeding = self.tail.succeeding.succeeding
            self.tail.succeeding.previous = self.tail
            self.size -= 1
            return value

    def unshift(self, value):
        newest = Node(value,
                      succeeding=self.head,
                      previous=self.head.previous)
        self.head.previous.succeeding = newest
        self.head.previous = newest
        self.size += 1

    def shift(self):
        if not self.head.previous.value:
            return None
        else:
            value = self.head.previous.value
            self.head.previous = self.head.previous.previous
            self.head.previous.succeeding = self.head
            self.size -= 1
            return value

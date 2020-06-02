class Node(object):
    def __init__(self, value=None, succeeding=None, previous=None):
        self.value = value
        self.succeeding = succeeding
        self.previous = previous


class LinkedList(object):

    def __init__(self):
        self.front = Node()
        self.back = Node(succeeding=self.front)
        self.front.previous = self.back
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        cursor = self.front.previous
        while cursor != self.back:
            yield cursor.value
            cursor = cursor.previous

    def is_empty(self):
        return self.size == 0

    def push(self, value):
        newest = Node(value,
                      succeeding=self.back.succeeding,
                      previous=self.back)
        self.back.succeeding.previous = newest
        self.back.succeeding = newest
        self.size += 1

    def pop(self):
        if self.is_empty():
            return None
        else:
            value = self.back.succeeding.value
            self.back.succeeding = self.back.succeeding.succeeding
            self.back.succeeding.previous = self.back
            self.size -= 1
            return value

    def shift(self):
        if self.is_empty():
            return None
        else:
            value = self.front.previous.value
            self.front.previous = self.front.previous.previous
            self.front.previous.succeeding = self.front
            self.size -= 1
            return value

    def unshift(self, value):
        newest = Node(value,
                      succeeding=self.front,
                      previous=self.front.previous)
        self.front.previous.succeeding = newest
        self.front.previous = newest
        self.size += 1

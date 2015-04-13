class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        return self.item.insert(0, item)

    def dequeue(self):
        return self.item.pop()

    def size(self):
        return len(self.item)

class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0, item)

    def removeFront(self):
        self.items.pop()

    def removeRear(self):
        self.items.pop(0)

    def size(self):
        return len(self.items)
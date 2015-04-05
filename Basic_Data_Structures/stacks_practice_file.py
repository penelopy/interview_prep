class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, new_item):
        self.items.append(new_item)

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) -1]

    def pop(self):
        return self.items.pop()


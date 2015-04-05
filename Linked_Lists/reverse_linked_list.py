class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class Linked_list(object):
    def __init__(self):
        self.head = None


    def print_list(self):
        current = self.head
        linky = []
        while current.next:
            linky.append(current.data)
            current = current.next
        linky.append(current.data)
        print linky

    def reverse_linked_list(self):
        self.tail = self.head
        current = self.head.next
        temp = current.next
        self.head.next = None
        while temp.next:
            current.next = self.head
            self.head = current
            current = temp
            temp = temp.next
        current.next = self.head
        self.head = temp
        self.head.next = current



a = Node("a")
b = Node("b")
d = Node("d")
o = Node("o")
m = Node("m")
e = Node("e")
n = Node("n")
a.next = b
b.next = d
d.next = o
o.next = m
m.next = e
e.next = n

abdomen = Linked_list()
abdomen.head = a

abdomen.print_list()
abdomen.reverse_linked_list()
abdomen.print_list()



""" CCI 2.1 Write code to remove duplicates from an unordered list"""

class Node: 
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
    def getData(self):
        return self.data
    def setData(self, newdata):
        self.data = newdata
    def getNext(self):
        return self.next
    def setNext(self, newnext):
        self.next = newnext

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def dedup(self):
        mydict = {}
        current = self.head
        previous = None
        while current != None:
            if current not in mydict:
                mydict[current] = 1
            else:
                previous = current
                current = current.getNext()

        if previous == None: 
            self.head = current.getNext()
        else: 
            previous.setNext(current.getNext())

""" CCI 2.5 You have two numbers represented by a linked list where each node contains a single digit. The digits are stored in reverse order, such that the 1s digit is at the head of the list. Write a function that adds two numbers and returns the sum as a linked list."""


class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self):
        temp = Node(item)


node1 = Node(7)
node1.












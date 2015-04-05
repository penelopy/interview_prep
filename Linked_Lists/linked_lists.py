# from Cynthia's lecture

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_node(self, data):
        new_node = Node(data)

        if self.head == None: 
            self.head = new_node

        if self.tail != None: 
            self.tail.next = new_node

        self.tail = new_node

    def print_list(self):
        node = self.head

        while node != None:
            print node.data
            node = node.next 

    def dedup(self, alist):

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
# from data structure book

class Node:
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self,item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self,item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()
        return found

    def remove(self,item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())

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

    def append(self, item): 
        current = self.head
        new_node = Node(item)

        while current.getNext() != None: 
            current = current.getNext()
        current.setNext(new_node)

    def index(self, position): 
        current = self.head
        i = 0
        while i < position: 
            current = current.getNext()
            i += 1
            if i == position: 
                return current.getData()

    def insert(self, data, position):
        current = self.head
        new_node = Node(data)
        i = 0
        while current != None and i < position: 
            current = current.getNext()
            i += 1
        if i == position: 
            temp = current.getNext()
            current = current.setNext(new_node)
            current = temp


ul = UnorderedList()

ul.add(5)
ul.add(21)
ul.add(13)
ul.add(34)
ul.add(29)

print ul.index(3)
print ul.insert(3, 55)

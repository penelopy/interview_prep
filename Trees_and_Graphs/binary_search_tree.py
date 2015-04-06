""" http://www.laurentluce.com/posts/binary-search-tree-library-in-python/"""
""" Binary Search Tree with insert, lookup and print methods"""

class Node: 
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


    def insert(self, data):
        if self.data: 
            if data < self.data: 
                if self.left is None:
                    self.left = Node(data)
                else: 
                    self.left.insert(data)

            elif data > self.data:
                if self.right is None: 
                    self.right = Node(data)
                else: 
                    self.right.insert(data)
        else: 
            self.data = data


    def lookup(self, data, parent=None):
        if data < self.data: 
            if self.left is None:
                return None, None
            return self.left.lookup(data, self)

        elif data > self.data: 
            if self.right is None:
                return None, None
            return self.right.lookup(data, self)
        else: 
            return self, parent

    def print_tree(self):
        if self.left: 
            self.left.print_tree()
        print self.data, 
        if self.right: 
            self.right.print_tree()


root = Node(8)
root.insert(3)
root.insert(10)
root.insert(1)
root.insert(6)
root.insert(4)
root.insert(7)
root.insert(14)
root.insert(13)

node, parent = root.lookup(6)
print node
print parent

# root.print_tree()
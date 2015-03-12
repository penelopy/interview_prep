"""NOTES AND PRACTICE FILE

Ex. Binary Tree 
    1
   / \
  2   3

Ex. Binary Search Tree

    2
   / \
  1   3


A binary search is performed on sorted data. With binary trees you use them to quickly look up numbers and compare them. They have quick insertion and lookup.  
"""

class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def get_right(self):
        return self.right
    def set_right(self, node):
        self.right = node
    def get_left(self):
        return self.left
    def set_left(self, node):
        self.left = node
    def set_value(self, number):
        self.value = number

def depth_first_traversal(self, node):
    """ DFT, recursive"""
    print node.value,

    if node.left: 
        depth_first_traversal(node.left)
    if node.right: 
        depth_first_traversal(node.right)

def breath_first_traversal(self, node):
    if not node: 
        return None
    else:
        queue = [node]
        while len(queue) > 0: 
            current = queue.pop(0)
            print current.value, 

            if current.left: 
                queue.append(current.left)
            if current.right: 
                queue.append(current.right)




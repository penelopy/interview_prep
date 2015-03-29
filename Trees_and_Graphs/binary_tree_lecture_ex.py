class Node(object):
    def __init__(self, value, data):
        self.value = value
        self.left = None
        self.right = None
        self.data = data

class Tree(object):
    def __init__(self):
        self.root = None

    # def search(self, value):
    #     node = self.root
    #     while node: 
    #         if value < node.value:
    #             node = node.left
    #         elif value > node.value:
    #             node = node.right
    #         else: 
    #             return node
    #     return "Not Found"

    # recursively searches the binary tree
    def r_search(node = self.root, value):
        if not node: 
            return "Not Found"
        if value < node.value:
            return r_search(node.left, value)
        elif value > node.value:
            return r_search(node.right, value)
        else: 
            return node

#####

    n = Node(7)
    t.append(n)

    class BinarySearchTree(object): 
        def __init__(self):
            self.root = None
        def append_node(self, new_node):
            if self.root == None:
                self.root = new_node
            else: 
                node = self.root
                while node: 
                    if (new_node.data < node.data) and node.left:
                        node = node.left
                    elif new_node.data < node.data:                      
                            node.left = new_node
                            return
                    elif (new_node.data > node.data) and node.right:
                        node = node.right          
                    elif (new_node.data > node.data):                      
                            node.right = new_node
                            return


t = BinarySearchTree()
t.append_node(7)
t.append_node(3)











"""This function checks whether the difference in depths of any two tree leafs is greater then one

Source: Interview Cake - https://www.interviewcake.com/question/balanced-binary-tree?utm_source=weekly_email
"""
def is_balanced(tree_root):
    depths = [] # we short-circuit as soon as we find more than 2

    # this stack will store tuples of (node, depth)
    nodes = Stack()
    nodes.push((tree_root, 0))

    while(not nodes.is_empty()):
        # pop a node and its depth from the top of our stack
        node, depth = nodes.pop()

        # case: we found a leaf
        if (not node.left) and (not node.right):

            # we only care if it's a new depth
            if depth not in depths:
                depths.append(depth)

                # two ways we might now have an unbalanced tree:
                # 1) more than 2 different leaf depths
                # 2) 2 leaf depths that are more than 1 apart
                if (len(depths) > 2) or \
                    (len(depths) == 2 and abs(depths[0] - depths[1]) > 1):
                    return False

        # case: this isn't a leaf--keep stepping down
        else:
            if node.left:
                nodes.push((node.left, depth+1))
            if node.right:
                nodes.push((node.right, depth+1))
    return True

"""This function checks whether a binary tree is a valid binary search tree

Source: Interview Cake - https://www.interviewcake.com/question/bst-checker?utm_source=weekly_email
"""
def bst_checker(root):
    # start at the root, with an arbitrarily low lower bound
    # and an arbitrarily high upper bound
    stack = Stack([(root, MIN_INT, MAX_INT)])

    # depth-first traversal
    while not stack.is_empty():
        node, lower_bound, upper_bound = stack.pop()

        # if this node is invalid, we return false right away
        if (node.value < lower_bound) or (node.value > upper_bound):
            return False

        if node.left:
            # this node must be less than the current node
            stack.push((node.left, lower_bound, node.value))
        if node.right:
            # this node must be greater than the current node
            stack.push((node.right, node.value, upper_bound))

    # if none of the nodes were invalid, return true
    # (at this point we have checked all nodes)
    return True
"""Alternate approach - risks stack overflow error"""
def bst_valid_recursive(root, lower_bound = MIN_INT, upper_bound = MAX_INT):
    if (not root):
      return True

    if (root.value > upper_bound or root.value < lower_bound):
      return False

    return bst_valid_recursive(root.left, lower_bound, root.value) \
      and bst_valid_recursive(root.right, root.value, upper_bound)

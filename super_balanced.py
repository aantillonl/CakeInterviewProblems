# -*- coding: utf-8 -*-

#Write a function to see if a binary tree ↴ is "superbalanced" (a new tree property we just made up).
#A tree is "superbalanced" if the difference between the depths of any two leaf nodes ↴ is no greater than one.

class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, node):
        self.left = node
        return self.left

    def insert_right(self, node):
        self.right = node
        return self.right
    
    

def isSuperBalanced(root: BinaryTreeNode):
    nodes = []
    depths = []
    cur_depth = 0
    
    cur_node = root
    
    # Iterative approach
    while cur_node:
        # if has children
        if(cur_node.left and cur_node.right):
            # append them to the iterating list. RIGHT LAST! in order to process right children first
            nodes.append([cur_node.left, cur_depth + 1])
            nodes.append([cur_node.right, cur_depth + 1])
        # If no children, therefore, is leaf, check depth
        else:
            # If is a new one, insert
            if cur_depth not in depths:
                depths.append(cur_depth)
            # eval if there are any depths that differ by more than 1
            if(max(depths) - min(depths) > 1):
                return False
        cur_node, cur_depth = nodes.pop() if len(nodes) > 0 else [None, 0]
    return True

# Test
n1 = BinaryTreeNode(1) # root
n2 = BinaryTreeNode(2)
n3 = BinaryTreeNode(3)
n4 = BinaryTreeNode(4)
n5 = BinaryTreeNode(5)
n6 = BinaryTreeNode(6)
n7 = BinaryTreeNode(7)
n8 = BinaryTreeNode(8)
n9 = BinaryTreeNode(9)
n10 = BinaryTreeNode(10)
n11 = BinaryTreeNode(11)
n12 = BinaryTreeNode(12)

n1.insert_left(n2)
n1.insert_right(n3)
n2.insert_left(n4)
n2.insert_right(n5)
n3.insert_left(n6)
n3.insert_right(n7)
n7.insert_left(n8)
n7.insert_right(n9)
n9.insert_left(n10)
n9.insert_right(n11)

print("Your tree %s superbalanced" % ("is" if isSuperBalanced(n1) else "is NOT"))

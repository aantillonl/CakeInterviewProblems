class BinaryTreeNode:

    def __init__(self, value):
        self.value = value
        self.left  = None
        self.right = None

    def insert_left(self, value):
        self.left = BinaryTreeNode(value)
        return self.left

    def insert_right(self, value):
        self.right = BinaryTreeNode(value)
        return self.right# -*- coding: utf-8 -*-

        
def inverseOrderTraverse(node: BinaryTreeNode, k):
    global n
   
    if n >= k or node is None: return
    inverseOrderTraverse(node.right,k)
    
    n = n+1
    if n == k:
        print("kth (%i) largest is %i" % (k, node.value))
    inverseOrderTraverse(node.left,k)
        
        
root = BinaryTreeNode(4)
root.insert_left(2)
root.insert_right(5)
root.left.insert_left(1)
root.left.insert_right(3)

n = 0
inverseOrderTraverse(root, 2)


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
    
    
def GetSecondMax(root: BinaryTreeNode):

    #if (root.right is None and root.left is None):
    #    return None
    
    cur_node = root
    second_max = None
    while cur_node:
        if cur_node.right:
            second_max = cur_node.value
        else:
            if cur_node.left:
                second_max = cur_node.left.value
        cur_node = cur_node.right
    return second_max
        
        
        

n1 = BinaryTreeNode(8) # root
n2 = BinaryTreeNode(4)
n3 = BinaryTreeNode(12)
n4 = BinaryTreeNode(5)
n5 = BinaryTreeNode(6)
n6 = BinaryTreeNode(10)
n7 = BinaryTreeNode(14)
n8 = BinaryTreeNode(1)
n9 = BinaryTreeNode(3)
n10 = BinaryTreeNode(5)
n11 = BinaryTreeNode(7)
n12 = BinaryTreeNode(9)
n13 = BinaryTreeNode(11)
n14 = BinaryTreeNode(13)
n15 = BinaryTreeNode(15)

n1.insert_left(n2)
n1.insert_right(n3)
n2.insert_left(n4)
n2.insert_right(n5)
n3.insert_left(n6)
n3.insert_right(n7)
n4.insert_left(n8)
n4.insert_right(n9)
n5.insert_left(n10)
n5.insert_right(n11)
n6.insert_right(n12)
n6.insert_right(n13)
n7.insert_left(n14)
n7.insert_right(n15)

print("Second max is %i" % (GetSecondMax(n1)))

# My notes
# What if the tree is only one node? I guess we will return None
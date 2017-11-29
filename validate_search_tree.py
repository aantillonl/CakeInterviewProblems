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
        

def validateBinarySearchTree(root: BinaryTreeNode):
    # Initialize values for the first iteration
    # The first iteration is kind of a corner case
    cur_node = root
    # Set a dumy value for parent and isLeftChild on the first iteration so the main func does not break
    parent_value = 0
    isLeftChild = None
    nodes = []

    while cur_node: 
        if cur_node.left:
            if not(cur_node.left.value < cur_node.value):
                return False
            nodes.append([cur_node.left, cur_node.value, True])
        if cur_node.right:
            if not(cur_node.right.value > cur_node.value):
                return False
            nodes.append([cur_node.right, cur_node.value, False])
        
        if cur_node != root:
            if isLeftChild and cur_node.right:
                if not(cur_node.right.value < parent_value):
                    return False
            if not isLeftChild and cur_node.left:
                if not(parent_value < cur_node.left.value):
                    return False
        cur_node, parent_value, isLeftChild = nodes.pop() if len(nodes) else [None, None, None]
    
    return True

n1 = BinaryTreeNode(4) # root
n2 = BinaryTreeNode(2)
n3 = BinaryTreeNode(6)
n4 = BinaryTreeNode(1)
n5 = BinaryTreeNode(3)
n6 = BinaryTreeNode(5)
n7 = BinaryTreeNode(7)
n8 = BinaryTreeNode(6)
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
#n9.insert_left(n10)
#n9.insert_right(n11)

print("Your tree %s valid" % ("is" if validateBinarySearchTree(n1) else "is NOT"))

# O(n)
# Space is worst case O(n)
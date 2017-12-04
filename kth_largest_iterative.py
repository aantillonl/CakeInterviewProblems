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
        return self.right
    
    
def findKthLargest(root: BinaryTreeNode, k):
    n = 0
    nodes = []
    cur_node = root
    
    while True:
            
        # First go to the left most node until it is none
        if cur_node is not None:
            nodes.append(cur_node)
            cur_node = cur_node.right
            next
        # start moving to the right
        if cur_node is None and len(nodes) > 0:
            cur_node = nodes.pop()
            print(cur_node.value)
            n = n + 1
            if n >= 2:
                return cur_node.value
            next
            cur_node = cur_node.left
        if cur_node is None and len(nodes) == 0:
            break
    
root = BinaryTreeNode(4)
root.insert_left(2)
root.insert_right(5)
root.left.insert_left(1)
root.left.insert_right(3)

print(findKthLargest(root,2))

class TreeNode:
    def __init__(self , val):
        self.val = val
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.val)
    

def is_skewed(node):
    if node is None:
        return True
    if node.left and node.right:
        return False
    if node.left:
        
        return is_skewed(node.left)
    if node.right:
        return is_skewed(node.right)
    return True

node = TreeNode(2)
node.left = TreeNode(3)
node.left.left = TreeNode(4)
node.left.left.right = TreeNode(4)
print(is_skewed(node))
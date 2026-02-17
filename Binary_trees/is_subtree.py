class TreeNode:
    def __init__(self , val):
        self.val = val
        self.right = None
        self.left = None

def is_subtree(node1 , node2):
    if node2 is None:
        return True

    if node1 is None:
        return False

    if node1.val == node2.val:
        return (is_subtree(node1.right , node2.right) and is_subtree(node1.left , node2.left))
    if node1.left:
        return is_subtree(node1.left)
    if node2.right:
        return is_subtree(node2.right)


        
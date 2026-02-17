from is_skewed import TreeNode

def is_same(node1 , node2):
    if node1 is None and node2 is None:
        return True
    if node1 is None or node2 is None:
        return False
    if node1.val != node2.val:
        return False
    return is_same(node1.left , node2.left) and is_same(node1.right , node2.right)

node1 = TreeNode(4)
node1.left = TreeNode(5)
node1.right = TreeNode(6)

node2 = TreeNode(4)
node2.left = TreeNode(5)
node2.right = TreeNode(4)

print(is_same(node1 , node2))

from is_skewed import TreeNode

def display_tree(node):
    if node is None:
        return
    print(node.val)
    display_tree(node.left)
    display_tree(node.right)

def merge_bt(node1 , node2):
    if node1 is None and node2 is None:
        return 
    if node1 is None or node2 is None:
        return node1 if node1 is not None else node2
    val = node1.val + node2.val
    new_node = TreeNode(val)
    new_node.left = merge_bt(node1.left , node2.left)
    new_node.right = merge_bt(node1.right , node2.right)

    return new_node

node1 = TreeNode(5)
node1.left = TreeNode(3)
node1.right = TreeNode(4)
node1.right.right = TreeNode(2)

node2 = TreeNode(4)
node2.left = TreeNode(1)
node2.right = TreeNode(1)

display_tree(merge_bt(node1 , node2))


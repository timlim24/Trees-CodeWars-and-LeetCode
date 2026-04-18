# Pre-order traversal
def pre_order(node):
    if node is None:
        return []

    left_tree = pre_order(node.left)
    right_tree = pre_order(node.right)

    return [node.data] + left_tree + right_tree

# In-order traversal
def in_order(node):
    if node is None:
        return []

    left_tree = in_order(node.left)
    right_tree = in_order(node.right)

    return left_tree+ [node.data] + right_tree

# Post-order traversal
def post_order(node):
    if node is None:
        return []

    left_tree = post_order(node.left)
    right_tree = post_order(node.right)

    return left_tree + right_tree + [node.data]

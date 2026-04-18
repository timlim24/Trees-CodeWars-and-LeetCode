def tree_by_levels(node):
    def _process_levels(node) -> dict[int: int]:
        if node is None:
            return {}
        left_tree = _process_levels(node.left)
        right_tree = _process_levels(node.right)

        levels = {0: [node.value]}
        for i in range(max(len(left_tree), len(right_tree))):
            left_side = left_tree.get(i) or []
            right_side = right_tree.get(i) or []
            levels[i+1] = left_side + right_side

        return levels

    levels = _process_levels(node)
    return sum(levels.values(), [])

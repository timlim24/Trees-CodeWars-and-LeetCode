# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        head = root

        if root is None:
            return None

        probe = root
        prev_node = TreeNode()
        while probe is not None and probe.val != key:
            prev_node = probe
            if key < probe.val:
                probe = probe.left
            else:
                probe = probe.right


        if probe is not None:
            if probe.left is not None:
                replacement_node = probe.left
                remaining_node = probe.right
            else:
                replacement_node = probe.right
                remaining_node = probe.left

            if root.val == key:
                head = replacement_node
            else:
                if key < prev_node.val:
                    prev_node.left = replacement_node
                else:
                    prev_node.right = replacement_node

            if remaining_node is not None:
                new_key = remaining_node.val
                probe = replacement_node
                while True:
                    if new_key < probe.val:
                        if probe.left is None:
                            probe.left = remaining_node
                            break
                        probe = probe.left

                    else:
                        if probe.right is None:
                            probe.right = remaining_node
                            break
                        probe = probe.right

        return head

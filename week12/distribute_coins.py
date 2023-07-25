# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.count_value = 0

        def traverse_tree(node):
            if node is None:
                return 0

            left = traverse_tree(node.left)
            right = traverse_tree(node.right)
            node.val += left + right
            self.count_value += abs(left) + abs(right)

            return node.val - 1

        traverse_tree(root)
        return self.count_value

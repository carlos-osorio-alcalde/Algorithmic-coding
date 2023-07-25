from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_current_sum = float("-inf")

        def path_sum(node):
            if not node:
                return 0

            left_sum = max(0, path_sum(node.left))
            right_sum = max(0, path_sum(node.right))

            self.max_current_sum = max(
                self.max_current_sum, node.val + left_sum + right_sum
            )
            return node.val + max(left_sum, right_sum)

        path_sum(root)
        return self.max_current_sum

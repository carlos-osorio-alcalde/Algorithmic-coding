# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def traverse(node):
            return max(traverse(node.left) + 1 if node.left else 0, traverse(node.right) + 1 if node.right else 0)
        
        return traverse(root) + 1 if root else 0
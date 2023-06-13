# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generate_trees(start, end):
            if start > end:
                return [None]

            trees = []
            for i in range(start, end + 1):
                left_subtrees = generate_trees(start, i - 1)
                right_subtrees = generate_trees(i + 1, end)

                for left in left_subtrees:
                    for right in right_subtrees:
                        root = TreeNode(i)
                        root.left = left
                        root.right = right
                        trees.append(root)

            return trees

        return generate_trees(1, n) if n > 0 else []
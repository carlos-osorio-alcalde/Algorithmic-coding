class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        seen_values = set()

        def find_value(root):
            if root is None:
                return False

            searched_value = k - root.val
            if searched_value in seen_values:
                return True
            else:
                if root is not None:
                    seen_values.add(root.val)
                    if root.left or root.right:
                        return find_value(root.left) or find_value(root.right)

            return False

        return find_value(root)


if __name__ == "__main__":
    root = TreeNode(2)
    root.left = TreeNode(0)
    root.right = TreeNode(3)
    root.left.left = TreeNode(-4)
    root.left.right = TreeNode(1)

    k = -1

    s = Solution()
    print(s.findTarget(root, k))

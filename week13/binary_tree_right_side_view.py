class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return None

        elements = [root.val]

        def helper(node, level):
            if not node:
                return None
            
            if len(elements) <= level:
                elements.append(node.val)

            helper(node.right, level + 1)
            helper(node.left, level + 1)
        
        helper(root, 0)

        return elements 
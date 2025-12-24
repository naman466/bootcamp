class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def maxVal(node):
            while node.right:
                node = node.right
            return node.val

        def minVal(node):
            while node.left:
                node = node.left
            return node.val

        if not root:
            return True

        if root.left and maxVal(root.left) >= root.val:
            return False

        if root.right and minVal(root.right) <= root.val:
            return False

        return self.isValidBST(root.left) and self.isValidBST(root.right)

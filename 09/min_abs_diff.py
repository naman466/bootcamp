class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.mn = float('inf')

        def helper(node):
            if not node:
                return 
            
            if node.left:
                curr_left = node.left
                while curr_left.right:
                    curr_left = curr_left.right
                self.mn = min(self.mn, abs(node.val - curr_left.val))
            
            if node.right:
                curr_right = node.right
                while curr_right.left:
                    curr_right = curr_right.left
                self.mn = min(self.mn, abs(node.val - curr_right.val))

            helper(node.left)
            helper(node.right)
        
        helper(root)
        return self.mn

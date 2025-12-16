class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def helper(low, high):
            if low > high:
                return None
            
            mid = (low + high) // 2
            root = TreeNode(nums[mid])
            
            root.left = helper(low, mid - 1)
            root.right = helper(mid + 1, high)
            
            return root

        return helper(0, len(nums) - 1)

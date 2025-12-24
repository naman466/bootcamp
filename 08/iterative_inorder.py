class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def inorderTraversal(root):
    stack = []
    curr = root
    result = []

    while curr is not None or stack:
        while curr is not None:
            stack.append(curr)
            curr = curr.left

        curr = stack.pop()
        result.append(curr.val)

        curr = curr.right

    return result

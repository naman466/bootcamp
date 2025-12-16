class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:

        def build(head, tail):
            if head == tail:
                return None

            slow = fast = head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next

            root = TreeNode(slow.val)

            root.left = build(head, slow)
            root.right = build(slow.next, tail)

            return root

        return build(head, None)

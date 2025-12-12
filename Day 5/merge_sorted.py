class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def pn(self):
        print(self.val)

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(10)

n5 = ListNode(3)
n6 = ListNode(7)
n7 = ListNode(8)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = None

n5.next = n6
n6.next = n7
n7.next = None   


def merge(head1, head2):
    ptrA = head1
    ptrB = head2
    
    dummy = ListNode(None)
    ptrC = dummy
    
    while ptrA and ptrB:
        if ptrA.val <= ptrB.val:
            ptrC.next = ListNode(ptrA.val)
            ptrA = ptrA.next
        else:
            ptrC.next = ListNode(ptrB.val)
            ptrB = ptrB.next
        ptrC = ptrC.next
    
    while ptrA:
        ptrC.next = ListNode(ptrA.val)
        ptrA = ptrA.next
        ptrC = ptrC.next
        
    while ptrB:
        ptrC.next = ListNode(ptrB.val)
        ptrB = ptrB.next
        ptrC = ptrC.next
    
    return dummy.next

def print_list(head):
    curr = head
    while curr:
        print(curr.val, end=" ")
        curr = curr.next
    print()

merged = merge(n1, n5)

print_list(merged)

        
            
            
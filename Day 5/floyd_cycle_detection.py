class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def pn(self):
        print(self.val)

n1 = ListNode(5)
n2 = ListNode(7)
n3 = ListNode(10)

n1.next = n2
n2.next = n3
n3.next = n1  

def detect_cycle(head):
    slow = head
    fast = head
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
        if slow == fast:
            return slow
    return None


loop = detect_cycle(n1)


def find_cycle_start(loop, head):
    ptr1 = head
    ptr2 = loop
    
    while ptr1 != ptr2:
        ptr1 = ptr1.next
        ptr2 = ptr2.next
    
    return ptr1   


cycle_start = find_cycle_start(loop, n1)


ptr = cycle_start
while ptr.next != cycle_start:
    ptr = ptr.next

ptr.next = None

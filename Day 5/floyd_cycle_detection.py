class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None
        
    def pn(self):
        print(self.val)

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(5)
n6 = ListNode(7)
n7 = ListNode(8)

n1.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7

n7.next = n3    
print("Before breaking loop, n7.next = ", n7.next)


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

print("Before breaking loop, n7.next = ", n7.next)


class ListNode:
    def __init__(self, val, power):
        self.val = val
        self.power = power
        self.next = None

    def pl(self):
        print(self.val)


x21 = ListNode(10, 2)
x11 = ListNode(5, 1)
c1  = ListNode(2, 0)

x21.next = x11
x11.next = c1

x22 = ListNode(10, 2)
x12 = ListNode(5, 1)
c2  = ListNode(2, 0)

x22.next = x12
x12.next = c2


def eval_x(head1, head2):
    curr1 = head1
    curr2 = head2

    while curr1 and curr2:
        if curr1.power == curr2.power:
            curr1.val += curr2.val
            curr1 = curr1.next
            curr2 = curr2.next
        elif curr1.power > curr2.power:
            curr1 = curr1.next
        else:
            curr2 = curr2.next


eval_x(x21, x22)

curr = x21
while curr:
    print(curr.val, curr.power)
    curr = curr.next

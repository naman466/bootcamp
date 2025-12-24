class ListNode:
    def __init__(self, val, power):
        self.val = val
        self.next = None
        self.power = power
        
    def pl(self):
        print(self.val)
        

x2 = ListNode(10, 2)
x1 = ListNode(5, 1)
c = ListNode(2, 0)

x2.next = x1
x1.next = c
c.next = None


    
def eval_x(head, x):
    curr = head
    expr = 0

    while(curr):
        expr += curr.val * (x**curr.power)
        curr = curr.next

    return expr


x = 2
print(eval_x(x2, x))

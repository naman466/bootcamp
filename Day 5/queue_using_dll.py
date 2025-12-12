class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None


class DLLQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, val):
        new_node = Node(val)
        if not self.rear:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            print("Queue is empty")
            return None
        val = self.front.val
        self.front = self.front.next
        if self.front:
            self.front.prev = None
        else:
            self.rear = None
        return val

    def peek(self):
        if self.front:
            return self.front.val
        return None

    def is_empty(self):
        return self.front is None

    def display(self):
        curr = self.front
        while curr:
            print(curr.val, end=" <- " if curr.next else "\n")
            curr = curr.next

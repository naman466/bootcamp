import queue

class Stack:
    def __init__(self):
        # q1 = main queue, q2 = helper queue
        self.q1 = queue.Queue(maxsize=0) 
        self.q2 = queue.Queue(maxsize=0) 

    def push(self, val):
        # O(n) push
        
        self.q2.put(val)
        while(self.q1.qsize() != 0):
            item = self.q1.get()
            self.q2.put(item)
        
        self.q1, self.q2 = self.q2, self.q1
        self.top_element = val
    
    def pop(self):
        # O(1) pop
        
        item = self.q1.get()
        return item
    
    def is_empty(self):
        return (self.q1.qsize() == 0)
        
    
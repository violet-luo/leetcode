class Node():
    def __init__(self, _val):
        self.next = None
        self.val = _val

class MyQueue:
    def __init__(self):
        self.first, self.last = None, None
    
    def enqueue(self, item):
        if self.first is None:
            self.first = Node(item)
            self.last = self.first
        else:
            self.last.next = Node(item)
            self.last = self.last.next

    def dequeue(self):
        if self.first:
            item = self.first.val
            self.first = self.first.next
            return item

        return 

"""

Runtime: 28 ms, faster than 82.14% of Python3 online submissions for Implement Queue using Stacks.
Memory Usage: 13.8 MB, less than 73.23% of Python3 online submissions for Implement Queue using Stacks.

"""

def __init__(self):
    self.s1 = []
    self.s2 = []
    
def push(self, x: int) -> None:
    while self.s1:
        self.s2.append(self.s1.pop())
    self.s1.append(x)
    while self.s2:
        self.s1.append(self.s2.pop())

def pop(self) -> int:
    return self.s1.pop()

def peek(self) -> int:
    return self.s1[-1]

def empty(self) -> bool:
    return not self.s1

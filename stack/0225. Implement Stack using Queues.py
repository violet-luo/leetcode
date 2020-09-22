"""

1. One queue, 队列添加元素后，反转前n-1个元素，栈顶元素始终保留在队首 

Runtime: 36 ms, faster than 26.40% of Python3 online submissions for Implement Stack using Queues.
Memory Usage: 13.8 MB, less than 58.53% of Python3 online submissions for Implement Stack using Queues.
"""

def __init__(self):
    self.q = []

def push(self, x: int) -> None:
    self.q.append(x)
    q_length = len(self.q)
    while q_length > 1:
        self.q.append(self.q.pop(0)) #反转前n-1个元素，栈顶元素始终保留在队首
        q_length -= 1

def pop(self) -> int:
    return self.q.pop(0)

def top(self) -> int:
    return self.q[0]

def empty(self) -> bool:
    return len(self.q) == 0

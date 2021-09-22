"""

1. With Helper Stack min_stack, top of which the min

"""

def __init__ (self):
    self.stack = []
    self.min_stack = []

def push(self, x: int):
    self.stack.append(x)
    # if x < top of min_stack, push the number into min_stack
    if len(self.helper) == 0 or x <= self.min_stack[-1]:
        self.min_stack.append(x)
    self.min_stack.append(self.min_stack[-1])
    
def pop(self):
    self.stack.pop()
    self.min_satck.pop()
    
def top(self):
    return self.stack[-1]
    
def getMin(self):
    return self.min_stack[-1]



"""

2. Without Helper Stack
Store the nubmer and min as a tuple e.g.(-2, -3)

Runtime: 92 ms, faster than 45.02% of Python3 online submissions for Min Stack.
Memory Usage: 18.2 MB, less than 6.33% of Python3 online submissions for Min Stack.

"""

def __init__(self):
    self.stack = []
    
def push(self, x):
    if not self.stack: 
        self.stack.append((x,x))
    else:
        self.stack.append((x, min(x, self.stack[-1][1]))) # tuple[1] stores the current min
        
def pop(self, x):
    self.stack.pop()
    
def top(self):
    return self.stack[-1][0] #return x
    
def getMin(self):
    return self.stack[-1][-1] #return -3

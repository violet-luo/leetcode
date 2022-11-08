# 1. Helper stack
class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = [math.inf]

    def push(self, x):
        self.stack.append(x)
        self.min_stack.append(min(x, self.min_stack[-1]))

    def pop(self):
        self.stack.pop()
        self.min_stack.pop()

    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.min_stack[-1]

# 2. No helper stack
def __init__(self):
    self.stack = []
    
def push(self, x):
    if not self.stack: 
        self.stack.append((x,x))
    else:
        self.stack.append((x, min(x, self.stack[-1][1]))) #与-3比的最小值
        
def pop(self, x):
    self.stack.pop()
    
def top(self):
    return self.stack[-1][0] #return x
    
def getMin(self):
    return self.stack[-1][-1] #return -3

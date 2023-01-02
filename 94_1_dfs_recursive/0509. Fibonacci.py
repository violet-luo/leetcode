# 1. dfs
def fib(self, n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return self.fib(n-1) + self.fib(n-2)

# 2. dp
def fib(self, n: int) -> int:
    arr = (n+1) * [0]
    
    for i in range(0, n+1):
        if i == 1:
            arr[1] = 1
        if i > 1:
            arr[i] = arr[i-1] + arr[i-2]
    return arr[-1]

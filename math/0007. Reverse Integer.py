"""

Runtime: 28 ms, faster than 90.25% of Python3 online submissions for Reverse Integer.
Memory Usage: 13.8 MB, less than 73.23% of Python3 online submissions for Reverse Integer.

"""

def reverse(self, x: int) -> int:
    r = int(str(abs(x))[::-1])

    if r >= pow(2,31):
        return 0

    return r if x > 0 else -r
    
    
     
"""

Runtime: 36 ms, faster than 54.67% of Python3 online submissions for Reverse Integer.
Memory Usage: 14 MB, less than 5.95% of Python3 online submissions for Reverse Integer.

"""

def reverse(self, x: int) -> int:
    result = 0

    if x < 0:
        symbol = -1
        x = -x
    else:
        symbol = 1

    while x:
        result = result * 10 + x % 10
        x //= 10

    return 0 if result > pow(2, 31) else result * symbol

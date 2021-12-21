"""

Runtime: 32 ms, faster than 65.80% of Python3 online submissions for Power of Two.
Memory Usage: 14.1 MB, less than 99.91% of Python3 online submissions for Power of Two.

"""

def isPowerOfTwo(self, n: int) -> bool:
    if n == 0:
        return False
    while n % 2 == 0:
        n /= 2
    return n == 1

"""

Runtime: 44 ms, faster than 27.12% of Python3 online submissions for Happy Number.
Memory Usage: 13.9 MB, less than 34.14% of Python3 online submissions for Happy Number.

"""
def isHappy(self, n: int) -> bool:
    visited = set()
    while n != 1 and n not in visited:
        visited.add(n)
        sum = 0
        while n != 0:
            sum += (n % 10) ** 2
            n //= 10
        n = sum
    return n == 1

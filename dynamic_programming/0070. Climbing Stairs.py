"""

Runtime: 28 ms, faster than 70.30% of Python3 online submissions for Climbing Stairs.
Memory Usage: 14.3 MB, less than 6.31% of Python3 online submissions for Climbing Stairs.

"""
def climbStairs(self, n: int) -> int:
    if n == 0:
        return 1
    if n <= 2:
        return n
    result = [1,2]
    for i in range(n-2):
        result.append(result[-2]+result[-1])
    return result[-1]

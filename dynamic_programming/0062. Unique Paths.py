"""

1. DP

"""



"""

2. Combination
Runtime: 40 ms, faster than 5.03% of Python3 online submissions for Unique Paths.
Memory Usage: 14.3 MB, less than 7.99% of Python3 online submissions for Unique Paths.

"""

def uniquePaths(self, m: int, n: int) -> int:
    if (m == 1 or n == 1):
        return 1 

    # make sure m <= n
    if (m > n):
        m, n = n, m

    temp, res = 1, 1
    for i in range(1, m):
        temp *= i
    for i in range(n, m + n - 1):
        res *= i
    return res//temp

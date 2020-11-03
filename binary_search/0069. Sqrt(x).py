"""

Runtime: 36 ms, faster than 59.06% of Python3 online submissions for Sqrt(x).
Memory Usage: 14 MB, less than 99.98% of Python3 online submissions for Sqrt(x).

"""

def mySqrt(self, x: int) -> int:
    l, r, ans = 0, x, -1
    while l <= r:
        mid = (l + r) // 2
        if mid * mid <= x:
            ans = mid
            l = mid + 1
        else:
            r = mid - 1
    return ans

"""

Runtime: 28 ms, faster than 73.57% of Python3 online submissions for Number of Digit One.
Memory Usage: 14.2 MB, less than 100.00% of Python3 online submissions for Number of Digit One.

"""

def countDigitOne(self, n: int) -> int:
    res = 0
    i = 1
    while i <= n:
        divider = i * 10
        res += (n // divider) * i + min(max(n % divider - i + 1, 0), i)
        i *= 10
    return res

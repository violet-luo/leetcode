"""

Runtime: 32 ms, faster than 66.46% of Python3 online submissions for Add Digits.
Memory Usage: 14 MB, less than 99.96% of Python3 online submissions for Add Digits.

"""

def addDigits(self, num: int) -> int:
    while num>9:
        num=sum(int(c) for c in str(num))
    return num

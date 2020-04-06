"""
Credit to @StefanPochmann

Runtime: 136 ms, faster than 82.59% of Python3 online submissions for Missing Number.
Memory Usage: 15.2 MB, less than 6.45% of Python3 online submissions for Missing Number.

"""

def missingNumber(self, nums):
    n = len(nums)
    return int(n * (n+1) / 2 - sum(nums))

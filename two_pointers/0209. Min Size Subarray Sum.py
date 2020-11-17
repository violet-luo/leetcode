"""

Runtime: 64 ms, faster than 96.21% of Python3 online submissions for Minimum Size Subarray Sum.
Memory Usage: 16.2 MB, less than 84.61% of Python3 online submissions for Minimum Size Subarray Sum.

"""

def minSubArrayLen(self, s: int, nums: List[int]) -> int:
    if nums is None or len(nums) == 0:
        return 0

    total = left = 0
    n = len(nums)
    res = n + 1

    for right, i in enumerate(nums):
        # form the first subarray that exceeds sum
        total += i
        while total >= s:
            res = min(res, right - left + 1)
            total -= nums[left]
            left += 1

    if res <= n:
        return res
    else:
        return 0

"""

Runtime: 32 ms, faster than 52.91% of Python3 online submissions for House Robber.
Memory Usage: 14.2 MB, less than 35.40% of Python3 online submissions for House Robber.

"""

def rob(self, nums: List[int]) -> int:
    last, now = 0, 0
    for num in nums:
        last, now = now, max(last+num, now)
    return now

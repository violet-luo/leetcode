"""

Runtime: 172 ms, faster than 31.65% of Python3 online submissions for Container With Most Water.
Memory Usage: 16.4 MB, less than 81.52% of Python3 online submissions for Container With Most Water.

"""

def maxArea(self, height: List[int]) -> int:
    l, r = 0, len(height) - 1
    ans = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        ans = max(ans, area)
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return ans

def maxArea(self, height):
    l, r = 0, len(height) - 1
    res = 0
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        res = max(res, area)
        # l和r不是同时移动，将短板向中间收拢
        if height[l] <= height[r]:
            l += 1
        else:
            r -= 1
    return ans

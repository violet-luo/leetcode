def maxArea(self, height: List[int]) -> int:
    max_water = 0
    l, r = 0, len(height) - 1
    while l < r:
        water = min(height[l], height[r]) * (r - l)
        max_water = max(max_water, water)
        if height[l] > height[r]:
            r -= 1
        else:
            l += 1

    return max_water

###

def maxArea(self, height: List[int]) -> int:
    max_water = 0
    left, right = 0, len(height) - 1
    
    while left < right:
        min_height = min(height[left], height[right])
        max_water = max(max_water, min_height * (right - left))
        # 左右不是同时向中间移动，将短板向中间收拢
        if height[left] <= height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

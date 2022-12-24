### 1. 遍历
def trapRainWater(heights):
    if not heights:
        return 0
    
    # 1. 从左到右扫描一边数组，获得每个位置往左这一段的最大值
    left_max = []
    curt_max = float('-inf')
    for height in heights:
        curt_max = max(curt_max, height)
        left_max.append(curt_max) # [0,1,1,2,2,2,2,3,3,3,3,3]
    
    # 2. 从右到左扫描一次获得每个位置向右的最大值
    right_max = []
    curt_max = float('-inf')
    for height in reversed(heights):
        curt_max = max(curt_max, height)
        right_max.append(curt_max) 
        
    right_max = right_max[::-1] # [3,3,3,3,3,3,3,3,2,2,2,1]
        
    water = 0
    n = len(heights)
    for i in range(n):
        water += (min(left_max[i], right_max[i]) - heights[i])
    return water


### 2. 双指针
def trapRainWater(self, heights):
    if not heights:
        return 0    
    left, right = 0, len(heights) - 1
    left_max, right_max = heights[left], heights[right]
    water = 0

    while left <= right:
        if left_max < right_max:
            left_max = max(left_max, heights[left])
            water += left_max - heights[left]
            left += 1
        else:
            right_max = max(right_max, heights[right])
            water += right_max - heights[right]
            right -= 1
                
    return water

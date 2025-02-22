def trapRainWater(heights):
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
    for i in range(len(heights)):
        water += (min(left_max[i], right_max[i]) - heights[i])
    return water

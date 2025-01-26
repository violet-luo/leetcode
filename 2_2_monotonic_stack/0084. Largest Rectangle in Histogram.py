def largestRectangleArea(self, heights) -> int:
    heights = [0] + heights + [0]
    stack = [0]
    max_area = 0
    
    for hi_index in range(1, len(heights)):
        while stack and heights[hi_index] < heights[stack[-1]]: # 直到走到比栈顶小的数字
            popped_index = stack.pop() # 当前最高点
            lo_index = stack[-1] + 1 # 之前最小值的右边

            area = heights[popped_index] * (hi_index - lo_index)
            max_area = max(max_area, area)
        
        stack.append(hi_index)
    
    return max_area

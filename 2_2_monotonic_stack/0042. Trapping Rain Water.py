def trap(self, height: List[int]) -> int:
    stack = [] # 单调递减栈
    res = 0
    
    for right in range(len(height)):
        # 如果当前柱子的高度比栈顶的柱子高，说明可以形成一个水池，计算雨水的体积
        while stack and height[right] > height[stack[-1]]:
            low = stack.pop() # 低柱子索引，要检查是否真的能形成一个水池
            if not stack: # 如果 stack 为空，说明 左边没有墙壁，无法形成水池
                continue
            left = stack[-1] # 左边界的索引
            water_height = min(height[left], height[right]) -  height[low]
            res += (right - left - 1) * water_height
        stack.append(right)
    return res

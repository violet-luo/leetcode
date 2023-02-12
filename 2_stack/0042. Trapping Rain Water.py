def trap(self, height):
    stack = [] # stores index, 栈底大栈顶小
    res = 0
    
    for i, h in enumerate(height):
        while stack and h > height[stack[-1]]:
            bottom = stack.pop() # 凹槽底部
            if stack:
                break
            left = stack[-1] # 凹槽左边
            # min(凹槽左边高度，凹槽右边高度) - 凹槽底部高度
            cur_height = min(height[left], height[i]) - height[bottom]
            res += (i - left - 1) * cur_height
        stack.append(i)
    
    return res

def largestRectangleArea(self, heights):
    if not heights:
        return 0
    n = len(heights)
    max_area = 0
    stack = []

    for i in range(n + 1):
        # 设置特殊数据, array后加入 heights[n] = -1
        value = -1 if i == n else heights[i]
        while stack and heights[stack[-1]] >= value:
            top = stack.pop(-1) # 扔掉大的数
            # 找左端点时栈空，设置特殊数据 heights[-1] = -1
            left = stack[-1] if stack else -1
            width = i - left - 1
            max_area = max(max_area, width * heights[top])
        stack.append(i)

    return max_area

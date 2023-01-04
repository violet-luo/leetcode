def dailyTemperatures(self, temperatures):
    stack = [] # stores index
    n = len(temperatures)
    res = [0] * n
    for i in range(n):
        while stack and temperatures[i] > temperatures[stack[-1]]: # 74 > 73
            res[stack[-1]] = i - stack[-1] # [1]
            stack.pop()
        stack.append(i)
    return res

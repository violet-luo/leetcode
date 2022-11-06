def generateParenthesis(self, n):
    res = []
    subset = ''
    self.dfs(0, 0, n, subset, res)
    return res

def dfs(self, left_count, right_count, n, subset, res):
    if left_count > n or right_count > n: # 递归出口
        return
    if left_count < right_count: # (()))
        return
    
    if left_count == n and right_count == n:
        res.append(subset)
    
    # 搜索加左括号的情况
    self.dfs(left_count + 1, right_count, n, subset + '(', res)
    
    # 搜索加右括号的情况
    self.dfs(left_count, right_count + 1, n, subset + ')', res)

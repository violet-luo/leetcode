def generateParenthesis(self, n):
    res, subset = [], []

    def dfs(left_cnt, right_cnt):
        if left_cnt == right_cnt == n:
            res.append(''.join(subset))
        if left_cnt < n:
            subset.append('(')
            dfs(left_cnt + 1, right_cnt)
            subset.pop()
        # ["()"]是有效的括号组合，["()",")("]不是，所以左括号个数一定大于等于右括号
        if right_cnt < left_cnt:
            subset.append(')')
            dfs(left_cnt, right_cnt + 1)
            subset.pop()
            
    dfs(0, 0)
    return res

###

def generateParenthesis(self, n):
    res, subset = [], ''

    def dfs(left_count, right_count, subset):
        if left_count > n or right_count > n:
            return
        # ["()"]是有效的括号组合，["()",")("]不是，所以左括号个数一定大于等于右括号
        if left_count < right_count:
            return
        if left_count == n and right_count == n:
            res.append(subset)
        dfs(left_count + 1, right_count, subset + '(')
        dfs(left_count, right_count + 1, subset + ')')
    
    dfs(0, 0, subset)
    return res

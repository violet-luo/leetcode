def isMatch(self, s, p):
    n, m = len(s), len(p)
    dp = [[False] * (n + 1) for i in range(m + 1)]
    dp[0][0] = True

    for i in range(1, m + 1):
        path = False #是否可以在该行使用*的特技
        for j in range(1, n + 1):
            if p[i - 1] == "*": #i是表格的索引，但不是p的索引
                if dp[i - 1][0] == True:
                    dp[i] = [True] * (n + 1)
                if dp[i - 1][j]: #只要顶上有了True，就可以开通*接下来的所有道路         
                    path = True
                if path:
                    dp[i][j] = True
            elif p[i - 1] == "?" or p[i - 1]==s[j - 1]: #先判断字母是否符合
                dp[i][j] = dp[i-1][j-1] #再看左上方格子是不是T
                    
    return dp[m][n]
  
###
# 九章解法
def isMatch(self, s, p):
  n, m = len(s), len(p)
  dp = [[False] * (m + 1) for _ in range(n + 1)]

  # initialization
  dp[0][0] = True
  for i in range(1, m + 1):
      dp[0][i] = dp[0][i - 1] and p[i - 1] == '*'

  # function
  for i in range(1, n + 1):
      for j in range(1, m + 1):
          if p[j - 1] == '*':
              dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
          else:
              dp[i][j] = dp[i - 1][j - 1] and (s[i - 1] == p[j - 1] or p[j - 1] == '?')

  return dp[n][m]
  
###
# 滚动数组优化
def isMatch(self, s, p):
    n, m = len(s), len(p)

    # state
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # initialization
    dp[0][0] = True
    for i in range(1, m + 1):
        dp[0][i] = dp[0][i - 1] and p[i - 1] == '*'

    # function
    for i in range(1, n + 1):
        dp[i % 2][0] = False # 滚动数组优化
        for j in range(1, m + 1):
            if p[j - 1] == '*':
                dp[i % 2][j] = dp[(i - 1) % 2][j] or dp[i % 2][j - 1]
            else:
                dp[i % 2][j] = dp[(i - 1) % 2][j - 1] and (
                    s[i - 1] == p[j - 1] or p[j - 1] == '?')

    return dp[n % 2][m]

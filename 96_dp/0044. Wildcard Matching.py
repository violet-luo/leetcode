def isMatch(self, s: str, p: str) -> bool:
    n, m = len(s), len(p)
    # dp[i][j]：s的前i个字符 s[:i] 与 p的前j个字符 p[:j] 匹配是否成功
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    dp[0][0] = True
    # 重点：initialization
    for j in range(1, m + 1):
        # 若 p 的第 j 个字符 p[j - 1] 是'*', 说明第 j 个字符可有可无
        # 只有前 j - 1个匹配得上，前 j 个也匹配得上
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # p的第j个字符是 *，无论是s的前i个字符和p的前j-1个字符匹配成功，还是s的前i-1个字符和p的前j个字符匹配成功
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] and p[j - 1] == s[i - 1]
    
    return dp[n][m]

###

def isMatch(self, s, p):
    n, m = len(s), len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]

    # 初始化：s,p 为空串时，匹配成功
    dp[0][0] = True
    # p 为空，s不为空，必为false(boolean默认为false, 无需处理)
    # s 为空，p不为空，由于*可以匹配0个字符，所以有可能为true
    for j in range(1, m + 1):
        # 若 p 的第 j 个字符 p[j - 1] 是'*', 说明第 j 个字符可有可无
        # 只有前 j - 1个匹配得上，前 j 个也匹配得上
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # p的第j个字符是 *，无论是s的前i个字符和p的前j-1个字符匹配成功，还是s的前i-1个字符和p的前j个字符匹配成功 
            if p[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            # p的第j个字符不是 *，如果dp[i-1][j-1]为true, 只有s[i-1]==p[j-1]或p=='?'时匹配成功
            else:
                if s[i - 1] == p[j - 1] or p[j - 1] == '?':
                    dp[i][j] = dp[i - 1][j - 1]
    return dp[n][m]

###

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

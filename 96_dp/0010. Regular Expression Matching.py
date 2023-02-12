def isMatch(self, s, p):
    n, m = len(s), len(p)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    
    # 初始化：s,p 为空串时，匹配成功
    dp[0][0] = True
    # p 为空，s不为空，必为false(boolean默认为false, 无需处理)
    # s 为空，p不为空，由于*可以匹配0个字符，所以有可能为true
    for j in range(1, m + 1):
        # 若 p 的第 j 个字符 p[j - 1] 是 '*'，说明第 j - 1、j 个可有可无
        # 那么如果前 j - 2 个已经匹配上，前 j 个也可以匹配上
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 2] #与44区别

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # p的第j个字符是 *
            if p[j - 1] == '*':
                # s的
                if s[i - 1] == p[j - 2] or p[j - 2] == '.':
                    dp[i][j] = dp[i][j - 2] or dp[i - 1][j]
                else: 
                    dp[i][j] = dp[i][j - 2]

            # p的第j个字符不是 *
            # 如果dp[i-1][j-1]为true, 只有s[i-1] == p[j-1] 或 p == '.' 时匹配成功
            elif s[i - 1] == p[j - 1] or p[j - 1] == '.':
                dp[i][j] = dp[i - 1][j - 1]

    return dp[n][m]

def wordBreak(self, s, wordDict):
    n = len(s)
    dp = [False] * (n + 1) # n + 1 为了让边界情况也能套用状态转移方程
    dp[0] = True

    for i in range(1, n + 1):
        for j in range(i):
            if not dp[j]:
                continue
            if s[j:i] in wordDict:
                dp[i] = True
                break 

    return dp[n]

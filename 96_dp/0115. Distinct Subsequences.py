def numDistinct(self, s: str, t: str) -> int:
    n = len(s)
    m = len(t)

    dp = [[0] * (m + 1) for i in range(n + 1)]

    # base case
    for i in range(n+1):
        dp[i][0] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if s[i - 1] == t[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]
            else:
                dp[i][j] = dp[i - 1][j]
    
    return dp[n][m]


### 滚动数组
def numDistinct(self, s: str, t: str) -> int:
    n, m = len(s), len(t)

    prev = [0] * (m + 1) # 只要存储前一行的DP结果
    prev[0] = 1  # Base case: 空字符串只有一种匹配方式

    for i in range(1, n + 1): # 遍历s
        cur = [0] * (m + 1) # 当前行DP数组
        cur[0] = 1  # Base case: 空字符串只有一种匹配方式

        for j in range(1, m + 1): # 遍历t
            if s[i - 1] == t[j - 1]:
                cur[j] = prev[j - 1] + prev[j]
            else:
                cur[j] = prev[j]

        prev = cur  # Move to the next row

    return prev[m]

### 1.
def backPack(self, m, A):
    n = len(A)
    dp = [[False] * (m + 1) for _ in range(n + 1)]
    dp[0][0] = True
    
    for i in range(1, n + 1):
        dp[i][0] = True
        for j in range(1, m + 1):
            # 背包空间大于A[i]
            if j >= A[i-1]:
                # dp[i-1][j]: 前i-1个数已经凑出了j的和
                # dp[i-1][j-A[i-1]: 前i-1个数已经凑出了 j - Ai 的和
                dp[i][j] = dp[i-1][j] or dp[i-1][j - A[i-1]]
            # 背包空间小于A[i]
            else:
                dp[i][j] = dp[i-1][j]
   
    for i in range(m, -1, -1):
        if dp[n][i]: # return最满
            return i
    return -1

### 2.
def backPack(self, m, A):
    n = len(A)
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 背包容量大于第i件物品
            if j >= A[i-1]:
                # dp[i-1][j]:前i-1个数可以组成的最靠近j的和，不需要第i个数
                # dp[i-1][j-A[i]]: 前i-1个数可以组成的最靠近 j - A[i-1], 加上A[i-1]才会更靠近j
                dp[i][j] = max(dp[i-1][j], dp[i-1][j-A[i-1]] + A[i-1])
            # 背包容量小于第i件物品，不取
            else:
                dp[i][j] = dp[i-1][j]

    return dp[n][m]

def backPackIII(self, A, V, m):
    if not A or not V:
        return 0
        
    n = len(A)
    dp = [[0] * (m+1) for _ in range(n+1)]
    
    for i in range(1, n + 1):
        for j in range(m + 1):
             if j >= A[i-1]:
                dp[i][j] = max(dp[i-1][j], dp[i][j - A[i-1]] + V[i-1])
             else:
                dp[i][j] = dp[i-1][j]
    return dp[n][m]
